"""
19. Remove Nth Node From End of List  ·  Medium  ·  Linked List
===============================================================
(run: python3 0019_remove_nth_node_from_end.py)

Remove the nth node from the end of the list and return its head.

  1->2->3->4->5, n = 2  ->  1->2->3->5

PATTERN: two pointers with a dummy head — advance the lead pointer n+1 steps,
then move both until lead falls off the end; trailing pointer stops before the
target. Time O(L), space O(1).
"""

from typing import Optional

from _helpers import ListNode, list_to_linked, linked_to_list


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert linked_to_list(remove_nth_from_end(list_to_linked([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert linked_to_list(remove_nth_from_end(list_to_linked([1]), 1)) == []
    assert linked_to_list(remove_nth_from_end(list_to_linked([1, 2]), 1)) == [1]
    assert linked_to_list(remove_nth_from_end(list_to_linked([1, 2]), 2)) == [2]  # remove head


if __name__ == "__main__":
    try:
        test()
        print("PASS  0019 remove_nth_from_end")
    except NotImplementedError:
        print("----  0019 remove_nth_from_end — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0019 remove_nth_from_end: {e}")
