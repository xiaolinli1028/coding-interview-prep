"""
Problem 5 (PyTorch) — Grouped-Query Attention (GQA / MQA)   (run: python3 p5_grouped_query_attention_torch.py)
=============================================================================================================
Causal GQA in PyTorch. K/V have fewer heads than Q; each group of
(n_head / n_kv_head) query heads shares one K/V head. n_kv_head==1 is MQA,
n_kv_head==n_head is MHA.

KV-cache aware: q_seq_len <= kv_seq_len. Query row i has absolute position
(kv_seq_len - q_seq_len + i) and attends to key cols 0..that position.

  scores = (Q @ K^T)/sqrt(head_dim) -> causal mask -> softmax -> @ V.

Tools: Tensor.repeat_interleave(rep, dim=0) to expand kv heads, transpose(-2,-1),
torch.triu for the mask, Tensor.masked_fill, torch.softmax. (Don't just call
F.scaled_dot_product_attention — implement it.)
"""

import math
import torch


def grouped_query_attention(q, k, v):
    """
    Args:
      q: torch.Tensor (n_head,    q_seq_len,  head_dim)
      k: torch.Tensor (n_kv_head, kv_seq_len, head_dim)
      v: torch.Tensor (n_kv_head, kv_seq_len, head_dim)
    Returns:
      torch.Tensor (n_head, q_seq_len, head_dim)
    """
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def _ref_mha_causal(q, k, v):
    nh, ql, hd = q.shape
    kl = k.shape[1]
    out = torch.zeros_like(q)
    for h in range(nh):
        s = q[h] @ k[h].T / math.sqrt(hd)
        mask = torch.triu(torch.ones(ql, kl), diagonal=kl - ql + 1).bool()
        s = s.masked_fill(mask, float("-inf"))
        out[h] = torch.softmax(s, dim=-1) @ v[h]
    return out


def test():
    torch.manual_seed(1)
    nh, kl, hd = 4, 5, 6
    # (a) MHA case: n_kv_head == n_head
    q = torch.randn(nh, kl, hd); k = torch.randn(nh, kl, hd); v = torch.randn(nh, kl, hd)
    assert torch.allclose(grouped_query_attention(q, k, v), _ref_mha_causal(q, k, v), atol=1e-5), "MHA"
    # (b) MQA: 1 kv head shared
    kk = torch.randn(1, kl, hd); vv = torch.randn(1, kl, hd)
    ref = _ref_mha_causal(q, kk.repeat_interleave(nh, 0), vv.repeat_interleave(nh, 0))
    assert torch.allclose(grouped_query_attention(q, kk, vv), ref, atol=1e-5), "MQA"
    # (c) GQA decode step: q_seq_len=1, kv_seq_len=5, n_kv_head=2
    q1 = torch.randn(nh, 1, hd)
    k2 = torch.randn(2, kl, hd); v2 = torch.randn(2, kl, hd)
    out = grouped_query_attention(q1, k2, v2)
    assert out.shape == (nh, 1, hd), out.shape
    s = q1[0, 0] @ k2[0].T / math.sqrt(hd)   # head 0 -> kv group 0
    assert torch.allclose(out[0, 0], torch.softmax(s, -1) @ v2[0], atol=1e-5), "decode value"


if __name__ == "__main__":
    try:
        test()
        print("PASS  p5 grouped_query_attention (torch)")
    except NotImplementedError:
        print("----  p5 grouped_query_attention (torch) — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  p5 grouped_query_attention (torch): {e}")
