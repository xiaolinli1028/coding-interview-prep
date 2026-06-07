"""
41. First Missing Positive  ·  Hard  ·  Arrays
==============================================
(run: python3 0041_first_missing_positive.py)

Return the smallest positive integer absent from nums, in O(n) time and O(1)
extra space.

  [3,4,-1,1]  ->  2

PATTERN: cyclic sort / index-as-hash — place each value v in slot v-1; then scan
for the first index i where nums[i] != i+1. Time O(n), space O(1).
"""

from typing import List


def first_missing_positive(nums: List[int]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert first_missing_positive([1, 2, 0]) == 3
    assert first_missing_positive([3, 4, -1, 1]) == 2
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1
    assert first_missing_positive([1]) == 2
    assert first_missing_positive([]) == 1


if __name__ == "__main__":
    try:
        test()
        print("PASS  0041 first_missing_positive")
    except NotImplementedError:
        print("----  0041 first_missing_positive — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0041 first_missing_positive: {e}")
