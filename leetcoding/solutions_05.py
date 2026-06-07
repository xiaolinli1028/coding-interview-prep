"""
Reference solutions — LeetCode Hot 100, batch 5 (Backtracking + Binary Search).
Don't open until you've attempted the problems.

Verify:  python3 solutions_05.py
"""

from bisect import bisect_left, bisect_right
from typing import List


# 0046 Permutations ────────────────────────────────────────────────────────────
def permute(nums: List[int]) -> List[List[int]]:
    res = []

    def bt(path, remaining):
        if not remaining:
            res.append(path[:])
            return
        for i in range(len(remaining)):
            bt(path + [remaining[i]], remaining[:i] + remaining[i + 1:])

    bt([], nums)
    return res


# 0078 Subsets ─────────────────────────────────────────────────────────────────
def subsets(nums: List[int]) -> List[List[int]]:
    res = [[]]
    for x in nums:
        res += [cur + [x] for cur in res]
    return res


# 0017 Letter Combinations ─────────────────────────────────────────────────────
def letter_combinations(digits: str) -> List[str]:
    if not digits:
        return []
    table = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
    }
    res = [""]
    for d in digits:
        res = [prefix + ch for prefix in res for ch in table[d]]
    return res


# 0039 Combination Sum ─────────────────────────────────────────────────────────
def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    candidates.sort()

    def bt(start, remaining, path):
        if remaining == 0:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            bt(i, remaining - candidates[i], path)
            path.pop()

    bt(0, target, [])
    return res


# 0022 Generate Parentheses ────────────────────────────────────────────────────
def generate_parenthesis(n: int) -> List[str]:
    res = []

    def bt(s, open_, close):
        if len(s) == 2 * n:
            res.append(s)
            return
        if open_ < n:
            bt(s + "(", open_ + 1, close)
        if close < open_:
            bt(s + ")", open_, close + 1)

    bt("", 0, 0)
    return res


# 0079 Word Search ─────────────────────────────────────────────────────────────
def exist(board: List[List[str]], word: str) -> bool:
    m, n = len(board), len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[i]:
            return False
        tmp = board[r][c]
        board[r][c] = "#"
        found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or
                 dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
        board[r][c] = tmp
        return found

    for r in range(m):
        for c in range(n):
            if dfs(r, c, 0):
                return True
    return False


# 0131 Palindrome Partitioning ─────────────────────────────────────────────────
def partition(s: str) -> List[List[str]]:
    res = []

    def bt(start, path):
        if start == len(s):
            res.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if piece == piece[::-1]:
                path.append(piece)
                bt(end, path)
                path.pop()

    bt(0, [])
    return res


# 0051 N-Queens ────────────────────────────────────────────────────────────────
def solve_n_queens(n: int) -> List[List[str]]:
    res = []
    cols, d1, d2 = set(), set(), set()
    placement = []

    def bt(r):
        if r == n:
            res.append(["".join("Q" if c == col else "." for c in range(n)) for col in placement])
            return
        for c in range(n):
            if c in cols or (r + c) in d1 or (r - c) in d2:
                continue
            cols.add(c); d1.add(r + c); d2.add(r - c); placement.append(c)
            bt(r + 1)
            cols.remove(c); d1.remove(r + c); d2.remove(r - c); placement.pop()

    bt(0)
    return res


# 0035 Search Insert Position ──────────────────────────────────────────────────
def search_insert(nums: List[int], target: int) -> int:
    return bisect_left(nums, target)


# 0074 Search a 2D Matrix ──────────────────────────────────────────────────────
def search_matrix(matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = matrix[mid // n][mid % n]
        if val == target:
            return True
        if val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


# 0034 Find First and Last Position ────────────────────────────────────────────
def search_range(nums: List[int], target: int) -> List[int]:
    lo = bisect_left(nums, target)
    if lo == len(nums) or nums[lo] != target:
        return [-1, -1]
    return [lo, bisect_right(nums, target) - 1]


# 0033 Search in Rotated Sorted Array ──────────────────────────────────────────
def search(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:                # left half sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                    # right half sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


# 0153 Find Minimum in Rotated Sorted Array ────────────────────────────────────
def find_min(nums: List[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]


# 0004 Median of Two Sorted Arrays ─────────────────────────────────────────────
def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    if len(A) > len(B):
        A, B = B, A
    m, n = len(A), len(B)
    half = (m + n + 1) // 2
    lo, hi = 0, m
    while lo <= hi:
        i = (lo + hi) // 2                       # cut in A
        j = half - i                             # cut in B
        a_left = A[i - 1] if i > 0 else float("-inf")
        a_right = A[i] if i < m else float("inf")
        b_left = B[j - 1] if j > 0 else float("-inf")
        b_right = B[j] if j < n else float("inf")
        if a_left <= b_right and b_left <= a_right:
            if (m + n) % 2:
                return float(max(a_left, b_left))
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        elif a_left > b_right:
            hi = i - 1
        else:
            lo = i + 1
    return 0.0


if __name__ == "__main__":
    import importlib
    mods = {
        "0046_permutations": [("permute", permute)],
        "0078_subsets": [("subsets", subsets)],
        "0017_letter_combinations_of_a_phone_number": [("letter_combinations", letter_combinations)],
        "0039_combination_sum": [("combination_sum", combination_sum)],
        "0022_generate_parentheses": [("generate_parenthesis", generate_parenthesis)],
        "0079_word_search": [("exist", exist)],
        "0131_palindrome_partitioning": [("partition", partition)],
        "0051_n_queens": [("solve_n_queens", solve_n_queens)],
        "0035_search_insert_position": [("search_insert", search_insert)],
        "0074_search_a_2d_matrix": [("search_matrix", search_matrix)],
        "0034_find_first_and_last_position": [("search_range", search_range)],
        "0033_search_in_rotated_sorted_array": [("search", search)],
        "0153_find_minimum_in_rotated_sorted_array": [("find_min", find_min)],
        "0004_median_of_two_sorted_arrays": [("find_median_sorted_arrays", find_median_sorted_arrays)],
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
