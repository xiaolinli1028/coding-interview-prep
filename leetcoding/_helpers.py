"""
Shared helpers for LeetCode problems: linked-list and binary-tree nodes plus
build/compare utilities so tests can use plain Python lists.

    from _helpers import ListNode, list_to_linked, linked_to_list
    from _helpers import TreeNode, build_tree, tree_to_list
"""

from typing import List, Optional


# ── Linked list ───────────────────────────────────────────────────────────────
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def list_to_linked(values: List[int]) -> Optional[ListNode]:
    """[1,2,3] -> 1->2->3 ; [] -> None."""
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def linked_to_list(head: Optional[ListNode]) -> List[int]:
    """1->2->3 -> [1,2,3]. (Assumes no cycle.)"""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def make_cycle(values: List[int], pos: int) -> Optional[ListNode]:
    """Build a list and connect the tail to index `pos` (-1 for no cycle)."""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


# ── Binary tree ───────────────────────────────────────────────────────────────
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """LeetCode level-order format with None for missing nodes.
       [3,9,20,None,None,15,7] -> the standard example tree."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Level-order with trailing None's trimmed (inverse of build_tree)."""
    if not root:
        return []
    out, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out
