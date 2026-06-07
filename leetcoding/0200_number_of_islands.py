"""
200. Number of Islands  ·  Medium  ·  Graph
===========================================
(run: python3 0200_number_of_islands.py)

Count islands in a grid of '1' (land) and '0' (water); cells connect
horizontally/vertically.

  [["1","1","0"],["1","0","0"],["0","0","1"]]  ->  2

PATTERN: scan cells; on each unvisited '1' run DFS/BFS flood-fill to sink the
whole island, incrementing the count. Time O(m*n), space O(m*n).
"""

from typing import List


def num_islands(grid: List[List[str]]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    g1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert num_islands([row[:] for row in g1]) == 1
    g2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert num_islands([row[:] for row in g2]) == 3
    assert num_islands([["0"]]) == 0
    assert num_islands([["1"]]) == 1
    assert num_islands([]) == 0


if __name__ == "__main__":
    try:
        test()
        print("PASS  0200 num_islands")
    except NotImplementedError:
        print("----  0200 num_islands — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0200 num_islands: {e}")
