"""
155. Min Stack  ·  Medium  ·  Stack (design)
============================================
(run: python3 0155_min_stack.py)

Design a stack supporting push, pop, top, and getMin — all in O(1).

PATTERN: keep an auxiliary stack of running minimums alongside the main stack (or
store (val, min_so_far) pairs). Each push records min(val, current_min). O(1) all.
"""


class MinStack:
    def __init__(self):
        # TODO
        raise NotImplementedError

    def push(self, val: int) -> None:
        raise NotImplementedError

    def pop(self) -> None:
        raise NotImplementedError

    def top(self) -> int:
        raise NotImplementedError

    def getMin(self) -> int:
        raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.getMin() == -3
    s.pop()
    assert s.top() == 0
    assert s.getMin() == -2
    # min restores correctly as elements with the min are popped
    s2 = MinStack()
    s2.push(1)
    s2.push(2)
    s2.push(0)
    assert s2.getMin() == 0
    s2.pop()
    assert s2.getMin() == 1


if __name__ == "__main__":
    try:
        test()
        print("PASS  0155 MinStack")
    except NotImplementedError:
        print("----  0155 MinStack — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0155 MinStack: {e}")
