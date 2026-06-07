"""
56. Merge Intervals  ·  Medium  ·  Arrays
=========================================
(run: python3 0056_merge_intervals.py)

Merge all overlapping intervals; return the non-overlapping intervals covering the
same ranges, sorted by start.

  [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]

PATTERN: sort by start, then sweep — if the current interval's start <= last
merged end, extend the end; otherwise append a new interval. Time O(n log n).
"""

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    f = merge
    assert f([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert f([[1, 4], [4, 5]]) == [[1, 5]], "touching intervals merge"
    assert f([[1, 4]]) == [[1, 4]]
    assert f([[1, 4], [0, 4]]) == [[0, 4]], "must sort first"
    assert f([[1, 4], [2, 3]]) == [[1, 4]], "fully contained"


if __name__ == "__main__":
    try:
        test()
        print("PASS  0056 merge")
    except NotImplementedError:
        print("----  0056 merge — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0056 merge: {e}")
