"""
199. Binary Tree Right Side View  ·  Medium  ·  Binary Tree
===========================================================
(run: python3 0199_binary_tree_right_side_view.py)

Return the values visible from the right side, top to bottom (the last node of
each level).

  [1,2,3,None,5,None,4]  ->  [1,3,4]

PATTERN: level-order BFS, taking the last node of each level (or DFS visiting
right child first and recording the first node seen per depth). Time O(n).
"""

from typing import List, Optional

from _helpers import TreeNode, build_tree


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert right_side_view(build_tree([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
    assert right_side_view(build_tree([1, None, 3])) == [1, 3]
    assert right_side_view(build_tree([])) == []
    assert right_side_view(build_tree([1, 2, 3, 4])) == [1, 3, 4]


if __name__ == "__main__":
    try:
        test()
        print("PASS  0199 right_side_view")
    except NotImplementedError:
        print("----  0199 right_side_view — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0199 right_side_view: {e}")
