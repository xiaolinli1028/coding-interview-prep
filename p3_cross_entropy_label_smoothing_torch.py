"""
Problem 3 (PyTorch) — Cross-Entropy with Label Smoothing   (run: python3 p3_cross_entropy_label_smoothing_torch.py)
==================================================================================================================
Implement it FROM SCRATCH in PyTorch (no F.cross_entropy / F.nll_loss). For
smoothing eps over V classes, the soft target for true class y is
t_j = (1-eps)*1[j==y] + eps/V, and the per-example loss is
-sum_j t_j * log_softmax(logits)_j. Return the mean over the batch.

You MAY use torch.log_softmax (that's the stable primitive). The test checks
your result against torch.nn.functional.cross_entropy(..., label_smoothing=eps),
so it must match PyTorch's own definition.
"""

import torch


def cross_entropy_label_smoothing(logits, targets, smoothing=0.0):
    """
    Args:
      logits: torch.Tensor (N, V)
      targets: torch.Tensor (N,) int64 class indices.
      smoothing: float in [0, 1).
    Returns:
      torch.Tensor scalar, mean loss.
    """
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    import torch.nn.functional as F
    torch.manual_seed(0)
    logits = torch.randn(8, 5)
    targets = torch.randint(0, 5, (8,))
    for eps in (0.0, 0.1, 0.3):
        mine = cross_entropy_label_smoothing(logits, targets, eps)
        ref = F.cross_entropy(logits, targets, label_smoothing=eps)
        assert torch.allclose(mine, ref, atol=1e-6), f"eps={eps}: {mine.item()} vs {ref.item()}"
    # stable with huge logits
    loss = cross_entropy_label_smoothing(torch.tensor([[1000.0, 0.0]]), torch.tensor([1]), 0.0)
    assert torch.isfinite(loss) and torch.isclose(loss, torch.tensor(1000.0), atol=1e-2), loss
    # returns a scalar tensor
    assert cross_entropy_label_smoothing(logits, targets, 0.1).ndim == 0


if __name__ == "__main__":
    try:
        test()
        print("PASS  p3 cross_entropy_label_smoothing (torch)")
    except NotImplementedError:
        print("----  p3 cross_entropy_label_smoothing (torch) — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p3 cross_entropy_label_smoothing (torch): {e}")
