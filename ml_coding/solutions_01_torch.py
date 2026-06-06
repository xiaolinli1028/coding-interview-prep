"""
Reference solutions (PyTorch) for p1–p5 torch versions.
Don't open until you've attempted them.

Verify against each problem's tests:  python3 solutions_01_torch.py
"""

import math
import torch


# P1 ──────────────────────────────────────────────────────────────────────────
def top_k_temperature(logits, k, temperature=1.0):
    logits = logits / temperature
    k = min(k, logits.shape[-1])
    vals, idx = torch.topk(logits, k, dim=-1)
    out = torch.full_like(logits, float("-inf"))
    out.scatter_(-1, idx, vals)
    return torch.softmax(out, dim=-1)


# P2 ──────────────────────────────────────────────────────────────────────────
def apply_repetition_penalty(logits, generated_ids, penalty):
    out = logits.clone().to(torch.float32)
    ids = torch.tensor(sorted(set(generated_ids)), dtype=torch.long)
    sel = out[ids]
    out[ids] = torch.where(sel > 0, sel / penalty, sel * penalty)
    return out


# P3 ──────────────────────────────────────────────────────────────────────────
def cross_entropy_label_smoothing(logits, targets, smoothing=0.0):
    log_probs = torch.log_softmax(logits, dim=-1)       # stable
    n, v = logits.shape
    nll = -log_probs[torch.arange(n), targets]          # (N,)
    smooth = -log_probs.mean(dim=-1)                    # (eps/V)*sum == eps*mean
    loss = (1 - smoothing) * nll + smoothing * smooth
    return loss.mean()


# P4 ──────────────────────────────────────────────────────────────────────────
def apply_rope(x, positions, base=10000.0):
    _, dim = x.shape
    half = dim // 2
    inv_freq = base ** (-torch.arange(half, dtype=x.dtype) / half)   # theta_i
    angles = positions.to(x.dtype).unsqueeze(-1) * inv_freq.unsqueeze(0)  # (seq, half)
    cos, sin = torch.cos(angles), torch.sin(angles)
    x_even, x_odd = x[:, 0::2], x[:, 1::2]
    out = torch.empty_like(x)
    out[:, 0::2] = x_even * cos - x_odd * sin
    out[:, 1::2] = x_even * sin + x_odd * cos
    return out


# P5 ──────────────────────────────────────────────────────────────────────────
def grouped_query_attention(q, k, v):
    n_head, q_len, hd = q.shape
    n_kv, kv_len = k.shape[0], k.shape[1]
    rep = n_head // n_kv
    k = k.repeat_interleave(rep, dim=0)                 # (n_head, kv_len, hd)
    v = v.repeat_interleave(rep, dim=0)
    scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(hd)
    mask = torch.triu(torch.ones(q_len, kv_len), diagonal=kv_len - q_len + 1).bool()
    scores = scores.masked_fill(mask.unsqueeze(0), float("-inf"))
    return torch.matmul(torch.softmax(scores, dim=-1), v)


if __name__ == "__main__":
    import importlib
    mods = {
        "p1_top_k_temperature_torch": [("top_k_temperature", top_k_temperature)],
        "p2_repetition_penalty_torch": [("apply_repetition_penalty", apply_repetition_penalty)],
        "p3_cross_entropy_label_smoothing_torch": [("cross_entropy_label_smoothing", cross_entropy_label_smoothing)],
        "p4_rope_torch": [("apply_rope", apply_rope)],
        "p5_grouped_query_attention_torch": [("grouped_query_attention", grouped_query_attention)],
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
