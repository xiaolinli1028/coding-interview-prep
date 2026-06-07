"""
139. Word Break  ·  Medium  ·  Dynamic Programming
==================================================
(run: python3 0139_word_break.py)

Return True if s can be segmented into a space-separated sequence of words from
the dictionary (each word reusable).

  s = "leetcode", wordDict = ["leet","code"]  ->  True

PATTERN: DP — dp[i] is True if some j<i has dp[j] and s[j:i] in the dict. Time
O(n^2 * L), space O(n).
"""

from typing import List


def word_break(s: str, wordDict: List[str]) -> bool:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert word_break("leetcode", ["leet", "code"]) is True
    assert word_break("applepenapple", ["apple", "pen"]) is True
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
    assert word_break("a", ["a"]) is True
    assert word_break("ab", ["a"]) is False


if __name__ == "__main__":
    try:
        test()
        print("PASS  0139 word_break")
    except NotImplementedError:
        print("----  0139 word_break — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0139 word_break: {e}")
