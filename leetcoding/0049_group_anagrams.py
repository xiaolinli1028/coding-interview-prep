"""
49. Group Anagrams  ·  Medium  ·  Hashing
=========================================
(run: python3 0049_group_anagrams.py)

Group the strings that are anagrams of each other. Return a list of groups (order
of groups and within groups doesn't matter — the test normalizes).

  ["eat","tea","tan","ate","nat","bat"]
    -> [["eat","tea","ate"], ["tan","nat"], ["bat"]]

PATTERN: hash by a canonical key — the sorted string (O(n·k log k)), or a 26-count
tuple (O(n·k)). Strings with the same key are anagrams.
"""

from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def _norm(groups):
    return sorted(tuple(sorted(g)) for g in groups)


def test():
    out = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert _norm(out) == _norm([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
    assert _norm(group_anagrams([""])) == _norm([[""]])
    assert _norm(group_anagrams(["a"])) == _norm([["a"]])
    assert _norm(group_anagrams(["abc", "bca", "xyz"])) == _norm([["abc", "bca"], ["xyz"]])


if __name__ == "__main__":
    try:
        test()
        print("PASS  0049 group_anagrams")
    except NotImplementedError:
        print("----  0049 group_anagrams — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0049 group_anagrams: {e}")
