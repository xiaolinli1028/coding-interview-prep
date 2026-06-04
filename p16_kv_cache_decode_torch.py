"""
Problem 16 (PyTorch) — KV-Cache Incremental Decoding   (run: python3 p16_kv_cache_decode_torch.py)
=================================================================================================
Same spec as the NumPy version, in PyTorch. One decode step: append the current
token's k/v to the cache, attend the current query over the full cache, return the
output and grown caches. No causal mask needed — the cache holds only the past.

KEY EQUATIONS  (per head; current step t, head_dim d_h)
  K = cat(k_cache, k_t),   V = cat(v_cache, v_t)             # lengths t -> t+1
  scores = q_t K^T / sqrt(d_h)        # (n_head, 1, t+1), no mask
  out_t  = softmax(scores) V

Tools: torch.cat(..., dim=1), torch.matmul, k.transpose(-2, -1), torch.softmax.
"""

import math
import torch


def kv_cache_decode_step(q_t, k_t, v_t, k_cache, v_cache):
    """
    Args:
      q_t, k_t, v_t: torch.Tensor (n_head, 1, head_dim).
      k_cache, v_cache: torch.Tensor (n_head, t, head_dim) (t may be 0).
    Returns:
      out_t: (n_head, 1, head_dim);  k_cache_new, v_cache_new: (n_head, t+1, head_dim)
    """
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def _prefill_causal(q, k, v):
    nh, seq, hd = q.shape
    scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(hd)
    mask = torch.triu(torch.ones(seq, seq), diagonal=1).bool()
    scores = scores.masked_fill(mask.unsqueeze(0), float("-inf"))
    return torch.matmul(torch.softmax(scores, dim=-1), v)


def test():
    torch.manual_seed(0)
    nh, seq, hd = 3, 6, 4
    q = torch.randn(nh, seq, hd, dtype=torch.float64)
    k = torch.randn(nh, seq, hd, dtype=torch.float64)
    v = torch.randn(nh, seq, hd, dtype=torch.float64)

    ref = _prefill_causal(q, k, v)

    kc = torch.zeros(nh, 0, hd, dtype=torch.float64)
    vc = torch.zeros(nh, 0, hd, dtype=torch.float64)
    outs = []
    for t in range(seq):
        out_t, kc, vc = kv_cache_decode_step(
            q[:, t:t + 1], k[:, t:t + 1], v[:, t:t + 1], kc, vc)
        assert out_t.shape == (nh, 1, hd), out_t.shape
        assert kc.shape == (nh, t + 1, hd), kc.shape
        outs.append(out_t)
    incremental = torch.cat(outs, dim=1)

    assert torch.allclose(incremental, ref, atol=1e-10), \
        f"cached decode != prefill, max diff {(incremental - ref).abs().max():.2e}"


if __name__ == "__main__":
    try:
        test()
        print("PASS  p16 kv_cache_decode_step (torch)")
    except NotImplementedError:
        print("----  p16 kv_cache_decode_step (torch) — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p16 kv_cache_decode_step (torch): {e}")
