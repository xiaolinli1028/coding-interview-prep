"""
Problem 11 — Top-p (Nucleus) Sampling             (run: python3 p11_top_p_nucleus.py)
=====================================================================================
Nucleus sampling (Holtzman et al. 2019). Given a probability distribution P over a
vocab and threshold p, keep the SMALLEST set of highest-probability tokens whose
cumulative probability reaches or exceeds p, then renormalize over that set:

    V^(p) = smallest prefix (by descending prob) with cumulative sum tau >= p
    P'(x) = P(x) / tau   if x in V^(p)   else 0

Return the new distribution P' in the ORIGINAL token order. You don't sample —
just return P'.

Example: P=[0.1, 0.5, 0.4], p=0.6 -> keep {0.5, 0.4} (tau=0.9) -> [0, 0.5, 0.4]/0.9.

KEY EQUATIONS
  V^(p) = smallest desc.-prob prefix with tau = sum_{x in V^(p)} P(x) >= p
  P'(x) = P(x)/tau   if x in V^(p)   else 0      (token crossing p is kept)
"""

import numpy as np


def nucleus(probs, p):
    """
    Args:
      probs: array-like (V,) a probability distribution (sums to 1).
      p: float in (0, 1], the nucleus threshold.
    Returns:
      np.ndarray (V,) renormalized distribution, zeros outside the nucleus,
      original order preserved.
    """
    probs = np.asarray(probs, dtype=np.float64)
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
        out = nucleus(probs, p)
        assert np.allclose(out, expected), f"nucleus({probs}, {p}) = {out}, want {expected}"
        assert np.isclose(np.sum(out), 1.0), f"must renormalize to 1, got {np.sum(out)}"


if __name__ == "__main__":
    try:
        test()
        print("PASS  p11 nucleus (top-p)")
    except NotImplementedError:
        print("----  p11 nucleus (top-p) — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p11 nucleus (top-p): {e}")
