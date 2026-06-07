"""
Reference solutions — LeetCode Hot 100, batch 2.
Don't open until you've attempted the problems.

Verify:  python3 solutions_02.py
"""

from typing import List


# 0128 Longest Consecutive Sequence ───────────────────────────────────────────
def longest_consecutive(nums: List[int]) -> int:
    s = set(nums)
    best = 0
    for x in s:
        if x - 1 not in s:                      # only start at a run's left end
            length = 1
            while x + length in s:
                length += 1
            best = max(best, length)
    return best


# 0056 Merge Intervals ────────────────────────────────────────────────────────
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda iv: iv[0])
    out = []
    for s, e in intervals:
        if out and s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return out


# 0189 Rotate Array ───────────────────────────────────────────────────────────
def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n
    def rev(i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    rev(0, n - 1)
    rev(0, k - 1)
    rev(k, n - 1)


# 0073 Set Matrix Zeroes ──────────────────────────────────────────────────────
def set_zeroes(matrix: List[List[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    col0 = any(matrix[i][0] == 0 for i in range(m))
    row0 = any(matrix[0][j] == 0 for j in range(n))
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if row0:
        for j in range(n):
            matrix[0][j] = 0
    if col0:
        for i in range(m):
            matrix[i][0] = 0


# 0054 Spiral Matrix ──────────────────────────────────────────────────────────
def spiral_order(matrix: List[List[int]]) -> List[int]:
    res = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            res.append(matrix[top][j])
        top += 1
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
    return res


# 0048 Rotate Image ───────────────────────────────────────────────────────────
def rotate_image(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n):                          # transpose
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:                          # reverse each row
        row.reverse()


# 0155 Min Stack ──────────────────────────────────────────────────────────────
class MinStack:
    def __init__(self):
        self._stack = []                        # (val, min_so_far)

    def push(self, val: int) -> None:
        m = val if not self._stack else min(val, self._stack[-1][1])
        self._stack.append((val, m))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]


# 0739 Daily Temperatures ─────────────────────────────────────────────────────
def daily_temperatures(temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = []                                  # indices, decreasing temps
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res


# 0055 Jump Game ──────────────────────────────────────────────────────────────
def can_jump(nums: List[int]) -> bool:
    reach = 0
    for i, x in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + x)
    return True


# 0070 Climbing Stairs ────────────────────────────────────────────────────────
def climb_stairs(n: int) -> int:
    a, b = 1, 1                                 # ways(0), ways(1)
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    import importlib
    mods = {
        "0128_longest_consecutive_sequence": [("longest_consecutive", longest_consecutive)],
        "0056_merge_intervals": [("merge", merge)],
        "0189_rotate_array": [("rotate", rotate)],
        "0073_set_matrix_zeroes": [("set_zeroes", set_zeroes)],
        "0054_spiral_matrix": [("spiral_order", spiral_order)],
        "0048_rotate_image": [("rotate", rotate_image)],
        "0155_min_stack": [("MinStack", MinStack)],
        "0739_daily_temperatures": [("daily_temperatures", daily_temperatures)],
        "0055_jump_game": [("can_jump", can_jump)],
        "0070_climbing_stairs": [("climb_stairs", climb_stairs)],
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
