"""
78. Subsets  ·  Medium  ·  Backtracking
=======================================
(run: python3 0078_subsets.py)

Return all subsets (the power set) of a list of distinct integers (any order).

  [1,2,3]  ->  8 subsets including [] and [1,2,3]

PATTERN: backtracking — at each index choose include/exclude, or iteratively
double the result set. Time O(n * 2^n), space O(n).
"""

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def _norm(res):
    return sorted(map(tuple, (sorted(s) for s in res)))


def test():
    assert _norm(subsets([1, 2, 3])) == _norm(
        [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    )
    assert _norm(subsets([0])) == _norm([[], [0]])
    assert len(subsets([1, 2, 3, 4])) == 16
    assert subsets([]) == [[]]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0078 subsets")
    except NotImplementedError:
        print("----  0078 subsets — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0078 subsets: {e}")
