"""
Reference solutions (PyTorch) for p11–p15 torch versions.
Don't open until you've attempted them.

Verify:  python3 solutions_03_torch.py
"""

import math
import torch


# P11 ─────────────────────────────────────────────────────────────────────────
def nucleus(probs, p):
    sorted_probs, order = torch.sort(probs, descending=True)
    cum = torch.cumsum(sorted_probs, dim=-1)
    # keep tokens up to and including the one that crosses p
    keep_sorted = cum - sorted_probs < p           # True for the nucleus (shifted cumsum)
    out = torch.zeros_like(probs)
    kept_idx = order[keep_sorted]
    out[kept_idx] = probs[kept_idx]
    return out / out.sum()


# P12 ─────────────────────────────────────────────────────────────────────────
def multi_head_attention(x, w_q, w_k, w_v, w_o, n_head):
    seq, d = x.shape
    hd = d // n_head
    q, k, v = x @ w_q, x @ w_k, x @ w_v
    split = lambda t: t.view(seq, n_head, hd).transpose(0, 1)   # (n_head, seq, hd)
    q, k, v = split(q), split(k), split(v)
    scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(hd)
    mask = torch.triu(torch.ones(seq, seq), diagonal=1).bool()
    scores = scores.masked_fill(mask.unsqueeze(0), float("-inf"))
    out = torch.matmul(torch.softmax(scores, dim=-1), v)        # (n_head, seq, hd)
    out = out.transpose(0, 1).reshape(seq, d)
    return out @ w_o


# P13 ─────────────────────────────────────────────────────────────────────────
def rms_norm(x, gamma, eps=1e-6):
    rms = torch.sqrt(x.pow(2).mean(dim=-1, keepdim=True) + eps)
    return (x / rms) * gamma


# P14 ─────────────────────────────────────────────────────────────────────────
def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    m = beta1 * m + (1 - beta1) * grad
    v = beta2 * v + (1 - beta2) * grad.pow(2)
    m_hat = m / (1 - beta1 ** t)
    v_hat = v / (1 - beta2 ** t)
    param = param - lr * m_hat / (v_hat.sqrt() + eps)
    return param, m, v


# P15 ─────────────────────────────────────────────────────────────────────────
def acceptance_prob(p_target, q_draft, token):
    return torch.clamp(p_target[token] / q_draft[token], max=1.0)


def residual_distribution(p_target, q_draft):
    r = torch.clamp(p_target - q_draft, min=0.0)
    s = r.sum()
    if s == 0:
        return p_target.clone()
    return r / s


if __name__ == "__main__":
    import importlib
    mods = {
        "p11_top_p_nucleus_torch": [("nucleus", nucleus)],
        "p12_multi_head_attention_torch": [("multi_head_attention", multi_head_attention)],
        "p13_rmsnorm_torch": [("rms_norm", rms_norm)],
        "p14_adam_step_torch": [("adam_step", adam_step)],
        "p15_speculative_decoding_torch": [("acceptance_prob", acceptance_prob),
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
