"""
994. Rotting Oranges  ·  Medium  ·  Graph (BFS)
===============================================
(run: python3 0994_rotting_oranges.py)

Grid cells: 0 empty, 1 fresh orange, 2 rotten. Each minute a rotten orange rots
its 4-adjacent fresh neighbors. Return minutes until none are fresh, or -1 if
some can never rot.

  [[2,1,1],[1,1,0],[0,1,1]]  ->  4

PATTERN: multi-source BFS from all initial rotten oranges, counting levels;
afterwards if any fresh remain, return -1. Time O(m*n).
"""

from typing import List


def oranges_rotting(grid: List[List[int]]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert oranges_rotting([[0, 2]]) == 0
    assert oranges_rotting([[0]]) == 0
    assert oranges_rotting([[1]]) == -1


if __name__ == "__main__":
    try:
        test()
        print("PASS  0994 oranges_rotting")
    except NotImplementedError:
        print("----  0994 oranges_rotting — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0994 oranges_rotting: {e}")
