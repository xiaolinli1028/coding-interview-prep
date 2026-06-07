"""
75. Sort Colors  ·  Medium  ·  Tricks
=====================================
(run: python3 0075_sort_colors.py)

Sort an array of 0s, 1s, and 2s in-place (Dutch National Flag).

  [2,0,2,1,1,0]  ->  [0,0,1,1,2,2]

PATTERN: three pointers low/mid/high — swap 0s to the front, 2s to the back,
leave 1s in the middle, in a single pass. Time O(n), space O(1).
"""

from typing import List


def sort_colors(nums: List[int]) -> None:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    a = [2, 0, 2, 1, 1, 0]
    sort_colors(a)
    assert a == [0, 0, 1, 1, 2, 2]
    b = [2, 0, 1]
    sort_colors(b)
    assert b == [0, 1, 2]
    c = [0]
    sort_colors(c)
    assert c == [0]
    d = [1, 1, 1]
    sort_colors(d)
    assert d == [1, 1, 1]
    e = [2, 2, 0, 0]
    sort_colors(e)
    assert e == [0, 0, 2, 2]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0075 sort_colors")
    except NotImplementedError:
        print("----  0075 sort_colors — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0075 sort_colors: {e}")
