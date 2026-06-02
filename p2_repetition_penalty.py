"""
Problem 2 — Repetition Penalty on Logits          (run: python3 p2_repetition_penalty.py)
=========================================================================================
CTRL-style repetition penalty (Keskar et al. 2019). Before sampling the next
token, penalize tokens already in the generated sequence. Per penalized token:

      logit  ->  logit / penalty     if logit > 0
      logit  ->  logit * penalty     if logit <= 0

(penalty > 1 pushes any seen token's logit toward / below zero.)
Return a NEW array; do not mutate the input. Each seen token penalized once.
"""

import numpy as np


def apply_repetition_penalty(logits, generated_ids, penalty):
    """
    Args:
      logits: np.ndarray (vocab,)
      generated_ids: list[int] token ids already generated (may repeat).
      penalty: float >= 1.0
    Returns:
      np.ndarray (vocab,) penalized logits.
    """
    logits = np.asarray(logits, dtype=np.float64)
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    out = apply_repetition_penalty(np.array([1.0, -1.0, 2.0]), [0, 2], penalty=2.0)
    assert np.allclose(out, [0.5, -1.0, 1.0]), out
    # negative logit multiplied; unseen token untouched
    out = apply_repetition_penalty(np.array([1.0, -1.0, 2.0]), [0, 1, 2], penalty=2.0)
    assert np.allclose(out, [0.5, -2.0, 1.0]), out
    # input not mutated
    src = np.array([1.0, 2.0])
    _ = apply_repetition_penalty(src, [0], penalty=3.0)
    assert np.allclose(src, [1.0, 2.0]), "input was mutated"
    # penalty=1 is a no-op
    out = apply_repetition_penalty(np.array([1.0, -2.0]), [0, 1], penalty=1.0)
    assert np.allclose(out, [1.0, -2.0]), out


if __name__ == "__main__":
    try:
        test()
        print("PASS  p2 repetition_penalty")
    except NotImplementedError:
        print("----  p2 repetition_penalty (not implemented yet)")
    except AssertionError as e:
        print(f"FAIL  p2 repetition_penalty: {e}")
