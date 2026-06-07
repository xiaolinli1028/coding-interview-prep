"""
105. Construct Binary Tree from Preorder and Inorder  ·  Medium  ·  Binary Tree
==============================================================================
(run: python3 0105_construct_binary_tree_from_preorder_and_inorder.py)

Given preorder and inorder traversals (no duplicate values), rebuild the tree.

  preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]  ->  [3,9,20,None,None,15,7]

PATTERN: preorder[0] is the root; its index in inorder splits left/right
subtrees. Recurse using an index map for O(1) lookups. Time O(n), space O(n).
"""

from typing import List, Optional

from _helpers import TreeNode, tree_to_list


def build_tree_from(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    r = build_tree_from([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert tree_to_list(r) == [3, 9, 20, None, None, 15, 7]
    assert tree_to_list(build_tree_from([-1], [-1])) == [-1]
    assert tree_to_list(build_tree_from([], [])) == []
    assert tree_to_list(build_tree_from([1, 2], [2, 1])) == [1, 2]   # left child
    assert tree_to_list(build_tree_from([1, 2], [1, 2])) == [1, None, 2]  # right child


if __name__ == "__main__":
    try:
        test()
        print("PASS  0105 build_tree_from")
    except NotImplementedError:
        print("----  0105 build_tree_from — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0105 build_tree_from: {e}")
