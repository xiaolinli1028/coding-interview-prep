# LeetCode Hot 100 — Top 50

Practice harness mirroring `ml_coding/`: each problem is one file with the stub +
embedded tests; reference solutions live in `solutions_NN.py`.

```bash
cd leetcoding
python3 0001_two_sum.py        # prints PASS / FAIL / not-implemented
python3 solutions_01.py        # verify batch-1 reference solutions
```

Each problem file: read the docstring, fill in the `# TODO`, run it. The tests
cover the LeetCode examples plus edge cases. `[x]` = implemented (stub+tests+ref).

---

## Hashing
- [x] 0001 — Two Sum · Easy
- [ ] 0049 — Group Anagrams · Medium
- [ ] 0128 — Longest Consecutive Sequence · Medium

## Two Pointers
- [x] 0283 — Move Zeroes · Easy
- [x] 0011 — Container With Most Water · Medium
- [x] 0015 — 3Sum · Medium
- [ ] 0042 — Trapping Rain Water · Hard

## Sliding Window
- [x] 0003 — Longest Substring Without Repeating Characters · Medium
- [ ] 0076 — Minimum Window Substring · Hard

## Arrays
- [x] 0053 — Maximum Subarray · Medium
- [ ] 0056 — Merge Intervals · Medium
- [x] 0238 — Product of Array Except Self · Medium
- [ ] 0041 — First Missing Positive · Hard

## Matrix
- [ ] 0054 — Spiral Matrix · Medium
- [ ] 0048 — Rotate Image · Medium

## Linked List
- [ ] 0206 — Reverse Linked List · Easy
- [ ] 0021 — Merge Two Sorted Lists · Easy
- [ ] 0141 — Linked List Cycle · Easy
- [ ] 0002 — Add Two Numbers · Medium
- [ ] 0146 — LRU Cache · Medium

## Binary Tree
- [ ] 0104 — Maximum Depth of Binary Tree · Easy
- [ ] 0226 — Invert Binary Tree · Easy
- [ ] 0101 — Symmetric Tree · Easy
- [ ] 0102 — Binary Tree Level Order Traversal · Medium
- [ ] 0098 — Validate Binary Search Tree · Medium
- [ ] 0236 — Lowest Common Ancestor · Medium

## Graph
- [ ] 0200 — Number of Islands · Medium
- [ ] 0207 — Course Schedule · Medium
- [ ] 0208 — Implement Trie · Medium

## Backtracking
- [ ] 0046 — Permutations · Medium
- [ ] 0078 — Subsets · Medium
- [ ] 0022 — Generate Parentheses · Medium

## Binary Search
- [ ] 0033 — Search in Rotated Sorted Array · Medium
- [ ] 0153 — Find Minimum in Rotated Sorted Array · Medium

## Stack
- [x] 0020 — Valid Parentheses · Easy
- [ ] 0155 — Min Stack · Medium
- [ ] 0739 — Daily Temperatures · Medium

## Heap
- [ ] 0215 — Kth Largest Element in an Array · Medium
- [ ] 0347 — Top K Frequent Elements · Medium

## Greedy
- [x] 0121 — Best Time to Buy and Sell Stock · Easy
- [ ] 0055 — Jump Game · Medium

## Dynamic Programming
- [ ] 0070 — Climbing Stairs · Easy
- [ ] 0198 — House Robber · Medium
- [ ] 0322 — Coin Change · Medium
- [ ] 0139 — Word Break · Medium
- [ ] 0300 — Longest Increasing Subsequence · Medium

## 2-D Dynamic Programming
- [ ] 0062 — Unique Paths · Medium
- [ ] 0072 — Edit Distance · Medium

## Tricks
- [ ] 0136 — Single Number · Easy
- [ ] 0169 — Majority Element · Easy

---

**Progress:** Batch 1 done (10/50). Next batches add linked-list/tree/graph
helpers (`ListNode`, `TreeNode`) shared via `_helpers.py`.
