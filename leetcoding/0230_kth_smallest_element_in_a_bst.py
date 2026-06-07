"""
230. Kth Smallest Element in a BST  ·  Medium  ·  Binary Tree
============================================================
(run: python3 0230_kth_smallest_element_in_a_bst.py)

Return the kth smallest value (1-indexed) in a BST.

  [3,1,4,None,2], k = 1  ->  1

PATTERN: inorder traversal of a BST yields sorted values; stop at the kth. Time
O(h + k), space O(h).
"""

from typing import Optional

from _helpers import TreeNode, build_tree


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert kth_smallest(build_tree([3, 1, 4, None, 2]), 1) == 1
    assert kth_smallest(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3) == 3
    assert kth_smallest(build_tree([1]), 1) == 1
    assert kth_smallest(build_tree([2, 1, 3]), 3) == 3


if __name__ == "__main__":
    try:
        test()
        print("PASS  0230 kth_smallest")
    except NotImplementedError:
        print("----  0230 kth_smallest — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0230 kth_smallest: {e}")
