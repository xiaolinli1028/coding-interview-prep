"""
5. Longest Palindromic Substring  ·  Medium  ·  2-D Dynamic Programming
======================================================================
(run: python3 0005_longest_palindromic_substring.py)

Return the longest palindromic substring of s. (If several share the max length,
any one is accepted; the test checks length and palindrome-ness.)

  "babad"  ->  "bab" (or "aba")

PATTERN: expand around each center (2n-1 centers, odd & even). Time O(n^2),
space O(1).
"""


def longest_palindrome(s: str) -> str:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def _is_pal(t):
    return t == t[::-1]


def test():
    r = longest_palindrome("babad")
    assert r in ("bab", "aba") and _is_pal(r)
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    r2 = longest_palindrome("")
    assert r2 == ""
    assert longest_palindrome("ac") in ("a", "c")
    assert longest_palindrome("forgeeksskeegfor") == "geeksskeeg"


if __name__ == "__main__":
    try:
        test()
        print("PASS  0005 longest_palindrome")
    except NotImplementedError:
        print("----  0005 longest_palindrome — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0005 longest_palindrome: {e}")
