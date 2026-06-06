"""
Problem 7 (PyTorch) — GRPO Group-Relative Advantages   (run: python3 p7_grpo_advantages_torch.py)
================================================================================================
Same spec as the NumPy version, in PyTorch.

    A_i = (r_i - mean(r_group)) / (std(r_group) + eps)        per group (per row)

Use POPULATION std (unbiased=False, i.e. ddof=0). Constant-reward groups must
return all zeros (eps guard). Watch out: torch.std defaults to unbiased=True.

KEY EQUATIONS  (per group of K samples)
  A_i = (r_i - mean(r)) / (std(r) + eps)        # population std (unbiased=False)
"""

import torch


def grpo_advantages(rewards, eps=1e-8):
    """
    Args:
      rewards: torch.Tensor (num_groups, group_size).
      eps: float.
    Returns:
      torch.Tensor (num_groups, group_size) advantages.
    """
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    out = grpo_advantages(torch.tensor([[0.0, 0.0, 0.0, 4.0]]))
    exp = (torch.tensor([0.0, 0.0, 0.0, 4.0]) - 1.0) / torch.tensor(3.0).sqrt()
    assert torch.allclose(out, exp, atol=1e-6), out
    torch.manual_seed(0)
    r = torch.randn(3, 5)
    out = grpo_advantages(r)
    assert torch.allclose(out.mean(dim=-1), torch.zeros(3), atol=1e-6), out.mean(dim=-1)
    # population std of the normalized rows ~ 1
    assert torch.allclose(out.std(dim=-1, unbiased=False), torch.ones(3), atol=1e-5), out
    out = grpo_advantages(torch.tensor([[5.0, 5.0, 5.0]]))
    assert torch.allclose(out, torch.zeros(1, 3)) and torch.isfinite(out).all(), out


if __name__ == "__main__":
    try:
        test()
        print("PASS  p7 grpo_advantages (torch)")
    except NotImplementedError:
        print("----  p7 grpo_advantages (torch) — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p7 grpo_advantages (torch): {e}")
