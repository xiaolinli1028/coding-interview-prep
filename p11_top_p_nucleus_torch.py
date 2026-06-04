"""
Problem 11 (PyTorch) — Top-p (Nucleus) Sampling   (run: python3 p11_top_p_nucleus_torch.py)
===========================================================================================
Same spec as the NumPy version, in PyTorch. Keep the smallest set of highest-prob
tokens whose cumulative probability >= p, renormalize over that set, original order.

Tools: torch.sort(descending=True), torch.cumsum, a boolean keep-mask, then scatter
the mask back to original positions. Watch the boundary: the token that *crosses* the
threshold must be KEPT.

KEY EQUATIONS
  V^(p) = smallest desc.-prob prefix with tau = sum_{x in V^(p)} P(x) >= p
  P'(x) = P(x)/tau   if x in V^(p)   else 0      (token crossing p is kept)
"""

import torch


def nucleus(probs, p):
    """
    Args:
      probs: torch.Tensor (V,) probability distribution.
      p: float in (0, 1].
    Returns:
      torch.Tensor (V,) renormalized distribution, zeros outside the nucleus.
    """
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    cases = [
        ([0.0, 0.0, 1.0], 0.9, [0.0, 0.0, 1.0]),
        ([0.1, 0.4, 0.4, 0.1], 0.5, [0.0, 0.5, 0.5, 0.0]),
        ([0.0, 0.1, 0.9], 0.1, [0.0, 0.0, 1.0]),
        ([0.3, 0.3, 0.1, 0.2, 0.1], 1.0, [0.3, 0.3, 0.1, 0.2, 0.1]),
        ([0.1, 0.5, 0.4], 0.6, [0.0, 0.5 / 0.9, 0.4 / 0.9]),
    ]
    for probs, p, expected in cases:
        out = nucleus(torch.tensor(probs), p)
        assert torch.allclose(out, torch.tensor(expected), atol=1e-6), \
            f"nucleus({probs}, {p}) = {out.tolist()}, want {expected}"
        assert torch.isclose(out.sum(), torch.tensor(1.0)), out.sum()


if __name__ == "__main__":
    try:
        test()
        print("PASS  p11 nucleus (top-p, torch)")
    except NotImplementedError:
        print("----  p11 nucleus (top-p, torch) — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p11 nucleus (top-p, torch): {e}")
