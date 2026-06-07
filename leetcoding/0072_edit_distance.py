"""
72. Edit Distance  ·  Medium  ·  2-D Dynamic Programming
=======================================================
(run: python3 0072_edit_distance.py)

Return the minimum number of insert / delete / replace operations to convert
word1 into word2.

  "horse", "ros"  ->  3

PATTERN: Levenshtein DP — dp[i][j] from match (diagonal) or 1 + min(insert,
delete, replace). Time O(m*n), space O(n) with rolling row.
"""


def min_distance(word1: str, word2: str) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert min_distance("horse", "ros") == 3
    assert min_distance("intention", "execution") == 5
    assert min_distance("", "abc") == 3
    assert min_distance("abc", "") == 3
    assert min_distance("abc", "abc") == 0


if __name__ == "__main__":
    try:
        test()
        print("PASS  0072 min_distance")
    except NotImplementedError:
        print("----  0072 min_distance — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0072 min_distance: {e}")
