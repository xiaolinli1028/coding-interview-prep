"""
Problem 9 (PyTorch) — Online (Streaming) Softmax   (run: python3 p9_online_softmax_torch.py)
============================================================================================
FlashAttention's numerical core, in PyTorch. Stream the vector in chunks of size
chunk_size, maintaining running max m and running denominator l:
    m_new = max(m, chunk.max())
    l     = l * exp(m - m_new) + sum(exp(chunk - m_new))
    m     = m_new
Then softmax(x)_i = exp(x_i - m) / l. Must match a standard stable softmax for any
chunk_size, including very large values.

KEY EQUATIONS  (streaming over blocks; running max m, denominator l)
  m' = max(m, max(block))
  l  = l * exp(m - m') + sum_j exp(x_j - m')
  m  = m'
  final:  softmax(x)_i = exp(x_i - m) / l
"""

import torch


def online_softmax(x, chunk_size):
    """
    Args:
      x: torch.Tensor (n,) 1-D logits.
      chunk_size: int >= 1.
    Returns:
      torch.Tensor (n,) probabilities summing to 1.
    """
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    torch.manual_seed(0)
    x = torch.randn(17, dtype=torch.float64)
    ref = torch.softmax(x, dim=-1)
    for cs in (1, 4, 17, 100):
        out = online_softmax(x, cs)
        assert torch.allclose(out, ref, atol=1e-12), f"chunk_size={cs}"
        assert torch.isclose(out.sum(), torch.tensor(1.0, dtype=torch.float64)), out.sum()
    big = torch.tensor([1000.0, 1001.0, 999.0, 1000.5], dtype=torch.float64)
    out = online_softmax(big, 2)
    assert torch.isfinite(out).all() and torch.allclose(out, torch.softmax(big, -1)), out


if __name__ == "__main__":
    try:
        test()
        print("PASS  p9 online_softmax (torch)")
    except NotImplementedError:
        print("----  p9 online_softmax (torch) — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p9 online_softmax (torch): {e}")
