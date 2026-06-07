"""
437. Path Sum III  ·  Medium  ·  Binary Tree
============================================
(run: python3 0437_path_sum_iii.py)

Count the number of downward paths (going parent->child, not necessarily starting
at the root or ending at a leaf) whose values sum to `targetSum`.

  [10,5,-3,3,2,None,11,3,-2,None,1], target = 8  ->  3

PATTERN: prefix-sum hash map along the current root-to-node path; the count of
prefix == current_sum - target gives paths ending here. Time O(n), space O(h).
"""

from typing import Optional

from _helpers import TreeNode, build_tree


def path_sum(root: Optional[TreeNode], targetSum: int) -> int:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    t = build_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    assert path_sum(t, 8) == 3
    assert path_sum(build_tree([]), 0) == 0
    assert path_sum(build_tree([1]), 1) == 1
    assert path_sum(build_tree([1, -2, -3]), -1) == 1
    # single negative-then-positive path
    assert path_sum(build_tree([0, 1, 1]), 1) == 4


if __name__ == "__main__":
    try:
        test()
        print("PASS  0437 path_sum")
    except NotImplementedError:
        print("----  0437 path_sum — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0437 path_sum: {e}")
