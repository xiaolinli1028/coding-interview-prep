"""
15. 3Sum  ·  Medium  ·  Two Pointers
====================================
(run: python3 0015_3sum.py)

Return all unique triplets [a,b,c] from `nums` with a + b + c == 0. The solution
set must not contain duplicate triplets (order within/among triplets doesn't
matter — the test normalizes).

  [-1,0,1,2,-1,-4] -> [[-1,-1,2], [-1,0,1]]

PATTERN: sort, then fix index i and two-pointer the rest. Skip duplicates for both
the fixed element and the moving pointers. Time O(n^2).
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def _norm(triplets):
    return sorted(tuple(sorted(t)) for t in triplets)


def test():
    assert _norm(three_sum([-1, 0, 1, 2, -1, -4])) == _norm([[-1, -1, 2], [-1, 0, 1]])
    assert three_sum([0, 1, 1]) == [], "no triplet sums to 0"
    assert _norm(three_sum([0, 0, 0])) == [(0, 0, 0)], "single zero triplet"
    assert _norm(three_sum([0, 0, 0, 0])) == [(0, 0, 0)], "dedup with extra zeros"
    got = _norm(three_sum([-2, 0, 1, 1, 2]))
    assert got == _norm([[-2, 0, 2], [-2, 1, 1]]), got


if __name__ == "__main__":
    try:
        test()
        print("PASS  0015 three_sum")
    except NotImplementedError:
        print("----  0015 three_sum — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0015 three_sum: {e}")
