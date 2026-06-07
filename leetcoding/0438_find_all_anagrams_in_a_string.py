"""
438. Find All Anagrams in a String  ·  Medium  ·  Sliding Window
===============================================================
(run: python3 0438_find_all_anagrams_in_a_string.py)

Return the start indices of all substrings of s that are anagrams of p.

  s = "cbaebabacd", p = "abc"  ->  [0,6]

PATTERN: fixed-size sliding window of len(p) over s, comparing character counts
(via a running count match). Time O(n), space O(1) (26 letters).
"""

from typing import List


def find_anagrams(s: str, p: str) -> List[int]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert find_anagrams("cbaebabacd", "abc") == [0, 6]
    assert find_anagrams("abab", "ab") == [0, 1, 2]
    assert find_anagrams("a", "aa") == []
    assert find_anagrams("aa", "bb") == []
    assert find_anagrams("baa", "aa") == [1]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0438 find_anagrams")
    except NotImplementedError:
        print("----  0438 find_anagrams — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0438 find_anagrams: {e}")
