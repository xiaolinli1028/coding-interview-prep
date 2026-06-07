"""
70. Climbing Stairs  ·  Easy  ·  Dynamic Programming
====================================================
(run: python3 0070_climbing_stairs.py)

You climb 1 or 2 steps at a time. How many distinct ways to reach the top of `n`
steps?

  n=2 -> 2 (1+1, 2)      n=3 -> 3 (1+1+1, 1+2, 2+1)

PATTERN: it's Fibonacci — ways(n) = ways(n-1) + ways(n-2). Roll two variables.
Time O(n), O(1) space.
"""


def climb_stairs(n: int) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    f = climb_stairs
    assert f(1) == 1
    assert f(2) == 2
    assert f(3) == 3
    assert f(5) == 8
    assert f(10) == 89


if __name__ == "__main__":
    try:
        test()
        print("PASS  0070 climb_stairs")
    except NotImplementedError:
        print("----  0070 climb_stairs — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0070 climb_stairs: {e}")
