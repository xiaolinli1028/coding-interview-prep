"""
Problem 10 (PyTorch) — Top-k MoE Router / Gating   (run: python3 p10_moe_router_torch.py)
=========================================================================================
Same spec as the NumPy version, in PyTorch. Route each token to its top-k experts;
gating weights are a softmax over only the selected k logits (rows sum to 1).

Return:
  expert_indices: (T, k) long — chosen expert ids, highest-logit first.
  gating_weights: (T, k) float — softmax over the k selected logits.

torch.topk returns (values, indices) already sorted descending — softmax the
values over the last dim.

KEY EQUATIONS
  T = top-k(g)                                  # selected expert set per token
  w_i = exp(g_i) / sum_{j in T} exp(g_j)        for i in T
"""

import torch


def moe_top_k_gating(router_logits, k):
    """
    Args:
      router_logits: torch.Tensor (T, E).
      k: int.
    Returns:
      (expert_indices (T, k) long, gating_weights (T, k) float)
    """
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    idx, w = moe_top_k_gating(torch.tensor([[1.0, 3.0, 2.0, 0.0]]), k=2)
    assert idx.shape == (1, 2) and w.shape == (1, 2), (idx.shape, w.shape)
    assert idx[0].tolist() == [1, 2], idx
    assert torch.allclose(w[0], torch.softmax(torch.tensor([3.0, 2.0]), -1)), w
    torch.manual_seed(0)
    logits = torch.randn(6, 8)
    idx, w = moe_top_k_gating(logits, k=3)
    assert idx.shape == (6, 3) and w.shape == (6, 3)
    assert torch.allclose(w.sum(dim=-1), torch.ones(6), atol=1e-6), w.sum(dim=-1)
    for t in range(6):
        true_top = set(torch.topk(logits[t], 3).indices.tolist())
        assert set(idx[t].tolist()) == true_top, (t, idx[t], true_top)
    assert idx.dtype == torch.long, idx.dtype


if __name__ == "__main__":
    try:
        test()
        print("PASS  p10 moe_top_k_gating (torch)")
    except NotImplementedError:
        print("----  p10 moe_top_k_gating (torch) — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p10 moe_top_k_gating (torch): {e}")
