"""
1143. Longest Common Subsequence  ·  Medium  ·  2-D Dynamic Programming
======================================================================
(run: python3 1143_longest_common_subsequence.py)

Return the length of the longest subsequence common to both strings (a
subsequence keeps order but need not be contiguous).

  "abcde", "ace"  ->  3   ("ace")

PATTERN: 2-D DP — dp[i][j] = dp[i-1][j-1]+1 if chars match, else
max(dp[i-1][j], dp[i][j-1]). Time O(m*n), space O(n) with rolling row.
"""


def longest_common_subsequence(text1: str, text2: str) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "abc") == 3
    assert longest_common_subsequence("abc", "def") == 0
    assert longest_common_subsequence("", "abc") == 0
    assert longest_common_subsequence("bsbininm", "jmjkbkjkv") == 1


if __name__ == "__main__":
    try:
        test()
        print("PASS  1143 longest_common_subsequence")
    except NotImplementedError:
        print("----  1143 longest_common_subsequence — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  1143 longest_common_subsequence: {e}")
