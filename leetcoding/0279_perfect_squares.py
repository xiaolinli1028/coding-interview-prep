"""
279. Perfect Squares  ·  Medium  ·  Dynamic Programming
=======================================================
(run: python3 0279_perfect_squares.py)

Return the least number of perfect-square numbers that sum to n.

  n = 12  ->  3   (4 + 4 + 4)
  n = 13  ->  2   (4 + 9)

PATTERN: DP — dp[i] = 1 + min(dp[i - sq]) over squares sq <= i. Time
O(n * sqrt(n)), space O(n).
"""


def num_squares(n: int) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert num_squares(12) == 3
    assert num_squares(13) == 2
    assert num_squares(1) == 1
    assert num_squares(4) == 1
    assert num_squares(7) == 4   # 4 + 1 + 1 + 1


if __name__ == "__main__":
    try:
        test()
        print("PASS  0279 num_squares")
    except NotImplementedError:
        print("----  0279 num_squares — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0279 num_squares: {e}")
