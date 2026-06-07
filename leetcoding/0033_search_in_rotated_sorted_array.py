"""
33. Search in Rotated Sorted Array  ·  Medium  ·  Binary Search
===============================================================
(run: python3 0033_search_in_rotated_sorted_array.py)

A sorted array of distinct values is rotated at an unknown pivot. Return the
index of target, or -1. Must run in O(log n).

  [4,5,6,7,0,1,2], target = 0  ->  4

PATTERN: modified binary search — one half is always sorted; decide which half
holds the target by comparing endpoints. Time O(log n), space O(1).
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
    assert search([1], 1) == 0
    assert search([5, 1, 3], 5) == 0
    assert search([4, 5, 6, 7, 0, 1, 2], 6) == 2


if __name__ == "__main__":
    try:
        test()
        print("PASS  0033 search")
    except NotImplementedError:
        print("----  0033 search — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0033 search: {e}")
