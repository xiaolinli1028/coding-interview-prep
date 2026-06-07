"""
55. Jump Game  ·  Medium  ·  Greedy
===================================
(run: python3 0055_jump_game.py)

Each nums[i] is the max jump length from index i. Return True if you can reach the
last index starting from index 0.

  [2,3,1,1,4] -> True       [3,2,1,0,4] -> False

PATTERN: greedy reachability — track the farthest index reachable so far; if you
ever stand on an index beyond that, you're stuck. Time O(n).
"""

from typing import List


def can_jump(nums: List[int]) -> bool:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    f = can_jump
    assert f([2, 3, 1, 1, 4]) is True
    assert f([3, 2, 1, 0, 4]) is False
    assert f([0]) is True, "already at the last index"
    assert f([2, 0, 0]) is True
    assert f([1, 0, 1, 0]) is False


if __name__ == "__main__":
    try:
        test()
        print("PASS  0055 can_jump")
    except NotImplementedError:
        print("----  0055 can_jump — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0055 can_jump: {e}")
