"""
Reference solutions (NumPy) for p16+.
Don't open until you've attempted them.

Verify:  python3 solutions_04.py
"""

import numpy as np


def softmax(x):
    e = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e / np.sum(e, axis=-1, keepdims=True)


# P16 ─────────────────────────────────────────────────────────────────────────
def kv_cache_decode_step(q_t, k_t, v_t, k_cache, v_cache):
    k = np.concatenate([k_cache, k_t], axis=1)     # (n_head, t+1, head_dim)
    v = np.concatenate([v_cache, v_t], axis=1)
    hd = q_t.shape[-1]
    scores = np.matmul(q_t, k.transpose(0, 2, 1)) / np.sqrt(hd)   # (n_head, 1, t+1)
    out = np.matmul(softmax(scores), v)            # (n_head, 1, head_dim)
    return out, k, v


if __name__ == "__main__":
    import importlib
    mods = {
        "p16_kv_cache_decode": [("kv_cache_decode_step", kv_cache_decode_step)],
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
