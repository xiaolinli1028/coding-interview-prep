"""
Problem 1 (PyTorch) — Top-k + Temperature Sampling   (run: python3 p1_top_k_temperature_torch.py)
=================================================================================================
Same spec as the NumPy version, but in PyTorch. Aim for idiomatic, vectorized
code that works on a batch of logits with shape (..., vocab) — NO python loops.

  - Temperature T: divide logits by T before softmax (T > 0).
  - Top-k: keep the k largest logits per row; others get probability 0.
  - Renormalize kept probabilities to sum to 1, preserving order.

PyTorch tools worth reaching for: torch.topk, Tensor.scatter_, torch.softmax,
torch.full_like. Handle k >= vocab (keep all).

KEY EQUATIONS
  scaled logits:  z_i / T          (T->0 sharpen, T->inf flatten)
  P_i = exp(z_i/T) / sum_{j in top-k} exp(z_j/T)   for i in top-k, else 0
"""

import torch


def top_k_temperature(logits, k, temperature=1.0):
    """
    Args:
      logits: torch.Tensor (..., vocab) raw scores.
      k: int.
      temperature: float > 0.
    Returns:
      torch.Tensor (..., vocab) probabilities; each row sums to 1, zeros outside top-k.
    """
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    # 1D: top-2, T=1 over [2,1,0,-1]
    out = top_k_temperature(torch.tensor([2.0, 1.0, 0.0, -1.0]), k=2, temperature=1.0)
    exp = torch.softmax(torch.tensor([2.0, 1.0]), 0)
    assert torch.allclose(out, torch.tensor([exp[0], exp[1], 0.0, 0.0])), out
    # temperature flattens
    out = top_k_temperature(torch.tensor([2.0, 0.0]), k=2, temperature=2.0)
    assert torch.allclose(out, torch.softmax(torch.tensor([1.0, 0.0]), 0)), out
    # k >= vocab keeps all
    out = top_k_temperature(torch.tensor([1.0, 2.0, 3.0]), k=10)
    assert torch.isclose(out.sum(), torch.tensor(1.0)) and (out > 0).all(), out
    # BATCHED (..., vocab): each row keeps exactly k and sums to 1
    batch = torch.tensor([[5.0, 4.0, 3.0, 2.0, 1.0],
                          [1.0, 2.0, 3.0, 4.0, 5.0]])
    out = top_k_temperature(batch, k=3)
    assert out.shape == batch.shape, out.shape
    assert torch.equal((out > 0).sum(dim=-1), torch.tensor([3, 3])), out
    assert torch.allclose(out.sum(dim=-1), torch.ones(2)), out


if __name__ == "__main__":
    try:
        test()
        print("PASS  p1 top_k_temperature (torch)")
    except NotImplementedError:
        print("----  p1 top_k_temperature (torch) — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p1 top_k_temperature (torch): {e}")
