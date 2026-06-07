"""
34. Find First and Last Position of Element  ·  Medium  ·  Binary Search
========================================================================
(run: python3 0034_find_first_and_last_position.py)

In a sorted array, return the first and last index of target, or [-1,-1] if it's
absent. Must run in O(log n).

  [5,7,7,8,8,10], target = 8  ->  [3,4]

PATTERN: two binary searches — lower bound (first >= target) and upper bound
(first > target). Time O(log n), space O(1).
"""

from typing import List


def search_range(nums: List[int], target: int) -> List[int]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert search_range([], 0) == [-1, -1]
    assert search_range([1], 1) == [0, 0]
    assert search_range([2, 2, 2], 2) == [0, 2]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0034 search_range")
    except NotImplementedError:
        print("----  0034 search_range — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0034 search_range: {e}")
