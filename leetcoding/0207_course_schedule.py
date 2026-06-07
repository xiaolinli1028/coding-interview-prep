"""
207. Course Schedule  ·  Medium  ·  Graph (Topological Sort)
============================================================
(run: python3 0207_course_schedule.py)

Given numCourses and prerequisite pairs [a, b] (take b before a), return True if
all courses can be finished (i.e. the graph has no cycle).

  numCourses = 2, prerequisites = [[1,0]]  ->  True
  numCourses = 2, prerequisites = [[1,0],[0,1]]  ->  False

PATTERN: Kahn's algorithm — repeatedly remove zero-indegree nodes; if all are
removed there's no cycle. Time O(V+E), space O(V+E).
"""

from typing import List


def can_finish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False
    assert can_finish(1, []) is True
    assert can_finish(4, [[1, 0], [2, 1], [3, 2]]) is True
    assert can_finish(3, [[0, 1], [1, 2], [2, 0]]) is False


if __name__ == "__main__":
    try:
        test()
        print("PASS  0207 can_finish")
    except NotImplementedError:
        print("----  0207 can_finish — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0207 can_finish: {e}")
