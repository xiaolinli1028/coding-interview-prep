# Key Equations — ML Coding Problem Sets

Quick-reference for every problem (p1–p15). Each entry: the core equation(s) you
must be able to write and derive, plus the one-line "why" interviewers probe.

---

## Set 01 — Decoding & Transformer Internals

### p1 — Top-k + Temperature Sampling
Temperature scaling then restrict to the top-k logits, then softmax:

$$
\tilde z_i = z_i / T, \qquad
P_i = \frac{e^{\tilde z_i}}{\sum_{j \in \text{top-}k} e^{\tilde z_j}} \;\; (i \in \text{top-}k),\quad 0 \text{ otherwise}
$$

- $T \to 0$ sharpens (→ argmax), $T \to \infty$ flattens (→ uniform).
- **Why `-inf` mask, not zero-after-softmax?** Masking the *logit* makes the softmax denominator sum only survivors → renormalization is automatic.

### p2 — Repetition Penalty (CTRL, Keskar et al. 2019)
For each already-generated token id:

$$
z_i \leftarrow
\begin{cases}
z_i / \alpha & z_i > 0 \\
z_i \cdot \alpha & z_i \le 0
\end{cases}, \qquad \alpha \ge 1
$$

- Penalty $\alpha>1$ pushes seen tokens' logits toward / below 0, lowering their prob.

### p3 — Cross-Entropy + Label Smoothing (Szegedy et al. 2016)
Soft target and loss (V classes, smoothing $\epsilon$):

$$
t_j = (1-\epsilon)\,\mathbb{1}[j=y] + \frac{\epsilon}{V},
\qquad
\mathcal{L} = -\sum_j t_j \,\log\mathrm{softmax}(z)_j
$$

Stable log-softmax (never `log(softmax(·))`):

$$
\log\mathrm{softmax}(z)_j = z_j - \underbrace{\Big(m + \log\textstyle\sum_k e^{z_k - m}\Big)}_{\text{logsumexp},\; m=\max_k z_k}
$$

### p4 — RoPE (Su et al. 2021)
Per 2-D pair $i$ (dims $2i, 2i{+}1$), frequency and rotation by angle $\phi = m\,\theta_i$ at position $m$:

$$
\theta_i = \text{base}^{-2i/d},\qquad
\begin{pmatrix} a' \\ b' \end{pmatrix}
=
\begin{pmatrix} \cos\phi & -\sin\phi \\ \sin\phi & \cos\phi \end{pmatrix}
\begin{pmatrix} a \\ b \end{pmatrix}
$$

- **Key property:** $\langle \mathrm{RoPE}(q,m),\, \mathrm{RoPE}(k,n)\rangle$ depends only on $m-n$ → relative position, and it extrapolates.

### p5 — Grouped-Query Attention (GQA / MQA)
Repeat each KV head $r = n_\text{head}/n_\text{kv}$ times, then standard causal attention:

$$
\mathrm{Attn}(Q,K,V) = \mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d_h}} + M\right)V,
\qquad
M_{ij} = \begin{cases} 0 & j \le i_\text{abs} \\ -\infty & \text{else} \end{cases}
$$

- KV-cache: query row $i$ has absolute position $(\text{kv\_len} - q\_\text{len} + i)$.
- **Why GQA?** KV cache memory shrinks by factor $r$ with little quality loss.

---

## Set 02 — Post-Training Losses & Building Blocks

### p6 — DPO (Rafailov et al. 2023)
With $\pi$ = policy, $\pi_\text{ref}$ = frozen reference, chosen $y_w$ / rejected $y_l$:

$$
\mathcal{L}_\text{DPO} = -\log\sigma\!\Big(\beta\big[(\log\pi(y_w)-\log\pi_\text{ref}(y_w)) - (\log\pi(y_l)-\log\pi_\text{ref}(y_l))\big]\Big)
$$

Implicit reward: $\;r(x,y) = \beta\,\log\frac{\pi(y\mid x)}{\pi_\text{ref}(y\mid x)} + \beta\log Z(x)$.
Stable form: $-\log\sigma(z) = \mathrm{softplus}(-z) = \log(1+e^{-z})$.

### p7 — GRPO Advantages (DeepSeek-R1)
Group of $K$ samples per prompt, baseline = group mean (no value net):

$$
A_i = \frac{r_i - \mathrm{mean}(\mathbf{r})}{\mathrm{std}(\mathbf{r}) + \epsilon}
$$

- Population std (ddof=0). Constant group → all zeros (eps guard).

### p8 — LayerNorm Backward
Forward: $\hat x = \dfrac{x-\mu}{\sqrt{\sigma^2+\epsilon}},\; y=\gamma\hat x+\beta$. With $d\hat x = dy\odot\gamma$ and means over the feature axis:

$$
\frac{\partial \mathcal L}{\partial x} = \frac{1}{\sqrt{\sigma^2+\epsilon}}\Big(d\hat x - \overline{d\hat x} - \hat x\,\overline{d\hat x \odot \hat x}\Big)
$$

- The two subtracted terms remove the gradient components along the mean and variance directions.

### p9 — Online Softmax (FlashAttention core)
Streaming running max $m$ and denominator $\ell$; on a new block with max $m_b$:

$$
m' = \max(m, m_b),\qquad
\ell \leftarrow \ell\,e^{\,m - m'} + \sum_{j\in\text{block}} e^{\,x_j - m'},\qquad m \leftarrow m'
$$

Final: $\mathrm{softmax}(x)_i = e^{x_i - m}/\ell$. The rescale $e^{m-m'}$ corrects the old partial sum.

### p10 — Top-k MoE Router (Shazeer et al. 2017)
Pick top-k experts per token, softmax over **only** those k logits:

$$
\mathcal{T} = \text{top-}k(g),\qquad
w_i = \frac{e^{g_i}}{\sum_{j\in\mathcal{T}} e^{g_j}}\;\; (i\in\mathcal{T})
$$

---

## Set 03 — Sampling, Attention, Norms, Optim, Spec-Decode

### p11 — Top-p / Nucleus (Holtzman et al. 2019)
Smallest high-prob set reaching threshold $p$, renormalized:

$$
V^{(p)} = \text{smallest prefix (desc.) with } \tau=\!\!\sum_{x\in V^{(p)}}\!\!P(x) \ge p,
\qquad
P'(x) = \frac{P(x)}{\tau}\;\mathbb{1}[x\in V^{(p)}]
$$

- The token that *crosses* the threshold is included.

### p12 — Multi-Head Attention (Vaswani et al. 2017)
$$
Q=xW_Q,\;K=xW_K,\;V=xW_V;\quad
\text{head}_h=\mathrm{softmax}\!\Big(\tfrac{Q_hK_h^\top}{\sqrt{d_h}}+M\Big)V_h
$$
$$
\mathrm{MHA}(x)=\big[\text{head}_1\,\Vert\,\cdots\,\Vert\,\text{head}_H\big]\,W_O,\qquad d_h = d_\text{model}/H
$$

- Causal mask $M$: $-\infty$ above the diagonal so position $t$ sees only $\le t$.

### p13 — RMSNorm (Zhang & Sennrich 2019)
$$
\mathrm{RMS}(x) = \sqrt{\tfrac{1}{d}\textstyle\sum_i x_i^2 + \epsilon},\qquad
y = \frac{x}{\mathrm{RMS}(x)}\odot \gamma
$$

- No mean subtraction, no bias → cheaper than LayerNorm; scale-invariant (eps=0).

### p14 — Adam (Kingma & Ba 2014)
$$
m_t = \beta_1 m_{t-1} + (1-\beta_1)g_t,\qquad
v_t = \beta_2 v_{t-1} + (1-\beta_2)g_t^2
$$
$$
\hat m_t = \frac{m_t}{1-\beta_1^t},\quad
\hat v_t = \frac{v_t}{1-\beta_2^t},\qquad
\theta_t = \theta_{t-1} - \eta\,\frac{\hat m_t}{\sqrt{\hat v_t}+\epsilon}
$$

- Bias correction $1-\beta^t$ matters most in early steps. AdamW differs: decoupled $-\eta\lambda\theta$ weight decay.

### p15 — Speculative Decoding (Leviathan et al. 2023)
Draft samples $x\sim q$; target gives $p$. Accept / residual resample:

$$
P_\text{accept}(x) = \min\!\Big(1, \frac{p(x)}{q(x)}\Big),\qquad
p_\text{res}(i) = \frac{\max(p(i)-q(i),\,0)}{\sum_j \max(p(j)-q(j),\,0)}
$$

- This exactly preserves sampling from $p$ (unbiased), while drafting cheaply from $q$.

---

## Set 04 — Inference Systems

### p16 — KV-Cache Incremental Decoding
Per head, at decode step $t$ (append current k/v, attend over the cache):

$$
K = [\,k_\text{cache}\;\Vert\;k_t\,],\quad V = [\,v_\text{cache}\;\Vert\;v_t\,]
\qquad(\text{length } t \to t{+}1)
$$
$$
\text{scores} = \frac{q_t K^\top}{\sqrt{d_h}}\;\;(\text{shape } 1\times(t{+}1),\ \textbf{no mask}),
\qquad
\text{out}_t = \mathrm{softmax}(\text{scores})\,V
$$

- **No causal mask needed** — the cache holds only past tokens, so causality is enforced by *what's in the cache*.
- **Why:** turns each decode step from $O(L^2)$ recompute into $O(L)$; the cache is the $2\,L\,n_\text{layers}\,d_\text{model}$ memory cost that GQA/MLA then attack.
- Step-by-step cached decode is **identical** to full parallel causal attention (prefill).
