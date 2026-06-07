"""
2. Add Two Numbers  ·  Medium  ·  Linked List
=============================================
(run: python3 0002_add_two_numbers.py)

Two non-empty linked lists represent non-negative integers with digits stored in
reverse order. Add them and return the sum as a linked list (also reversed).

  2->4->3 (342) + 5->6->4 (465)  ->  7->0->8 (807)

PATTERN: walk both lists together carrying the overflow, building the result with
a dummy head. Time O(max(m,n)), space O(max(m,n)).
"""

from typing import Optional

from _helpers import ListNode, list_to_linked, linked_to_list


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    r = add_two_numbers(list_to_linked([2, 4, 3]), list_to_linked([5, 6, 4]))
    assert linked_to_list(r) == [7, 0, 8]
    assert linked_to_list(add_two_numbers(list_to_linked([0]), list_to_linked([0]))) == [0]
    # 999 + 1 = 1000
    r2 = add_two_numbers(list_to_linked([9, 9, 9]), list_to_linked([1]))
    assert linked_to_list(r2) == [0, 0, 0, 1]
    r3 = add_two_numbers(list_to_linked([9, 9]), list_to_linked([1]))
    assert linked_to_list(r3) == [0, 0, 1]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0002 add_two_numbers")
    except NotImplementedError:
        print("----  0002 add_two_numbers — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0002 add_two_numbers: {e}")
