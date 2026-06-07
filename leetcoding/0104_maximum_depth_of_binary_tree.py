"""
104. Maximum Depth of Binary Tree  ·  Easy  ·  Binary Tree
==========================================================
(run: python3 0104_maximum_depth_of_binary_tree.py)

Return the maximum depth (number of nodes along the longest root-to-leaf path).

  [3,9,20,None,None,15,7]  ->  3

PATTERN: recursion — depth = 1 + max(depth(left), depth(right)). Time O(n),
space O(h).
"""

from typing import Optional

from _helpers import TreeNode, build_tree


def max_depth(root: Optional[TreeNode]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert max_depth(build_tree([3, 9, 20, None, None, 15, 7])) == 3
    assert max_depth(build_tree([])) == 0
    assert max_depth(build_tree([1])) == 1
    assert max_depth(build_tree([1, 2, None, 3, None, 4])) == 4   # left-leaning chain


if __name__ == "__main__":
    try:
        test()
        print("PASS  0104 max_depth")
    except NotImplementedError:
        print("----  0104 max_depth — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0104 max_depth: {e}")
