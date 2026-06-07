"""
45. Jump Game II  ·  Medium  ·  Greedy
======================================
(run: python3 0045_jump_game_ii.py)

Each nums[i] is the max jump length from index i. Return the minimum number of
jumps to reach the last index (a solution always exists).

  [2,3,1,1,4]  ->  2   (index 0 -> 1 -> 4)

PATTERN: greedy BFS-by-levels — track the current jump's farthest reach; when you
reach its end, take another jump. Time O(n), space O(1).
"""

from typing import List


def jump(nums: List[int]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert jump([2, 3, 1, 1, 4]) == 2
    assert jump([2, 3, 0, 1, 4]) == 2
    assert jump([0]) == 0
    assert jump([1, 2]) == 1
    assert jump([1, 1, 1, 1]) == 3


if __name__ == "__main__":
    try:
        test()
        print("PASS  0045 jump")
    except NotImplementedError:
        print("----  0045 jump — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0045 jump: {e}")
