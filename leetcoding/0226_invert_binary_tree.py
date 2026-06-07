"""
226. Invert Binary Tree  ·  Easy  ·  Binary Tree
================================================
(run: python3 0226_invert_binary_tree.py)

Invert a binary tree (mirror it) and return the root.

  [4,2,7,1,3,6,9]  ->  [4,7,2,9,6,3,1]

PATTERN: recursion — swap left and right children, then recurse on both. Time
O(n), space O(h).
"""

from typing import Optional

from _helpers import TreeNode, build_tree, tree_to_list


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert tree_to_list(invert_tree(build_tree([4, 2, 7, 1, 3, 6, 9]))) == [4, 7, 2, 9, 6, 3, 1]
    assert tree_to_list(invert_tree(build_tree([2, 1, 3]))) == [2, 3, 1]
    assert tree_to_list(invert_tree(build_tree([]))) == []
    assert tree_to_list(invert_tree(build_tree([1]))) == [1]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0226 invert_tree")
    except NotImplementedError:
        print("----  0226 invert_tree — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0226 invert_tree: {e}")
