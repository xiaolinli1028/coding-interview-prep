"""
131. Palindrome Partitioning  ·  Medium  ·  Backtracking
========================================================
(run: python3 0131_palindrome_partitioning.py)

Partition string s so every substring is a palindrome; return all such
partitionings.

  "aab"  ->  [["a","a","b"],["aa","b"]]

PATTERN: backtracking — at each position try every prefix that is a palindrome,
recurse on the rest. Time O(n * 2^n), space O(n).
"""

from typing import List


def partition(s: str) -> List[List[str]]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def _norm(res):
    return sorted(map(tuple, res))


def test():
    assert _norm(partition("aab")) == _norm([["a", "a", "b"], ["aa", "b"]])
    assert partition("a") == [["a"]]
    assert _norm(partition("aba")) == _norm([["a", "b", "a"], ["aba"]])
    assert _norm(partition("aa")) == _norm([["a", "a"], ["aa"]])


if __name__ == "__main__":
    try:
        test()
        print("PASS  0131 partition")
    except NotImplementedError:
        print("----  0131 partition — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0131 partition: {e}")
