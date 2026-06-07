"""
54. Spiral Matrix  ·  Medium  ·  Matrix
=======================================
(run: python3 0054_spiral_matrix.py)

Return all elements of the matrix in spiral (clockwise) order.

  [[1,2,3],[4,5,6],[7,8,9]] -> [1,2,3,6,9,8,7,4,5]

PATTERN: maintain four boundaries (top, bottom, left, right); walk right, down,
left, up, shrinking the boundary after each pass. Guard against re-walking a single
remaining row/column. Time O(m*n).
"""

from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    f = spiral_order
    assert f([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert f([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == \
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert f([[1]]) == [1]
    assert f([[1, 2], [3, 4]]) == [1, 2, 4, 3]
    assert f([[1], [2], [3]]) == [1, 2, 3], "single column"


if __name__ == "__main__":
    try:
        test()
        print("PASS  0054 spiral_order")
    except NotImplementedError:
        print("----  0054 spiral_order — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0054 spiral_order: {e}")
