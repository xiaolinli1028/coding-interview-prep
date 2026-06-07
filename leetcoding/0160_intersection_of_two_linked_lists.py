"""
160. Intersection of Two Linked Lists  ·  Easy  ·  Linked List
=============================================================
(run: python3 0160_intersection_of_two_linked_lists.py)

Given the heads of two singly linked lists, return the node at which they
intersect, or None if they don't. The lists keep their original structure.

  A = 4->1->8->4->5, B = 5->6->1->8->4->5, intersect at value 8

PATTERN: two pointers, each walking its own list then switching to the other's
head. They meet at the intersection after at most lenA+lenB steps. Time O(m+n),
space O(1).
"""

from typing import Optional

from _helpers import ListNode


def get_intersection_node(headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    # Build shared tail 8->4->5, with two distinct prefixes.
    tail = ListNode(8, ListNode(4, ListNode(5)))
    a = ListNode(4, ListNode(1, tail))
    b = ListNode(5, ListNode(6, ListNode(1, tail)))
    assert get_intersection_node(a, b) is tail

    # No intersection.
    c = ListNode(2, ListNode(6, ListNode(4)))
    d = ListNode(1, ListNode(5))
    assert get_intersection_node(c, d) is None

    # Whole lists share head.
    e = ListNode(1, ListNode(2))
    assert get_intersection_node(e, e) is e

    # One list empty.
    assert get_intersection_node(None, e) is None


if __name__ == "__main__":
    try:
        test()
        print("PASS  0160 get_intersection_node")
    except NotImplementedError:
        print("----  0160 get_intersection_node — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0160 get_intersection_node: {e}")
