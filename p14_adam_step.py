"""
Problem 14 — Adam Optimizer Step                  (run: python3 p14_adam_step.py)
================================================================================
Implement ONE Adam update (Kingma & Ba 2014), including bias correction:

    m = b1*m + (1-b1)*g                  # 1st moment (mean)
    v = b2*v + (1-b2)*g^2                # 2nd moment (uncentered variance)
    m_hat = m / (1 - b1^t)              # bias-corrected
    v_hat = v / (1 - b2^t)
    param = param - lr * m_hat / (sqrt(v_hat) + eps)

`t` is the 1-based step number (the step you are taking now). Return the updated
param and the new (m, v). Note: this is Adam, NOT AdamW — no decoupled weight decay.

KEY EQUATIONS  (t = 1-based step)
  m = b1*m + (1-b1)*g;     v = b2*v + (1-b2)*g^2
  m_hat = m/(1-b1^t);      v_hat = v/(1-b2^t)
  param -= lr * m_hat / (sqrt(v_hat) + eps)
"""

import numpy as np


def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    Args:
      param: np.ndarray, current parameters.
      grad:  np.ndarray, gradient dL/dparam.
      m, v:  np.ndarray, running 1st/2nd moments (zeros initially).
      t: int, 1-based timestep.
      lr, beta1, beta2, eps: floats.
    Returns:
      (param_new, m_new, v_new) all np.ndarray.
    """
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    # single step from zero state, hand-computed
    p = np.array([1.0]); g = np.array([0.1])
    m = np.zeros(1); v = np.zeros(1)
    p1, m1, v1 = adam_step(p, g, m, v, t=1, lr=0.1)
    # m=0.01, v=1e-5; m_hat=0.1, v_hat=0.01; step = 0.1 * 0.1/(0.1+1e-8) ~ 0.1
    assert np.allclose(m1, 0.01) and np.allclose(v1, 1e-5), (m1, v1)
    assert np.allclose(p1, 1.0 - 0.1 * 0.1 / (0.1 + 1e-8)), p1
    # input not mutated
    assert np.allclose(p, [1.0]) and np.allclose(m, [0.0]), "inputs mutated"
    # convergence: minimize f(x)=sum(x^2), grad=2x, should approach 0
    x = np.array([5.0, -3.0]); m = np.zeros(2); vv = np.zeros(2)
    for step in range(1, 4001):
        x, m, vv = adam_step(x, 2 * x, m, vv, t=step, lr=0.05)
    assert np.all(np.abs(x) < 1e-2), f"did not converge: {x}"


if __name__ == "__main__":
    try:
        test()
        print("PASS  p14 adam_step")
    except NotImplementedError:
        print("----  p14 adam_step — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p14 adam_step: {e}")
