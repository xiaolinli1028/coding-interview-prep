"""
234. Palindrome Linked List  ·  Easy  ·  Linked List
====================================================
(run: python3 0234_palindrome_linked_list.py)

Return True if a singly linked list reads the same forwards and backwards.

  1->2->2->1  ->  True
  1->2        ->  False

PATTERN: find the midpoint with slow/fast pointers, reverse the second half,
then compare the two halves node by node. Time O(n), space O(1).
"""

from typing import Optional

from _helpers import ListNode, list_to_linked


def is_palindrome(head: Optional[ListNode]) -> bool:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert is_palindrome(list_to_linked([1, 2, 2, 1])) is True
    assert is_palindrome(list_to_linked([1, 2, 3, 2, 1])) is True   # odd length
    assert is_palindrome(list_to_linked([1, 2])) is False
    assert is_palindrome(list_to_linked([1])) is True
    assert is_palindrome(list_to_linked([])) is True


if __name__ == "__main__":
    try:
        test()
        print("PASS  0234 is_palindrome")
    except NotImplementedError:
        print("----  0234 is_palindrome — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0234 is_palindrome: {e}")
