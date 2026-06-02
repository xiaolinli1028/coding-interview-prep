"""
Problem 6 — DPO Loss                              (run: python3 p6_dpo_loss.py)
==============================================================================
Direct Preference Optimization loss (Rafailov et al. 2023). Given per-example
sequence log-probabilities for the CHOSEN and REJECTED responses under both the
trained policy and the frozen reference model, the loss is:

    pi_logratio  = logp_policy_chosen   - logp_policy_rejected
    ref_logratio = logp_ref_chosen      - logp_ref_rejected
    L = -log sigmoid( beta * (pi_logratio - ref_logratio) )

Return the MEAN loss over the batch.

Numerical-stability note: -log sigmoid(z) = softplus(-z) = log(1 + exp(-z)).
Use np.logaddexp(0, -z) rather than np.log(sigmoid(z)) to avoid overflow.
"""

import numpy as np


def dpo_loss(policy_chosen_logps, policy_rejected_logps,
             ref_chosen_logps, ref_rejected_logps, beta=0.1):
    """
    Args:
      policy_chosen_logps:   np.ndarray (B,)  sum log p_theta(chosen)
      policy_rejected_logps: np.ndarray (B,)
      ref_chosen_logps:      np.ndarray (B,)  sum log p_ref(chosen)
      ref_rejected_logps:    np.ndarray (B,)
      beta: float, KL strength.
    Returns:
      float, mean DPO loss.
    """
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    z = np.zeros(4)
    # policy == ref everywhere -> logits 0 -> loss = -log sigmoid(0) = log 2
    loss = dpo_loss(z, z, z, z, beta=0.1)
    assert np.isclose(loss, np.log(2)), loss
    # single example, beta=1: policy prefers chosen by 1 nat, ref neutral
    loss = dpo_loss(np.array([0.0]), np.array([-1.0]),
                    np.array([0.0]), np.array([0.0]), beta=1.0)
    assert np.isclose(loss, np.logaddexp(0, -1.0)), loss   # softplus(-1)=0.31326
    # lower loss when policy separates chosen/rejected more than ref does
    good = dpo_loss(np.array([0.0]), np.array([-2.0]),
                    np.array([0.0]), np.array([0.0]), beta=1.0)
    bad = dpo_loss(np.array([0.0]), np.array([2.0]),
                   np.array([0.0]), np.array([0.0]), beta=1.0)
    assert good < bad, (good, bad)
    # stability with large margins
    loss = dpo_loss(np.array([100.0]), np.array([-100.0]),
                    np.array([0.0]), np.array([0.0]), beta=1.0)
    assert np.isfinite(loss) and loss >= 0, loss


if __name__ == "__main__":
    try:
        test()
        print("PASS  p6 dpo_loss")
    except NotImplementedError:
        print("----  p6 dpo_loss (not implemented yet)")
    except AssertionError as e:
        print(f"FAIL  p6 dpo_loss: {e}")
