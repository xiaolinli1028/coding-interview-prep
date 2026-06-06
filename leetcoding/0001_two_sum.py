"""
1. Two Sum  ·  Easy  ·  Hashing                   (run: python3 0001_two_sum.py)
================================================================================
Given an array of integers `nums` and an integer `target`, return the indices of
the two numbers that add up to `target`. Exactly one solution exists; you may not
use the same element twice. Return the indices in any order.

  nums = [2,7,11,15], target = 9  ->  [0,1]   (2 + 7)

PATTERN: one-pass hash map. For each x, check if (target - x) was already seen.
Time O(n), space O(n).
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    def ok(nums, target, res):
        assert len(res) == 2 and res[0] != res[1], res
        assert nums[res[0]] + nums[res[1]] == target, (nums, target, res)

    ok([2, 7, 11, 15], 9, two_sum([2, 7, 11, 15], 9))
    ok([3, 2, 4], 6, two_sum([3, 2, 4], 6))
    ok([3, 3], 6, two_sum([3, 3], 6))            # duplicate values
    ok([-1, -2, -3, -4, -5], -8, two_sum([-1, -2, -3, -4, -5], -8))  # negatives


if __name__ == "__main__":
    try:
        test()
        print("PASS  0001 two_sum")
    except NotImplementedError:
        print("----  0001 two_sum — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0001 two_sum: {e}")
