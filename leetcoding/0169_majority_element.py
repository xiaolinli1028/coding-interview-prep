"""
169. Majority Element  ·  Easy  ·  Tricks
=========================================
(run: python3 0169_majority_element.py)

Return the element appearing more than n/2 times (guaranteed to exist).

  [2,2,1,1,1,2,2]  ->  2

PATTERN: Boyer-Moore voting — keep a candidate and a count; matching votes +1,
others -1, swap candidate when count hits 0. Time O(n), space O(1).
"""

from typing import List


def majority_element(nums: List[int]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert majority_element([3, 2, 3]) == 3
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
    assert majority_element([1]) == 1
    assert majority_element([5, 5, 5, 1, 2]) == 5


if __name__ == "__main__":
    try:
        test()
        print("PASS  0169 majority_element")
    except NotImplementedError:
        print("----  0169 majority_element — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0169 majority_element: {e}")
