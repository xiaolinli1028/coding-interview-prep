"""
Reference solutions (NumPy) for p6–p10.
Don't open until you've attempted them.

Verify:  python3 solutions_02.py
"""

import numpy as np


# P6 ──────────────────────────────────────────────────────────────────────────
def dpo_loss(policy_chosen_logps, policy_rejected_logps,
             ref_chosen_logps, ref_rejected_logps, beta=0.1):
    pi = np.asarray(policy_chosen_logps) - np.asarray(policy_rejected_logps)
    ref = np.asarray(ref_chosen_logps) - np.asarray(ref_rejected_logps)
    z = beta * (pi - ref)
    # -log sigmoid(z) = softplus(-z) = log(1 + exp(-z)) = logaddexp(0, -z)
    return float(np.mean(np.logaddexp(0.0, -z)))


# P7 ──────────────────────────────────────────────────────────────────────────
def grpo_advantages(rewards, eps=1e-8):
    rewards = np.asarray(rewards, dtype=np.float64)
    mean = rewards.mean(axis=-1, keepdims=True)
    std = rewards.std(axis=-1, keepdims=True)           # ddof=0
    return (rewards - mean) / (std + eps)


# P8 ──────────────────────────────────────────────────────────────────────────
def layer_norm_backward(dy, x, gamma, eps=1e-5):
    x = np.asarray(x, dtype=np.float64)
    mu = x.mean(-1, keepdims=True)
    var = x.var(-1, keepdims=True)                       # ddof=0
    inv = 1.0 / np.sqrt(var + eps)
    xhat = (x - mu) * inv
    dxhat = dy * gamma
    dx = inv * (dxhat
                - dxhat.mean(-1, keepdims=True)
                - xhat * (dxhat * xhat).mean(-1, keepdims=True))
    return dx


# P9 ──────────────────────────────────────────────────────────────────────────
def online_softmax(x, chunk_size):
    x = np.asarray(x, dtype=np.float64)
    m = -np.inf
    l = 0.0
    for start in range(0, len(x), chunk_size):
        chunk = x[start:start + chunk_size]
        m_new = max(m, float(chunk.max()))
        l = l * np.exp(m - m_new) + np.exp(chunk - m_new).sum()
        m = m_new
    return np.exp(x - m) / l


# P10 ─────────────────────────────────────────────────────────────────────────
def moe_top_k_gating(router_logits, k):
    router_logits = np.asarray(router_logits, dtype=np.float64)
    T = router_logits.shape[0]
    # top-k indices per row, sorted by logit descending
    order = np.argsort(-router_logits, axis=-1)[:, :k]   # (T, k)
    rows = np.arange(T)[:, None]
    top_logits = router_logits[rows, order]              # (T, k)
    e = np.exp(top_logits - top_logits.max(axis=-1, keepdims=True))
    weights = e / e.sum(axis=-1, keepdims=True)
    return order, weights


if __name__ == "__main__":
    import importlib
    mods = {
        "p6_dpo_loss": [("dpo_loss", dpo_loss)],
        "p7_grpo_advantages": [("grpo_advantages", grpo_advantages)],
        "p8_layernorm_backward": [("layer_norm_backward", layer_norm_backward)],
        "p9_online_softmax": [("online_softmax", online_softmax)],
        "p10_moe_router": [("moe_top_k_gating", moe_top_k_gating)],
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
