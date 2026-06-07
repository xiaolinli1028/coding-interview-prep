"""
51. N-Queens  ·  Hard  ·  Backtracking
======================================
(run: python3 0051_n_queens.py)

Place n queens on an n x n board so none attack each other; return all distinct
solutions as boards of '.' and 'Q'.

  n = 4  ->  2 solutions

PATTERN: backtracking row by row, tracking used columns and both diagonals
(r+c, r-c) in sets. Time O(n!), space O(n).
"""

from typing import List


def solve_n_queens(n: int) -> List[List[str]]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def _valid(board):
    n = len(board)
    cols, d1, d2 = set(), set(), set()
    count = 0
    for r in range(n):
        assert len(board[r]) == n
        for c in range(n):
            if board[r][c] == "Q":
                count += 1
                assert c not in cols and (r + c) not in d1 and (r - c) not in d2
                cols.add(c)
                d1.add(r + c)
                d2.add(r - c)
    assert count == n


def test():
    sols4 = solve_n_queens(4)
    assert len(sols4) == 2
    for b in sols4:
        _valid(b)
    assert solve_n_queens(1) == [["Q"]]
    assert solve_n_queens(2) == []
    assert solve_n_queens(3) == []
    assert len(solve_n_queens(5)) == 10


if __name__ == "__main__":
    try:
        test()
        print("PASS  0051 solve_n_queens")
    except NotImplementedError:
        print("----  0051 solve_n_queens — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0051 solve_n_queens: {e}")
