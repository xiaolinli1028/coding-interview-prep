"""
124. Binary Tree Maximum Path Sum  ·  Hard  ·  Binary Tree
==========================================================
(run: python3 0124_binary_tree_maximum_path_sum.py)

A path is any sequence of nodes connected by edges, each node used at most once;
the path need not pass through the root. Return the maximum path sum.

  [-10,9,20,None,None,15,7]  ->  42   (15 + 20 + 7)

PATTERN: post-order DFS returning the best downward gain (>=0) from each node;
at each node update the answer with left_gain + node + right_gain. Time O(n).
"""

from typing import Optional

from _helpers import TreeNode, build_tree


def max_path_sum(root: Optional[TreeNode]) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert max_path_sum(build_tree([1, 2, 3])) == 6
    assert max_path_sum(build_tree([-10, 9, 20, None, None, 15, 7])) == 42
    assert max_path_sum(build_tree([-3])) == -3        # single negative node
    assert max_path_sum(build_tree([2, -1])) == 2
    assert max_path_sum(build_tree([-2, -1])) == -1


if __name__ == "__main__":
    try:
        test()
        print("PASS  0124 max_path_sum")
    except NotImplementedError:
        print("----  0124 max_path_sum — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0124 max_path_sum: {e}")
