"""
79. Word Search  ·  Medium  ·  Backtracking
===========================================
(run: python3 0079_word_search.py)

Given an m x n board of characters and a word, return True if the word can be
formed from sequentially adjacent (up/down/left/right) cells, each used once.

  board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCCED" -> True

PATTERN: DFS backtracking from each starting cell, marking visited cells and
restoring them on backtrack. Time O(m*n*4^L), space O(L).
"""

from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert exist([row[:] for row in board], "ABCCED") is True
    assert exist([row[:] for row in board], "SEE") is True
    assert exist([row[:] for row in board], "ABCB") is False
    assert exist([["a"]], "a") is True
    assert exist([["a", "b"]], "ba") is True


if __name__ == "__main__":
    try:
        test()
        print("PASS  0079 exist")
    except NotImplementedError:
        print("----  0079 exist — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0079 exist: {e}")
