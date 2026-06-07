"""
23. Merge k Sorted Lists  ·  Hard  ·  Linked List
=================================================
(run: python3 0023_merge_k_sorted_lists.py)

Merge k sorted linked lists into one sorted list and return its head.

  [1->4->5, 1->3->4, 2->6]  ->  1->1->2->3->4->4->5->6

PATTERN: min-heap of (val, list_index, node) across the k current heads, popping
the smallest each step. Time O(N log k), space O(k).
"""

from typing import List, Optional

from _helpers import ListNode, list_to_linked, linked_to_list


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    lists = [list_to_linked([1, 4, 5]), list_to_linked([1, 3, 4]), list_to_linked([2, 6])]
    assert linked_to_list(merge_k_lists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert linked_to_list(merge_k_lists([])) == []
    assert linked_to_list(merge_k_lists([list_to_linked([])])) == []
    assert linked_to_list(merge_k_lists([list_to_linked([]), list_to_linked([1])])) == [1]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0023 merge_k_lists")
    except NotImplementedError:
        print("----  0023 merge_k_lists — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0023 merge_k_lists: {e}")
