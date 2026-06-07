"""
239. Sliding Window Maximum  ·  Hard  ·  Monotonic Deque
========================================================
(run: python3 0239_sliding_window_maximum.py)

Return the maximum of each contiguous window of size k as it slides over nums.

  [1,3,-1,-3,5,3,6,7], k = 3  ->  [3,3,5,5,6,7]

PATTERN: monotonic decreasing deque of indices; the front is always the window's
max, and out-of-window indices are popped. Time O(n), space O(k).
"""

from typing import List


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert max_sliding_window([1], 1) == [1]
    assert max_sliding_window([1, -1], 1) == [1, -1]
    assert max_sliding_window([9, 11], 2) == [11]
    assert max_sliding_window([4, 3, 2, 1], 2) == [4, 3, 2]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0239 max_sliding_window")
    except NotImplementedError:
        print("----  0239 max_sliding_window — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0239 max_sliding_window: {e}")
