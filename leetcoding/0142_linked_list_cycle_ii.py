"""
142. Linked List Cycle II  ·  Medium  ·  Linked List
====================================================
(run: python3 0142_linked_list_cycle_ii.py)

Return the node where the cycle begins, or None if there is no cycle.

  3->2->0->-4, tail -> index 1  ->  the node with value 2

PATTERN: Floyd's algorithm. After slow/fast meet, reset one pointer to head and
advance both by 1; they meet at the cycle entrance. Time O(n), space O(1).
"""

from typing import Optional

from _helpers import ListNode, make_cycle


def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    h = make_cycle([3, 2, 0, -4], 1)
    node = detect_cycle(h)
    assert node is not None and node.val == 2

    h2 = make_cycle([1, 2], 0)
    node2 = detect_cycle(h2)
    assert node2 is not None and node2.val == 1

    assert detect_cycle(make_cycle([1, 2, 3], -1)) is None
    assert detect_cycle(make_cycle([1], -1)) is None
    assert detect_cycle(make_cycle([], -1)) is None


if __name__ == "__main__":
    try:
        test()
        print("PASS  0142 detect_cycle")
    except NotImplementedError:
        print("----  0142 detect_cycle — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0142 detect_cycle: {e}")
