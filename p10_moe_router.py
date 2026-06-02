"""
Problem 10 — Top-k MoE Router / Gating            (run: python3 p10_moe_router.py)
==================================================================================
Mixture-of-Experts routing (Shazeer et al. 2017; Switch/Mixtral style). Each token
gets router logits over E experts. Route each token to its top-k experts and form
gating weights by softmax over ONLY the selected k logits (so the weights for the
chosen experts sum to 1 per token).

Return:
  expert_indices: (T, k) int — the chosen expert ids, highest-logit first.
  gating_weights: (T, k) float — softmax over the selected k logits, rows sum to 1.

Tip: take top-k along axis=-1, gather those logits, softmax over the k axis.
"""

import numpy as np


def moe_top_k_gating(router_logits, k):
    """
    Args:
      router_logits: np.ndarray (T, E) per-token logits over E experts.
      k: int, experts per token (1 <= k <= E).
    Returns:
      (expert_indices (T, k) int, gating_weights (T, k) float)
    """
    router_logits = np.asarray(router_logits, dtype=np.float64)
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def _softmax(x):
    e = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e / e.sum(axis=-1, keepdims=True)


def test():
    # single token, k=2: logits [1,3,2,0] -> experts [1,2], weights softmax([3,2])
    idx, w = moe_top_k_gating(np.array([[1.0, 3.0, 2.0, 0.0]]), k=2)
    assert idx.shape == (1, 2) and w.shape == (1, 2), (idx.shape, w.shape)
    assert list(idx[0]) == [1, 2], idx
    assert np.allclose(w[0], _softmax(np.array([3.0, 2.0]))), w
    # weights sum to 1 per token, for a batch
    rng = np.random.default_rng(0)
    logits = rng.standard_normal((6, 8))
    idx, w = moe_top_k_gating(logits, k=3)
    assert idx.shape == (6, 3) and w.shape == (6, 3)
    assert np.allclose(w.sum(axis=-1), 1.0), w.sum(axis=-1)
    # selected experts really are the k largest logits per row
    for t in range(6):
        true_top = set(np.argsort(-logits[t])[:3])
        assert set(idx[t].tolist()) == true_top, (t, idx[t], true_top)
    # k == E reduces to a full softmax over all experts
    idx, w = moe_top_k_gating(np.array([[2.0, 0.0, 1.0]]), k=3)
    assert np.allclose(np.sort(w[0]), np.sort(_softmax(np.array([2.0, 0.0, 1.0])))), w


if __name__ == "__main__":
    try:
        test()
        print("PASS  p10 moe_top_k_gating")
    except NotImplementedError:
        print("----  p10 moe_top_k_gating (not implemented yet)")
    except AssertionError as e:
        print(f"FAIL  p10 moe_top_k_gating: {e}")
