"""
543. Diameter of Binary Tree  ·  Easy  ·  Binary Tree
=====================================================
(run: python3 0543_diameter_of_binary_tree.py)

Return the length (number of edges) of the longest path between any two nodes.
The path may or may not pass through the root.

  [1,2,3,4,5]  ->  3   (path 4->2->1->3 or 5->2->1->3)

PATTERN: post-order DFS returning subtree height; at each node update the best
diameter = left_height + right_height. Time O(n), space O(h).
"""

from typing import Optional

from _helpers import TreeNode, build_tree


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert diameter_of_binary_tree(build_tree([1, 2, 3, 4, 5])) == 3
    assert diameter_of_binary_tree(build_tree([1, 2])) == 1
    assert diameter_of_binary_tree(build_tree([1])) == 0
    assert diameter_of_binary_tree(build_tree([])) == 0


if __name__ == "__main__":
    try:
        test()
        print("PASS  0543 diameter_of_binary_tree")
    except NotImplementedError:
        print("----  0543 diameter_of_binary_tree — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0543 diameter_of_binary_tree: {e}")
