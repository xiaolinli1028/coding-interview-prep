"""
287. Find the Duplicate Number  ·  Medium  ·  Tricks
====================================================
(run: python3 0287_find_the_duplicate_number.py)

An array of n+1 integers each in [1, n] has exactly one repeated number (possibly
repeated several times). Find it without modifying the array and in O(1) space.

  [1,3,4,2,2]  ->  2

PATTERN: treat values as next-index pointers; the duplicate creates a cycle.
Floyd's tortoise & hare finds the cycle entrance. Time O(n), space O(1).
"""

from typing import List


def find_duplicate(nums: List[int]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert find_duplicate([1, 3, 4, 2, 2]) == 2
    assert find_duplicate([3, 1, 3, 4, 2]) == 3
    assert find_duplicate([1, 1]) == 1
    assert find_duplicate([2, 2, 2, 2, 2]) == 2
    assert find_duplicate([1, 4, 4, 2, 3]) == 4


if __name__ == "__main__":
    try:
        test()
        print("PASS  0287 find_duplicate")
    except NotImplementedError:
        print("----  0287 find_duplicate — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0287 find_duplicate: {e}")
