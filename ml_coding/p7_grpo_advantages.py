"""
Problem 7 — GRPO Group-Relative Advantages        (run: python3 p7_grpo_advantages.py)
======================================================================================
Group Relative Policy Optimization (DeepSeek-R1 / DeepSeekMath). For each prompt
you sample a GROUP of K responses and score them. GRPO drops the value network
and uses the group's own statistics as the baseline:

    A_i = (r_i - mean(r_group)) / (std(r_group) + eps)

Compute advantages per group (per row). Use POPULATION std (ddof=0). A degenerate
group where all rewards are equal must yield all-zero advantages (the eps guard).

KEY EQUATIONS  (per group of K samples)
  A_i = (r_i - mean(r)) / (std(r) + eps)        # population std (ddof=0)
"""

import numpy as np


def grpo_advantages(rewards, eps=1e-8):
    """
    Args:
      rewards: np.ndarray (num_groups, group_size) scalar rewards.
      eps: float, guard for zero-variance groups.
    Returns:
      np.ndarray (num_groups, group_size) normalized advantages.
    """
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    # known group [0,0,0,4]: mean=1, std=sqrt(3)=1.7320508
    out = grpo_advantages(np.array([[0.0, 0.0, 0.0, 4.0]]))
    exp = (np.array([0, 0, 0, 4.0]) - 1.0) / np.sqrt(3.0)
    assert np.allclose(out, exp), out
    # advantages are zero-mean within each group
    rng = np.random.default_rng(0)
    r = rng.standard_normal((3, 5))
    out = grpo_advantages(r)
    assert np.allclose(out.mean(axis=-1), 0.0, atol=1e-8), out.mean(axis=-1)
    # and approximately unit std per group
    assert np.allclose(out.std(axis=-1), 1.0, atol=1e-6), out.std(axis=-1)
    # constant-reward group -> all zeros (no div-by-zero)
    out = grpo_advantages(np.array([[5.0, 5.0, 5.0]]))
    assert np.allclose(out, 0.0), out
    assert np.all(np.isfinite(out))


if __name__ == "__main__":
    try:
        test()
        print("PASS  p7 grpo_advantages")
    except NotImplementedError:
        print("----  p7 grpo_advantages (not implemented yet)")
    except AssertionError as e:
        print(f"FAIL  p7 grpo_advantages: {e}")
