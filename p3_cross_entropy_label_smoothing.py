"""
Problem 3 — Cross-Entropy with Label Smoothing   (run: python3 p3_cross_entropy_label_smoothing.py)
===================================================================================================
Mean cross-entropy over a batch with label smoothing (Szegedy et al. 2016).
For smoothing eps and V classes, the soft target for true class y is:

      t_j = (1 - eps) * 1[j == y]  +  eps / V

Loss for one example = -sum_j t_j * log_softmax(logits)_j .  Return the MEAN
over the batch. Use a numerically stable log-softmax — do NOT do
np.log(softmax(...)) (log of tiny probs underflows; see the huge-logit test).

KEY EQUATIONS
  soft target:  t_j = (1 - eps) * 1[j == y] + eps / V
  loss:         L = -sum_j t_j * log_softmax(z)_j
  stable:       log_softmax(z) = z - logsumexp(z)
                logsumexp(z)   = m + log(sum(exp(z - m))),  m = max(z)
"""

import numpy as np


def cross_entropy_label_smoothing(logits, targets, smoothing=0.0):
    """
    Args:
      logits: np.ndarray (N, V)
      targets: np.ndarray (N,) int class indices in [0, V).
      smoothing: float in [0, 1).
    Returns:
      float, mean loss over the N examples.
    """
    logits = np.asarray(logits, dtype=np.float64)
    targets = np.asarray(targets)
    k = targets.shape[-1]
    targets_smoothes = (1 - smoothing) * targets + smoothing / k
    
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    # no smoothing, single example
    loss = cross_entropy_label_smoothing(np.array([[2.0, 0.0]]), np.array([0]), 0.0)
    assert np.isclose(loss, 0.12692801, atol=1e-6), loss
    # smoothing=0.2
    loss = cross_entropy_label_smoothing(np.array([[2.0, 0.0]]), np.array([0]), 0.2)
    assert np.isclose(loss, 0.32692801, atol=1e-6), loss
    # stable with huge logits (np.log(softmax) would underflow)
    loss = cross_entropy_label_smoothing(np.array([[1000.0, 0.0]]), np.array([1]), 0.0)
    assert np.isfinite(loss) and np.isclose(loss, 1000.0, atol=1e-3), loss
    # mean over batch
    loss = cross_entropy_label_smoothing(
        np.array([[2.0, 0.0], [0.0, 2.0]]), np.array([0, 1]), 0.0)
    assert np.isclose(loss, 0.12692801, atol=1e-6), loss


if __name__ == "__main__":
    try:
        test()
        print("PASS  p3 cross_entropy_label_smoothing")
    except NotImplementedError:
        print("----  p3 cross_entropy_label_smoothing (not implemented yet)")
    except AssertionError as e:
        print(f"FAIL  p3 cross_entropy_label_smoothing: {e}")
