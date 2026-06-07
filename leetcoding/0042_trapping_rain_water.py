"""
42. Trapping Rain Water  ·  Hard  ·  Two Pointers
=================================================
(run: python3 0042_trapping_rain_water.py)

Given bar heights of width 1, compute how much rain water is trapped.

  [0,1,0,2,1,0,1,3,2,1,2,1]  ->  6

PATTERN: two pointers tracking left_max / right_max; water above the shorter side
is bounded by its running max. Time O(n), space O(1).
"""

from typing import List


def trap(height: List[int]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap([4, 2, 0, 3, 2, 5]) == 9
    assert trap([]) == 0
    assert trap([1, 2, 3]) == 0
    assert trap([3, 0, 2, 0, 4]) == 7


if __name__ == "__main__":
    try:
        test()
        print("PASS  0042 trap")
    except NotImplementedError:
        print("----  0042 trap — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0042 trap: {e}")
