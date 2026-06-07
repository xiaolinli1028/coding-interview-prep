"""
141. Linked List Cycle  ·  Easy  ·  Linked List
===============================================
(run: python3 0141_linked_list_cycle.py)

Return True if the linked list has a cycle (some node's next points back to an
earlier node).

  3->2->0->-4, tail -> node index 1  ->  True

PATTERN: Floyd's tortoise & hare — a slow (+1) and fast (+2) pointer meet iff a
cycle exists. Time O(n), space O(1).
"""

from typing import Optional

from _helpers import ListNode, make_cycle


def has_cycle(head: Optional[ListNode]) -> bool:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert has_cycle(make_cycle([3, 2, 0, -4], 1)) is True
    assert has_cycle(make_cycle([1, 2], 0)) is True
    assert has_cycle(make_cycle([1, 2, 3], -1)) is False
    assert has_cycle(make_cycle([1], -1)) is False
    assert has_cycle(make_cycle([], -1)) is False


if __name__ == "__main__":
    try:
        test()
        print("PASS  0141 has_cycle")
    except NotImplementedError:
        print("----  0141 has_cycle — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0141 has_cycle: {e}")
