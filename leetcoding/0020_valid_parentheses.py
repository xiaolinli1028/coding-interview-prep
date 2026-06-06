"""
20. Valid Parentheses  ·  Easy  ·  Stack
========================================
(run: python3 0020_valid_parentheses.py)

Given a string of just '()[]{}', decide if brackets are closed in the correct
order: every open has a matching close of the same type, properly nested.

  "()[]{}" -> True      "(]" -> False      "([)]" -> False      "{[]}" -> True

PATTERN: stack. Push opens; on a close, the stack top must be the matching open.
Empty stack at the end == valid. Time O(n).
"""


def is_valid(s: str) -> bool:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    f = is_valid
    assert f("()") is True
    assert f("()[]{}") is True
    assert f("(]") is False
    assert f("([)]") is False, "interleaved is invalid"
    assert f("{[]}") is True
    assert f("(") is False, "unclosed open"
    assert f("]") is False, "close with empty stack"
    assert f("") is True, "empty is valid"


if __name__ == "__main__":
    try:
        test()
        print("PASS  0020 is_valid")
    except NotImplementedError:
        print("----  0020 is_valid — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0020 is_valid: {e}")
