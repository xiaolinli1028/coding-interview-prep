"""
215. Kth Largest Element in an Array  ·  Medium  ·  Heap
========================================================
(run: python3 0215_kth_largest_element_in_an_array.py)

Return the kth largest element (in sorted order, not distinct) in nums.

  [3,2,1,5,6,4], k = 2  ->  5

PATTERN: maintain a size-k min-heap of the largest seen so far; the root is the
answer (or quickselect for O(n) average). Time O(n log k), space O(k).
"""

from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert find_kth_largest([1], 1) == 1
    assert find_kth_largest([2, 1], 2) == 1
    assert find_kth_largest([7, 7, 7], 2) == 7


if __name__ == "__main__":
    try:
        test()
        print("PASS  0215 find_kth_largest")
    except NotImplementedError:
        print("----  0215 find_kth_largest — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0215 find_kth_largest: {e}")
