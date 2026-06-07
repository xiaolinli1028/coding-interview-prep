"""
763. Partition Labels  ·  Medium  ·  Greedy
===========================================
(run: python3 0763_partition_labels.py)

Partition s into as many parts as possible so each letter appears in at most one
part. Return the sizes of the parts in order.

  "ababcbacadefegdehijhklij"  ->  [9,7,8]

PATTERN: record each letter's last index; sweep extending the current part's end
to max(last index seen); cut when the cursor reaches that end. Time O(n).
"""

from typing import List


def partition_labels(s: str) -> List[int]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert partition_labels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert partition_labels("eccbbbbdec") == [10]
    assert partition_labels("a") == [1]
    assert partition_labels("abc") == [1, 1, 1]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0763 partition_labels")
    except NotImplementedError:
        print("----  0763 partition_labels — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0763 partition_labels: {e}")
