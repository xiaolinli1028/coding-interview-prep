"""
198. House Robber  ·  Medium  ·  Dynamic Programming
====================================================
(run: python3 0198_house_robber.py)

You cannot rob two adjacent houses. Return the maximum money you can rob.

  [2,7,9,3,1]  ->  12   (2 + 9 + 1)

PATTERN: DP — best[i] = max(best[i-1], best[i-2] + nums[i]); roll two variables.
Time O(n), space O(1).
"""

from typing import List


def rob(nums: List[int]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([5]) == 5
    assert rob([]) == 0
    assert rob([2, 1, 1, 2]) == 4


if __name__ == "__main__":
    try:
        test()
        print("PASS  0198 rob")
    except NotImplementedError:
        print("----  0198 rob — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0198 rob: {e}")
