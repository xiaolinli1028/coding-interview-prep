"""
98. Validate Binary Search Tree  ·  Medium  ·  Binary Tree
==========================================================
(run: python3 0098_validate_binary_search_tree.py)

Return True if a binary tree is a valid BST: every node's left subtree < node <
right subtree (strictly), for the whole subtree.

  [2,1,3]  ->  True
  [5,1,4,None,None,3,6]  ->  False

PATTERN: DFS carrying an open (low, high) interval that tightens as you descend.
Time O(n), space O(h).
"""

from typing import Optional

from _helpers import TreeNode, build_tree


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert is_valid_bst(build_tree([2, 1, 3])) is True
    assert is_valid_bst(build_tree([5, 1, 4, None, None, 3, 6])) is False
    assert is_valid_bst(build_tree([])) is True
    assert is_valid_bst(build_tree([1])) is True
    # 3 is in the right subtree of 5 but equals/less than an ancestor bound -> invalid
    assert is_valid_bst(build_tree([5, 4, 6, None, None, 3, 7])) is False


if __name__ == "__main__":
    try:
        test()
        print("PASS  0098 is_valid_bst")
    except NotImplementedError:
        print("----  0098 is_valid_bst — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0098 is_valid_bst: {e}")
