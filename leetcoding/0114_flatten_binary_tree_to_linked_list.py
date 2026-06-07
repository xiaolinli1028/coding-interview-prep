"""
114. Flatten Binary Tree to Linked List  ·  Medium  ·  Binary Tree
==================================================================
(run: python3 0114_flatten_binary_tree_to_linked_list.py)

Flatten the tree into a "linked list" in-place: each node's right child is the
next node in preorder, and all left children become None.

  [1,2,5,3,4,None,6]  ->  1->2->3->4->5->6 (down the right spine)

PATTERN: reverse-preorder DFS (right, left, node) keeping a running `prev`, or a
Morris-style threading. Result is preorder along right pointers. Time O(n).
"""

from typing import Optional

from _helpers import TreeNode, build_tree


def flatten(root: Optional[TreeNode]) -> None:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def _spine(root):
    out = []
    while root:
        assert root.left is None, "left child must be None after flatten"
        out.append(root.val)
        root = root.right
    return out


def test():
    t = build_tree([1, 2, 5, 3, 4, None, 6])
    flatten(t)
    assert _spine(t) == [1, 2, 3, 4, 5, 6]

    t2 = build_tree([])
    flatten(t2)
    assert t2 is None or _spine(t2) == []

    t3 = build_tree([1])
    flatten(t3)
    assert _spine(t3) == [1]

    t4 = build_tree([1, 2, 3])
    flatten(t4)
    assert _spine(t4) == [1, 2, 3]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0114 flatten")
    except NotImplementedError:
        print("----  0114 flatten — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0114 flatten: {e}")
