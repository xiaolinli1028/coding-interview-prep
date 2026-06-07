"""
739. Daily Temperatures  ·  Medium  ·  Stack (monotonic)
=======================================================
(run: python3 0739_daily_temperatures.py)

For each day, how many days until a warmer temperature? 0 if none later.

  [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]

PATTERN: monotonic decreasing stack of indices. When today's temp exceeds the temp
at the stack top, pop and record the day gap. Each index pushed/popped once -> O(n).
"""

from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    f = daily_temperatures
    assert f([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert f([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert f([30, 60, 90]) == [1, 1, 0]
    assert f([90, 80, 70]) == [0, 0, 0], "strictly decreasing"
    assert f([50]) == [0]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0739 daily_temperatures")
    except NotImplementedError:
        print("----  0739 daily_temperatures — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0739 daily_temperatures: {e}")
