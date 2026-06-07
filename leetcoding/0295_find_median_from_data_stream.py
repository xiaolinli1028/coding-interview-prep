"""
295. Find Median from Data Stream  ·  Hard  ·  Heap (design)
============================================================
(run: python3 0295_find_median_from_data_stream.py)

Design a structure that supports addNum(num) and findMedian() over a growing
stream.

PATTERN: two heaps — a max-heap for the lower half and a min-heap for the upper
half, kept balanced in size. Median is a top (or the average of the two tops).
addNum O(log n), findMedian O(1).
"""


class MedianFinder:
    def __init__(self):
        # TODO
        raise NotImplementedError

    def addNum(self, num: int) -> None:
        raise NotImplementedError

    def findMedian(self) -> float:
        raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0

    mf2 = MedianFinder()
    for x in [5, 1, 4, 2, 3]:
        mf2.addNum(x)
    assert mf2.findMedian() == 3.0
    mf2.addNum(6)
    assert mf2.findMedian() == 3.5


if __name__ == "__main__":
    try:
        test()
        print("PASS  0295 MedianFinder")
    except NotImplementedError:
        print("----  0295 MedianFinder — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0295 MedianFinder: {e}")
