"""
31. Next Permutation  ·  Medium  ·  Tricks
==========================================
(run: python3 0031_next_permutation.py)

Rearrange nums in-place into the lexicographically next greater permutation. If
none exists (it's the highest), wrap around to the lowest (ascending) order.

  [1,2,3]  ->  [1,3,2]
  [3,2,1]  ->  [1,2,3]

PATTERN: find the rightmost ascent i (nums[i] < nums[i+1]); swap nums[i] with the
rightmost value greater than it; reverse the suffix. Time O(n), space O(1).
"""

from typing import List


def next_permutation(nums: List[int]) -> None:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    a = [1, 2, 3]
    next_permutation(a)
    assert a == [1, 3, 2]
    b = [3, 2, 1]
    next_permutation(b)
    assert b == [1, 2, 3]
    c = [1, 1, 5]
    next_permutation(c)
    assert c == [1, 5, 1]
    d = [1]
    next_permutation(d)
    assert d == [1]
    e = [1, 3, 2]
    next_permutation(e)
    assert e == [2, 1, 3]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0031 next_permutation")
    except NotImplementedError:
        print("----  0031 next_permutation — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0031 next_permutation: {e}")
