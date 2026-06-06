"""
Reference solutions for problems p1–p5.
Don't open this until you've attempted the problems.

Verify the references pass every problem's own tests:  python3 solutions_01.py
"""

import numpy as np


def softmax(x):
    e = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e / np.sum(e, axis=-1, keepdims=True)


# P1 ──────────────────────────────────────────────────────────────────────────
def top_k_temperature(logits, k, temperature=1.0):
    logits = np.asarray(logits, dtype=np.float64) / temperature
    k = min(k, logits.shape[-1])
    keep = np.argpartition(logits, -k)[-k:]          # indices of top-k logits
    masked = np.full_like(logits, -np.inf)
    masked[keep] = logits[keep]
    return softmax(masked)


# P2 ──────────────────────────────────────────────────────────────────────────
def apply_repetition_penalty(logits, generated_ids, penalty):
    out = np.array(logits, dtype=np.float64)         # copy, don't mutate input
    for tid in set(generated_ids):
        out[tid] = out[tid] / penalty if out[tid] > 0 else out[tid] * penalty
    return out


# P3 ──────────────────────────────────────────────────────────────────────────
def cross_entropy_label_smoothing(logits, targets, smoothing=0.0):
    logits = np.asarray(logits, dtype=np.float64)
    targets = np.asarray(targets)
    N, V = logits.shape
    m = np.max(logits, axis=-1, keepdims=True)        # stable log-softmax
    log_probs = logits - m - np.log(np.sum(np.exp(logits - m), axis=-1, keepdims=True))
    true_lp = log_probs[np.arange(N), targets]        # (N,)
    sum_lp = np.sum(log_probs, axis=-1)               # (N,)
    loss = -((1 - smoothing) * true_lp + (smoothing / V) * sum_lp)
    return float(np.mean(loss))


# P4 ──────────────────────────────────────────────────────────────────────────
def apply_rope(x, positions, base=10000.0):
    x = np.asarray(x, dtype=np.float64)
    positions = np.asarray(positions, dtype=np.float64)
    _, dim = x.shape
    half = dim // 2
    inv_freq = base ** (-np.arange(half, dtype=np.float64) / half)   # theta_i
    angles = positions[:, None] * inv_freq[None, :]                  # (seq, half)
    cos, sin = np.cos(angles), np.sin(angles)
    x_even, x_odd = x[:, 0::2], x[:, 1::2]
    out = np.empty_like(x)
    out[:, 0::2] = x_even * cos - x_odd * sin
    out[:, 1::2] = x_even * sin + x_odd * cos
    return out


# P5 ──────────────────────────────────────────────────────────────────────────
def grouped_query_attention(q, k, v):
    q = np.asarray(q, dtype=np.float64)
    k = np.asarray(k, dtype=np.float64)
    v = np.asarray(v, dtype=np.float64)
    n_head, q_len, head_dim = q.shape
    n_kv, kv_len = k.shape[0], k.shape[1]
    rep = n_head // n_kv
    k = np.repeat(k, rep, axis=0)                     # (n_head, kv_len, head_dim)
    v = np.repeat(v, rep, axis=0)
    scores = np.matmul(q, np.transpose(k, (0, 2, 1))) / np.sqrt(head_dim)
    mask = np.triu(np.ones((q_len, kv_len)), k=kv_len - q_len + 1)
    scores = np.where(mask[None] == 1, -np.inf, scores)
    return np.matmul(softmax(scores), v)


if __name__ == "__main__":
    # run each problem's own test() against these references
    import importlib
    mods = {
        "p1_top_k_temperature": [("top_k_temperature", top_k_temperature)],
        "p2_repetition_penalty": [("apply_repetition_penalty", apply_repetition_penalty)],
        "p3_cross_entropy_label_smoothing": [("cross_entropy_label_smoothing", cross_entropy_label_smoothing)],
        "p4_rope": [("apply_rope", apply_rope)],
        "p5_grouped_query_attention": [("grouped_query_attention", grouped_query_attention)],
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
