"""
560. Subarray Sum Equals K  ·  Medium  ·  Prefix Sum
====================================================
(run: python3 0560_subarray_sum_equals_k.py)

Return the number of contiguous subarrays summing to k.

  [1,1,1], k = 2  ->  2

PATTERN: running prefix sum + hash map of prefix-sum counts; each step adds the
count of (prefix - k) seen so far. Time O(n), space O(n).
"""

from typing import List


def subarray_sum(nums: List[int], k: int) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert subarray_sum([1, 1, 1], 2) == 2
    assert subarray_sum([1, 2, 3], 3) == 2
    assert subarray_sum([1], 0) == 0
    assert subarray_sum([-1, -1, 1], 0) == 1
    assert subarray_sum([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4


if __name__ == "__main__":
    try:
        test()
        print("PASS  0560 subarray_sum")
    except NotImplementedError:
        print("----  0560 subarray_sum — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0560 subarray_sum: {e}")
