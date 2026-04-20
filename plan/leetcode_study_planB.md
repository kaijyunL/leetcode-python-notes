# 🚀 LeetCode 高效刷题计划（前200题 + 模板题）

> **制定日期**: 2026-03-07 | **已完成**: #18-23 | **总题数**: 176 + 18 模板题
> **策略**: 专题突破，由易到难，间隔复习

---

## ⏰ 建议节奏 & 方法论

| 阶段 | 每日题量 | 每题时限 | 周期 |
|------|---------|---------|------|
| 基础巩固 | 3-4 题 | 30 min | 3 周 |
| 专题突破 | 2-3 题 | 40 min | 6 周 |
| 综合提升 | 2 题 | 45 min | 3 周 |

**核心原则**: ① 先暴力再优化 ② 超45min看题解 ③ 每专题总结模板 ④ 1/3/7/14天复习

---

## 🧠 刷题心态与策略指南

> **核心认知：刷题吃力 ≠ 基本功不扎实，算法思维是一种需要专门训练的技能。**

### 刷题能力 vs 工作能力

这是两个有交集但不完全相同的技能树：

| 工作中用到的能力 | 刷题考察的能力 |
|-----------------|---------------|
| 系统设计、架构思维 | **算法思维**（需专项训练） |
| 代码可读性、可维护性 | 数据结构的灵活运用 |
| 业务理解、需求分析 | 时间/空间复杂度的敏感度 |
| 团队协作、工具链使用 | 在限定时间内快速建模 |
| 调试和排查问题 | 题型模式识别能力 |

> 💡 就像一个经验丰富的厨师不一定能在限时赛中表现最好——不是厨艺不行，而是"比赛型烹饪"是另一种能力。

### 感到吃力的真正原因

1. **缺乏「题型模式识别」能力** — 刷题的核心不是记住每道题的解法，而是识别题型 → 套用对应的思路框架。需要**按专题分类练习**（本计划已按专题组织 ✅）
2. **从暴力到最优的过渡不够自然** — 对常见优化技巧（双指针、滑动窗口、单调栈、记忆化等）还需要更多"肌肉记忆"
3. **按编号顺序刷效率不高** — 集中刷同一类型的题目更容易建立模式识别能力

### 🎯 高效刷题五原则

1. **不要自我怀疑** — 刷题是专项训练，和工作能力是两码事
2. **按专题刷** — 集中练习同一类型的题，比按编号刷效率高 3-5 倍（本计划已按专题组织 ✅）
3. **控制难度曲线** — 每个专题先做 🟢简单 → 🟡中等，🔴困难题先暂时跳过
4. **重复 > 数量** — 做过的中等题，隔 3 天再做一遍，比多做一道新题更有价值（配合下方复习日志 ✅）
5. **限时训练** — 给自己设定时间（🟢15min，🟡25min，🔴40min），培养在压力下思考的能力

---

## 📅 第一阶段：基础数据结构（第 1-3 周）

### 1.1 数组 & 哈希表（17 题）

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 1 | Two Sum | 🟢 | 哈希表一次遍历 | ⬜ |
| 26 | Remove Duplicates from Sorted Array | 🟢 | 快慢指针原地 | ⬜ |
| 27 | Remove Element | 🟢 | 双指针覆盖 | ⬜ |
| 31 | Next Permutation | 🟡 | 找规律：降序→交换→翻转 | ⬜ |
| 36 | Valid Sudoku | 🟡 | 行/列/宫哈希集合 | ⬜ |
| 41 | First Missing Positive | 🔴 | 原地哈希(索引映射) | ⬜ |
| 48 | Rotate Image | 🟡 | 转置+水平翻转 | ⬜ |
| 49 | Group Anagrams | 🟡 | 排序/计数作 key | ⬜ |
| 54 | Spiral Matrix | 🟡 | 四边界收缩 | ⬜ |
| 59 | Spiral Matrix II | 🟡 | 同上，填充 | ⬜ |
| 66 | Plus One | 🟢 | 进位处理 | ⬜ |
| 73 | Set Matrix Zeroes | 🟡 | 首行首列作标记 | ⬜ |
| 118 | Pascal's Triangle | 🟢 | 逐行构建 | ⬜ |
| 119 | Pascal's Triangle II | 🟢 | 滚动数组优化 | ⬜ |
| 128 | Longest Consecutive Sequence | 🟡 | 哈希集合 O(n) | ⬜ |
| 169 | Majority Element | 🟢 | Boyer-Moore 投票 | ⬜ |
| 189 | Rotate Array | 🟡 | 三次翻转法 | ⬜ |

**📋 推荐刷题顺序：**

> 🟢 基础入门 → 🟡 技巧强化 → 🔴 综合挑战

| 顺序 | # | 题目 | 理由 |
|:----:|---|------|------|
| 1 | 1 | Two Sum | 🟢 哈希表入门，最经典的第一道 |
| 2 | 66 | Plus One | 🟢 简单数组操作 + 进位思维 |
| 3 | 26 | Remove Duplicates | 🟢 快慢指针在数组中的基础用法 |
| 4 | 27 | Remove Element | 🟢 与 #26 同类型，巩固双指针覆盖 |
| 5 | 169 | Majority Element | 🟢 Boyer-Moore 投票法，面试高频 |
| 6 | 118 | Pascal's Triangle | 🟢 逐行构建，DP 思维启蒙 |
| 7 | 119 | Pascal's Triangle II | 🟢 #118 的进阶，学会滚动数组优化 |
| 8 | 189 | Rotate Array | 🟡 三次翻转法，经典原地操作 |
| 9 | 49 | Group Anagrams | 🟡 哈希表进阶，排序/计数做 key |
| 10 | 128 | Longest Consecutive Sequence | 🟡 哈希集合 O(n)，经典面试题 |
| 11 | 48 | Rotate Image | 🟡 矩阵操作入门：转置 + 翻转 |
| 12 | 54 | Spiral Matrix | 🟡 四边界收缩法 |
| 13 | 59 | Spiral Matrix II | 🟡 #54 的填充版，紧跟加深理解 |
| 14 | 73 | Set Matrix Zeroes | 🟡 原地标记技巧 |
| 15 | 36 | Valid Sudoku | 🟡 行/列/宫哈希，综合哈希应用 |
| 16 | 31 | Next Permutation | 🟡 找规律题，降序→交换→翻转 |
| 17 | 41 | First Missing Positive | 🔴 原地哈希终极应用，理解索引映射 |

### 1.2 字符串（13 题）

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 6 | Zigzag Conversion | 🟡 | 按行分组/周期 | ⬜ |
| 8 | String to Integer (atoi) | 🟡 | 状态机/边界处理 | ⬜ |
| 14 | Longest Common Prefix | 🟢 | 纵向逐字符比较 | ⬜ |
| 28 | Find the Index of First Occurrence | 🟢 | KMP 算法 | ⬜ |
| 38 | Count and Say | 🟡 | 递推模拟 | ⬜ |
| 43 | Multiply Strings | 🟡 | 竖式乘法逐位 | ⬜ |
| 58 | Length of Last Word | 🟢 | 反向遍历 | ⬜ |
| 65 | Valid Number | 🔴 | 有限状态机 | ⬜ |
| 67 | Add Binary | 🟢 | 模拟加法进位 | ⬜ |
| 68 | Text Justification | 🔴 | 贪心模拟排版 | ⬜ |
| 125 | Valid Palindrome | 🟢 | 双指针跳非字母 | ⬜ |
| 151 | Reverse Words in a String | 🟡 | 分割+反转 | ⬜ |
| 165 | Compare Version Numbers | 🟡 | 分割逐段比较 | ⬜ |

**📋 推荐刷题顺序：**

> 🟢 基础遍历 → 🟡 模式匹配/模拟 → 🔴 状态机/排版

| 顺序 | # | 题目 | 理由 |
|:----:|---|------|------|
| 1 | 58 | Length of Last Word | 🟢 字符串最基础操作，热身 |
| 2 | 14 | Longest Common Prefix | 🟢 纵向逐字符比较，锻炼基础思维 |
| 3 | 125 | Valid Palindrome | 🟢 双指针在字符串中的应用 |
| 4 | 67 | Add Binary | 🟢 模拟加法进位，与 #66(Plus One) 呼应 |
| 5 | 28 | Find the Index of First Occurrence | 🟢 串匹配入门，可延伸学 KMP |
| 6 | 165 | Compare Version Numbers | 🟡 分割逐段比较，边界处理练习 |
| 7 | 151 | Reverse Words in a String | 🟡 分割 + 反转，字符串综合操作 |
| 8 | 38 | Count and Say | 🟡 递推模拟，培养读题能力 |
| 9 | 6 | Zigzag Conversion | 🟡 按行分组/周期规律 |
| 10 | 43 | Multiply Strings | 🟡 竖式乘法逐位，#67 进阶版 |
| 11 | 8 | String to Integer (atoi) | 🟡 状态机/边界处理，面试常考 |
| 12 | 65 | Valid Number | 🔴 完整有限状态机实现，#8 的升级 |
| 13 | 68 | Text Justification | 🔴 贪心模拟排版，综合模拟能力 |

### 1.3 链表（15 + 3✅ + 1模板 = 19 题）

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 2 | Add Two Numbers | 🟡 | 进位链表相加 | ⬜ |
| 19 | Remove Nth Node From End | 🟡 | 快慢指针 | ✅ |
| 21 | Merge Two Sorted Lists | 🟢 | 递归/迭代合并 | ✅ |
| 23 | Merge k Sorted Lists | 🔴 | 最小堆多路归并 | ✅ |
| 24 | Swap Nodes in Pairs | 🟡 | 递归/哑节点 | ⬜ |
| 25 | Reverse Nodes in k-Group | 🔴 | 分组反转 | ⬜ |
| 61 | Rotate List | 🟡 | 成环+断开 | ⬜ |
| 82 | Remove Duplicates from Sorted List II | 🟡 | 哑节点+跳过 | ⬜ |
| 83 | Remove Duplicates from Sorted List | 🟢 | 遍历去重 | ⬜ |
| 86 | Partition List | 🟡 | 双链表分割合并 | ⬜ |
| 92 | Reverse Linked List II | 🟡 | 区间反转 | ⬜ |
| 138 | Copy List with Random Pointer | 🟡 | 哈希/交织复制 | ⬜ |
| 141 | Linked List Cycle | 🟢 | 快慢指针检测 | ⬜ |
| 142 | Linked List Cycle II | 🟡 | Floyd 找入口 | ⬜ |
| 143 | Reorder List | 🟡 | 找中点+反转+合并 | ⬜ |
| 147 | Insertion Sort List | 🟡 | 链表插入排序 | ⬜ |
| 148 | Sort List | 🟡 | 归并排序链表 | ⬜ |
| 160 | Intersection of Two Linked Lists | 🟢 | 双指针走等距 | ⬜ |
| **206** | **Reverse Linked List** 🏷️模板 | 🟢 | 迭代/递归反转 | ⬜ |

**📋 推荐刷题顺序：**

> ⚠️ **必须先做 #206（反转链表模板）**，它是后续多道题的基础！

| 顺序 | # | 题目 | 理由 |
|:----:|---|------|------|
| 1 | **206** | **Reverse Linked List** 🏷️ | 🟢 **链表核心模板**，迭代/递归反转必须先掌握 |
| 2 | 83 | Remove Duplicates from Sorted List | 🟢 最简单的链表遍历操作 |
| 3 | 21 | Merge Two Sorted Lists | 🟢 递归/迭代合并，链表基础 ✅ |
| 4 | 160 | Intersection of Two Linked Lists | 🟢 双指针走等距，直觉训练 |
| 5 | 141 | Linked List Cycle | 🟢 快慢指针检测环 |
| 6 | 142 | Linked List Cycle II | 🟡 Floyd 找入口，#141 的直接进阶 |
| 7 | 2 | Add Two Numbers | 🟡 链表进位相加 |
| 8 | 19 | Remove Nth Node From End | 🟡 快慢指针变体 ✅ |
| 9 | 24 | Swap Nodes in Pairs | 🟡 递归/哑节点，依赖 #206 思路 |
| 10 | 92 | Reverse Linked List II | 🟡 区间反转，#206 的直接升级版 |
| 11 | 82 | Remove Duplicates II | 🟡 哑节点 + 跳过，#83 的进阶 |
| 12 | 86 | Partition List | 🟡 双链表分割合并 |
| 13 | 61 | Rotate List | 🟡 成环 + 断开 |
| 14 | 143 | Reorder List | 🟡 综合题：找中点 + 反转(#206) + 合并(#21) |
| 15 | 138 | Copy List with Random Pointer | 🟡 哈希/交织复制，拓宽思路 |
| 16 | 147 | Insertion Sort List | 🟡 链表排序入门 |
| 17 | 148 | Sort List | 🟡 归并排序链表，#147 后做 |
| 18 | 25 | Reverse Nodes in k-Group | 🔴 分组反转，依赖 #206 + #24 |
| 19 | 23 | Merge k Sorted Lists | 🔴 多路归并，依赖 #21 ✅ |

### 1.4 栈 & 队列（6 + 1✅ + 1模板 = 8 题）

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 20 | Valid Parentheses | 🟢 | 括号匹配 | ✅ |
| 32 | Longest Valid Parentheses | 🔴 | 栈/DP 两种解法 | ⬜ |
| 42 | Trapping Rain Water | 🔴 | 单调栈/双指针 | ⬜ |
| 71 | Simplify Path | 🟡 | 栈处理路径 | ⬜ |
| 84 | Largest Rectangle in Histogram | 🔴 | 单调递增栈 | ⬜ |
| 150 | Evaluate Reverse Polish Notation | 🟡 | 栈模拟计算 | ⬜ |
| 155 | Min Stack | 🟡 | 辅助栈同步 | ⬜ |
| **739** | **Daily Temperatures** 🏷️模板 | 🟡 | 单调递减栈 | ⬜ |

**📋 推荐刷题顺序：**

> 先掌握栈基本用法 → 单调栈模板 → Hard 综合题

| 顺序 | # | 题目 | 理由 |
|:----:|---|------|------|
| 1 | 20 | Valid Parentheses | 🟢 栈最经典入门 ✅ |
| 2 | 155 | Min Stack | 🟡 辅助栈思想，数据结构设计 |
| 3 | 150 | Evaluate Reverse Polish Notation | 🟡 栈模拟计算，加深栈的理解 |
| 4 | 71 | Simplify Path | 🟡 栈处理路径，字符串 + 栈综合 |
| 5 | **739** | **Daily Temperatures** 🏷️ | 🟡 **单调栈核心模板**，后续题依赖 |
| 6 | 84 | Largest Rectangle in Histogram | 🔴 单调递增栈经典，依赖 #739 思路 |
| 7 | 42 | Trapping Rain Water | 🔴 单调栈/双指针，与 #84 思路相通 |
| 8 | 32 | Longest Valid Parentheses | 🔴 栈/DP，#20 的终极升级版 |

---

## 📅 第二阶段：核心算法范式（第 4-6 周）

### 2.1 双指针 & 滑动窗口（9 + 1✅ + 1模板 = 11 题）

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 3 | Longest Substring Without Repeating Chars | 🟡 | 滑窗+哈希 | ⬜ |
| 11 | Container With Most Water | 🟡 | 贪心对撞指针 | ⬜ |
| 15 | 3Sum | 🟡 | 排序+双指针去重 | ⬜ |
| 16 | 3Sum Closest | 🟡 | 排序+双指针 | ⬜ |
| 18 | 4Sum | 🟡 | 排序+多层双指针 | ✅ |
| 30 | Substring with Concatenation of All Words | 🔴 | 多起点滑窗 | ⬜ |
| 76 | Minimum Window Substring | 🔴 | 滑窗收缩模板 | ⬜ |
| 80 | Remove Duplicates from Sorted Array II | 🟡 | 通用覆盖写法 | ⬜ |
| 88 | Merge Sorted Array | 🟢 | 逆向双指针 | ⬜ |
| 167 | Two Sum II | 🟡 | 有序对撞指针 | ⬜ |
| **438** | **Find All Anagrams** 🏷️模板 | 🟡 | 固定窗口+计数 | ⬜ |

**📋 推荐刷题顺序：**

> 双指针基础 → 多指针组合 → 滑动窗口模板 → Hard 滑窗

| 顺序 | # | 题目 | 理由 |
|:----:|---|------|------|
| 1 | 88 | Merge Sorted Array | 🟢 逆向双指针，最简单的双指针题 |
| 2 | 167 | Two Sum II | 🟡 有序对撞指针，双指针套路入门 |
| 3 | 11 | Container With Most Water | 🟡 贪心对撞指针，#167 的变体 |
| 4 | 80 | Remove Duplicates II | 🟡 通用覆盖写法，与1.1中 #26/#27 呼应 |
| 5 | 15 | 3Sum | 🟡 排序 + 双指针去重，经典高频 |
| 6 | 16 | 3Sum Closest | 🟡 #15 的变体，紧跟做 |
| 7 | 18 | 4Sum | 🟡 多层双指针，#15/#16 的扩展 ✅ |
| 8 | 3 | Longest Substring Without Repeating | 🟡 **滑窗入门**，掌握「扩张+收缩」模式 |
| 9 | **438** | **Find All Anagrams** 🏷️ | 🟡 固定窗口 + 计数，滑窗模板题 |
| 10 | 76 | Minimum Window Substring | 🔴 滑窗收缩模板，#3/#438 的终极版 |
| 11 | 30 | Substring with Concat of All Words | 🔴 多起点滑窗，#76 思路 + 更复杂约束 |

### 2.2 二分查找（10 题）

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 4 | Median of Two Sorted Arrays | 🔴 | 二分找分割点 | ⬜ |
| 33 | Search in Rotated Sorted Array | 🟡 | 判断有序半边 | ⬜ |
| 34 | Find First and Last Position | 🟡 | 左右边界二分 | ⬜ |
| 35 | Search Insert Position | 🟢 | 基础二分 | ⬜ |
| 69 | Sqrt(x) | 🟢 | 二分/牛顿法 | ⬜ |
| 74 | Search a 2D Matrix | 🟡 | 展平成一维二分 | ⬜ |
| 81 | Search in Rotated Sorted Array II | 🟡 | 含重复元素 | ⬜ |
| 153 | Find Minimum in Rotated Sorted Array | 🟡 | 旋转数组极值 | ⬜ |
| 154 | Find Minimum in Rotated Sorted Array II | 🔴 | 含重复+最坏O(n) | ⬜ |
| 162 | Find Peak Element | 🟡 | 峰值二分 | ⬜ |

**📋 推荐刷题顺序：**

> 基础二分 → 边界变体 → 旋转数组系列 → Hard

| 顺序 | # | 题目 | 理由 |
|:----:|---|------|------|
| 1 | 35 | Search Insert Position | 🟢 最基础的二分模板 |
| 2 | 69 | Sqrt(x) | 🟢 二分应用，理解「逼近」思想 |
| 3 | 34 | Find First and Last Position | 🟡 左右边界二分，#35 的直接进阶 |
| 4 | 74 | Search a 2D Matrix | 🟡 展平成一维二分 |
| 5 | 162 | Find Peak Element | 🟡 峰值二分，扩展二分适用范围 |
| 6 | 33 | Search in Rotated Sorted Array | 🟡 旋转数组入门，判断有序半边 |
| 7 | 153 | Find Minimum in Rotated Array | 🟡 旋转数组找极值，与 #33 互补 |
| 8 | 81 | Search in Rotated Array II | 🟡 #33 含重复元素版本 |
| 9 | 154 | Find Minimum in Rotated II | 🔴 #153 含重复版，最坏 O(n) |
| 10 | 4 | Median of Two Sorted Arrays | 🔴 二分终极题，需前面功底 |

### 2.3 排序（5 题）

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 56 | Merge Intervals | 🟡 | 排序后合并 | ⬜ |
| 57 | Insert Interval | 🟡 | 区间插入合并 | ⬜ |
| 75 | Sort Colors | 🟡 | 荷兰旗三路分区 | ⬜ |
| 164 | Maximum Gap | 🔴 | 桶排序 O(n) | ⬜ |
| 179 | Largest Number | 🟡 | 自定义排序规则 | ⬜ |

**📋 推荐刷题顺序：**

> 算法应用 → 区间问题 → 特殊排序

| 顺序 | # | 题目 | 理由 |
|:----:|---|------|------|
| 1 | 75 | Sort Colors | 🟡 荷兰旗三路分区，排序基础 |
| 2 | 56 | Merge Intervals | 🟡 排序后合并，区间问题入门 |
| 3 | 57 | Insert Interval | 🟡 #56 的变体，区间插入合并 |
| 4 | 179 | Largest Number | 🟡 自定义排序规则，面试常考 |
| 5 | 164 | Maximum Gap | 🔴 桶排序 O(n)，理解非比较排序 |

### 2.4 回溯（14 + 1✅ = 15 题）

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 17 | Letter Combinations of a Phone Number | 🟡 | 多选一组合 | ⬜ |
| 22 | Generate Parentheses | 🟡 | 括号生成 | ✅ |
| 37 | Sudoku Solver | 🔴 | 约束回溯 | ⬜ |
| 39 | Combination Sum | 🟡 | 可重复选 | ⬜ |
| 40 | Combination Sum II | 🟡 | 不重复+去重 | ⬜ |
| 46 | Permutations | 🟡 | 排列模板 | ⬜ |
| 47 | Permutations II | 🟡 | 排列+去重 | ⬜ |
| 51 | N-Queens | 🔴 | 经典回溯+剪枝 | ⬜ |
| 52 | N-Queens II | 🔴 | 同上计数版 | ⬜ |
| 77 | Combinations | 🟡 | 组合模板 | ⬜ |
| 78 | Subsets | 🟡 | 子集模板 | ⬜ |
| 79 | Word Search | 🟡 | 网格DFS回溯 | ⬜ |
| 90 | Subsets II | 🟡 | 子集+去重 | ⬜ |
| 93 | Restore IP Addresses | 🟡 | 分段回溯 | ⬜ |
| 131 | Palindrome Partitioning | 🟡 | 回溯+预处理 | ⬜ |

**📋 推荐刷题顺序：**

> 三大模板（子集→组合→排列）→ 变体去重 → 字符串回溯 → Hard

| 顺序 | # | 题目 | 理由 |
|:----:|---|------|------|
| 1 | 78 | Subsets | 🟡 **子集模板**，回溯最基础框架 |
| 2 | 90 | Subsets II | 🟡 子集 + 去重，紧跟 #78 |
| 3 | 77 | Combinations | 🟡 **组合模板**，限制长度的子集 |
| 4 | 39 | Combination Sum | 🟡 可重复选，#77 变体 |
| 5 | 40 | Combination Sum II | 🟡 不重复 + 去重，#39 + #90 的结合 |
| 6 | 46 | Permutations | 🟡 **排列模板** |
| 7 | 47 | Permutations II | 🟡 排列 + 去重，#46 直接升级 |
| 8 | 17 | Letter Combinations of Phone | 🟡 多选一组合，应用回溯 |
| 9 | 22 | Generate Parentheses | 🟡 条件约束回溯 ✅ |
| 10 | 93 | Restore IP Addresses | 🟡 分段回溯，字符串切割 |
| 11 | 131 | Palindrome Partitioning | 🟡 回溯 + 预处理判回文 |
| 12 | 79 | Word Search | 🟡 网格 DFS 回溯，拓宽场景 |
| 13 | 51 | N-Queens | 🔴 经典回溯 + 剪枝 |
| 14 | 52 | N-Queens II | 🔴 #51 计数版，紧跟做 |
| 15 | 37 | Sudoku Solver | 🔴 约束回溯终极题 |

---

## 📅 第三阶段：树 & 图（第 7-9 周）

### 3.1 二叉树（21 题）

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 94 | Binary Tree Inorder Traversal | 🟢 | 中序(栈/Morris) | ⬜ |
| 100 | Same Tree | 🟢 | 递归比较 | ⬜ |
| 101 | Symmetric Tree | 🟢 | 镜像递归 | ⬜ |
| 102 | Binary Tree Level Order Traversal | 🟡 | BFS 层序 | ⬜ |
| 103 | Binary Tree Zigzag Level Order | 🟡 | 之字形BFS | ⬜ |
| 104 | Maximum Depth of Binary Tree | 🟢 | 递归求深度 | ⬜ |
| 105 | Construct from Preorder and Inorder | 🟡 | 分治+哈希定位 | ⬜ |
| 106 | Construct from Inorder and Postorder | 🟡 | 分治 | ⬜ |
| 107 | Binary Tree Level Order II | 🟡 | BFS+翻转 | ⬜ |
| 110 | Balanced Binary Tree | 🟢 | 后序判高度 | ⬜ |
| 111 | Minimum Depth of Binary Tree | 🟢 | 注意叶子节点 | ⬜ |
| 112 | Path Sum | 🟢 | 根到叶递归 | ⬜ |
| 113 | Path Sum II | 🟡 | DFS+回溯路径 | ⬜ |
| 114 | Flatten Binary Tree to Linked List | 🟡 | 前序展开 | ⬜ |
| 116 | Populating Next Right Pointers | 🟡 | 层次连接(O(1)空间) | ⬜ |
| 117 | Populating Next Right Pointers II | 🟡 | 非完美树版本 | ⬜ |
| 124 | Binary Tree Maximum Path Sum | 🔴 | 后序+全局最大值 | ⬜ |
| 129 | Sum Root to Leaf Numbers | 🟡 | DFS 路径数字求和 | ⬜ |
| 144 | Binary Tree Preorder Traversal | 🟢 | 前序(栈) | ⬜ |
| 145 | Binary Tree Postorder Traversal | 🟢 | 后序(栈) | ⬜ |
| 199 | Binary Tree Right Side View | 🟡 | BFS/DFS 取每层最右 | ⬜ |

**📋 推荐刷题顺序：**

> 三序遍历 → 基本属性 → 路径问题 → 层序系列 → 构造/变换

| 顺序 | # | 题目 | 理由 |
|:----:|---|------|------|
| 1 | 144 | Binary Tree Preorder Traversal | 🟢 前序遍历，树的第一步 |
| 2 | 94 | Binary Tree Inorder Traversal | 🟢 中序遍历，栈/Morris |
| 3 | 145 | Binary Tree Postorder Traversal | 🟢 后序遍历，三序全掌握 |
| 4 | 104 | Maximum Depth | 🟢 递归求深度，最简单的递归 |
| 5 | 111 | Minimum Depth | 🟢 注意叶子节点边界，与 #104 对比 |
| 6 | 100 | Same Tree | 🟢 递归比较两棵树 |
| 7 | 101 | Symmetric Tree | 🟢 镜像递归，#100 的变体 |
| 8 | 110 | Balanced Binary Tree | 🟢 后序判高度，综合 #104 |
| 9 | 112 | Path Sum | 🟢 根到叶递归 |
| 10 | 113 | Path Sum II | 🟡 DFS+回溯路径，#112 的进阶 |
| 11 | 129 | Sum Root to Leaf Numbers | 🟡 路径数字求和，#112 类似 |
| 12 | 102 | Level Order Traversal | 🟡 BFS 层序，层序系列基础 |
| 13 | 107 | Level Order II | 🟡 BFS + 翻转，#102 变体 |
| 14 | 103 | Zigzag Level Order | 🟡 之字形BFS，#102 变体 |
| 15 | 199 | Right Side View | 🟡 BFS/DFS 取最右，层序应用 |
| 16 | 116 | Next Right Pointers | 🟡 层次连接 O(1) 空间 |
| 17 | 117 | Next Right Pointers II | 🟡 非完美树版本，#116 升级 |
| 18 | 105 | Construct from Pre+Inorder | 🟡 分治 + 哈希定位 |
| 19 | 106 | Construct from In+Postorder | 🟡 分治，与 #105 对称 |
| 20 | 114 | Flatten to Linked List | 🟡 前序展开 |
| 21 | 124 | Maximum Path Sum | 🔴 后序 + 全局最大值，树的终极题 |

### 3.2 二叉搜索树 BST（7 + 2模板 = 9 题）

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 95 | Unique Binary Search Trees II | 🟡 | 递归生成所有 BST | ⬜ |
| 96 | Unique Binary Search Trees | 🟡 | 卡特兰数 DP | ⬜ |
| 98 | Validate Binary Search Tree | 🟡 | 中序/上下界 | ⬜ |
| 99 | Recover Binary Search Tree | 🟡 | 中序找两个错位 | ⬜ |
| 108 | Convert Sorted Array to BST | 🟢 | 分治取中点 | ⬜ |
| 109 | Convert Sorted List to BST | 🟡 | 快慢指针+递归 | ⬜ |
| 173 | Binary Search Tree Iterator | 🟡 | 栈模拟中序 | ⬜ |
| **230** | **Kth Smallest in BST** 🏷️模板 | 🟡 | 中序第k个 | ⬜ |
| **235** | **LCA of BST** 🏷️模板 | 🟡 | BST 分岔点 | ⬜ |

**📋 推荐刷题顺序：**

> BST 性质（中序有序）→ 构造 → 设计 → 生成

| 顺序 | # | 题目 | 理由 |
|:----:|---|------|------|
| 1 | 108 | Convert Sorted Array to BST | 🟢 分治取中点，理解 BST 构造 |
| 2 | 98 | Validate BST | 🟡 中序/上下界，BST 核心性质 |
| 3 | **230** | **Kth Smallest in BST** 🏷️ | 🟡 中序第k个，运用 BST 有序性 |
| 4 | **235** | **LCA of BST** 🏷️ | 🟡 BST 分岔点，利用大小关系 |
| 5 | 99 | Recover BST | 🟡 中序找两个错位，#98 的进阶 |
| 6 | 173 | BST Iterator | 🟡 栈模拟中序，迭代器设计 |
| 7 | 109 | Convert Sorted List to BST | 🟡 快慢指针 + 递归，#108 链表版 |
| 8 | 96 | Unique BSTs | 🟡 卡特兰数 DP，思维跳跃 |
| 9 | 95 | Unique BSTs II | 🟡 递归生成所有 BST，#96 的输出版 |

### 3.3 图论 / BFS / DFS（5 + 4模板 = 9 题）

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 126 | Word Ladder II | 🔴 | BFS建图+DFS回溯 | ⬜ |
| 127 | Word Ladder | 🔴 | 双向 BFS | ⬜ |
| 130 | Surrounded Regions | 🟡 | 边界 DFS 标记 | ⬜ |
| 133 | Clone Graph | 🟡 | BFS/DFS+哈希 | ⬜ |
| 200 | Number of Islands | 🟡 | 网格 DFS/BFS | ⬜ |
| **207** | **Course Schedule** 🏷️模板 | 🟡 | 拓扑排序 BFS | ⬜ |
| **210** | **Course Schedule II** 🏷️模板 | 🟡 | 拓扑输出序列 | ⬜ |
| **547** | **Number of Provinces** 🏷️模板 | 🟡 | 并查集入门 | ⬜ |
| **695** | **Max Area of Island** 🏷️模板 | 🟡 | DFS 计面积 | ⬜ |

**📋 推荐刷题顺序：**

> 网格 DFS 入门 → 图遍历 → 拓扑排序 → 并查集 → Hard BFS

| 顺序 | # | 题目 | 理由 |
|:----:|---|------|------|
| 1 | 200 | Number of Islands | 🟡 网格 DFS/BFS 入门，图论第一题 |
| 2 | **695** | **Max Area of Island** 🏷️ | 🟡 DFS 计面积，#200 的自然扩展 |
| 3 | 130 | Surrounded Regions | 🟡 边界 DFS 标记，#200 变体 |
| 4 | 133 | Clone Graph | 🟡 BFS/DFS + 哈希，图的复制 |
| 5 | **207** | **Course Schedule** 🏷️ | 🟡 拓扑排序 BFS，检测环 |
| 6 | **210** | **Course Schedule II** 🏷️ | 🟡 拓扑输出序列，#207 的进阶 |
| 7 | **547** | **Number of Provinces** 🏷️ | 🟡 并查集入门，换一种图的表示 |
| 8 | 127 | Word Ladder | 🔴 双向 BFS，字符串 + 图 |
| 9 | 126 | Word Ladder II | 🔴 BFS建图 + DFS回溯，#127 终极版 |

---

## 📅 第四阶段：动态规划（第 10-13 周）

### 4.1 一维 DP（8 + 2模板 = 10 题）

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 53 | Maximum Subarray | 🟡 | Kadane 算法 | ⬜ |
| 70 | Climbing Stairs | 🟢 | 斐波那契 DP | ⬜ |
| 91 | Decode Ways | 🟡 | 分段选择 DP | ⬜ |
| 121 | Best Time to Buy and Sell Stock | 🟢 | 维护历史最低 | ⬜ |
| 139 | Word Break | 🟡 | 字符串切分 DP | ⬜ |
| 140 | Word Break II | 🔴 | DP+回溯输出 | ⬜ |
| 152 | Maximum Product Subarray | 🟡 | 同时维护最大最小 | ⬜ |
| 198 | House Robber | 🟡 | 选/不选 | ⬜ |
| **300** | **LIS** 🏷️模板 | 🟡 | DP+二分 O(nlogn) | ⬜ |
| **322** | **Coin Change** 🏷️模板 | 🟡 | 完全背包 | ⬜ |

**📋 推荐刷题顺序：**

> DP 入门 → 子数组问题 → 选择问题 → 字符串 DP → 经典模板

| 顺序 | # | 题目 | 理由 |
|:----:|---|------|------|
| 1 | 70 | Climbing Stairs | 🟢 斐波那契，最简单的 DP |
| 2 | 121 | Best Time to Buy and Sell Stock | 🟢 维护历史最低，一次遍历 |
| 3 | 53 | Maximum Subarray | 🟡 Kadane 算法，子数组 DP 入门 |
| 4 | 152 | Maximum Product Subarray | 🟡 同时维护最大最小，#53 变体 |
| 5 | 198 | House Robber | 🟡 选/不选，经典线性 DP |
| 6 | 91 | Decode Ways | 🟡 分段选择 DP，#70 的字符串版 |
| 7 | **322** | **Coin Change** 🏷️ | 🟡 **完全背包模板**，必须掌握 |
| 8 | **300** | **LIS** 🏷️ | 🟡 DP + 二分 O(nlogn)，面试高频 |
| 9 | 139 | Word Break | 🟡 字符串切分 DP，综合应用 |
| 10 | 140 | Word Break II | 🔴 DP + 回溯输出，#139 的进阶 |

### 4.2 二维 DP（14 题）

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 5 | Longest Palindromic Substring | 🟡 | 中心扩展/区间DP | ⬜ |
| 10 | Regular Expression Matching | 🔴 | 复杂字符串 DP | ⬜ |
| 44 | Wildcard Matching | 🔴 | 通配符 DP | ⬜ |
| 62 | Unique Paths | 🟡 | 网格 DP | ⬜ |
| 63 | Unique Paths II | 🟡 | 含障碍物 | ⬜ |
| 64 | Minimum Path Sum | 🟡 | 网格最优路径 | ⬜ |
| 72 | Edit Distance | 🟡 | 经典字符串 DP | ⬜ |
| 85 | Maximal Rectangle | 🔴 | 基于84题扩展 | ⬜ |
| 87 | Scramble String | 🔴 | 区间 DP/记忆化 | ⬜ |
| 97 | Interleaving String | 🟡 | 交错匹配 DP | ⬜ |
| 115 | Distinct Subsequences | 🔴 | 子序列计数 DP | ⬜ |
| 120 | Triangle | 🟡 | 自底向上 DP | ⬜ |
| 132 | Palindrome Partitioning II | 🔴 | 最小分割 DP | ⬜ |
| 174 | Dungeon Game | 🔴 | 逆向网格 DP | ⬜ |

**📋 推荐刷题顺序：**

> 网格 DP → 字符串 DP → 区间 DP → Hard 综合

| 顺序 | # | 题目 | 理由 |
|:----:|---|------|------|
| 1 | 62 | Unique Paths | 🟡 最简单的网格 DP |
| 2 | 63 | Unique Paths II | 🟡 含障碍物，#62 直接变体 |
| 3 | 64 | Minimum Path Sum | 🟡 最优路径，#62/#63 思路 |
| 4 | 120 | Triangle | 🟡 自底向上 DP，变形网格 |
| 5 | 5 | Longest Palindromic Substring | 🟡 中心扩展/区间 DP，字符串 DP 入门 |
| 6 | 72 | Edit Distance | 🟡 经典字符串 DP，面试高频 |
| 7 | 97 | Interleaving String | 🟡 交错匹配 DP |
| 8 | 115 | Distinct Subsequences | 🔴 子序列计数 DP |
| 9 | 132 | Palindrome Partitioning II | 🔴 最小分割 DP，#5 + DP |
| 10 | 174 | Dungeon Game | 🔴 逆向网格 DP，#64 的逆向思维 |
| 11 | 10 | Regular Expression Matching | 🔴 复杂字符串 DP |
| 12 | 44 | Wildcard Matching | 🔴 通配符 DP，与 #10 对比 |
| 13 | 87 | Scramble String | 🔴 区间 DP/记忆化 |
| 14 | 85 | Maximal Rectangle | 🔴 基于 #84(单调栈) 扩展 |

### 4.3 股票系列 & 背包（5 + 3模板 = 8 题）

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 122 | Best Time to Buy and Sell Stock II | 🟡 | 贪心/状态机 | ⬜ |
| 123 | Best Time to Buy and Sell Stock III | 🔴 | 至多两次交易 | ⬜ |
| 188 | Best Time to Buy and Sell Stock IV | 🔴 | 至多k次交易 | ⬜ |
| 146 | LRU Cache | 🟡 | 哈希+双向链表 | ⬜ |
| **416** | **Partition Equal Subset Sum** 🏷️模板 | 🟡 | 0-1 背包 | ⬜ |
| **494** | **Target Sum** 🏷️模板 | 🟡 | 0-1 背包变体 | ⬜ |
| **518** | **Coin Change II** 🏷️模板 | 🟡 | 完全背包计数 | ⬜ |

**📋 推荐刷题顺序：**

> 背包模板 → 股票状态机 → 设计题

| 顺序 | # | 题目 | 理由 |
|:----:|---|------|------|
| 1 | **416** | **Partition Equal Subset Sum** 🏷️ | 🟡 **0-1 背包模板**，先掌握 |
| 2 | **494** | **Target Sum** 🏷️ | 🟡 0-1 背包变体，#416 直接进阶 |
| 3 | **518** | **Coin Change II** 🏷️ | 🟡 **完全背包模板**，与 4.1 的 #322 对比 |
| 4 | 122 | Best Time to Buy and Sell Stock II | 🟡 贪心/状态机，股票系列入门 |
| 5 | 123 | Best Time to Buy and Sell Stock III | 🔴 至多两次交易，#122 进阶 |
| 6 | 188 | Best Time to Buy and Sell Stock IV | 🔴 至多k次交易，#123 泛化版 |
| 7 | 146 | LRU Cache | 🟡 哈希 + 双向链表，数据结构设计 |

---

## 📅 第五阶段：高级算法 & 综合（第 14-16 周）

### 5.1 贪心（4 题）

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 45 | Jump Game II | 🟡 | BFS 层思维 | ⬜ |
| 55 | Jump Game | 🟡 | 最远可达位置 | ⬜ |
| 134 | Gas Station | 🟡 | 净油量分析 | ⬜ |
| 135 | Candy | 🔴 | 两次遍历 | ⬜ |

**📋 推荐刷题顺序：**

| 顺序 | # | 题目 | 理由 |
|:----:|---|------|------|
| 1 | 55 | Jump Game | 🟡 最远可达位置，贪心入门 |
| 2 | 45 | Jump Game II | 🟡 BFS 层思维，#55 的进阶 |
| 3 | 134 | Gas Station | 🟡 净油量分析，全局贪心 |
| 4 | 135 | Candy | 🔴 两次遍历，贪心综合 |

### 5.2 位运算（6 题）

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 89 | Gray Code | 🟡 | 格雷码 i^(i>>1) | ⬜ |
| 136 | Single Number | 🟢 | 异或消除 | ⬜ |
| 137 | Single Number II | 🟡 | 逐位统计 mod 3 | ⬜ |
| 187 | Repeated DNA Sequences | 🟡 | 哈希/位压缩 | ⬜ |
| 190 | Reverse Bits | 🟢 | 逐位翻转 | ⬜ |
| 191 | Number of 1 Bits | 🟢 | n & (n-1) | ⬜ |

**📋 推荐刷题顺序：**

| 顺序 | # | 题目 | 理由 |
|:----:|---|------|------|
| 1 | 136 | Single Number | 🟢 异或消除，位运算最经典入门 |
| 2 | 191 | Number of 1 Bits | 🟢 n & (n-1) 技巧 |
| 3 | 190 | Reverse Bits | 🟢 逐位翻转，#191 同类 |
| 4 | 137 | Single Number II | 🟡 逐位统计 mod 3，#136 进阶 |
| 5 | 89 | Gray Code | 🟡 格雷码 i^(i>>1)，数学 + 位运算 |
| 6 | 187 | Repeated DNA Sequences | 🟡 哈希/位压缩 |

### 5.3 数学（12 题）

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| 7 | Reverse Integer | 🟡 | 溢出判断 | ⬜ |
| 9 | Palindrome Number | 🟢 | 翻转一半比较 | ⬜ |
| 12 | Integer to Roman | 🟡 | 贪心映射表 | ⬜ |
| 13 | Roman to Integer | 🟢 | 减法规则 | ⬜ |
| 29 | Divide Two Integers | 🟡 | 倍增/位移 | ⬜ |
| 50 | Pow(x, n) | 🟡 | 快速幂 | ⬜ |
| 60 | Permutation Sequence | 🔴 | 阶乘+逐位确定 | ⬜ |
| 149 | Max Points on a Line | 🔴 | 斜率哈希计数 | ⬜ |
| 166 | Fraction to Recurring Decimal | 🟡 | 长除法+哈希找循环 | ⬜ |
| 168 | Excel Sheet Column Title | 🟢 | 26进制(注意从1开始) | ⬜ |
| 171 | Excel Sheet Column Number | 🟢 | 26进制转十进制 | ⬜ |
| 172 | Factorial Trailing Zeroes | 🟡 | 统计因子5 | ⬜ |

**📋 推荐刷题顺序：**

> 简单数字 → 进制/映射 → 计算/模拟 → Hard

| 顺序 | # | 题目 | 理由 |
|:----:|---|------|------|
| 1 | 9 | Palindrome Number | 🟢 翻转一半比较 |
| 2 | 7 | Reverse Integer | 🟡 溢出判断，#9 同类 |
| 3 | 13 | Roman to Integer | 🟢 减法规则 |
| 4 | 12 | Integer to Roman | 🟡 贪心映射表，#13 的反向 |
| 5 | 171 | Excel Sheet Column Number | 🟢 26进制转十进制 |
| 6 | 168 | Excel Sheet Column Title | 🟢 26进制(从1开始)，#171 反向 |
| 7 | 172 | Factorial Trailing Zeroes | 🟡 统计因子5 |
| 8 | 50 | Pow(x, n) | 🟡 快速幂 |
| 9 | 29 | Divide Two Integers | 🟡 倍增/位移 |
| 10 | 166 | Fraction to Recurring Decimal | 🟡 长除法 + 哈希找循环 |
| 11 | 60 | Permutation Sequence | 🔴 阶乘 + 逐位确定 |
| 12 | 149 | Max Points on a Line | 🔴 斜率哈希计数 |

### 5.4 堆 & 字典树（3 + 3模板 = 6 题）

| # | 题目 | 难度 | 关键点 | 状态 |
|---|------|------|--------|------|
| **208** | **Implement Trie** 🏷️模板 | 🟡 | Trie 基础实现 | ⬜ |
| **211** | **Design Add and Search Words** 🏷️模板 | 🟡 | Trie+DFS通配 | ⬜ |
| **212** | **Word Search II** 🏷️模板 | 🔴 | Trie+回溯 | ⬜ |
| **215** | **Kth Largest Element** 🏷️模板 | 🟡 | 快速选择/堆 | ⬜ |
| **295** | **Find Median from Data Stream** 🏷️模板 | 🔴 | 对顶堆 | ⬜ |
| **347** | **Top K Frequent Elements** 🏷️模板 | 🟡 | 桶排序/堆 | ⬜ |

**📋 推荐刷题顺序：**

> 堆基础 → 堆进阶 → 字典树系列（三题递进）

| 顺序 | # | 题目 | 理由 |
|:----:|---|------|------|
| 1 | **215** | **Kth Largest Element** 🏷️ | 🟡 快速选择/堆，堆的入门 |
| 2 | **347** | **Top K Frequent Elements** 🏷️ | 🟡 桶排序/堆，#215 扩展 |
| 3 | **295** | **Find Median from Data Stream** 🏷️ | 🔴 对顶堆，堆的终极应用 |
| 4 | **208** | **Implement Trie** 🏷️ | 🟡 Trie 基础实现，字典树第一步 |
| 5 | **211** | **Add and Search Words** 🏷️ | 🟡 Trie + DFS 通配，#208 进阶 |
| 6 | **212** | **Word Search II** 🏷️ | 🔴 Trie + 回溯，#208 + #79 综合 |

---

## 📊 统计面板

| 专题 | 题数 | 已完成 | 完成率 |
|------|------|--------|--------|
| 数组 & 哈希表 | 17 | 0 | 0% |
| 字符串 | 13 | 0 | 0% |
| 链表 | 19 | 3 | 16% |
| 栈 & 队列 | 8 | 1 | 13% |
| 双指针 & 滑窗 | 11 | 1 | 9% |
| 二分查找 | 10 | 0 | 0% |
| 排序 | 5 | 0 | 0% |
| 回溯 | 15 | 1 | 7% |
| 二叉树 | 21 | 0 | 0% |
| BST | 9 | 0 | 0% |
| 图论 | 9 | 0 | 0% |
| 一维 DP | 10 | 0 | 0% |
| 二维 DP | 14 | 0 | 0% |
| 股票 & 背包 | 8 | 0 | 0% |
| 贪心 | 4 | 0 | 0% |
| 位运算 | 6 | 0 | 0% |
| 数学 | 12 | 0 | 0% |
| 堆 & 字典树 | 6 | 0 | 0% |
| **总计** | **197** | **6** | **3%** |

> 其中前200题内 **176 题**，200以外模板题 **18 题**（标 🏷️），Premium/SQL/Shell 已排除

---

## 🔑 代码模板区（完成专题后总结）

### 滑动窗口 / 二分 / 回溯 / BFS·DFS / DP
```python
# TODO: 逐专题总结
```

## 📝 复习日志

| 日期 | 复习题目 | 独立做出? | 备注 |
|------|---------|----------|------|
| | | | |
