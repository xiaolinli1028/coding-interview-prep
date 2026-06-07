# LeetCode Hot 100

Practice harness mirroring `ml_coding/`: each problem is one file with the stub +
embedded tests; reference solutions live in `solutions_NN.py` (grouped by batch).
Linked-list / tree / graph problems share `_helpers.py` (ListNode, TreeNode,
builders, comparators).

```bash
cd leetcoding
python3 0001_two_sum.py        # fill the # TODO, run -> PASS / FAIL / not-implemented
python3 solutions_01.py        # verify a batch's reference solutions
```

`[x]` = implemented (stub + tests + reference).  Full Hot 100 below, grouped by pattern.

## Hashing
- [x] 0001 — Two Sum · Easy
- [x] 0049 — Group Anagrams · Medium
- [x] 0128 — Longest Consecutive Sequence · Medium

## Two Pointers
- [x] 0283 — Move Zeroes · Easy
- [x] 0011 — Container With Most Water · Medium
- [x] 0015 — 3Sum · Medium
- [ ] 0042 — Trapping Rain Water · Hard

## Sliding Window
- [x] 0003 — Longest Substring Without Repeating Characters · Medium
- [ ] 0438 — Find All Anagrams in a String · Medium

## Substring
- [ ] 0560 — Subarray Sum Equals K · Medium
- [ ] 0239 — Sliding Window Maximum · Hard
- [ ] 0076 — Minimum Window Substring · Hard

## Arrays
- [x] 0053 — Maximum Subarray · Medium
- [x] 0056 — Merge Intervals · Medium
- [x] 0189 — Rotate Array · Medium
- [x] 0238 — Product of Array Except Self · Medium
- [ ] 0041 — First Missing Positive · Hard

## Matrix
- [x] 0073 — Set Matrix Zeroes · Medium
- [x] 0054 — Spiral Matrix · Medium
- [x] 0048 — Rotate Image · Medium
- [ ] 0240 — Search a 2D Matrix II · Medium

## Linked List
- [ ] 0160 — Intersection of Two Linked Lists · Easy
- [ ] 0206 — Reverse Linked List · Easy
- [ ] 0234 — Palindrome Linked List · Easy
- [ ] 0141 — Linked List Cycle · Easy
- [ ] 0142 — Linked List Cycle II · Medium
- [ ] 0021 — Merge Two Sorted Lists · Easy
- [ ] 0002 — Add Two Numbers · Medium
- [ ] 0019 — Remove Nth Node From End of List · Medium
- [ ] 0024 — Swap Nodes in Pairs · Medium
- [ ] 0025 — Reverse Nodes in k-Group · Hard
- [ ] 0138 — Copy List with Random Pointer · Medium
- [ ] 0148 — Sort List · Medium
- [ ] 0023 — Merge k Sorted Lists · Hard
- [ ] 0146 — LRU Cache · Medium

## Binary Tree
- [ ] 0094 — Binary Tree Inorder Traversal · Easy
- [ ] 0104 — Maximum Depth of Binary Tree · Easy
- [ ] 0226 — Invert Binary Tree · Easy
- [ ] 0101 — Symmetric Tree · Easy
- [ ] 0543 — Diameter of Binary Tree · Easy
- [ ] 0102 — Binary Tree Level Order Traversal · Medium
- [ ] 0108 — Convert Sorted Array to Binary Search Tree · Easy
- [ ] 0098 — Validate Binary Search Tree · Medium
- [ ] 0230 — Kth Smallest Element in a BST · Medium
- [ ] 0199 — Binary Tree Right Side View · Medium
- [ ] 0114 — Flatten Binary Tree to Linked List · Medium
- [ ] 0105 — Construct Binary Tree from Preorder and Inorder · Medium
- [ ] 0437 — Path Sum III · Medium
- [ ] 0236 — Lowest Common Ancestor of a Binary Tree · Medium
- [ ] 0124 — Binary Tree Maximum Path Sum · Hard

## Graph
- [ ] 0200 — Number of Islands · Medium
- [ ] 0994 — Rotting Oranges · Medium
- [ ] 0207 — Course Schedule · Medium
- [ ] 0208 — Implement Trie (Prefix Tree) · Medium

## Backtracking
- [ ] 0046 — Permutations · Medium
- [ ] 0078 — Subsets · Medium
- [ ] 0017 — Letter Combinations of a Phone Number · Medium
- [ ] 0039 — Combination Sum · Medium
- [ ] 0022 — Generate Parentheses · Medium
- [ ] 0079 — Word Search · Medium
- [ ] 0131 — Palindrome Partitioning · Medium
- [ ] 0051 — N-Queens · Hard

## Binary Search
- [ ] 0035 — Search Insert Position · Easy
- [ ] 0074 — Search a 2D Matrix · Medium
- [ ] 0034 — Find First and Last Position of Element · Medium
- [ ] 0033 — Search in Rotated Sorted Array · Medium
- [ ] 0153 — Find Minimum in Rotated Sorted Array · Medium
- [ ] 0004 — Median of Two Sorted Arrays · Hard

## Stack
- [x] 0020 — Valid Parentheses · Easy
- [x] 0155 — Min Stack · Medium
- [ ] 0394 — Decode String · Medium
- [x] 0739 — Daily Temperatures · Medium
- [ ] 0084 — Largest Rectangle in Histogram · Hard

## Heap
- [ ] 0215 — Kth Largest Element in an Array · Medium
- [ ] 0347 — Top K Frequent Elements · Medium
- [ ] 0295 — Find Median from Data Stream · Hard

## Greedy
- [x] 0121 — Best Time to Buy and Sell Stock · Easy
- [x] 0055 — Jump Game · Medium
- [ ] 0045 — Jump Game II · Medium
- [ ] 0763 — Partition Labels · Medium

## Dynamic Programming
- [x] 0070 — Climbing Stairs · Easy
- [ ] 0118 — Pascal's Triangle · Easy
- [ ] 0198 — House Robber · Medium
- [ ] 0279 — Perfect Squares · Medium
- [ ] 0322 — Coin Change · Medium
- [ ] 0139 — Word Break · Medium
- [ ] 0300 — Longest Increasing Subsequence · Medium
- [ ] 0152 — Maximum Product Subarray · Medium
- [ ] 0416 — Partition Equal Subset Sum · Medium
- [ ] 0032 — Longest Valid Parentheses · Hard

## 2-D Dynamic Programming
- [ ] 0062 — Unique Paths · Medium
- [ ] 0064 — Minimum Path Sum · Medium
- [ ] 0005 — Longest Palindromic Substring · Medium
- [ ] 1143 — Longest Common Subsequence · Medium
- [ ] 0072 — Edit Distance · Medium

## Tricks
- [ ] 0136 — Single Number · Easy
- [ ] 0169 — Majority Element · Easy
- [ ] 0075 — Sort Colors · Medium
- [ ] 0031 — Next Permutation · Medium
- [ ] 0287 — Find the Duplicate Number · Medium

---

**Progress:** 20 / 100 implemented (batches 1-2). Remaining batches are generated
incrementally; each adds ~10 problems + a `solutions_NN.py`.
