"""
148. Sort List  ·  Medium  ·  Linked List
=========================================
(run: python3 0148_sort_list.py)

Sort a linked list in ascending order and return the head.

  4->2->1->3  ->  1->2->3->4

PATTERN: top-down merge sort — split at the midpoint (slow/fast), sort each half
recursively, merge. Time O(n log n), space O(log n) recursion.
"""

from typing import Optional

from _helpers import ListNode, list_to_linked, linked_to_list


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert linked_to_list(sort_list(list_to_linked([4, 2, 1, 3]))) == [1, 2, 3, 4]
    assert linked_to_list(sort_list(list_to_linked([-1, 5, 3, 4, 0]))) == [-1, 0, 3, 4, 5]
    assert linked_to_list(sort_list(list_to_linked([]))) == []
    assert linked_to_list(sort_list(list_to_linked([1]))) == [1]
    assert linked_to_list(sort_list(list_to_linked([2, 1]))) == [1, 2]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0148 sort_list")
    except NotImplementedError:
        print("----  0148 sort_list — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0148 sort_list: {e}")
