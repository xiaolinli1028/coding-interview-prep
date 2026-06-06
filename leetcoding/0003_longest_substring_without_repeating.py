"""
3. Longest Substring Without Repeating Characters  ·  Medium  ·  Sliding Window
==============================================================================
(run: python3 0003_longest_substring_without_repeating.py)

Given a string `s`, return the length of the longest substring without repeating
characters.

  "abcabcbb" -> 3 ("abc")      "bbbbb" -> 1 ("b")      "pwwkew" -> 3 ("wke")

PATTERN: sliding window with a last-seen-index map. Expand right; when you hit a
repeat inside the window, jump left past its previous position. Time O(n).
"""


def length_of_longest_substring(s: str) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    f = length_of_longest_substring
    assert f("abcabcbb") == 3, f("abcabcbb")
    assert f("bbbbb") == 1, f("bbbbb")
    assert f("pwwkew") == 3, f("pwwkew")
    assert f("") == 0, "empty string"
    assert f(" ") == 1, "single space"
    assert f("dvdf") == 3, "dvdf -> 'vdf' (window must jump correctly)"
    assert f("abba") == 2, "abba -> left pointer must not move backward"


if __name__ == "__main__":
    try:
        test()
        print("PASS  0003 length_of_longest_substring")
    except NotImplementedError:
        print("----  0003 length_of_longest_substring — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0003 length_of_longest_substring: {e}")
