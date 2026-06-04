"""
Reference solutions (NumPy) for p11–p15.
Don't open until you've attempted them.

Verify:  python3 solutions_03.py
"""

import numpy as np


def softmax(x):
    e = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e / np.sum(e, axis=-1, keepdims=True)


# P11 ─────────────────────────────────────────────────────────────────────────
def nucleus(probs, p):
    probs = np.asarray(probs, dtype=np.float64)
    order = np.argsort(-probs)                 # indices, highest prob first
    sorted_probs = probs[order]
    cum = np.cumsum(sorted_probs)
    # smallest prefix whose cumulative >= p (keep the crossing token)
    cutoff = int(np.searchsorted(cum, p))      # first index with cum >= p
    cutoff = min(cutoff, len(probs) - 1)
    keep = order[:cutoff + 1]
    tau = probs[keep].sum()
    out = np.zeros_like(probs)
    out[keep] = probs[keep] / tau
    return out


# P12 ─────────────────────────────────────────────────────────────────────────
def multi_head_attention(x, w_q, w_k, w_v, w_o, n_head):
    x = np.asarray(x, dtype=np.float64)
    seq, d = x.shape
    hd = d // n_head
    q, k, v = x @ w_q, x @ w_k, x @ w_v
    # (seq, d) -> (n_head, seq, hd)
    split = lambda t: t.reshape(seq, n_head, hd).transpose(1, 0, 2)
    q, k, v = split(q), split(k), split(v)
    scores = np.matmul(q, k.transpose(0, 2, 1)) / np.sqrt(hd)   # (n_head, seq, seq)
    mask = np.triu(np.ones((seq, seq)), 1)
    scores = np.where(mask[None] == 1, -np.inf, scores)
    out = np.matmul(softmax(scores), v)                        # (n_head, seq, hd)
    out = out.transpose(1, 0, 2).reshape(seq, d)
    return out @ w_o


# P13 ─────────────────────────────────────────────────────────────────────────
def rms_norm(x, gamma, eps=1e-6):
    x = np.asarray(x, dtype=np.float64)
    rms = np.sqrt(np.mean(x**2, axis=-1, keepdims=True) + eps)
    return (x / rms) * gamma


# P14 ─────────────────────────────────────────────────────────────────────────
def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    m = beta1 * m + (1 - beta1) * grad
    v = beta2 * v + (1 - beta2) * grad**2
    m_hat = m / (1 - beta1**t)
    v_hat = v / (1 - beta2**t)
    param = param - lr * m_hat / (np.sqrt(v_hat) + eps)
    return param, m, v


# P15 ─────────────────────────────────────────────────────────────────────────
def acceptance_prob(p_target, q_draft, token):
    p_target = np.asarray(p_target, dtype=np.float64)
    q_draft = np.asarray(q_draft, dtype=np.float64)
    return min(1.0, p_target[token] / q_draft[token])


def residual_distribution(p_target, q_draft):
    p_target = np.asarray(p_target, dtype=np.float64)
    q_draft = np.asarray(q_draft, dtype=np.float64)
    r = np.clip(p_target - q_draft, 0, None)
    s = r.sum()
    if s == 0:
        return p_target.copy()
    return r / s


if __name__ == "__main__":
    import importlib
    mods = {
        "p11_top_p_nucleus": [("nucleus", nucleus)],
        "p12_multi_head_attention": [("multi_head_attention", multi_head_attention)],
        "p13_rmsnorm": [("rms_norm", rms_norm)],
        "p14_adam_step": [("adam_step", adam_step)],
        "p15_speculative_decoding": [("acceptance_prob", acceptance_prob),
                                     ("residual_distribution", residual_distribution)],
    }
    for name, fns in mods.items():
        mod = importlib.import_module(name)
        for attr, fn in fns:
            setattr(mod, attr, fn)
        try:
            mod.test()
            print(f"PASS  {name}")
        except Exception as e:
            print(f"FAIL  {name}: {e}")
