"""
Reference solutions — LeetCode Hot 100, batch 1.
Don't open until you've attempted the problems.

Verify all batch-1 references pass their own tests:  python3 solutions_01.py
"""

from collections import defaultdict
from typing import List


# 0001 Two Sum ────────────────────────────────────────────────────────────────
def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}                                  # value -> index
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []


# 0003 Longest Substring Without Repeating ────────────────────────────────────
def length_of_longest_substring(s: str) -> int:
    last = {}                                  # char -> last index seen
    left = best = 0
    for right, c in enumerate(s):
        if c in last and last[c] >= left:
            left = last[c] + 1                 # jump past the previous occurrence
        last[c] = right
        best = max(best, right - left + 1)
    return best


# 0011 Container With Most Water ──────────────────────────────────────────────
def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        best = max(best, (right - left) * min(height[left], height[right]))
        if height[left] < height[right]:       # move the shorter wall
            left += 1
        else:
            right -= 1
    return best


# 0015 3Sum ───────────────────────────────────────────────────────────────────
def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue                           # skip duplicate fixed element
        if nums[i] > 0:
            break                              # sorted: no way to reach 0
        lo, hi = i + 1, n - 1
        while lo < hi:
            s = nums[i] + nums[lo] + nums[hi]
            if s < 0:
                lo += 1
            elif s > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1                     # skip dup
                while lo < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1
    return res


# 0020 Valid Parentheses ──────────────────────────────────────────────────────
def is_valid(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for c in s:
        if c in pairs:                         # a closing bracket
            if not stack or stack.pop() != pairs[c]:
                return False
        else:
            stack.append(c)
    return not stack


# 0053 Maximum Subarray ───────────────────────────────────────────────────────
def max_sub_array(nums: List[int]) -> int:
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)                  # extend or restart
        best = max(best, cur)
    return best


# 0121 Best Time to Buy and Sell Stock ────────────────────────────────────────
def max_profit(prices: List[int]) -> int:
    min_price = float("inf")
    best = 0
    for p in prices:
        min_price = min(min_price, p)
        best = max(best, p - min_price)
    return best


# 0238 Product of Array Except Self ───────────────────────────────────────────
def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    out = [1] * n
    for i in range(1, n):                       # prefix product into out
        out[i] = out[i - 1] * nums[i - 1]
    suffix = 1
    for i in range(n - 1, -1, -1):              # multiply running suffix
        out[i] *= suffix
        suffix *= nums[i]
    return out


# 0283 Move Zeroes ────────────────────────────────────────────────────────────
def move_zeroes(nums: List[int]) -> None:
    w = 0                                       # next slot for a non-zero
    for x in nums:
        if x != 0:
            nums[w] = x
            w += 1
    for i in range(w, len(nums)):
        nums[i] = 0


# 0049 Group Anagrams ─────────────────────────────────────────────────────────
def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))                  # canonical anagram key
        groups[key].append(s)
    return list(groups.values())


if __name__ == "__main__":
    import importlib
    mods = {
        "0001_two_sum": [("two_sum", two_sum)],
        "0003_longest_substring_without_repeating": [("length_of_longest_substring", length_of_longest_substring)],
        "0011_container_with_most_water": [("max_area", max_area)],
        "0015_3sum": [("three_sum", three_sum)],
        "0020_valid_parentheses": [("is_valid", is_valid)],
        "0053_maximum_subarray": [("max_sub_array", max_sub_array)],
        "0121_best_time_to_buy_sell_stock": [("max_profit", max_profit)],
        "0238_product_except_self": [("product_except_self", product_except_self)],
        "0283_move_zeroes": [("move_zeroes", move_zeroes)],
        "0049_group_anagrams": [("group_anagrams", group_anagrams)],
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
