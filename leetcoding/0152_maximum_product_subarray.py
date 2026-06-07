"""
152. Maximum Product Subarray  ·  Medium  ·  Dynamic Programming
===============================================================
(run: python3 0152_maximum_product_subarray.py)

Return the largest product of a contiguous (non-empty) subarray.

  [2,3,-2,4]  ->  6   ([2,3])

PATTERN: track running max AND min products (a negative flips them); update both
at each step. Time O(n), space O(1).
"""

from typing import List


def max_product(nums: List[int]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert max_product([2, 3, -2, 4]) == 6
    assert max_product([-2, 0, -1]) == 0
    assert max_product([-2, 3, -4]) == 24
    assert max_product([-2]) == -2
    assert max_product([2, -5, -2, -4, 3]) == 24


if __name__ == "__main__":
    try:
        test()
        print("PASS  0152 max_product")
    except NotImplementedError:
        print("----  0152 max_product — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0152 max_product: {e}")
