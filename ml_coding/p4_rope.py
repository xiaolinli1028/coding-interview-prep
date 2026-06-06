"""
Problem 4 — RoPE: Rotary Positional Embedding     (run: python3 p4_rope.py)
===========================================================================
Apply rotary embeddings (Su et al. 2021) to a (seq_len, dim) tensor. `dim` is
even. Treat the vector as dim/2 consecutive 2D pairs (indices (0,1), (2,3), ...).
Pair i is rotated by angle  theta_i * pos , where

      theta_i = base ** (-2i / dim),   i = 0 .. dim/2 - 1

Rotation of pair (a, b) by angle phi:
      a' = a*cos(phi) - b*sin(phi)
      b' = a*sin(phi) + b*cos(phi)

`positions[m]` is the absolute position of row m (supports a KV-cache where
rows don't start at 0).

KEY EQUATIONS                                    (pair i = dims 2i, 2i+1)
  theta_i = base^(-2i/dim) = base^(-i/half),   half = dim/2   # the two forms are equal
  phi = pos * theta_i
  a' = a*cos(phi) - b*sin(phi)
  b' = a*sin(phi) + b*cos(phi)
  property: <RoPE(q,m), RoPE(k,n)> depends only on (m - n)    # relative position
"""

import numpy as np


def apply_rope(x, positions, base=10000.0):
    """
    Args:
      x: np.ndarray (seq_len, dim), dim even.
      positions: np.ndarray (seq_len,) int absolute positions.
      base: float, RoPE base frequency (theta).
    Returns:
      np.ndarray (seq_len, dim), rotated.
    """
    x = np.asarray(x, dtype=np.float64)
    positions = np.asarray(positions, dtype=np.float64)
    half = x.shape[-1] // 2
    inv_freq = base ** (- np.arange(half) / half)
    angle = positions[:, None] * inv_freq[None, :]
    cos, sin = np.cos(angle), np.sin(angle)
    even, odd = x[:, 0::2], x[:, 1::2]
    output = np.zeros_like(x)
    output[:, 0::2] = cos * even - sin * odd
    output[:, 1::2] = sin * even + cos * odd
    return output


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    rng = np.random.default_rng(0)
    dim, n = 8, 6
    x = rng.standard_normal((n, dim))
    out = apply_rope(x, np.arange(n))
    # (a) position 0 is identity (all angles 0)
    assert np.allclose(out[0], x[0]), "pos 0 must be identity"
    # (b) norm preserved per 2D pair (rotation is orthogonal)
    for i in range(0, dim, 2):
        assert np.allclose(np.linalg.norm(out[:, i:i+2], axis=1),
                           np.linalg.norm(x[:, i:i+2], axis=1)), "norm not preserved"
    # (c) THE key property: <rope(q,m), rope(k,n)> depends only on (m-n)
    q = rng.standard_normal(dim); k = rng.standard_normal(dim)
    def rotdot(m, n):
        rq = apply_rope(q[None, :], np.array([m]))[0]
        rk = apply_rope(k[None, :], np.array([n]))[0]
        return rq @ rk
    assert np.isclose(rotdot(5, 2), rotdot(3, 0), atol=1e-9), "relative-position property broken"
    assert np.isclose(rotdot(7, 4), rotdot(3, 0), atol=1e-9), "relative-position property broken"


if __name__ == "__main__":
    try:
        test()
        print("PASS  p4 apply_rope")
    except NotImplementedError:
        print("----  p4 apply_rope (not implemented yet)")
    except AssertionError as e:
        print(f"FAIL  p4 apply_rope: {e}")
