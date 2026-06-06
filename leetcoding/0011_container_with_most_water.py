"""
11. Container With Most Water  ·  Medium  ·  Two Pointers
========================================================
(run: python3 0011_container_with_most_water.py)

Given heights[i], pick two lines that with the x-axis form a container holding the
most water. Return the max area = (right - left) * min(height[left], height[right]).

  [1,8,6,2,5,4,8,3,7] -> 49

PATTERN: two pointers from both ends; always move the SHORTER wall inward (moving
the taller one can never increase area). Time O(n).
"""

from typing import List


def max_area(height: List[int]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    f = max_area
    assert f([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49, f([1, 8, 6, 2, 5, 4, 8, 3, 7])
    assert f([1, 1]) == 1, f([1, 1])
    assert f([4, 3, 2, 1, 4]) == 16, "two equal tall ends far apart"
    assert f([1, 2, 1]) == 2, f([1, 2, 1])


if __name__ == "__main__":
    try:
        test()
        print("PASS  0011 max_area")
    except NotImplementedError:
        print("----  0011 max_area — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0011 max_area: {e}")
