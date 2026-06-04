"""
Problem 5 — Grouped-Query Attention (GQA / MQA)   (run: python3 p5_grouped_query_attention.py)
==============================================================================================
Causal multi-head attention where K/V have FEWER heads than Q (GQA). Each group
of (n_head / n_kv_head) query heads shares one K/V head. n_kv_head == 1 is MQA;
n_kv_head == n_head is vanilla MHA.

KV-cache aware: q_seq_len may be < kv_seq_len. Query row i corresponds to
absolute position (kv_seq_len - q_seq_len + i) and may attend to key cols
0 .. that position.

  scores = (Q @ K^T) / sqrt(head_dim)   then add causal mask, softmax, @ V.

KEY EQUATIONS
  repeat each KV head r = n_head / n_kv times, then standard attention:
  Attn(Q,K,V) = softmax(Q K^T / sqrt(d_h) + M) V
  causal M_ij = 0 if j <= i_abs else -inf;   i_abs = kv_len - q_len + i
"""

import numpy as np


def softmax(x):
    e = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e / np.sum(e, axis=-1, keepdims=True)


def grouped_query_attention(q, k, v):
    """
    Args:
      q: np.ndarray (n_head,    q_seq_len,  head_dim)
      k: np.ndarray (n_kv_head, kv_seq_len, head_dim)
      v: np.ndarray (n_kv_head, kv_seq_len, head_dim)
         (n_head % n_kv_head == 0; q_seq_len <= kv_seq_len)
    Returns:
      np.ndarray (n_head, q_seq_len, head_dim)
    """
    q = np.asarray(q, dtype=np.float64)
    k = np.asarray(k, dtype=np.float64)
    v = np.asarray(v, dtype=np.float64)
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def _ref_mha_causal(q, k, v):
    nh, ql, hd = q.shape
    kl = k.shape[1]
    out = np.zeros_like(q)
    for h in range(nh):
        s = q[h] @ k[h].T / np.sqrt(hd)
        mask = np.triu(np.ones((ql, kl)), k=kl - ql + 1)
        s = np.where(mask == 1, -np.inf, s)
        out[h] = softmax(s) @ v[h]
    return out


def test():
    rng = np.random.default_rng(1)
    nh, kl, hd = 4, 5, 6
    # (a) n_kv_head == n_head equals vanilla MHA
    q = rng.standard_normal((nh, kl, hd))
    k = rng.standard_normal((nh, kl, hd))
    v = rng.standard_normal((nh, kl, hd))
    assert np.allclose(grouped_query_attention(q, k, v), _ref_mha_causal(q, k, v)), "MHA case"
    # (b) MQA: 1 kv head shared by all q heads
    kk = rng.standard_normal((1, kl, hd)); vv = rng.standard_normal((1, kl, hd))
    ref = _ref_mha_causal(q, np.repeat(kk, nh, 0), np.repeat(vv, nh, 0))
    assert np.allclose(grouped_query_attention(q, kk, vv), ref), "MQA case"
    # (c) GQA with KV-cache: q_seq_len=1 (decode step), kv_seq_len=5
    q1 = rng.standard_normal((nh, 1, hd))
    k2 = rng.standard_normal((2, kl, hd)); v2 = rng.standard_normal((2, kl, hd))
    out = grouped_query_attention(q1, k2, v2)
    assert out.shape == (nh, 1, hd), out.shape
    s = q1[0, 0] @ k2[0].T / np.sqrt(hd)   # head 0 -> kv group 0
    assert np.allclose(out[0, 0], softmax(s) @ v2[0]), "decode-step value mismatch"


if __name__ == "__main__":
    try:
        test()
        print("PASS  p5 grouped_query_attention")
    except NotImplementedError:
        print("----  p5 grouped_query_attention (not implemented yet)")
    except AssertionError as e:
        print(f"FAIL  p5 grouped_query_attention: {e}")
