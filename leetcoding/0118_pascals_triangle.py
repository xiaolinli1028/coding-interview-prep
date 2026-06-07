"""
118. Pascal's Triangle  ·  Easy  ·  Dynamic Programming
=======================================================
(run: python3 0118_pascals_triangle.py)

Return the first numRows of Pascal's triangle.

  numRows = 5  ->  [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

PATTERN: each row built from the previous — interior entry [j] = prev[j-1] +
prev[j]; edges are 1. Time O(numRows^2), space O(numRows^2).
"""

from typing import List


def generate(numRows: int) -> List[List[int]]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert generate(1) == [[1]]
    assert generate(2) == [[1], [1, 1]]
    assert generate(0) == []


if __name__ == "__main__":
    try:
        test()
        print("PASS  0118 generate")
    except NotImplementedError:
        print("----  0118 generate — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0118 generate: {e}")
