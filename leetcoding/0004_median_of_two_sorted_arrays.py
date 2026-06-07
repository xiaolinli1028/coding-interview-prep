"""
4. Median of Two Sorted Arrays  ·  Hard  ·  Binary Search
=========================================================
(run: python3 0004_median_of_two_sorted_arrays.py)

Return the median of two sorted arrays. Aim for O(log(m+n)).

  [1,3], [2]  ->  2.0
  [1,2], [3,4]  ->  2.5

PATTERN: binary search a partition of the smaller array so the left halves of
both arrays form the lower half of the merged array. Time O(log min(m,n)).
"""

from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
    assert find_median_sorted_arrays([], [1]) == 1.0
    assert find_median_sorted_arrays([2], []) == 2.0
    assert find_median_sorted_arrays([1, 2, 3], [4, 5, 6]) == 3.5
    assert find_median_sorted_arrays([0, 0], [0, 0]) == 0.0


if __name__ == "__main__":
    try:
        test()
        print("PASS  0004 find_median_sorted_arrays")
    except NotImplementedError:
        print("----  0004 find_median_sorted_arrays — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0004 find_median_sorted_arrays: {e}")
