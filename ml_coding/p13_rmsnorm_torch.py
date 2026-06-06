"""
Problem 13 (PyTorch) — RMSNorm                    (run: python3 p13_rmsnorm_torch.py)
=====================================================================================
RMSNorm (Zhang & Sennrich 2019), in PyTorch:
    rms = sqrt( mean(x^2, dim=-1) + eps )
    y   = (x / rms) * gamma
No mean subtraction, no bias. The test cross-checks against torch.nn.functional.rms_norm.

KEY EQUATIONS
  rms = sqrt( mean(x^2 over last dim) + eps )
  y   = (x / rms) * gamma            # no mean subtraction, no bias
"""

import torch


def rms_norm(x, gamma, eps=1e-6):
    """
    Args:
      x: torch.Tensor (..., D)
      gamma: torch.Tensor (D,)
      eps: float.
    Returns:
      torch.Tensor (..., D)
    """
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    import torch.nn.functional as F
    # hand-computed
    out = rms_norm(torch.tensor([3.0, 4.0]), torch.ones(2), eps=0.0)
    assert torch.allclose(out, torch.tensor([3.0, 4.0]) / torch.tensor(12.5).sqrt()), out
    # batched, cross-check against F.rms_norm
    torch.manual_seed(0)
    x = torch.randn(4, 6, dtype=torch.float64)
    g = torch.randn(6, dtype=torch.float64)
    out = rms_norm(x, g, eps=1e-6)
    ref = F.rms_norm(x, (6,), weight=g, eps=1e-6)
    assert torch.allclose(out, ref, atol=1e-9), "mismatch vs F.rms_norm"
    # scale invariance with eps=0
    a = rms_norm(torch.tensor([1.0, 2.0, 3.0]), torch.ones(3), eps=0.0)
    b = rms_norm(torch.tensor([10.0, 20.0, 30.0]), torch.ones(3), eps=0.0)
    assert torch.allclose(a, b), "should be scale-invariant when eps=0"


if __name__ == "__main__":
    try:
        test()
        print("PASS  p13 rms_norm (torch)")
    except NotImplementedError:
        print("----  p13 rms_norm (torch) — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p13 rms_norm (torch): {e}")
