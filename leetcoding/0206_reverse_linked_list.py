"""
206. Reverse Linked List  ·  Easy  ·  Linked List
=================================================
(run: python3 0206_reverse_linked_list.py)

Reverse a singly linked list and return the new head.

  1->2->3->4->5  ->  5->4->3->2->1

PATTERN: iterative pointer reversal — keep prev, walk forward flipping each
node's next to prev. Time O(n), space O(1).
"""

from typing import Optional

from _helpers import ListNode, list_to_linked, linked_to_list


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert linked_to_list(reverse_list(list_to_linked([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert linked_to_list(reverse_list(list_to_linked([1, 2]))) == [2, 1]
    assert linked_to_list(reverse_list(list_to_linked([7]))) == [7]
    assert linked_to_list(reverse_list(list_to_linked([]))) == []


if __name__ == "__main__":
    try:
        test()
        print("PASS  0206 reverse_list")
    except NotImplementedError:
        print("----  0206 reverse_list — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0206 reverse_list: {e}")
