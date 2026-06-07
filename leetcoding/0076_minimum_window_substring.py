"""
76. Minimum Window Substring  ·  Hard  ·  Sliding Window
========================================================
(run: python3 0076_minimum_window_substring.py)

Return the smallest substring of s containing every character of t (with
multiplicity), or "" if none exists.

  s = "ADOBECODEBANC", t = "ABC"  ->  "BANC"

PATTERN: expanding/contracting sliding window with a need-count map and a
`missing` counter; shrink from the left while the window is valid. Time O(n).
"""


def min_window(s: str, t: str) -> str:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("", "a") == ""
    assert min_window("aa", "aa") == "aa"


if __name__ == "__main__":
    try:
        test()
        print("PASS  0076 min_window")
    except NotImplementedError:
        print("----  0076 min_window — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0076 min_window: {e}")
