"""
Problem 12 (PyTorch) — Multi-Head Attention from Scratch   (run: python3 p12_multi_head_attention_torch.py)
==========================================================================================================
Causal multi-head self-attention end to end, in PyTorch. Same spec as NumPy:

    Q = x @ w_q,  K = x @ w_k,  V = x @ w_v
    reshape to (n_head, seq, head_dim); per-head scaled-dot-product with causal mask;
    concat -> (seq, d_model) -> @ w_o

Do it WITHOUT torch.nn.MultiheadAttention / F.scaled_dot_product_attention — the
point is to write the mechanism. Reshape with .view / .transpose, mask with
masked_fill, softmax over the key axis.

KEY EQUATIONS  (d_h = d_model / n_head; M causal: -inf above diagonal)
  Q = x W_q,  K = x W_k,  V = x W_v
  head_h = softmax(Q_h K_h^T / sqrt(d_h) + M) V_h
  MHA(x) = concat(head_1, ..., head_H) W_o
"""

import math
import torch


def multi_head_attention(x, w_q, w_k, w_v, w_o, n_head):
    """
    Args:
      x: (seq, d_model); w_q/w_k/w_v/w_o: (d_model, d_model); n_head: int.
    Returns:
      torch.Tensor (seq, d_model)
    """
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def _ref(x, w_q, w_k, w_v, w_o, n_head):
    seq, d = x.shape
    hd = d // n_head
    q, k, v = x @ w_q, x @ w_k, x @ w_v
    out = torch.zeros(seq, d, dtype=x.dtype)
    mask = torch.triu(torch.ones(seq, seq), diagonal=1).bool()
    for h in range(n_head):
        sl = slice(h * hd, (h + 1) * hd)
        s = q[:, sl] @ k[:, sl].T / math.sqrt(hd)
        s = s.masked_fill(mask, float("-inf"))
        out[:, sl] = torch.softmax(s, dim=-1) @ v[:, sl]
    return out @ w_o


def test():
    torch.manual_seed(0)
    seq, d, nh = 5, 8, 2
    x = torch.randn(seq, d, dtype=torch.float64)
    w_q, w_k, w_v, w_o = (torch.randn(d, d, dtype=torch.float64) for _ in range(4))

    out = multi_head_attention(x, w_q, w_k, w_v, w_o, nh)
    assert out.shape == (seq, d), out.shape
    assert torch.allclose(out, _ref(x, w_q, w_k, w_v, w_o, nh), atol=1e-9), "value mismatch"
    # causality: perturbing the last token must not change earlier outputs
    x2 = x.clone(); x2[-1] += 10.0
    out2 = multi_head_attention(x2, w_q, w_k, w_v, w_o, nh)
    assert torch.allclose(out[:-1], out2[:-1], atol=1e-9), "not causal"


if __name__ == "__main__":
    try:
        test()
        print("PASS  p12 multi_head_attention (torch)")
    except NotImplementedError:
        print("----  p12 multi_head_attention (torch) — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p12 multi_head_attention (torch): {e}")
