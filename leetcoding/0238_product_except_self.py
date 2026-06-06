"""
238. Product of Array Except Self  ·  Medium  ·  Arrays
======================================================
(run: python3 0238_product_except_self.py)

Return `answer` where answer[i] = product of all nums except nums[i]. Must run in
O(n) and WITHOUT using division.

  [1,2,3,4] -> [24,12,8,6]

PATTERN: two passes of prefix/suffix products. answer[i] = (product of everything
left of i) * (product of everything right of i). The right pass can reuse the
output array with a running suffix variable. Time O(n), O(1) extra (besides output).
"""

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    f = product_except_self
    assert f([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert f([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0], "with a zero"
    assert f([2, 3]) == [3, 2]
    assert f([0, 0]) == [0, 0], "two zeros -> all zero"


if __name__ == "__main__":
    try:
        test()
        print("PASS  0238 product_except_self")
    except NotImplementedError:
        print("----  0238 product_except_self — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0238 product_except_self: {e}")
