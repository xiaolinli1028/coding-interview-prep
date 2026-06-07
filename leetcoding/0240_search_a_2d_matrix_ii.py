"""
240. Search a 2D Matrix II  ·  Medium  ·  Matrix
================================================
(run: python3 0240_search_a_2d_matrix_ii.py)

Each row is sorted left-to-right and each column top-to-bottom. Return True if
target is present.

  matrix sorted both ways, target = 5  ->  True

PATTERN: start at the top-right corner; move left if too big, down if too small.
Time O(m+n), space O(1).
"""

from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    m = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    assert search_matrix(m, 5) is True
    assert search_matrix(m, 20) is False
    assert search_matrix([[1]], 1) is True
    assert search_matrix([[1]], 2) is False
    assert search_matrix(m, 30) is True


if __name__ == "__main__":
    try:
        test()
        print("PASS  0240 search_matrix")
    except NotImplementedError:
        print("----  0240 search_matrix — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0240 search_matrix: {e}")
