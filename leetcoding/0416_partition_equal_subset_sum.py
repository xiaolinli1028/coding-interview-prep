"""
416. Partition Equal Subset Sum  ·  Medium  ·  Dynamic Programming
=================================================================
(run: python3 0416_partition_equal_subset_sum.py)

Return True if the array can be split into two subsets with equal sum.

  [1,5,11,5]  ->  True   ([1,5,5] and [11])

PATTERN: subset-sum / 0-1 knapsack for target = total/2 using a boolean DP set
(or bitset). Time O(n * sum), space O(sum).
"""

from typing import List


def can_partition(nums: List[int]) -> bool:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert can_partition([1, 5, 11, 5]) is True
    assert can_partition([1, 2, 3, 5]) is False
    assert can_partition([1, 1]) is True
    assert can_partition([1]) is False
    assert can_partition([2, 2, 2, 2]) is True


if __name__ == "__main__":
    try:
        test()
        print("PASS  0416 can_partition")
    except NotImplementedError:
        print("----  0416 can_partition — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0416 can_partition: {e}")
