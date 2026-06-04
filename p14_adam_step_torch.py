"""
Problem 14 (PyTorch) — Adam Optimizer Step        (run: python3 p14_adam_step_torch.py)
=======================================================================================
One Adam update (Kingma & Ba 2014) with bias correction, in PyTorch tensor ops
(don't use torch.optim — implement the math). Same formulas as the NumPy version;
t is the 1-based step. Return (param_new, m_new, v_new). The test cross-checks the
first step against torch.optim.Adam.

KEY EQUATIONS  (t = 1-based step)
  m = b1*m + (1-b1)*g;     v = b2*v + (1-b2)*g^2
  m_hat = m/(1-b1^t);      v_hat = v/(1-b2^t)
  param -= lr * m_hat / (sqrt(v_hat) + eps)
"""

import torch


def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    Args:
      param, grad, m, v: torch.Tensor (same shape).
      t: int, 1-based timestep.
      lr, beta1, beta2, eps: floats.
    Returns:
      (param_new, m_new, v_new)
    """
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    # cross-check first step against torch.optim.Adam
    torch.manual_seed(0)
    w0 = torch.randn(3, 4, dtype=torch.float64)
    g = torch.randn(3, 4, dtype=torch.float64)

    p = w0.clone().requires_grad_(True)
    opt = torch.optim.Adam([p], lr=0.01)
    p.grad = g.clone()
    opt.step()

    mine, m1, v1 = adam_step(w0.clone(), g.clone(),
                             torch.zeros_like(w0), torch.zeros_like(w0),
                             t=1, lr=0.01)
    assert torch.allclose(mine, p.detach(), atol=1e-10), \
        f"differs from torch.optim.Adam, max {(mine - p.detach()).abs().max():.2e}"

    # convergence on f(x)=sum(x^2)
    x = torch.tensor([5.0, -3.0], dtype=torch.float64)
    m = torch.zeros(2, dtype=torch.float64); vv = torch.zeros(2, dtype=torch.float64)
    for step in range(1, 4001):
        x, m, vv = adam_step(x, 2 * x, m, vv, t=step, lr=0.05)
    assert torch.all(x.abs() < 1e-2), f"did not converge: {x}"


if __name__ == "__main__":
    try:
        test()
        print("PASS  p14 adam_step (torch)")
    except NotImplementedError:
        print("----  p14 adam_step (torch) — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p14 adam_step (torch): {e}")
