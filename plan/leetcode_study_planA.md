# 🚀 LeetCode 高效刷题计划

> **制定日期**: 2026-03-07
> **当前进度**: 已完成 LeetCode 18-23（涵盖双指针、链表、栈、回溯、分治/堆）
> **目标**: 系统性掌握核心算法与数据结构，具备面试实战能力

---

## 📋 计划总览

本计划按 **「专题突破」** 模式组织，而非简单的顺序刷题。每个专题包含：
1. **核心概念** — 需要掌握的关键思想
2. **必刷题目** — 由易到难，层层递进
3. **目标耗时** — 每道题建议的时间上限

### ⏰ 建议节奏
| 阶段 | 每日题量 | 每题时限 | 预计周期 |
|------|---------|---------|---------|
| 基础巩固 | 3-4 题 | 30 min | 2 周 |
| 专题突破 | 2-3 题 | 40 min | 4 周 |
| 综合提升 | 2 题 | 45 min | 2 周 |
| 模拟面试 | 3-4 题/次 | 60 min/次 | 持续 |

### 🎯 刷题方法论
1. **先想再看**: 每道题先独立思考 15-20 分钟，想不出来再看提示
2. **暴力优先**: 先写出暴力解法，再逐步优化
3. **总结模板**: 每个专题结束后整理代码模板
4. **间隔复习**: 使用艾宾浩斯记忆法，在 1天/3天/7天/14天 后复习
5. **归类总结**: 识别题目之间的相似性，举一反三

---

## 📅 第一阶段：基础数据结构（第 1-2 周）

### 1.1 数组 & 哈希表 ⭐
> **核心**: 哈希加速查找、原地操作、计数技巧

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | 🟢 | 哈希表一次遍历 | ⬜ |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | 🟡 | 排序/计数作为 key | ⬜ |
| 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | 🟡 | 哈希集合 O(n) | ⬜ |
| 36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | 🟡 | 行/列/宫哈希 | ⬜ |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | 🟡 | 前缀积 & 后缀积 | ⬜ |
| 41 | [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) | 🔴 | 原地哈希(索引映射) | ⬜ |

### 1.2 字符串 ⭐
> **核心**: 双指针、滑窗、KMP/Z函数

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | 🟡 | 滑动窗口 + 哈希 | ⬜ |
| 76 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | 🔴 | 滑动窗口模板 | ⬜ |
| 5 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | 🟡 | 中心扩展 / Manacher | ⬜ |
| 438 | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | 🟡 | 固定窗口 + 计数 | ⬜ |
| 28 | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | 🟢 | KMP 算法 | ⬜ |

### 1.3 链表 ⭐
> **核心**: 哑节点、快慢指针、反转、合并
> **已完成**: #19, #21, #23

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | 🟢 | 迭代/递归反转 | ⬜ |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | 🟢 | 快慢指针检测环 | ⬜ |
| 142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | 🟡 | Floyd 算法找入口 | ⬜ |
| 25 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | 🔴 | 分组反转 | ⬜ |
| 146 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | 🟡 | 哈希+双向链表 | ⬜ |
| 138 | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | 🟡 | 哈希/交织复制 | ⬜ |

### 1.4 栈 & 队列 ⭐
> **核心**: 单调栈、括号匹配、辅助栈
> **已完成**: #20

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/) | 🟡 | 辅助栈同步更新 | ⬜ |
| 84 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | 🔴 | 单调栈经典 | ⬜ |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | 🔴 | 单调栈 / 双指针 | ⬜ |
| 739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | 🟡 | 单调递减栈 | ⬜ |
| 394 | [Decode String](https://leetcode.com/problems/decode-string/) | 🟡 | 栈模拟递归 | ⬜ |
| 224 | [Basic Calculator](https://leetcode.com/problems/basic-calculator/) | 🔴 | 栈处理括号 | ⬜ |

---

## 📅 第二阶段：核心算法范式（第 3-4 周）

### 2.1 双指针 & 滑动窗口 ⭐⭐
> **核心**: 对撞指针、快慢指针、窗口收缩条件
> **已完成**: #18 (4Sum)

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | 🟡 | 排序+双指针去重 | ⬜ |
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | 🟡 | 贪心+对撞指针 | ⬜ |
| 209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | 🟡 | 滑动窗口 | ⬜ |
| 567 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | 🟡 | 固定窗口 | ⬜ |
| 30 | [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) | 🔴 | 多指针滑窗 | ⬜ |

### 2.2 二分查找 ⭐⭐
> **核心**: 边界处理、搜索空间、最小化/最大化问题

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 704 | [Binary Search](https://leetcode.com/problems/binary-search/) | 🟢 | 基础模板 | ⬜ |
| 34 | [Find First and Last Position](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | 🟡 | 左右边界二分 | ⬜ |
| 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | 🟡 | 旋转数组二分 | ⬜ |
| 153 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | 🟡 | 旋转数组极值 | ⬜ |
| 4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | 🔴 | 二分查找分割点 | ⬜ |
| 875 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | 🟡 | 二分答案 | ⬜ |

### 2.3 排序 ⭐
> **核心**: 归并、快排、桶排序、自定义排序

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 912 | [Sort an Array](https://leetcode.com/problems/sort-an-array/) | 🟡 | 快排/归并实现 | ⬜ |
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | 🟡 | 排序后合并 | ⬜ |
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | 🟡 | 三路快排/荷兰旗 | ⬜ |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | 🟡 | 桶排序/快速选择 | ⬜ |
| 215 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | 🟡 | 快速选择 O(n) | ⬜ |

### 2.4 回溯 ⭐⭐
> **核心**: 选择-探索-撤销、剪枝优化
> **已完成**: #22 (Generate Parentheses)

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 46 | [Permutations](https://leetcode.com/problems/permutations/) | 🟡 | 排列模板 | ⬜ |
| 78 | [Subsets](https://leetcode.com/problems/subsets/) | 🟡 | 子集模板 | ⬜ |
| 39 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | 🟡 | 组合+去重 | ⬜ |
| 79 | [Word Search](https://leetcode.com/problems/word-search/) | 🟡 | 网格回溯 | ⬜ |
| 51 | [N-Queens](https://leetcode.com/problems/n-queens/) | 🔴 | 经典回溯+剪枝 | ⬜ |
| 131 | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | 🟡 | 回溯+动规预处理 | ⬜ |

---

## 📅 第三阶段：树 & 图（第 5-6 周）

### 3.1 二叉树 ⭐⭐
> **核心**: 递归思维、遍历框架、分治思想

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | 🟢 | 递归基础 | ⬜ |
| 226 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | 🟢 | 递归翻转 | ⬜ |
| 101 | [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) | 🟢 | 镜像判断 | ⬜ |
| 102 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | 🟡 | BFS 层序 | ⬜ |
| 236 | [Lowest Common Ancestor](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | 🟡 | 后序遍历 LCA | ⬜ |
| 124 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | 🔴 | 后序+全局最大 | ⬜ |
| 297 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | 🔴 | 前序序列化 | ⬜ |
| 105 | [Construct Binary Tree from Preorder and Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | 🟡 | 分治构建 | ⬜ |

### 3.2 二叉搜索树 (BST) ⭐
> **核心**: BST 性质、中序有序、搜索/插入/删除

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 98 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | 🟡 | 中序/范围判断 | ⬜ |
| 230 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | 🟡 | 中序第k个 | ⬜ |
| 235 | [Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | 🟡 | BST 分岔点 | ⬜ |
| 450 | [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) | 🟡 | 删除+替换 | ⬜ |

### 3.3 图论基础 ⭐⭐
> **核心**: DFS/BFS、拓扑排序、并查集

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | 🟡 | 网格 DFS/BFS | ⬜ |
| 695 | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | 🟡 | DFS 计面积 | ⬜ |
| 207 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | 🟡 | 拓扑排序(BFS) | ⬜ |
| 210 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | 🟡 | 拓扑排序输出序列 | ⬜ |
| 133 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | 🟡 | BFS/DFS + 哈希 | ⬜ |
| 127 | [Word Ladder](https://leetcode.com/problems/word-ladder/) | 🔴 | 双向 BFS | ⬜ |
| 547 | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | 🟡 | 并查集入门 | ⬜ |

---

## 📅 第四阶段：动态规划（第 7-8 周）

### 4.1 一维 DP ⭐⭐
> **核心**: 状态定义、转移方程、空间优化

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | 🟢 | DP 入门 | ⬜ |
| 198 | [House Robber](https://leetcode.com/problems/house-robber/) | 🟡 | 选/不选 | ⬜ |
| 213 | [House Robber II](https://leetcode.com/problems/house-robber-ii/) | 🟡 | 环形分解 | ⬜ |
| 139 | [Word Break](https://leetcode.com/problems/word-break/) | 🟡 | 字符串 DP | ⬜ |
| 300 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | 🟡 | LIS：DP + 二分 | ⬜ |
| 152 | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | 🟡 | 维护最大最小 | ⬜ |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) | 🟡 | 完全背包 | ⬜ |

### 4.2 二维 DP ⭐⭐
> **核心**: 网格DP、区间DP、字符串DP

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 62 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | 🟡 | 网格 DP 入门 | ⬜ |
| 64 | [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) | 🟡 | 网格最优路径 | ⬜ |
| 1143 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | 🟡 | LCS 经典 | ⬜ |
| 72 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | 🟡 | 字符串DP经典 | ⬜ |
| 10 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | 🔴 | 复杂字符串DP | ⬜ |
| 312 | [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | 🔴 | 区间 DP | ⬜ |

### 4.3 背包问题 ⭐⭐
> **核心**: 0-1背包、完全背包、多重背包

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 416 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | 🟡 | 0-1 背包 | ⬜ |
| 494 | [Target Sum](https://leetcode.com/problems/target-sum/) | 🟡 | 0-1 背包变体 | ⬜ |
| 518 | [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | 🟡 | 完全背包计数 | ⬜ |
| 474 | [Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/) | 🟡 | 二维背包 | ⬜ |

---

## 📅 第五阶段：高级数据结构 & 算法（第 9-10 周）

### 5.1 堆 / 优先队列 ⭐⭐
> **核心**: 大顶堆、小顶堆、Top-K 问题
> **已完成**: #23 (Merge k Sorted Lists 使用了堆)

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 295 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | 🔴 | 对顶堆 | ⬜ |
| 373 | [Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | 🟡 | 多路归并堆 | ⬜ |
| 621 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | 🟡 | 贪心+堆 | ⬜ |
| 767 | [Reorganize String](https://leetcode.com/problems/reorganize-string/) | 🟡 | 贪心+堆 | ⬜ |

### 5.2 字典树 (Trie) ⭐
> **核心**: 前缀匹配、字符串检索

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 208 | [Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) | 🟡 | Trie 基础实现 | ⬜ |
| 211 | [Design Add and Search Words](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | 🟡 | Trie + DFS | ⬜ |
| 212 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | 🔴 | Trie + 回溯 | ⬜ |

### 5.3 贪心算法 ⭐⭐
> **核心**: 局部最优→全局最优、反证法

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 55 | [Jump Game](https://leetcode.com/problems/jump-game/) | 🟡 | 最远可达 | ⬜ |
| 45 | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | 🟡 | BFS 层思维 | ⬜ |
| 134 | [Gas Station](https://leetcode.com/problems/gas-station/) | 🟡 | 净油量分析 | ⬜ |
| 763 | [Partition Labels](https://leetcode.com/problems/partition-labels/) | 🟡 | 最远出现位置 | ⬜ |
| 135 | [Candy](https://leetcode.com/problems/candy/) | 🔴 | 两次遍历 | ⬜ |

### 5.4 位运算 ⭐
> **核心**: 异或性质、位掩码

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 136 | [Single Number](https://leetcode.com/problems/single-number/) | 🟢 | 异或消除 | ⬜ |
| 191 | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | 🟢 | n & (n-1) | ⬜ |
| 338 | [Counting Bits](https://leetcode.com/problems/counting-bits/) | 🟢 | DP + 位运算 | ⬜ |
| 371 | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | 🟡 | 位运算加法 | ⬜ |

---

## 📅 第六阶段：综合提升 & 面试高频（第 11-12 周）

### 6.1 设计题 ⭐
| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 380 | [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | 🟡 | 数组+哈希 | ⬜ |
| 355 | [Design Twitter](https://leetcode.com/problems/design-twitter/) | 🟡 | 堆+链表 | ⬜ |
| 460 | [LFU Cache](https://leetcode.com/problems/lfu-cache/) | 🔴 | 双哈希+双向链表 | ⬜ |

### 6.2 数学 & 技巧题 ⭐
| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 48 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | 🟡 | 转置+翻转 | ⬜ |
| 54 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | 🟡 | 边界收缩 | ⬜ |
| 73 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | 🟡 | 原地标记 | ⬜ |
| 169 | [Majority Element](https://leetcode.com/problems/majority-element/) | 🟢 | Boyer-Moore 投票 | ⬜ |
| 287 | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | 🟡 | Floyd 判环 | ⬜ |

---

## 📊 统计面板

| 专题 | 总题数 | 已完成 | 完成率 |
|------|--------|--------|--------|
| 数组 & 哈希表 | 6 | 0 | 0% |
| 字符串 | 5 | 0 | 0% |
| 链表 | 6 (+3 已做) | 3 | 33% |
| 栈 & 队列 | 6 (+1 已做) | 1 | 14% |
| 双指针 & 滑窗 | 5 (+1 已做) | 1 | 17% |
| 二分查找 | 6 | 0 | 0% |
| 排序 | 5 | 0 | 0% |
| 回溯 | 6 (+1 已做) | 1 | 14% |
| 二叉树 | 8 | 0 | 0% |
| BST | 4 | 0 | 0% |
| 图论 | 7 | 0 | 0% |
| 一维 DP | 7 | 0 | 0% |
| 二维 DP | 6 | 0 | 0% |
| 背包问题 | 4 | 0 | 0% |
| 堆 | 4 (+1 已做) | 1 | 20% |
| 字典树 | 3 | 0 | 0% |
| 贪心 | 5 | 0 | 0% |
| 位运算 | 4 | 0 | 0% |
| 设计题 | 3 | 0 | 0% |
| 数学技巧 | 5 | 0 | 0% |
| **总计** | **109 (+6 已做)** | **7** | **6%** |

---

## 🔑 每个专题的代码模板（刷完专题后总结）

> 完成每个专题后，在下方记录该专题的通用模板代码。

### 滑动窗口模板
```python
# TODO: 完成「字符串」专题后总结
```

### 二分查找模板
```python
# TODO: 完成「二分查找」专题后总结
```

### 回溯模板
```python
# TODO: 完成「回溯」专题后总结
```

### BFS/DFS 模板
```python
# TODO: 完成「图论」专题后总结
```

### 动态规划模板
```python
# TODO: 完成「DP」专题后总结
```

---

## 📝 复习日志

| 日期 | 复习题目 | 是否独立做出 | 备注 |
|------|---------|-------------|------|
| | | | |

---

## 💡 Tips & 注意事项

1. **不要死磕**：一道题超过 45 分钟没思路，果断看题解，理解后重新写一遍
2. **手写代码**：面试时没有 IDE，平时练习尽量少依赖自动补全
3. **口述思路**：练习时大声说出自己的思路，模拟面试场景
4. **关注边界**：空数组、单元素、负数、溢出等边界条件
5. **时空复杂度**：每道题都要分析时间和空间复杂度
6. **总结规律**：相似题目归类，找到通用解题框架
