"""
Problem 8 — LayerNorm Backward Pass               (run: python3 p8_layernorm_backward.py)
=========================================================================================
Forward (over the last axis, D features):
    mu   = mean(x)
    var  = mean((x - mu)^2)            # population variance (ddof=0)
    xhat = (x - mu) / sqrt(var + eps)
    y    = gamma * xhat + beta

Given the upstream gradient dy = dL/dy, implement the gradient w.r.t. the INPUT,
dx = dL/dx, for each row independently. (beta does not affect dx.)

Derive it — the clean closed form is, with dxhat = dy * gamma and means over the
last axis:
    dx = (1/sqrt(var+eps)) * ( dxhat - mean(dxhat) - xhat * mean(dxhat * xhat) )

The test does a finite-difference gradient check, so any correct dx passes.
"""

import numpy as np


def layer_norm_backward(dy, x, gamma, eps=1e-5):
    """
    Args:
      dy: np.ndarray (N, D) upstream gradient dL/dy.
      x:  np.ndarray (N, D) the forward input.
      gamma: np.ndarray (D,) scale parameter.
      eps: float.
    Returns:
      np.ndarray (N, D) gradient dL/dx.
    """
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def _forward(x, gamma, beta, eps=1e-5):
    mu = x.mean(-1, keepdims=True)
    var = x.var(-1, keepdims=True)        # ddof=0
    return gamma * (x - mu) / np.sqrt(var + eps) + beta


def test():
    rng = np.random.default_rng(0)
    N, D = 4, 6
    x = rng.standard_normal((N, D))
    gamma = rng.standard_normal(D)
    beta = rng.standard_normal(D)
    dy = rng.standard_normal((N, D))
    eps = 1e-5

    analytic = layer_norm_backward(dy, x, gamma, eps)

    # finite-difference check on L = sum(dy * y)
    h = 1e-6
    numeric = np.zeros_like(x)
    for i in range(N):
        for j in range(D):
            xp = x.copy(); xp[i, j] += h
            xm = x.copy(); xm[i, j] -= h
            Lp = np.sum(dy * _forward(xp, gamma, beta, eps))
            Lm = np.sum(dy * _forward(xm, gamma, beta, eps))
            numeric[i, j] = (Lp - Lm) / (2 * h)

    assert np.allclose(analytic, numeric, atol=1e-5), \
        f"max diff {np.abs(analytic - numeric).max():.2e}"


if __name__ == "__main__":
    try:
        test()
        print("PASS  p8 layer_norm_backward")
    except NotImplementedError:
        print("----  p8 layer_norm_backward (not implemented yet)")
    except AssertionError as e:
        print(f"FAIL  p8 layer_norm_backward: {e}")
