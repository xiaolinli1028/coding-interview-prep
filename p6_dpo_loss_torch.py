"""
Problem 6 (PyTorch) — DPO Loss                    (run: python3 p6_dpo_loss_torch.py)
=====================================================================================
Same spec as the NumPy version, in PyTorch.

    pi_logratio  = policy_chosen_logps  - policy_rejected_logps
    ref_logratio = ref_chosen_logps     - ref_rejected_logps
    L = -log sigmoid( beta * (pi_logratio - ref_logratio) )   (mean over batch)

Use torch.nn.functional.logsigmoid for stability (NOT torch.log(torch.sigmoid(...))).
Keep it differentiable — don't detach the policy logps.
"""

import torch


def dpo_loss(policy_chosen_logps, policy_rejected_logps,
             ref_chosen_logps, ref_rejected_logps, beta=0.1):
    """
    Args:
      *_logps: torch.Tensor (B,) sequence log-probs.
      beta: float.
    Returns:
      torch.Tensor scalar, mean DPO loss.
    """
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    import torch.nn.functional as F
    z = torch.zeros(4)
    loss = dpo_loss(z, z, z, z, beta=0.1)
    assert torch.isclose(loss, torch.log(torch.tensor(2.0))), loss
    # match an explicit reference
    pc = torch.tensor([0.0]); pr = torch.tensor([-1.0])
    rc = torch.tensor([0.0]); rr = torch.tensor([0.0])
    ref = -F.logsigmoid(torch.tensor([1.0])).mean()
    assert torch.isclose(dpo_loss(pc, pr, rc, rr, beta=1.0), ref), "ref mismatch"
    # gradient flows to the policy logps
    pc = torch.tensor([0.5], requires_grad=True)
    pr = torch.tensor([0.2], requires_grad=True)
    out = dpo_loss(pc, pr, torch.zeros(1), torch.zeros(1), beta=0.1)
    out.backward()
    assert pc.grad is not None and pr.grad is not None, "no gradient"
    assert out.ndim == 0, "loss must be scalar"
    # stability with large margins
    big = dpo_loss(torch.tensor([100.0]), torch.tensor([-100.0]),
                   torch.zeros(1), torch.zeros(1), beta=1.0)
    assert torch.isfinite(big) and big >= 0, big


if __name__ == "__main__":
    try:
        test()
        print("PASS  p6 dpo_loss (torch)")
    except NotImplementedError:
        print("----  p6 dpo_loss (torch) — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p6 dpo_loss (torch): {e}")
