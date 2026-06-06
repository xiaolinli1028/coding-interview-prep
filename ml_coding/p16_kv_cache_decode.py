"""
Problem 16 — KV-Cache Incremental Decoding        (run: python3 p16_kv_cache_decode.py)
=======================================================================================
At decode time you generate one token at a time. Recomputing attention over the
whole prefix every step is O(L^2) wasted work; instead you keep a KV CACHE: the keys
and values for all past tokens, and each new token only computes its own q/k/v,
APPENDS k/v to the cache, and attends over the cache.

Implement one decode step:
  1. append the current token's k, v to the cache  ->  K, V of length t+1
  2. attention of the current query over the full K, V
  3. return the output and the grown caches

Crucial subtlety: NO causal mask is needed here. The cache holds only positions
0..t-1 (the past), and the current token legitimately attends to all of them plus
itself. Causality is enforced by *what's in the cache*, not by a mask.

KEY EQUATIONS  (per head; current step t, head_dim d_h)
  K = concat(k_cache, k_t),   V = concat(v_cache, v_t)        # lengths t -> t+1
  scores = q_t K^T / sqrt(d_h)        # shape (n_head, 1, t+1), no mask
  out_t  = softmax(scores) V
Equivalence: running this step-by-step from an empty cache reproduces full
parallel causal attention over the whole sequence (the test checks exactly this).
"""

import numpy as np


def softmax(x):
    e = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e / np.sum(e, axis=-1, keepdims=True)


def kv_cache_decode_step(q_t, k_t, v_t, k_cache, v_cache):
    """
    One cached decode step.

    Args:
      q_t, k_t, v_t: np.ndarray (n_head, 1, head_dim) — current token's q/k/v.
      k_cache, v_cache: np.ndarray (n_head, t, head_dim) — past keys/values
                        (t may be 0 for the first token).
    Returns:
      out_t: np.ndarray (n_head, 1, head_dim) — attention output for this token.
      k_cache_new, v_cache_new: np.ndarray (n_head, t+1, head_dim) — grown caches.
    """
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def _prefill_causal(q, k, v):
    """Reference: full parallel causal attention over the whole sequence."""
    nh, seq, hd = q.shape
    scores = np.matmul(q, k.transpose(0, 2, 1)) / np.sqrt(hd)
    mask = np.triu(np.ones((seq, seq)), 1)
    scores = np.where(mask[None] == 1, -np.inf, scores)
    return np.matmul(softmax(scores), v)


def test():
    rng = np.random.default_rng(0)
    nh, seq, hd = 3, 6, 4
    q = rng.standard_normal((nh, seq, hd))
    k = rng.standard_normal((nh, seq, hd))
    v = rng.standard_normal((nh, seq, hd))

    ref = _prefill_causal(q, k, v)                 # (nh, seq, hd)

    # decode incrementally from an empty cache
    kc = np.zeros((nh, 0, hd))
    vc = np.zeros((nh, 0, hd))
    outs = []
    for t in range(seq):
        out_t, kc, vc = kv_cache_decode_step(
            q[:, t:t + 1], k[:, t:t + 1], v[:, t:t + 1], kc, vc)
        assert out_t.shape == (nh, 1, hd), out_t.shape
        assert kc.shape == (nh, t + 1, hd), kc.shape       # cache grows by 1 each step
        outs.append(out_t)
    incremental = np.concatenate(outs, axis=1)             # (nh, seq, hd)

    # the whole point: cached decode == parallel causal attention
    assert np.allclose(incremental, ref), \
        f"cached decode != prefill, max diff {np.abs(incremental - ref).max():.2e}"


if __name__ == "__main__":
    try:
        test()
        print("PASS  p16 kv_cache_decode_step")
    except NotImplementedError:
        print("----  p16 kv_cache_decode_step — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p16 kv_cache_decode_step: {e}")
