"""
136. Single Number  ·  Easy  ·  Tricks
======================================
(run: python3 0136_single_number.py)

Every element appears twice except one. Return that single element, in O(n) time
and O(1) space.

  [4,1,2,1,2]  ->  4

PATTERN: XOR all elements — pairs cancel to 0, leaving the unique value. Time
O(n), space O(1).
"""

from typing import List


def single_number(nums: List[int]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert single_number([2, 2, 1]) == 1
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([1]) == 1
    assert single_number([0, 1, 0]) == 1
    assert single_number([-1, -1, -2]) == -2


if __name__ == "__main__":
    try:
        test()
        print("PASS  0136 single_number")
    except NotImplementedError:
        print("----  0136 single_number — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0136 single_number: {e}")
