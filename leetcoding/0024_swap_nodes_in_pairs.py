"""
24. Swap Nodes in Pairs  ·  Medium  ·  Linked List
==================================================
(run: python3 0024_swap_nodes_in_pairs.py)

Swap every two adjacent nodes and return the head. Don't modify values, only the
links.

  1->2->3->4  ->  2->1->4->3

PATTERN: dummy head + a pointer before each pair; relink prev->second->first->
rest. Time O(n), space O(1).
"""

from typing import Optional

from _helpers import ListNode, list_to_linked, linked_to_list


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert linked_to_list(swap_pairs(list_to_linked([1, 2, 3, 4]))) == [2, 1, 4, 3]
    assert linked_to_list(swap_pairs(list_to_linked([1, 2, 3]))) == [2, 1, 3]  # odd
    assert linked_to_list(swap_pairs(list_to_linked([]))) == []
    assert linked_to_list(swap_pairs(list_to_linked([1]))) == [1]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0024 swap_pairs")
    except NotImplementedError:
        print("----  0024 swap_pairs — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0024 swap_pairs: {e}")
