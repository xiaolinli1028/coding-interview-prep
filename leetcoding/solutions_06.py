"""
Reference solutions — LeetCode Hot 100, batch 6 (DP + 2-D DP).
Don't open until you've attempted the problems.

Verify:  python3 solutions_06.py
"""

from bisect import bisect_left
from typing import List


# 0118 Pascal's Triangle ───────────────────────────────────────────────────────
def generate(numRows: int) -> List[List[int]]:
    rows = []
    for r in range(numRows):
        row = [1] * (r + 1)
        for j in range(1, r):
            row[j] = rows[r - 1][j - 1] + rows[r - 1][j]
        rows.append(row)
    return rows


# 0198 House Robber ────────────────────────────────────────────────────────────
def rob(nums: List[int]) -> int:
    prev, cur = 0, 0
    for x in nums:
        prev, cur = cur, max(cur, prev + x)
    return cur


# 0279 Perfect Squares ─────────────────────────────────────────────────────────
def num_squares(n: int) -> int:
    dp = [0] + [float("inf")] * n
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    return dp[n]


# 0322 Coin Change ─────────────────────────────────────────────────────────────
def coin_change(coins: List[int], amount: int) -> int:
    dp = [0] + [float("inf")] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1


# 0139 Word Break ──────────────────────────────────────────────────────────────
def word_break(s: str, wordDict: List[str]) -> bool:
    words = set(wordDict)
    n = len(s)
    dp = [True] + [False] * n
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]


# 0300 Longest Increasing Subsequence ──────────────────────────────────────────
def length_of_lis(nums: List[int]) -> int:
    tails = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


# 0152 Maximum Product Subarray ────────────────────────────────────────────────
def max_product(nums: List[int]) -> int:
    best = cur_max = cur_min = nums[0]
    for x in nums[1:]:
        if x < 0:
            cur_max, cur_min = cur_min, cur_max
        cur_max = max(x, cur_max * x)
        cur_min = min(x, cur_min * x)
        best = max(best, cur_max)
    return best


# 0416 Partition Equal Subset Sum ──────────────────────────────────────────────
def can_partition(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    reachable = {0}
    for x in nums:
        reachable |= {s + x for s in reachable if s + x <= target}
        if target in reachable:
            return True
    return target in reachable


# 0032 Longest Valid Parentheses ───────────────────────────────────────────────
def longest_valid_parentheses(s: str) -> int:
    stack = [-1]
    best = 0
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                best = max(best, i - stack[-1])
    return best


# 0062 Unique Paths ────────────────────────────────────────────────────────────
def unique_paths(m: int, n: int) -> int:
    row = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            row[j] += row[j - 1]
    return row[-1]


# 0064 Minimum Path Sum ────────────────────────────────────────────────────────
def min_path_sum(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    row = [0] * n
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                row[j] = grid[0][0]
            elif i == 0:
                row[j] = row[j - 1] + grid[i][j]
            elif j == 0:
                row[j] = row[j] + grid[i][j]
            else:
                row[j] = min(row[j], row[j - 1]) + grid[i][j]
    return row[-1]


# 0005 Longest Palindromic Substring ───────────────────────────────────────────
def longest_palindrome(s: str) -> str:
    if not s:
        return ""
    start, end = 0, 0

    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r - 1

    for i in range(len(s)):
        for l, r in (expand(i, i), expand(i, i + 1)):
            if r - l > end - start:
                start, end = l, r
    return s[start:end + 1]


# 1143 Longest Common Subsequence ──────────────────────────────────────────────
def longest_common_subsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    prev = [0] * (n + 1)
    for i in range(1, m + 1):
        cur = [0] * (n + 1)
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                cur[j] = prev[j - 1] + 1
            else:
                cur[j] = max(prev[j], cur[j - 1])
        prev = cur
    return prev[n]


# 0072 Edit Distance ───────────────────────────────────────────────────────────
def min_distance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    prev = list(range(n + 1))
    for i in range(1, m + 1):
        cur = [i] + [0] * n
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                cur[j] = prev[j - 1]
            else:
                cur[j] = 1 + min(prev[j], cur[j - 1], prev[j - 1])
        prev = cur
    return prev[n]


if __name__ == "__main__":
    import importlib
    mods = {
        "0118_pascals_triangle": [("generate", generate)],
        "0198_house_robber": [("rob", rob)],
        "0279_perfect_squares": [("num_squares", num_squares)],
        "0322_coin_change": [("coin_change", coin_change)],
        "0139_word_break": [("word_break", word_break)],
        "0300_longest_increasing_subsequence": [("length_of_lis", length_of_lis)],
        "0152_maximum_product_subarray": [("max_product", max_product)],
        "0416_partition_equal_subset_sum": [("can_partition", can_partition)],
        "0032_longest_valid_parentheses": [("longest_valid_parentheses", longest_valid_parentheses)],
        "0062_unique_paths": [("unique_paths", unique_paths)],
        "0064_minimum_path_sum": [("min_path_sum", min_path_sum)],
        "0005_longest_palindromic_substring": [("longest_palindrome", longest_palindrome)],
        "1143_longest_common_subsequence": [("longest_common_subsequence", longest_common_subsequence)],
        "0072_edit_distance": [("min_distance", min_distance)],
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
