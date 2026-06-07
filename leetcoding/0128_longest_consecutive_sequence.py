"""
128. Longest Consecutive Sequence  ·  Medium  ·  Hashing
=======================================================
(run: python3 0128_longest_consecutive_sequence.py)

Return the length of the longest run of consecutive integers in `nums`. Must run
in O(n) (so no full sort).

  [100,4,200,1,3,2] -> 4   (the run 1,2,3,4)

PATTERN: put nums in a set. Only start counting a run from a number whose
predecessor (x-1) is NOT in the set (a run's left end). Each number is visited
O(1) amortized -> O(n).
"""

from typing import List


def longest_consecutive(nums: List[int]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    f = longest_consecutive
    assert f([100, 4, 200, 1, 3, 2]) == 4
    assert f([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert f([]) == 0
    assert f([1, 2, 0, 1]) == 3, "duplicates shouldn't extend the run"
    assert f([10]) == 1


if __name__ == "__main__":
    try:
        test()
        print("PASS  0128 longest_consecutive")
    except NotImplementedError:
        print("----  0128 longest_consecutive — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0128 longest_consecutive: {e}")
