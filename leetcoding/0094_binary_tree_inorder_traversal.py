"""
94. Binary Tree Inorder Traversal  ·  Easy  ·  Binary Tree
==========================================================
(run: python3 0094_binary_tree_inorder_traversal.py)

Return the inorder (left, node, right) traversal of a binary tree's values.

  [1,None,2,3]  ->  [1,3,2]

PATTERN: recursion (or an explicit stack) visiting left subtree, node, right
subtree. Time O(n), space O(h).
"""

from typing import List, Optional

from _helpers import TreeNode, build_tree


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert inorder_traversal(build_tree([1, None, 2, 3])) == [1, 3, 2]
    assert inorder_traversal(build_tree([])) == []
    assert inorder_traversal(build_tree([1])) == [1]
    assert inorder_traversal(build_tree([2, 1, 3])) == [1, 2, 3]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0094 inorder_traversal")
    except NotImplementedError:
        print("----  0094 inorder_traversal — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0094 inorder_traversal: {e}")
