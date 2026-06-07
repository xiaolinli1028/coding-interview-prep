"""
236. Lowest Common Ancestor of a Binary Tree  ·  Medium  ·  Binary Tree
=======================================================================
(run: python3 0236_lowest_common_ancestor.py)

Return the lowest node that is an ancestor of both p and q (a node can be its own
ancestor). All values are unique; p and q exist in the tree.

  [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 1  ->  3

PATTERN: post-order DFS — if the current node is p or q, or p and q are found in
different subtrees, it's the LCA. Time O(n), space O(h).
"""

from typing import Optional

from _helpers import TreeNode, build_tree


def lowest_common_ancestor(root, p, q):
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def _find(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return _find(root.left, val) or _find(root.right, val)


def _lca(values, pv, qv):
    root = build_tree(values)
    p, q = _find(root, pv), _find(root, qv)
    return lowest_common_ancestor(root, p, q).val


def test():
    vals = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    assert _lca(vals, 5, 1) == 3
    assert _lca(vals, 5, 4) == 5      # one is ancestor of the other
    assert _lca(vals, 6, 4) == 5
    assert _lca([1, 2], 1, 2) == 1


if __name__ == "__main__":
    try:
        test()
        print("PASS  0236 lowest_common_ancestor")
    except NotImplementedError:
        print("----  0236 lowest_common_ancestor — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0236 lowest_common_ancestor: {e}")
