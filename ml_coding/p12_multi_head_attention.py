"""
Problem 12 — Multi-Head Attention from Scratch    (run: python3 p12_multi_head_attention.py)
============================================================================================
Implement causal multi-head self-attention (Vaswani et al. 2017) end to end,
including the input projections and output projection:

    Q = x W_q,  K = x W_k,  V = x W_v          (each (seq, d_model))
    split into n_head heads of size head_dim = d_model / n_head
    head_h = softmax( Q_h K_h^T / sqrt(head_dim) + causal_mask ) V_h
    concat heads -> (seq, d_model) -> @ W_o

Use a causal mask so position t attends only to positions <= t (fill masked
scores with -inf before softmax).

KEY EQUATIONS  (d_h = d_model / n_head; M causal: -inf above diagonal)
  Q = x W_q,  K = x W_k,  V = x W_v
  head_h = softmax(Q_h K_h^T / sqrt(d_h) + M) V_h
  MHA(x) = concat(head_1, ..., head_H) W_o
"""

import numpy as np


def softmax(x):
    e = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e / np.sum(e, axis=-1, keepdims=True)


def multi_head_attention(x, w_q, w_k, w_v, w_o, n_head):
    """
    Args:
      x:   np.ndarray (seq, d_model)
      w_q: np.ndarray (d_model, d_model)
      w_k: np.ndarray (d_model, d_model)
      w_v: np.ndarray (d_model, d_model)
      w_o: np.ndarray (d_model, d_model)
      n_head: int, divides d_model.
    Returns:
      np.ndarray (seq, d_model)
    """
    x = np.asarray(x, dtype=np.float64)
    seq, d_model = x.shape
    hd = d_model // n_head
    q, k, v = x @ w_q, x @ w_k, x @ w_v
    split = lambda x: x.reshape(seq, n_head, hd).transpose(1, 0, 2)
    q, k, v = split(q), split(k), split(v)
    scores = q @ k.transpose(0, 2, 1) / np.sqrt(hd)

    mask = np.triu(np.ones((seq, seq)), 1)
    scores = np.where(mask == 1, -np.inf, scores)

    out = softmax(scores) @ v
    out = out.transpose(1, 0, 2).reshape(seq, -1)
    return out @ w_o
    


# ── tests ─────────────────────────────────────────────────────────────────────
def _ref(x, w_q, w_k, w_v, w_o, n_head):
    seq, d = x.shape
    hd = d // n_head
    q, k, v = x @ w_q, x @ w_k, x @ w_v
    out = np.zeros((seq, d))
    for h in range(n_head):
        sl = slice(h * hd, (h + 1) * hd)
        qh, kh, vh = q[:, sl], k[:, sl], v[:, sl]
        s = qh @ kh.T / np.sqrt(hd)
        mask = np.triu(np.ones((seq, seq)), 1)
        s = np.where(mask == 1, -np.inf, s)
        out[:, sl] = softmax(s) @ vh
    return out @ w_o


def test():
    rng = np.random.default_rng(0)
    seq, d, nh = 5, 8, 2
    x = rng.standard_normal((seq, d))
    w_q, w_k, w_v, w_o = (rng.standard_normal((d, d)) for _ in range(4))

    out = multi_head_attention(x, w_q, w_k, w_v, w_o, nh)
    assert out.shape == (seq, d), out.shape
    # (a) matches an independent per-head reference
    assert np.allclose(out, _ref(x, w_q, w_k, w_v, w_o, nh)), "value mismatch vs reference"
    # (b) causality: perturbing the LAST token must not change earlier outputs
    x2 = x.copy(); x2[-1] += 10.0
    out2 = multi_head_attention(x2, w_q, w_k, w_v, w_o, nh)
    assert np.allclose(out[:-1], out2[:-1]), "not causal: future token leaked into past"


if __name__ == "__main__":
    try:
        test()
        print("PASS  p12 multi_head_attention")
    except NotImplementedError:
        print("----  p12 multi_head_attention — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p12 multi_head_attention: {e}")
