"""
17. Letter Combinations of a Phone Number  ·  Medium  ·  Backtracking
=====================================================================
(run: python3 0017_letter_combinations_of_a_phone_number.py)

Given digits 2-9, return all letter combinations the number could spell (phone
keypad mapping). Return [] for an empty string.

  "23"  ->  ["ad","ae","af","bd","be","bf","cd","ce","cf"]

PATTERN: backtracking over the digits, appending one mapped letter at each step.
Time O(4^n * n), space O(n).
"""

from typing import List


def letter_combinations(digits: str) -> List[str]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert sorted(letter_combinations("23")) == sorted(
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    )
    assert letter_combinations("") == []
    assert sorted(letter_combinations("2")) == ["a", "b", "c"]
    assert len(letter_combinations("79")) == 4 * 4   # 7->4 letters, 9->4 letters


if __name__ == "__main__":
    try:
        test()
        print("PASS  0017 letter_combinations")
    except NotImplementedError:
        print("----  0017 letter_combinations — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0017 letter_combinations: {e}")
