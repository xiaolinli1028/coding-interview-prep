"""
Problem 15 (PyTorch) — Speculative Decoding Acceptance   (run: python3 p15_speculative_decoding_torch.py)
========================================================================================================
Same spec as the NumPy version, in PyTorch.
  acceptance_prob(p, q, token) = min(1, p[token] / q[token])
  residual_distribution(p, q)  = normalize(clamp(p - q, min=0)); fall back to p if it sums to 0.

Tools: torch.clamp(min=0), torch.clamp(max=1.0) / torch.minimum.

KEY EQUATIONS
  accept x with prob:  min(1, p(x) / q(x))
  residual:  p_res(i) = max(p(i) - q(i), 0) / sum_j max(p(j) - q(j), 0)
  (this keeps the output distribution exactly equal to sampling from p)
"""

import torch


def acceptance_prob(p_target, q_draft, token):
    """min(1, p_target[token] / q_draft[token]) as a scalar tensor."""
    # TODO
    raise NotImplementedError


def residual_distribution(p_target, q_draft):
    """Normalized clamp(p_target - q_draft, min=0); fall back to p_target if it sums to 0."""
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    p = torch.tensor([0.5, 0.3, 0.2])
    q = torch.tensor([0.4, 0.4, 0.2])
    assert torch.isclose(torch.as_tensor(acceptance_prob(p, q, 0)).float(), torch.tensor(1.0))
    assert torch.isclose(torch.as_tensor(acceptance_prob(p, q, 1)).float(), torch.tensor(0.75))
    assert torch.isclose(torch.as_tensor(acceptance_prob(p, q, 2)).float(), torch.tensor(1.0))
    r = residual_distribution(p, q)
    assert torch.allclose(r, torch.tensor([1.0, 0.0, 0.0])) and torch.isclose(r.sum(), torch.tensor(1.0)), r
    p3 = torch.tensor([0.5, 0.4, 0.1]); q3 = torch.tensor([0.1, 0.1, 0.8])
    r3 = residual_distribution(p3, q3)
    assert torch.allclose(r3, torch.tensor([0.4 / 0.7, 0.3 / 0.7, 0.0])), r3
    # degenerate p==q -> fall back to p
    assert torch.allclose(residual_distribution(p, p), p), "should fall back to p"


if __name__ == "__main__":
    try:
        test()
        print("PASS  p15 speculative_decoding (torch)")
    except NotImplementedError:
        print("----  p15 speculative_decoding (torch) — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p15 speculative_decoding (torch): {e}")
