"""
Reference solutions — LeetCode Hot 100, batch 3 (Linked List).
Don't open until you've attempted the problems.

Verify:  python3 solutions_03.py
"""

import heapq
from typing import List, Optional

from _helpers import ListNode


# 0160 Intersection of Two Linked Lists ────────────────────────────────────────
def get_intersection_node(headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
    a, b = headA, headB
    while a is not b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a


# 0206 Reverse Linked List ─────────────────────────────────────────────────────
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev


# 0234 Palindrome Linked List ──────────────────────────────────────────────────
def is_palindrome(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:                    # slow -> middle
        slow = slow.next
        fast = fast.next.next
    prev = None                                  # reverse second half
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    left, right = head, prev
    while right:                                 # compare halves
        if left.val != right.val:
            return False
        left, right = left.next, right.next
    return True


# 0141 Linked List Cycle ───────────────────────────────────────────────────────
def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


# 0142 Linked List Cycle II ────────────────────────────────────────────────────
def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            p = head
            while p is not slow:
                p = p.next
                slow = slow.next
            return p
    return None


# 0021 Merge Two Sorted Lists ──────────────────────────────────────────────────
def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = tail = ListNode()
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next, list1 = list1, list1.next
        else:
            tail.next, list2 = list2, list2.next
        tail = tail.next
    tail.next = list1 or list2
    return dummy.next


# 0002 Add Two Numbers ─────────────────────────────────────────────────────────
def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = tail = ListNode()
    carry = 0
    while l1 or l2 or carry:
        s = carry
        if l1:
            s += l1.val
            l1 = l1.next
        if l2:
            s += l2.val
            l2 = l2.next
        carry, digit = divmod(s, 10)
        tail.next = ListNode(digit)
        tail = tail.next
    return dummy.next


# 0019 Remove Nth Node From End ────────────────────────────────────────────────
def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    lead = trail = dummy
    for _ in range(n + 1):
        lead = lead.next
    while lead:
        lead = lead.next
        trail = trail.next
    trail.next = trail.next.next
    return dummy.next


# 0024 Swap Nodes in Pairs ─────────────────────────────────────────────────────
def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = prev = ListNode(0, head)
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
    return dummy.next


# 0025 Reverse Nodes in k-Group ────────────────────────────────────────────────
def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # Check whether k nodes remain.
    node = head
    for _ in range(k):
        if not node:
            return head
        node = node.next
    # Reverse the first k nodes.
    prev = None
    cur = head
    for _ in range(k):
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    head.next = reverse_k_group(cur, k)          # head is now tail of this group
    return prev


# 0138 Copy List with Random Pointer ───────────────────────────────────────────
def copy_random_list(head):
    if head is None:
        return None
    from importlib import import_module
    Node = import_module("0138_copy_list_with_random_pointer").Node
    mapping = {None: None}
    cur = head
    while cur:
        mapping[cur] = Node(cur.val)
        cur = cur.next
    cur = head
    while cur:
        mapping[cur].next = mapping[cur.next]
        mapping[cur].random = mapping[cur.random]
        cur = cur.next
    return mapping[head]


# 0148 Sort List ───────────────────────────────────────────────────────────────
def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    slow, fast = head, head.next                 # split into two halves
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    left = sort_list(head)
    right = sort_list(mid)
    return merge_two_lists(left, right)


# 0023 Merge k Sorted Lists ────────────────────────────────────────────────────
def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    dummy = tail = ListNode()
    while heap:
        _, i, node = heapq.heappop(heap)
        tail.next = node
        tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    tail.next = None
    return dummy.next


# 0146 LRU Cache ───────────────────────────────────────────────────────────────
class LRUCache:
    class _Node:
        __slots__ = ("key", "val", "prev", "next")

        def __init__(self, key=0, val=0):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.head = self._Node()                 # most-recent sentinel
        self.tail = self._Node()                 # least-recent sentinel
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove(node)
            self._add_front(node)
            return
        node = self._Node(key, value)
        self.map[key] = node
        self._add_front(node)
        if len(self.map) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]


if __name__ == "__main__":
    import importlib
    mods = {
        "0160_intersection_of_two_linked_lists": [("get_intersection_node", get_intersection_node)],
        "0206_reverse_linked_list": [("reverse_list", reverse_list)],
        "0234_palindrome_linked_list": [("is_palindrome", is_palindrome)],
        "0141_linked_list_cycle": [("has_cycle", has_cycle)],
        "0142_linked_list_cycle_ii": [("detect_cycle", detect_cycle)],
        "0021_merge_two_sorted_lists": [("merge_two_lists", merge_two_lists)],
        "0002_add_two_numbers": [("add_two_numbers", add_two_numbers)],
        "0019_remove_nth_node_from_end": [("remove_nth_from_end", remove_nth_from_end)],
        "0024_swap_nodes_in_pairs": [("swap_pairs", swap_pairs)],
        "0025_reverse_nodes_in_k_group": [("reverse_k_group", reverse_k_group)],
        "0138_copy_list_with_random_pointer": [("copy_random_list", copy_random_list)],
        "0148_sort_list": [("sort_list", sort_list)],
        "0023_merge_k_sorted_lists": [("merge_k_lists", merge_k_lists)],
        "0146_lru_cache": [("LRUCache", LRUCache)],
    }
    for name, fns in mods.items():
        mod = importlib.import_module(name)
        for attr, fn in fns:
            setattr(mod, attr, fn)
        try:
            mod.test()
            print(f"PASS  {name}")
        except Exception as e:
            print(f"FAIL  {name}: {e}")
