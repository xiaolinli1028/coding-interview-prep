"""
Reference solutions — LeetCode Hot 100, batch 4 (Binary Tree).
Don't open until you've attempted the problems.

Verify:  python3 solutions_04.py
"""

from collections import defaultdict, deque
from typing import List, Optional

from _helpers import TreeNode


# 0094 Inorder Traversal ───────────────────────────────────────────────────────
def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    out, stack, cur = [], [], root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        out.append(cur.val)
        cur = cur.right
    return out


# 0104 Maximum Depth ───────────────────────────────────────────────────────────
def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# 0226 Invert Binary Tree ──────────────────────────────────────────────────────
def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


# 0101 Symmetric Tree ──────────────────────────────────────────────────────────
def is_symmetric(root: Optional[TreeNode]) -> bool:
    def mirror(a, b):
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return mirror(a.left, b.right) and mirror(a.right, b.left)
    return mirror(root.left, root.right) if root else True


# 0543 Diameter ────────────────────────────────────────────────────────────────
def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    best = 0

    def height(node):
        nonlocal best
        if not node:
            return 0
        lh = height(node.left)
        rh = height(node.right)
        best = max(best, lh + rh)
        return 1 + max(lh, rh)

    height(root)
    return best


# 0102 Level Order Traversal ───────────────────────────────────────────────────
def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        out.append(level)
    return out


# 0108 Sorted Array to BST ─────────────────────────────────────────────────────
def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
    def build(lo, hi):
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        node = TreeNode(nums[mid])
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node
    return build(0, len(nums) - 1)


# 0098 Validate BST ────────────────────────────────────────────────────────────
def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def valid(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return valid(node.left, low, node.val) and valid(node.right, node.val, high)
    return valid(root, float("-inf"), float("inf"))


# 0230 Kth Smallest in BST ─────────────────────────────────────────────────────
def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    stack, cur = [], root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        k -= 1
        if k == 0:
            return cur.val
        cur = cur.right
    return -1


# 0199 Right Side View ─────────────────────────────────────────────────────────
def right_side_view(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        out.append(q[-1].val)
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return out


# 0114 Flatten to Linked List ──────────────────────────────────────────────────
def flatten(root: Optional[TreeNode]) -> None:
    prev = None

    def visit(node):                            # reverse preorder: right, left, node
        nonlocal prev
        if not node:
            return
        visit(node.right)
        visit(node.left)
        node.right = prev
        node.left = None
        prev = node

    visit(root)


# 0105 Build Tree from Preorder + Inorder ──────────────────────────────────────
def build_tree_from(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    idx = {v: i for i, v in enumerate(inorder)}
    self_pre = iter(preorder)

    def build(lo, hi):
        if lo > hi:
            return None
        val = next(self_pre)
        node = TreeNode(val)
        mid = idx[val]
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node

    return build(0, len(inorder) - 1)


# 0437 Path Sum III ────────────────────────────────────────────────────────────
def path_sum(root: Optional[TreeNode], targetSum: int) -> int:
    count = 0
    prefix = defaultdict(int)
    prefix[0] = 1

    def dfs(node, running):
        nonlocal count
        if not node:
            return
        running += node.val
        count += prefix[running - targetSum]
        prefix[running] += 1
        dfs(node.left, running)
        dfs(node.right, running)
        prefix[running] -= 1

    dfs(root, 0)
    return count


# 0236 Lowest Common Ancestor ──────────────────────────────────────────────────
def lowest_common_ancestor(root, p, q):
    if not root or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right


# 0124 Max Path Sum ────────────────────────────────────────────────────────────
def max_path_sum(root: Optional[TreeNode]) -> int:
    best = float("-inf")

    def gain(node):
        nonlocal best
        if not node:
            return 0
        left = max(gain(node.left), 0)
        right = max(gain(node.right), 0)
        best = max(best, node.val + left + right)
        return node.val + max(left, right)

    gain(root)
    return best


if __name__ == "__main__":
    import importlib
    mods = {
        "0094_binary_tree_inorder_traversal": [("inorder_traversal", inorder_traversal)],
        "0104_maximum_depth_of_binary_tree": [("max_depth", max_depth)],
        "0226_invert_binary_tree": [("invert_tree", invert_tree)],
        "0101_symmetric_tree": [("is_symmetric", is_symmetric)],
        "0543_diameter_of_binary_tree": [("diameter_of_binary_tree", diameter_of_binary_tree)],
        "0102_binary_tree_level_order_traversal": [("level_order", level_order)],
        "0108_convert_sorted_array_to_bst": [("sorted_array_to_bst", sorted_array_to_bst)],
        "0098_validate_binary_search_tree": [("is_valid_bst", is_valid_bst)],
        "0230_kth_smallest_element_in_a_bst": [("kth_smallest", kth_smallest)],
        "0199_binary_tree_right_side_view": [("right_side_view", right_side_view)],
        "0114_flatten_binary_tree_to_linked_list": [("flatten", flatten)],
        "0105_construct_binary_tree_from_preorder_and_inorder": [("build_tree_from", build_tree_from)],
        "0437_path_sum_iii": [("path_sum", path_sum)],
        "0236_lowest_common_ancestor": [("lowest_common_ancestor", lowest_common_ancestor)],
        "0124_binary_tree_maximum_path_sum": [("max_path_sum", max_path_sum)],
    }
    for name, fns in mods.items():
        mod = importlib.import_module(name)
        for attr, fn in fns:
            setattr(mod, attr, fn)
        try:
            mod.test()
            print(f"PASS  {name}")
        except Exception as e:
            print(f"FAIL  {name}: {e}")
