"""
74. Search a 2D Matrix  ·  Medium  ·  Binary Search
===================================================
(run: python3 0074_search_a_2d_matrix.py)

Each row is sorted left-to-right and the first value of each row is greater than
the last of the previous row. Return True if target is present.

  [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3  ->  True

PATTERN: treat the matrix as one sorted array of length m*n and binary search,
mapping a flat index to (row, col). Time O(log(m*n)), space O(1).
"""

from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert search_matrix(m, 3) is True
    assert search_matrix(m, 13) is False
    assert search_matrix(m, 60) is True
    assert search_matrix([[1]], 1) is True
    assert search_matrix([[1]], 2) is False


if __name__ == "__main__":
    try:
        test()
        print("PASS  0074 search_matrix")
    except NotImplementedError:
        print("----  0074 search_matrix — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0074 search_matrix: {e}")
