"""
35. Search Insert Position  ·  Easy  ·  Binary Search
=====================================================
(run: python3 0035_search_insert_position.py)

Given a sorted array of distinct integers and a target, return the index where it
is found, or where it would be inserted to keep the array sorted.

  [1,3,5,6], target = 5  ->  2 ;  target = 2  ->  1

PATTERN: binary search for the leftmost position >= target (lower bound). Time
O(log n), space O(1).
"""

from typing import List


def search_insert(nums: List[int], target: int) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert search_insert([1, 3, 5, 6], 5) == 2
    assert search_insert([1, 3, 5, 6], 2) == 1
    assert search_insert([1, 3, 5, 6], 7) == 4
    assert search_insert([1, 3, 5, 6], 0) == 0
    assert search_insert([1], 1) == 0


if __name__ == "__main__":
    try:
        test()
        print("PASS  0035 search_insert")
    except NotImplementedError:
        print("----  0035 search_insert — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0035 search_insert: {e}")
