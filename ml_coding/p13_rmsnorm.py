"""
Problem 13 — RMSNorm                              (run: python3 p13_rmsnorm.py)
==============================================================================
Root Mean Square LayerNorm (Zhang & Sennrich 2019), used in LLaMA, T5, etc.
Unlike LayerNorm it does NOT subtract the mean and has no bias — just rescales by
the root-mean-square over the last axis, then applies a learned gain:

    rms = sqrt( mean(x^2) + eps )           # mean over last axis
    y   = (x / rms) * gamma

Why it matters: cheaper than LayerNorm (no mean / no recentering) and empirically
just as good — interviewers like the "why drop the mean?" discussion.

KEY EQUATIONS
  rms = sqrt( mean(x^2 over last dim) + eps )
  y   = (x / rms) * gamma            # no mean subtraction, no bias
"""

import numpy as np


def rms_norm(x, gamma, eps=1e-6):
    """
    Args:
      x: np.ndarray (..., D)
      gamma: np.ndarray (D,) learned scale.
      eps: float.
    Returns:
      np.ndarray (..., D)
    """
    x = np.asarray(x, dtype=np.float64)
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    # hand-computed: x=[3,4], mean(x^2)=12.5, rms=sqrt(12.5)=3.5355339
    out = rms_norm(np.array([3.0, 4.0]), np.ones(2), eps=0.0)
    assert np.allclose(out, np.array([3.0, 4.0]) / np.sqrt(12.5)), out
    # gamma scales per-feature
    out = rms_norm(np.array([3.0, 4.0]), np.array([2.0, 0.5]), eps=0.0)
    assert np.allclose(out, np.array([3.0, 4.0]) / np.sqrt(12.5) * np.array([2.0, 0.5])), out
    # batched (..., D): each row normalized independently
    rng = np.random.default_rng(0)
    x = rng.standard_normal((4, 6)); g = rng.standard_normal(6)
    out = rms_norm(x, g, eps=1e-6)
    ref = x / np.sqrt(np.mean(x**2, axis=-1, keepdims=True) + 1e-6) * g
    assert np.allclose(out, ref), "batched mismatch"
    # scale invariance (eps=0): scaling a row by c leaves the normalized output unchanged
    a = rms_norm(np.array([1.0, 2.0, 3.0]), np.ones(3), eps=0.0)
    b = rms_norm(np.array([10.0, 20.0, 30.0]), np.ones(3), eps=0.0)
    assert np.allclose(a, b), "should be invariant to input scale when eps=0"


if __name__ == "__main__":
    try:
        test()
        print("PASS  p13 rms_norm")
    except NotImplementedError:
        print("----  p13 rms_norm — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p13 rms_norm: {e}")
