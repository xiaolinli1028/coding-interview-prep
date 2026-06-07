"""
322. Coin Change  ·  Medium  ·  Dynamic Programming
===================================================
(run: python3 0322_coin_change.py)

Given coin denominations and an amount, return the fewest coins to make that
amount, or -1 if impossible. Unlimited supply of each coin.

  coins = [1,2,5], amount = 11  ->  3   (5 + 5 + 1)

PATTERN: unbounded-knapsack DP — dp[a] = 1 + min(dp[a - c]) over coins c <= a.
Time O(amount * len(coins)), space O(amount).
"""

from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([1, 2, 5], 0) == 0
    assert coin_change([2, 5, 10, 1], 27) == 4


if __name__ == "__main__":
    try:
        test()
        print("PASS  0322 coin_change")
    except NotImplementedError:
        print("----  0322 coin_change — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0322 coin_change: {e}")
