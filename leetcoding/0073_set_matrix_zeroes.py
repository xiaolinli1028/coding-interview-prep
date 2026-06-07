"""
73. Set Matrix Zeroes  ·  Medium  ·  Matrix
===========================================
(run: python3 0073_set_matrix_zeroes.py)

If an element is 0, set its entire row and column to 0, IN PLACE.

  [[1,1,1],[1,0,1],[1,1,1]] -> [[1,0,1],[0,0,0],[1,0,1]]

PATTERN: don't allocate O(m+n) marker arrays if you can avoid it — use the first
row and first column as the markers (track separately whether row0/col0 themselves
need zeroing). O(1) extra space.
"""

from typing import List


def set_zeroes(matrix: List[List[int]]) -> None:
    """Modify matrix in place. Returns None."""
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    def run(m):
        set_zeroes(m)
        return m

    assert run([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    assert run([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]) == \
        [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    assert run([[1]]) == [[1]]
    assert run([[0]]) == [[0]]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0073 set_zeroes")
    except NotImplementedError:
        print("----  0073 set_zeroes — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0073 set_zeroes: {e}")
