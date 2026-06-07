"""
48. Rotate Image  ·  Medium  ·  Matrix
======================================
(run: python3 0048_rotate_image.py)

Rotate an n x n matrix 90 degrees clockwise, IN PLACE.

  [[1,2,3],[4,5,6],[7,8,9]] -> [[7,4,1],[8,5,2],[9,6,3]]

PATTERN: transpose, then reverse each row. (Equivalently rotate 4-cycles of cells
in place.) O(n^2) time, O(1) extra space.
"""

from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """Modify matrix in place. Returns None."""
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    def run(m):
        rotate(m)
        return m

    assert run([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert run([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]
    assert run([[1]]) == [[1]]
    assert run([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]) == \
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0048 rotate")
    except NotImplementedError:
        print("----  0048 rotate — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0048 rotate: {e}")
