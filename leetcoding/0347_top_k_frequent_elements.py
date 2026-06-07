"""
347. Top K Frequent Elements  ·  Medium  ·  Heap
=================================================
(run: python3 0347_top_k_frequent_elements.py)

Return the k most frequent elements (any order).

  [1,1,1,2,2,3], k = 2  ->  [1,2]

PATTERN: count frequencies, then bucket sort by frequency (or a size-k heap).
Time O(n), space O(n).
"""

from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert sorted(top_k_frequent([4, 4, 5, 5, 6], 2)) == [4, 5]
    assert sorted(top_k_frequent([1, 2, 3], 3)) == [1, 2, 3]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0347 top_k_frequent")
    except NotImplementedError:
        print("----  0347 top_k_frequent — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0347 top_k_frequent: {e}")
