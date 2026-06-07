"""
25. Reverse Nodes in k-Group  ·  Hard  ·  Linked List
=====================================================
(run: python3 0025_reverse_nodes_in_k_group.py)

Reverse the nodes of the list k at a time and return the modified list. Nodes in
a final group of fewer than k stay in their original order.

  1->2->3->4->5, k = 2  ->  2->1->4->3->5
  1->2->3->4->5, k = 3  ->  3->2->1->4->5

PATTERN: count k nodes ahead; if a full group exists, reverse it iteratively and
recurse/iterate on the rest. Time O(n), space O(1) iterative.
"""

from typing import Optional

from _helpers import ListNode, list_to_linked, linked_to_list


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert linked_to_list(reverse_k_group(list_to_linked([1, 2, 3, 4, 5]), 2)) == [2, 1, 4, 3, 5]
    assert linked_to_list(reverse_k_group(list_to_linked([1, 2, 3, 4, 5]), 3)) == [3, 2, 1, 4, 5]
    assert linked_to_list(reverse_k_group(list_to_linked([1, 2, 3, 4]), 4)) == [4, 3, 2, 1]
    assert linked_to_list(reverse_k_group(list_to_linked([1, 2, 3]), 1)) == [1, 2, 3]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0025 reverse_k_group")
    except NotImplementedError:
        print("----  0025 reverse_k_group — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0025 reverse_k_group: {e}")
