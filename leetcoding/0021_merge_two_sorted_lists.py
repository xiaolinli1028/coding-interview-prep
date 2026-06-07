"""
21. Merge Two Sorted Lists  ·  Easy  ·  Linked List
===================================================
(run: python3 0021_merge_two_sorted_lists.py)

Merge two sorted linked lists into one sorted list and return its head.

  1->2->4, 1->3->4  ->  1->1->2->3->4->4

PATTERN: dummy head + tail pointer; repeatedly splice the smaller front node,
then attach whatever remains. Time O(m+n), space O(1).
"""

from typing import Optional

from _helpers import ListNode, list_to_linked, linked_to_list


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    a = list_to_linked([1, 2, 4])
    b = list_to_linked([1, 3, 4])
    assert linked_to_list(merge_two_lists(a, b)) == [1, 1, 2, 3, 4, 4]
    assert linked_to_list(merge_two_lists(list_to_linked([]), list_to_linked([]))) == []
    assert linked_to_list(merge_two_lists(list_to_linked([]), list_to_linked([0]))) == [0]
    assert linked_to_list(merge_two_lists(list_to_linked([1, 5]), list_to_linked([2, 3]))) == [1, 2, 3, 5]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0021 merge_two_lists")
    except NotImplementedError:
        print("----  0021 merge_two_lists — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0021 merge_two_lists: {e}")
