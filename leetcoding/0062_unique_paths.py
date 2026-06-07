"""
62. Unique Paths  ·  Medium  ·  2-D Dynamic Programming
=======================================================
(run: python3 0062_unique_paths.py)

A robot at the top-left of an m x n grid can only move right or down. Return how
many distinct paths reach the bottom-right.

  m = 3, n = 7  ->  28

PATTERN: DP grid where dp[i][j] = dp[i-1][j] + dp[i][j-1]; a single rolling row
suffices. Time O(m*n), space O(n).
"""


def unique_paths(m: int, n: int) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert unique_paths(3, 7) == 28
    assert unique_paths(3, 2) == 3
    assert unique_paths(1, 1) == 1
    assert unique_paths(1, 10) == 1
    assert unique_paths(3, 3) == 6


if __name__ == "__main__":
    try:
        test()
        print("PASS  0062 unique_paths")
    except NotImplementedError:
        print("----  0062 unique_paths — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0062 unique_paths: {e}")
