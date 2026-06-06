"""
121. Best Time to Buy and Sell Stock  ·  Easy  ·  Greedy
=======================================================
(run: python3 0121_best_time_to_buy_sell_stock.py)

prices[i] is the price on day i. Buy on one day, sell on a LATER day. Return the
max profit, or 0 if no profit is possible.

  [7,1,5,3,6,4] -> 5  (buy at 1, sell at 6)      [7,6,4,3,1] -> 0

PATTERN: track the minimum price seen so far; profit = price - min_so_far. Single
pass, O(n). (One buy/sell only.)
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    f = max_profit
    assert f([7, 1, 5, 3, 6, 4]) == 5
    assert f([7, 6, 4, 3, 1]) == 0, "monotonically decreasing -> 0"
    assert f([1, 2]) == 1
    assert f([2, 4, 1]) == 2, "best pair is early, not the global min/max"
    assert f([3, 3, 3]) == 0, "flat"


if __name__ == "__main__":
    try:
        test()
        print("PASS  0121 max_profit")
    except NotImplementedError:
        print("----  0121 max_profit — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0121 max_profit: {e}")
