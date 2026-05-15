# 14. 一维 DP

本目录按最新 `plan/leetcode_study_planB.md` 的一维 DP 顺序整理。

| 顺序 | 题号 | 题目 | 关键点 | 目录 |
|:--:|---:|---|---|---|
| 1 | 70 | Climbing Stairs | 斐波那契 DP | `01_q70` |
| 2 | 121 | Best Time to Buy and Sell Stock | 维护历史最低 | `02_q121` |
| 3 | 53 | Maximum Subarray | Kadane 算法 | `03_q53` |
| 4 | 152 | Maximum Product Subarray | 同时维护最大/最小 | `04_q152` |
| 5 | 198 | House Robber | 选 / 不选 | `05_q198` |
| 6 | 213 | House Robber II | 环形约束拆两段 | `06_q213` |
| 7 | 91 | Decode Ways | 分段选择 DP | `07_q91` |
| 8 | 279 | Perfect Squares | 完全背包 / BFS 最短步数 | `08_q279` |
| 9 | 322 | Coin Change | 完全背包最少硬币 | `09_q322` |
| 10 | 377 | Combination Sum IV | 排列型完全背包 | `10_q377` |
| 11 | 300 | Longest Increasing Subsequence | DP + 二分 | `11_q300` |
| 12 | 139 | Word Break | 字符串切分 DP | `12_q139` |
| 13 | 140 | Word Break II（选做） | DP 剪枝 + 回溯输出 | `13_q140` |

## 模板辨析

| 类型 | 代表题 | 状态转移特征 |
|---|---|---|
| 斐波那契型 | 70, 91 | `dp[i]` 由前 1/2 个位置转移 |
| 子数组型 | 53, 152 | `dp[i]` 表示“必须以 i 结尾”的最优值 |
| 选择型 | 198, 213 | 当前选或不选，通常可压缩成两个变量 |
| 完全背包 | 279, 322, 377 | 物品可重复；注意最值、组合数、排列数的循环顺序 |
| 子序列型 | 300 | 可用 `O(n^2)` DP，也可用贪心 + 二分优化 |
| 字符串切分 | 139, 140 | `dp[i]` 表示前缀能否被合法切分，输出型再接回溯 |
