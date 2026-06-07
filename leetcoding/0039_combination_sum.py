"""
39. Combination Sum  ·  Medium  ·  Backtracking
===============================================
(run: python3 0039_combination_sum.py)

Given distinct candidates and a target, return all unique combinations that sum
to target. The same number may be chosen unlimited times.

  candidates = [2,3,6,7], target = 7  ->  [[2,2,3],[7]]

PATTERN: backtracking that may reuse the current index (so passing `i` not `i+1`)
to allow repeats; prune when the running sum exceeds target. Time exponential.
"""

from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def _norm(res):
    return sorted(map(tuple, (sorted(c) for c in res)))


def test():
    assert _norm(combination_sum([2, 3, 6, 7], 7)) == _norm([[2, 2, 3], [7]])
    assert _norm(combination_sum([2, 3, 5], 8)) == _norm([[2, 2, 2, 2], [2, 3, 3], [3, 5]])
    assert combination_sum([2], 1) == []
    assert _norm(combination_sum([1], 2)) == _norm([[1, 1]])


if __name__ == "__main__":
    try:
        test()
        print("PASS  0039 combination_sum")
    except NotImplementedError:
        print("----  0039 combination_sum — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0039 combination_sum: {e}")
