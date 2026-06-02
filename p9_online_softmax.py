"""
Problem 9 — Online (Streaming) Softmax            (run: python3 p9_online_softmax.py)
=====================================================================================
The numerical core of FlashAttention: compute softmax over a long vector in a
single streaming pass over fixed-size chunks, WITHOUT ever materializing the full
exp() array, while staying numerically stable.

Maintain two running statistics as you consume chunks:
    m = running max of all values seen so far
    l = running sum of exp(value - m)
When a new chunk arrives with its own max m_chunk, the correct rescale is:
    m_new = max(m, m_chunk)
    l     = l * exp(m - m_new) + sum(exp(chunk - m_new))
    m     = m_new
After the pass, the normalizer is l and softmax(x)_i = exp(x_i - m) / l.

Result must equal a standard stable softmax to floating precision, for any
chunk_size, including with very large values (where naive exp overflows).
"""

import numpy as np


def online_softmax(x, chunk_size):
    """
    Args:
      x: np.ndarray (n,) 1-D logits.
      chunk_size: int, streaming block size (>= 1).
    Returns:
      np.ndarray (n,) softmax probabilities (sum to 1).
    """
    x = np.asarray(x, dtype=np.float64)
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def _ref_softmax(x):
    e = np.exp(x - np.max(x))
    return e / e.sum()


def test():
    rng = np.random.default_rng(0)
    x = rng.standard_normal(17)
    for cs in (1, 4, 17, 100):
        out = online_softmax(x, cs)
        assert np.allclose(out, _ref_softmax(x)), f"chunk_size={cs}"
        assert np.isclose(out.sum(), 1.0), f"chunk_size={cs} sum={out.sum()}"
    # numerical stability: huge values would overflow a naive exp()
    big = np.array([1000.0, 1001.0, 999.0, 1000.5])
    out = online_softmax(big, 2)
    assert np.all(np.isfinite(out)) and np.allclose(out, _ref_softmax(big)), out


if __name__ == "__main__":
    try:
        test()
        print("PASS  p9 online_softmax")
    except NotImplementedError:
        print("----  p9 online_softmax (not implemented yet)")
    except AssertionError as e:
        print(f"FAIL  p9 online_softmax: {e}")
