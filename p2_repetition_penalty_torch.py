"""
Problem 2 (PyTorch) — Repetition Penalty on Logits   (run: python3 p2_repetition_penalty_torch.py)
==================================================================================================
CTRL-style penalty (Keskar et al. 2019), in PyTorch. Per seen token:

      logit -> logit / penalty   if logit > 0
      logit -> logit * penalty   if logit <= 0

Return a NEW tensor (don't mutate input). Vectorize with torch.where over the
gathered logits — avoid a python loop over token ids.

Tools: torch.tensor(ids), advanced indexing logits[ids], torch.where, .clone().
"""

import torch


def apply_repetition_penalty(logits, generated_ids, penalty):
    """
    Args:
      logits: torch.Tensor (vocab,)
      generated_ids: list[int] (may repeat).
      penalty: float >= 1.0
    Returns:
      torch.Tensor (vocab,) penalized logits.
    """
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    out = apply_repetition_penalty(torch.tensor([1.0, -1.0, 2.0]), [0, 2], 2.0)
    assert torch.allclose(out, torch.tensor([0.5, -1.0, 1.0])), out
    out = apply_repetition_penalty(torch.tensor([1.0, -1.0, 2.0]), [0, 1, 2], 2.0)
    assert torch.allclose(out, torch.tensor([0.5, -2.0, 1.0])), out
    # input not mutated
    src = torch.tensor([1.0, 2.0])
    _ = apply_repetition_penalty(src, [0], 3.0)
    assert torch.allclose(src, torch.tensor([1.0, 2.0])), "input mutated"
    # penalty=1 no-op
    out = apply_repetition_penalty(torch.tensor([1.0, -2.0]), [0, 1], 1.0)
    assert torch.allclose(out, torch.tensor([1.0, -2.0])), out


if __name__ == "__main__":
    try:
        test()
        print("PASS  p2 repetition_penalty (torch)")
    except NotImplementedError:
        print("----  p2 repetition_penalty (torch) — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p2 repetition_penalty (torch): {e}")
