"""
64. Minimum Path Sum  ·  Medium  ·  2-D Dynamic Programming
==========================================================
(run: python3 0064_minimum_path_sum.py)

Given an m x n grid of non-negative numbers, find a path from top-left to
bottom-right (moving only right/down) minimizing the sum of values.

  [[1,3,1],[1,5,1],[4,2,1]]  ->  7   (1->3->1->1->1)

PATTERN: DP where dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]); rolling
row. Time O(m*n), space O(n).
"""

from typing import List


def min_path_sum(grid: List[List[int]]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert min_path_sum([[1, 2, 3], [4, 5, 6]]) == 12
    assert min_path_sum([[5]]) == 5
    assert min_path_sum([[1, 2], [1, 1]]) == 3


if __name__ == "__main__":
    try:
        test()
        print("PASS  0064 min_path_sum")
    except NotImplementedError:
        print("----  0064 min_path_sum — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0064 min_path_sum: {e}")
