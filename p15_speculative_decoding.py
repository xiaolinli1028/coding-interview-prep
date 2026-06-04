"""
Problem 15 — Speculative Decoding Acceptance       (run: python3 p15_speculative_decoding.py)
=============================================================================================
Speculative / assisted decoding (Leviathan et al. 2023; Chen et al. 2023). A small
DRAFT model proposes token x sampled from q; the big TARGET model gives distribution
p. To keep the output distribution EXACTLY equal to sampling from p, you:

  1. Accept x with probability  min(1, p(x) / q(x)).
  2. If rejected, sample a replacement from the residual distribution
        p_res(i) = max(p(i) - q(i), 0) / sum_j max(p(j) - q(j), 0).

Implement both pieces (the deterministic math — no RNG needed). For the degenerate
case where the residual sums to 0, fall back to returning p unchanged.

KEY EQUATIONS
  accept x with prob:  min(1, p(x) / q(x))
  residual:  p_res(i) = max(p(i) - q(i), 0) / sum_j max(p(j) - q(j), 0)
  (this keeps the output distribution exactly equal to sampling from p)
"""

import numpy as np


def acceptance_prob(p_target, q_draft, token):
    """min(1, p_target[token] / q_draft[token])."""
    p_target = np.asarray(p_target, dtype=np.float64)
    q_draft = np.asarray(q_draft, dtype=np.float64)
    # TODO
    raise NotImplementedError


def residual_distribution(p_target, q_draft):
    """Normalized max(p_target - q_draft, 0); fall back to p_target if it sums to 0."""
    p_target = np.asarray(p_target, dtype=np.float64)
    q_draft = np.asarray(q_draft, dtype=np.float64)
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    p = np.array([0.5, 0.3, 0.2])
    q = np.array([0.4, 0.4, 0.2])
    # acceptance
    assert np.isclose(acceptance_prob(p, q, 0), 1.0), "p>q -> always accept"
    assert np.isclose(acceptance_prob(p, q, 1), 0.75), "0.3/0.4"
    assert np.isclose(acceptance_prob(p, q, 2), 1.0), "equal -> accept"
    # residual: max(p-q,0) = [0.1, 0, 0] -> [1, 0, 0]
    r = residual_distribution(p, q)
    assert np.allclose(r, [1.0, 0.0, 0.0]), r
    assert np.isclose(r.sum(), 1.0)
    # a richer residual
    p2 = np.array([0.6, 0.1, 0.3]); q2 = np.array([0.2, 0.5, 0.3])
    r2 = residual_distribution(p2, q2)   # max = [0.4, 0, 0] -> [1,0,0]
    assert np.allclose(r2, [1.0, 0.0, 0.0]), r2
    p3 = np.array([0.5, 0.4, 0.1]); q3 = np.array([0.1, 0.1, 0.8])
    r3 = residual_distribution(p3, q3)   # max = [0.4, 0.3, 0] -> /0.7
    assert np.allclose(r3, [0.4 / 0.7, 0.3 / 0.7, 0.0]), r3
    # degenerate: p == q -> residual sums to 0 -> fall back to p
    r4 = residual_distribution(p, p)
    assert np.allclose(r4, p), r4


if __name__ == "__main__":
    try:
        test()
        print("PASS  p15 speculative_decoding")
    except NotImplementedError:
        print("----  p15 speculative_decoding — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p15 speculative_decoding: {e}")
