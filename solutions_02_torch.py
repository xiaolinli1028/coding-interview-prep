"""
Reference solutions (PyTorch) for p6–p10 torch versions.
Don't open until you've attempted them.

Verify:  python3 solutions_02_torch.py
"""

import torch
import torch.nn.functional as F


# P6 ──────────────────────────────────────────────────────────────────────────
def dpo_loss(policy_chosen_logps, policy_rejected_logps,
             ref_chosen_logps, ref_rejected_logps, beta=0.1):
    pi = policy_chosen_logps - policy_rejected_logps
    ref = ref_chosen_logps - ref_rejected_logps
    return -F.logsigmoid(beta * (pi - ref)).mean()


# P7 ──────────────────────────────────────────────────────────────────────────
def grpo_advantages(rewards, eps=1e-8):
    mean = rewards.mean(dim=-1, keepdim=True)
    std = rewards.std(dim=-1, unbiased=False, keepdim=True)   # population std
    return (rewards - mean) / (std + eps)


# P8 ──────────────────────────────────────────────────────────────────────────
def layer_norm_backward(dy, x, gamma, eps=1e-5):
    mu = x.mean(-1, keepdim=True)
    var = x.var(-1, unbiased=False, keepdim=True)
    inv = torch.rsqrt(var + eps)
    xhat = (x - mu) * inv
    dxhat = dy * gamma
    dx = inv * (dxhat
                - dxhat.mean(-1, keepdim=True)
                - xhat * (dxhat * xhat).mean(-1, keepdim=True))
    return dx


# P9 ──────────────────────────────────────────────────────────────────────────
def online_softmax(x, chunk_size):
    m = torch.tensor(float("-inf"), dtype=x.dtype)
    l = torch.tensor(0.0, dtype=x.dtype)
    for start in range(0, x.shape[0], chunk_size):
        chunk = x[start:start + chunk_size]
        m_new = torch.maximum(m, chunk.max())
        l = l * torch.exp(m - m_new) + torch.exp(chunk - m_new).sum()
        m = m_new
    return torch.exp(x - m) / l


# P10 ─────────────────────────────────────────────────────────────────────────
def moe_top_k_gating(router_logits, k):
    top_logits, expert_indices = torch.topk(router_logits, k, dim=-1)  # sorted desc
    gating_weights = torch.softmax(top_logits, dim=-1)
    return expert_indices, gating_weights


if __name__ == "__main__":
    import importlib
    mods = {
        "p6_dpo_loss_torch": [("dpo_loss", dpo_loss)],
        "p7_grpo_advantages_torch": [("grpo_advantages", grpo_advantages)],
        "p8_layernorm_backward_torch": [("layer_norm_backward", layer_norm_backward)],
        "p9_online_softmax_torch": [("online_softmax", online_softmax)],
        "p10_moe_router_torch": [("moe_top_k_gating", moe_top_k_gating)],
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
