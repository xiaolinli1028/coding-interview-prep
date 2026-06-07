"""
84. Largest Rectangle in Histogram  ·  Hard  ·  Stack
=====================================================
(run: python3 0084_largest_rectangle_in_histogram.py)

Given bar heights of width 1, return the area of the largest rectangle in the
histogram.

  [2,1,5,6,2,3]  ->  10   (bars 5 and 6, width 2)

PATTERN: monotonic increasing stack of indices; when a shorter bar appears, pop
and compute areas using the popped height and the spanning width. Time O(n).
"""

from typing import List


def largest_rectangle_area(heights: List[int]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10
    assert largest_rectangle_area([2, 4]) == 4
    assert largest_rectangle_area([1]) == 1
    assert largest_rectangle_area([]) == 0
    assert largest_rectangle_area([2, 2, 2]) == 6


if __name__ == "__main__":
    try:
        test()
        print("PASS  0084 largest_rectangle_area")
    except NotImplementedError:
        print("----  0084 largest_rectangle_area — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0084 largest_rectangle_area: {e}")
