"""
300. Longest Increasing Subsequence  ·  Medium  ·  Dynamic Programming
======================================================================
(run: python3 0300_longest_increasing_subsequence.py)

Return the length of the longest strictly increasing subsequence.

  [10,9,2,5,3,7,101,18]  ->  4   ([2,3,7,101])

PATTERN: patience sorting — keep `tails`, the smallest tail for each LIS length,
and binary-search the insertion point. Time O(n log n), space O(n).
"""

from typing import List


def length_of_lis(nums: List[int]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
    assert length_of_lis([7, 7, 7, 7]) == 1
    assert length_of_lis([1]) == 1
    assert length_of_lis([]) == 0


if __name__ == "__main__":
    try:
        test()
        print("PASS  0300 length_of_lis")
    except NotImplementedError:
        print("----  0300 length_of_lis — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0300 length_of_lis: {e}")
