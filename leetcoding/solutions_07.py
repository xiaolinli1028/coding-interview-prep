"""
Reference solutions — LeetCode Hot 100, batch 7
(Two Pointers / Sliding Window / Substring / Arrays / Matrix / Graph / Stack /
 Heap / Greedy / Tricks — the remaining 23 problems).
Don't open until you've attempted the problems.

Verify:  python3 solutions_07.py
"""

import heapq
from collections import Counter, defaultdict, deque
from typing import List


# 0042 Trapping Rain Water ──────────────────────────────────────────────────────
def trap(height: List[int]) -> int:
    if not height:
        return 0
    l, r = 0, len(height) - 1
    left_max = right_max = total = 0
    while l < r:
        if height[l] < height[r]:
            left_max = max(left_max, height[l])
            total += left_max - height[l]
            l += 1
        else:
            right_max = max(right_max, height[r])
            total += right_max - height[r]
            r -= 1
    return total


# 0438 Find All Anagrams ────────────────────────────────────────────────────────
def find_anagrams(s: str, p: str) -> List[int]:
    if len(p) > len(s):
        return []
    need = Counter(p)
    window = Counter(s[:len(p)])
    res = []
    if window == need:
        res.append(0)
    for i in range(len(p), len(s)):
        window[s[i]] += 1
        left = s[i - len(p)]
        window[left] -= 1
        if window[left] == 0:
            del window[left]
        if window == need:
            res.append(i - len(p) + 1)
    return res


# 0560 Subarray Sum Equals K ────────────────────────────────────────────────────
def subarray_sum(nums: List[int], k: int) -> int:
    counts = defaultdict(int)
    counts[0] = 1
    running = total = 0
    for x in nums:
        running += x
        total += counts[running - k]
        counts[running] += 1
    return total


# 0239 Sliding Window Maximum ───────────────────────────────────────────────────
def max_sliding_window(nums: List[int], k: int) -> List[int]:
    dq = deque()                                 # indices, decreasing values
    res = []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res


# 0076 Minimum Window Substring ─────────────────────────────────────────────────
def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ""
    need = Counter(t)
    missing = len(t)
    best = (float("inf"), 0, 0)
    left = 0
    for right, c in enumerate(s):
        if need[c] > 0:
            missing -= 1
        need[c] -= 1
        while missing == 0:
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right)
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return "" if best[0] == float("inf") else s[best[1]:best[2] + 1]


# 0041 First Missing Positive ───────────────────────────────────────────────────
def first_missing_positive(nums: List[int]) -> int:
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1


# 0240 Search a 2D Matrix II ────────────────────────────────────────────────────
def search_matrix_ii(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    r, c = 0, len(matrix[0]) - 1
    while r < len(matrix) and c >= 0:
        v = matrix[r][c]
        if v == target:
            return True
        if v > target:
            c -= 1
        else:
            r += 1
    return False


# 0200 Number of Islands ────────────────────────────────────────────────────────
def num_islands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])

    def sink(r, c):
        if 0 <= r < m and 0 <= c < n and grid[r][c] == "1":
            grid[r][c] = "0"
            sink(r + 1, c); sink(r - 1, c); sink(r, c + 1); sink(r, c - 1)

    count = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == "1":
                count += 1
                sink(r, c)
    return count


# 0994 Rotting Oranges ──────────────────────────────────────────────────────────
def oranges_rotting(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 2:
                q.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
    minutes = 0
    while q and fresh:
        minutes += 1
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
    return -1 if fresh else minutes


# 0207 Course Schedule ──────────────────────────────────────────────────────────
def can_finish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)
    indeg = [0] * numCourses
    for a, b in prerequisites:
        graph[b].append(a)
        indeg[a] += 1
    q = deque(i for i in range(numCourses) if indeg[i] == 0)
    seen = 0
    while q:
        node = q.popleft()
        seen += 1
        for nxt in graph[node]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return seen == numCourses


# 0208 Implement Trie ───────────────────────────────────────────────────────────
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True

    def _find(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node:
                return None
            node = node[ch]
        return node

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and "$" in node

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None


# 0394 Decode String ────────────────────────────────────────────────────────────
def decode_string(s: str) -> str:
    stack = []
    cur = ""
    num = 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == "[":
            stack.append((cur, num))
            cur, num = "", 0
        elif ch == "]":
            prev, k = stack.pop()
            cur = prev + cur * k
        else:
            cur += ch
    return cur


# 0084 Largest Rectangle in Histogram ──────────────────────────────────────────
def largest_rectangle_area(heights: List[int]) -> int:
    stack = []                                   # indices with increasing heights
    best = 0
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            best = max(best, height * width)
        stack.append(i)
    return best


# 0215 Kth Largest Element ─────────────────────────────────────────────────────
def find_kth_largest(nums: List[int], k: int) -> int:
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


# 0347 Top K Frequent Elements ─────────────────────────────────────────────────
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    counts = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for val, freq in counts.items():
        buckets[freq].append(val)
    res = []
    for freq in range(len(buckets) - 1, 0, -1):
        for val in buckets[freq]:
            res.append(val)
            if len(res) == k:
                return res
    return res


# 0295 Find Median from Data Stream ─────────────────────────────────────────────
class MedianFinder:
    def __init__(self):
        self.lo = []                             # max-heap (negated)
        self.hi = []                             # min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2


# 0045 Jump Game II ─────────────────────────────────────────────────────────────
def jump(nums: List[int]) -> int:
    jumps = end = farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == end:
            jumps += 1
            end = farthest
    return jumps


# 0763 Partition Labels ─────────────────────────────────────────────────────────
def partition_labels(s: str) -> List[int]:
    last = {ch: i for i, ch in enumerate(s)}
    res = []
    start = end = 0
    for i, ch in enumerate(s):
        end = max(end, last[ch])
        if i == end:
            res.append(end - start + 1)
            start = i + 1
    return res


# 0136 Single Number ────────────────────────────────────────────────────────────
def single_number(nums: List[int]) -> int:
    x = 0
    for v in nums:
        x ^= v
    return x


# 0169 Majority Element ─────────────────────────────────────────────────────────
def majority_element(nums: List[int]) -> int:
    candidate = None
    count = 0
    for x in nums:
        if count == 0:
            candidate = x
        count += 1 if x == candidate else -1
    return candidate


# 0075 Sort Colors ──────────────────────────────────────────────────────────────
def sort_colors(nums: List[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# 0031 Next Permutation ─────────────────────────────────────────────────────────
def next_permutation(nums: List[int]) -> None:
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])


# 0287 Find the Duplicate Number ───────────────────────────────────────────────
def find_duplicate(nums: List[int]) -> int:
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


if __name__ == "__main__":
    import importlib
    mods = {
        "0042_trapping_rain_water": [("trap", trap)],
        "0438_find_all_anagrams_in_a_string": [("find_anagrams", find_anagrams)],
        "0560_subarray_sum_equals_k": [("subarray_sum", subarray_sum)],
        "0239_sliding_window_maximum": [("max_sliding_window", max_sliding_window)],
        "0076_minimum_window_substring": [("min_window", min_window)],
        "0041_first_missing_positive": [("first_missing_positive", first_missing_positive)],
        "0240_search_a_2d_matrix_ii": [("search_matrix", search_matrix_ii)],
        "0200_number_of_islands": [("num_islands", num_islands)],
        "0994_rotting_oranges": [("oranges_rotting", oranges_rotting)],
        "0207_course_schedule": [("can_finish", can_finish)],
        "0208_implement_trie": [("Trie", Trie)],
        "0394_decode_string": [("decode_string", decode_string)],
        "0084_largest_rectangle_in_histogram": [("largest_rectangle_area", largest_rectangle_area)],
        "0215_kth_largest_element_in_an_array": [("find_kth_largest", find_kth_largest)],
        "0347_top_k_frequent_elements": [("top_k_frequent", top_k_frequent)],
        "0295_find_median_from_data_stream": [("MedianFinder", MedianFinder)],
        "0045_jump_game_ii": [("jump", jump)],
        "0763_partition_labels": [("partition_labels", partition_labels)],
        "0136_single_number": [("single_number", single_number)],
        "0169_majority_element": [("majority_element", majority_element)],
        "0075_sort_colors": [("sort_colors", sort_colors)],
        "0031_next_permutation": [("next_permutation", next_permutation)],
        "0287_find_the_duplicate_number": [("find_duplicate", find_duplicate)],
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
