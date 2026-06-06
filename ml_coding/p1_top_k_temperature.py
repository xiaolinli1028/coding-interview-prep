"""
Problem 1 — Top-k + Temperature Sampling          (run: python3 p1_top_k_temperature.py)
=========================================================================================
Given raw logits, apply temperature scaling then restrict to the top-k highest
logits, and return a renormalized probability distribution (zeros elsewhere).
Output order must match input order.

  - Temperature T: divide logits by T BEFORE softmax. T -> 0 sharpens,
    T -> inf flattens. Assume T > 0.
  - Top-k: keep the k largest logits; everything else gets probability 0.
  - Renormalize the kept probabilities so they sum to 1.

Edge cases: k >= len(logits) (keep all); ties at the boundary (keep exactly k,
breaking ties by index is fine).

KEY EQUATIONS
  scaled logits:  z_i / T          (T->0 sharpen, T->inf flatten)
  P_i = exp(z_i/T) / sum_{j in top-k} exp(z_j/T)   for i in top-k, else 0
"""

import numpy as np


def softmax(x):
    """Numerically stable softmax over the last axis."""
    e = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e / np.sum(e, axis=-1, keepdims=True)


def top_k_temperature(logits, k, temperature=1.0):
    """
    Args:
      logits: np.ndarray (vocab,) raw scores (can be negative).
      k: int, number of highest-logit tokens to keep.
      temperature: float > 0.
    Returns:
      np.ndarray (vocab,) probabilities summing to 1, zeros outside top-k.
    """
    logits = np.asarray(logits, dtype=np.float64) / temperature
    k = min(k, logits.shape[-1])
    kept_indices = np.argpartition(logits, -k)[-k:]
    top_k_logits = np.full_like(logits, -np.inf)
    top_k_logits[kept_indices] = logits[kept_indices]
    return softmax(top_k_logits)
    

    


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    # top-2, T=1 over [2,1,0,-1] -> softmax([2,1]) on first two, rest 0
    out = top_k_temperature(np.array([2.0, 1.0, 0.0, -1.0]), k=2, temperature=1.0)
    exp = np.array([np.exp(2), np.exp(1), 0, 0]); exp = exp / exp.sum()
    assert np.allclose(out, exp), f"{out} != {exp}"
    # temperature flattens: [2,0], T=2 -> softmax([1,0])
    out = top_k_temperature(np.array([2.0, 0.0]), k=2, temperature=2.0)
    assert np.allclose(out, softmax(np.array([1.0, 0.0]))), out
    # k >= vocab keeps everything; sums to 1
    out = top_k_temperature(np.array([1.0, 2.0, 3.0]), k=10, temperature=1.0)
    assert np.isclose(out.sum(), 1.0) and np.all(out > 0), out
    # exactly k nonzero entries
    out = top_k_temperature(np.array([5.0, 4.0, 3.0, 2.0, 1.0]), k=3, temperature=1.0)
    assert np.sum(out > 0) == 3 and np.isclose(out.sum(), 1.0), out


if __name__ == "__main__":
    try:
        test()
        print("PASS  p1 top_k_temperature")
    except NotImplementedError:
        print("----  p1 top_k_temperature (not implemented yet)")
    except AssertionError as e:
        print(f"FAIL  p1 top_k_temperature: {e}")
