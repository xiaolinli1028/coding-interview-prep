"""
Reference solutions (PyTorch) for p16+ torch versions.
Don't open until you've attempted them.

Verify:  python3 solutions_04_torch.py
"""

import math
import torch


# P16 ─────────────────────────────────────────────────────────────────────────
def kv_cache_decode_step(q_t, k_t, v_t, k_cache, v_cache):
    k = torch.cat([k_cache, k_t], dim=1)           # (n_head, t+1, head_dim)
    v = torch.cat([v_cache, v_t], dim=1)
    hd = q_t.shape[-1]
    scores = torch.matmul(q_t, k.transpose(-2, -1)) / math.sqrt(hd)
    out = torch.matmul(torch.softmax(scores, dim=-1), v)
    return out, k, v


if __name__ == "__main__":
    import importlib
    mods = {
        "p16_kv_cache_decode_torch": [("kv_cache_decode_step", kv_cache_decode_step)],
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
