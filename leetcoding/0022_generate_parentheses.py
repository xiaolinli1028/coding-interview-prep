"""
22. Generate Parentheses  ·  Medium  ·  Backtracking
====================================================
(run: python3 0022_generate_parentheses.py)

Given n pairs of parentheses, generate all well-formed combinations.

  n = 3  ->  ["((()))","(()())","(())()","()(())","()()()"]

PATTERN: backtracking — add '(' while open < n, add ')' while close < open. Time
O(4^n / sqrt(n)) (Catalan), space O(n).
"""

from typing import List


def generate_parenthesis(n: int) -> List[str]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert sorted(generate_parenthesis(3)) == sorted(
        ["((()))", "(()())", "(())()", "()(())", "()()()"]
    )
    assert generate_parenthesis(1) == ["()"]
    assert sorted(generate_parenthesis(2)) == sorted(["(())", "()()"])
    assert len(generate_parenthesis(4)) == 14   # Catalan(4)


if __name__ == "__main__":
    try:
        test()
        print("PASS  0022 generate_parenthesis")
    except NotImplementedError:
        print("----  0022 generate_parenthesis — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0022 generate_parenthesis: {e}")
