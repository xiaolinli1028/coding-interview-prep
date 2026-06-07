"""
32. Longest Valid Parentheses  ·  Hard  ·  Dynamic Programming
=============================================================
(run: python3 0032_longest_valid_parentheses.py)

Return the length of the longest valid (well-formed) parentheses substring.

  ")()())"  ->  4   ("()()")

PATTERN: stack of indices seeded with -1; on ')' pop and measure i - stack[-1];
if the stack empties push i as a new base. Time O(n), space O(n).
"""


def longest_valid_parentheses(s: str) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert longest_valid_parentheses("(()") == 2
    assert longest_valid_parentheses(")()())") == 4
    assert longest_valid_parentheses("") == 0
    assert longest_valid_parentheses("()(()") == 2
    assert longest_valid_parentheses("()(())") == 6


if __name__ == "__main__":
    try:
        test()
        print("PASS  0032 longest_valid_parentheses")
    except NotImplementedError:
        print("----  0032 longest_valid_parentheses — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0032 longest_valid_parentheses: {e}")
