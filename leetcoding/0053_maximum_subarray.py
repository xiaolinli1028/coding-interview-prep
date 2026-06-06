"""
53. Maximum Subarray  ·  Medium  ·  DP (Kadane)
===============================================
(run: python3 0053_maximum_subarray.py)

Return the largest sum of any contiguous non-empty subarray of `nums`.

  [-2,1,-3,4,-1,2,1,-5,4] -> 6  (subarray [4,-1,2,1])

PATTERN: Kadane. best_ending_here = max(x, best_ending_here + x); track the global
max. Intuition: extend the running subarray only while it helps. Time O(n).
"""

from typing import List


def max_sub_array(nums: List[int]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    f = max_sub_array
    assert f([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert f([1]) == 1
    assert f([5, 4, -1, 7, 8]) == 23
    assert f([-1]) == -1, "single negative"
    assert f([-3, -1, -2]) == -1, "all negative -> least negative element"


if __name__ == "__main__":
    try:
        test()
        print("PASS  0053 max_sub_array")
    except NotImplementedError:
        print("----  0053 max_sub_array — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0053 max_sub_array: {e}")
