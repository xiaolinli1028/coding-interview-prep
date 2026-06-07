"""
102. Binary Tree Level Order Traversal  ·  Medium  ·  Binary Tree
=================================================================
(run: python3 0102_binary_tree_level_order_traversal.py)

Return the level-order traversal as a list of levels (left to right).

  [3,9,20,None,None,15,7]  ->  [[3],[9,20],[15,7]]

PATTERN: BFS with a queue, processing one full level per outer iteration. Time
O(n), space O(n).
"""

from typing import List, Optional

from _helpers import TreeNode, build_tree


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert level_order(build_tree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
    assert level_order(build_tree([1])) == [[1]]
    assert level_order(build_tree([])) == []
    assert level_order(build_tree([1, 2, 3, 4, None, None, 5])) == [[1], [2, 3], [4, 5]]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0102 level_order")
    except NotImplementedError:
        print("----  0102 level_order — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0102 level_order: {e}")
