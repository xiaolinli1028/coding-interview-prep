"""
46. Permutations  ·  Medium  ·  Backtracking
============================================
(run: python3 0046_permutations.py)

Return all permutations of a list of distinct integers (in any order).

  [1,2,3]  ->  6 permutations

PATTERN: backtracking — pick each unused element in turn, recurse, undo. Time
O(n * n!), space O(n).
"""

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def _norm(res):
    return sorted(map(tuple, res))


def test():
    assert _norm(permute([1, 2, 3])) == _norm(
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    )
    assert _norm(permute([0, 1])) == _norm([[0, 1], [1, 0]])
    assert permute([1]) == [[1]]
    assert len(permute([1, 2, 3, 4])) == 24


if __name__ == "__main__":
    try:
        test()
        print("PASS  0046 permute")
    except NotImplementedError:
        print("----  0046 permute — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0046 permute: {e}")
