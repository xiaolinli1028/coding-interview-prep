"""
Problem 8 (PyTorch) — LayerNorm Backward Pass     (run: python3 p8_layernorm_backward_torch.py)
==============================================================================================
Implement the backward MANUALLY (no autograd inside your function). Forward, over
the last axis with population variance:
    xhat = (x - mean) / sqrt(var + eps);   y = gamma * xhat + beta
Given dy = dL/dy, return dx = dL/dx:
    dxhat = dy * gamma
    dx = (1/sqrt(var+eps)) * ( dxhat - mean(dxhat) - xhat * mean(dxhat * xhat) )

The test compares your dx against PyTorch autograd, so it must match exactly.
Operate on a plain tensor (no grad tracking needed inside the function).
"""

import torch


def layer_norm_backward(dy, x, gamma, eps=1e-5):
    """
    Args:
      dy: torch.Tensor (N, D) upstream gradient.
      x:  torch.Tensor (N, D) forward input.
      gamma: torch.Tensor (D,) scale.
      eps: float.
    Returns:
      torch.Tensor (N, D) dL/dx.
    """
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    torch.manual_seed(0)
    N, D = 4, 6
    x = torch.randn(N, D, dtype=torch.float64, requires_grad=True)
    gamma = torch.randn(D, dtype=torch.float64)
    beta = torch.randn(D, dtype=torch.float64)
    dy = torch.randn(N, D, dtype=torch.float64)
    eps = 1e-5

    # autograd reference
    mu = x.mean(-1, keepdim=True)
    var = x.var(-1, unbiased=False, keepdim=True)
    y = gamma * (x - mu) / torch.sqrt(var + eps) + beta
    y.backward(dy)
    ref_dx = x.grad

    mine = layer_norm_backward(dy, x.detach(), gamma, eps)
    assert torch.allclose(mine, ref_dx, atol=1e-9), \
        f"max diff {(mine - ref_dx).abs().max().item():.2e}"


if __name__ == "__main__":
    try:
        test()
        print("PASS  p8 layer_norm_backward (torch)")
    except NotImplementedError:
        print("----  p8 layer_norm_backward (torch) — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p8 layer_norm_backward (torch): {e}")
