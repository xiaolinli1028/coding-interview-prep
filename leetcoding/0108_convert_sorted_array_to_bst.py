"""
108. Convert Sorted Array to Binary Search Tree  ·  Easy  ·  Binary Tree
=======================================================================
(run: python3 0108_convert_sorted_array_to_bst.py)

Convert an ascending sorted array into a height-balanced BST. Return the root.
(Multiple answers are valid; the test checks BST validity, balance, and that the
inorder traversal matches the input.)

  [-10,-3,0,5,9]  ->  a balanced BST, e.g. [0,-3,9,-10,None,5]

PATTERN: pick the middle as root (keeps it balanced), recurse on the left and
right halves. Time O(n), space O(log n).
"""

from typing import List, Optional

from _helpers import TreeNode


def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def _inorder(node, out):
    if node:
        _inorder(node.left, out)
        out.append(node.val)
        _inorder(node.right, out)


def _height(node):
    if not node:
        return 0
    return 1 + max(_height(node.left), _height(node.right))


def _balanced(node):
    if not node:
        return True
    if abs(_height(node.left) - _height(node.right)) > 1:
        return False
    return _balanced(node.left) and _balanced(node.right)


def _check(nums):
    root = sorted_array_to_bst(nums)
    out = []
    _inorder(root, out)
    assert out == sorted(nums), out          # BST + same elements
    assert _balanced(root), "not height-balanced"


def test():
    _check([-10, -3, 0, 5, 9])
    _check([1, 3])
    _check([0])
    _check([])
    _check([1, 2, 3, 4, 5, 6, 7])


if __name__ == "__main__":
    try:
        test()
        print("PASS  0108 sorted_array_to_bst")
    except NotImplementedError:
        print("----  0108 sorted_array_to_bst — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0108 sorted_array_to_bst: {e}")
