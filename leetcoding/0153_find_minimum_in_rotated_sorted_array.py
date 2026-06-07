"""
153. Find Minimum in Rotated Sorted Array  ·  Medium  ·  Binary Search
======================================================================
(run: python3 0153_find_minimum_in_rotated_sorted_array.py)

A sorted array of distinct values is rotated at an unknown pivot. Return the
minimum element. Must run in O(log n).

  [3,4,5,1,2]  ->  1

PATTERN: binary search — compare nums[mid] to nums[hi]; if greater, the min is to
the right, else at mid or left. Time O(log n), space O(1).
"""

from typing import List


def find_min(nums: List[int]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert find_min([3, 4, 5, 1, 2]) == 1
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0
    assert find_min([11, 13, 15, 17]) == 11    # not rotated
    assert find_min([2, 1]) == 1
    assert find_min([1]) == 1


if __name__ == "__main__":
    try:
        test()
        print("PASS  0153 find_min")
    except NotImplementedError:
        print("----  0153 find_min — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0153 find_min: {e}")
