"""
Problem 4 (PyTorch) — RoPE: Rotary Positional Embedding   (run: python3 p4_rope_torch.py)
=========================================================================================
RoPE (Su et al. 2021) in PyTorch. dim is even; treat the vector as dim/2
consecutive 2D pairs (0,1),(2,3),... Pair i rotates by angle theta_i * pos with
theta_i = base ** (-2i/dim), i = 0..dim/2-1. Rotation of (a,b) by phi:
      a' = a*cos - b*sin ,  b' = a*sin + b*cos

positions[m] is the absolute position of row m (KV-cache friendly).

Tools: torch.arange, broadcasting (positions[:,None] * inv_freq[None,:]),
torch.cos/sin, slicing x[:, 0::2] / x[:, 1::2], torch.empty_like.
"""

import torch


def apply_rope(x, positions, base=10000.0):
    """
    Args:
      x: torch.Tensor (seq_len, dim), dim even.
      positions: torch.Tensor (seq_len,) int absolute positions.
      base: float.
    Returns:
      torch.Tensor (seq_len, dim), rotated.
    """
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    torch.manual_seed(0)
    dim, n = 8, 6
    x = torch.randn(n, dim)
    out = apply_rope(x, torch.arange(n))
    # (a) position 0 is identity
    assert torch.allclose(out[0], x[0], atol=1e-6), "pos 0 must be identity"
    # (b) norm preserved per 2D pair (rotation orthogonal)
    for i in range(0, dim, 2):
        assert torch.allclose(out[:, i:i+2].norm(dim=1), x[:, i:i+2].norm(dim=1), atol=1e-6), "norm"
    # (c) relative-position property: <rope(q,m), rope(k,n)> depends only on (m-n)
    q = torch.randn(dim); k = torch.randn(dim)
    def rotdot(m, n):
        rq = apply_rope(q[None, :], torch.tensor([m]))[0]
        rk = apply_rope(k[None, :], torch.tensor([n]))[0]
        return (rq @ rk).item()
    assert abs(rotdot(5, 2) - rotdot(3, 0)) < 1e-5, "relative-position broken"
    assert abs(rotdot(7, 4) - rotdot(3, 0)) < 1e-5, "relative-position broken"


if __name__ == "__main__":
    try:
        test()
        print("PASS  p4 apply_rope (torch)")
    except NotImplementedError:
        print("----  p4 apply_rope (torch) — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p4 apply_rope (torch): {e}")
