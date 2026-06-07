"""
101. Symmetric Tree  ·  Easy  ·  Binary Tree
============================================
(run: python3 0101_symmetric_tree.py)

Return True if a binary tree is a mirror image of itself around its center.

  [1,2,2,3,4,4,3]  ->  True
  [1,2,2,None,3,None,3]  ->  False

PATTERN: recurse on (left, right) pairs — mirror iff values match and (left.left,
right.right) and (left.right, right.left) are mirrors. Time O(n), space O(h).
"""

from typing import Optional

from _helpers import TreeNode, build_tree


def is_symmetric(root: Optional[TreeNode]) -> bool:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert is_symmetric(build_tree([1, 2, 2, 3, 4, 4, 3])) is True
    assert is_symmetric(build_tree([1, 2, 2, None, 3, None, 3])) is False
    assert is_symmetric(build_tree([])) is True
    assert is_symmetric(build_tree([1])) is True
    assert is_symmetric(build_tree([1, 2, 3])) is False


if __name__ == "__main__":
    try:
        test()
        print("PASS  0101 is_symmetric")
    except NotImplementedError:
        print("----  0101 is_symmetric — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0101 is_symmetric: {e}")
