# LeetCode 40 — 组合总和 II（Combination Sum II）

## 题目

给你一个整数数组 `candidates` 和一个目标整数 `target`。

找出 `candidates` 中所有可以使数字和为 `target` 的组合。

每个数字在每个组合中只能使用一次。

结果中不能包含重复组合，返回顺序不限。

### 示例

```
输入: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
输出: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
```

---

## 和 Q39 的区别

Q39 Combination Sum：

```
candidates 没有重复元素
每个数字可以重复使用
```

所以 Q39 选了 `candidates[i]` 后，下一层还可以继续从 `i` 开始：

```python
backtrack(i, remain - num)
```

Q40 Combination Sum II：

```
candidates 可能有重复元素
每个下标的数字只能使用一次
```

所以 Q40 选了 `candidates[i]` 后，下一层必须从 `i + 1` 开始：

```python
backtrack(i + 1, remain - num)
```

同时，因为 `candidates` 可能有重复数字，还要去重。

---

## 核心规则

Q40 有两个关键点：

### 1. 每个数字只能用一次

如果当前选择了下标 `i` 的数字，下一层只能从后面继续选：

```python
backtrack(i + 1, remain - num)
```

这表示当前下标不会再被使用。

### 2. 同一层跳过重复数字

先排序：

```python
candidates.sort()
```

排序后，相同数字会挨在一起。

然后在同一层循环里跳过重复数字：

```python
if i > start and candidates[i] == candidates[i - 1]:
    continue
```

这句的含义是：

```
如果当前数字和同一层前一个数字相同，就跳过当前数字
```

这样可以避免重复组合。

---

## 解法一览

| 解法 | 思路 | 时间复杂度 | 空间复杂度 | 是否推荐面试 |
|---|---|---|---|---|
| 1. 暴力回溯 + set 去重 | 枚举选/不选，找到答案后排序去重 | 指数级 | 指数级 | 只适合理解 |
| 2. 回溯 + 同层去重 | 排序，用 `start` 和 `i > start` 去重 | 指数级 | 指数级 | 可以写 |
| 3. 排序 + 回溯 + 去重 + 剪枝 | 在方法 2 基础上，用 `num > remain` 剪枝 | 指数级 | 指数级 | **面试推荐 ✅** |

---

## 解法 1：暴力回溯 + set 去重

### 思路

最直接的方式是：

1. 每个下标的数字都可以选或不选
2. 当路径和等于 `target`，把当前路径排序后放进 `set`
3. 最后把 `set` 转回列表

为什么要排序后再放进 `set`？

因为可能出现相同组合：

```
candidates = [1, 1, 6]
target = 7
```

选择第一个 `1` 和 `6` 得到：

```
[1, 6]
```

选择第二个 `1` 和 `6` 也得到：

```
[1, 6]
```

它们应该只保留一个。

### 代码

```python
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        seen = set()
        path = []

        def backtrack(index: int, total: int) -> None:
            if total == target:
                seen.add(tuple(sorted(path)))
                return

            if index == len(candidates) or total > target:
                return

            path.append(candidates[index])
            backtrack(index + 1, total + candidates[index])
            path.pop()

            backtrack(index + 1, total)

        backtrack(0, 0)
        return [list(item) for item in seen]
```

### 评价

这个方法可以帮助理解“每个下标只能用一次”。

但它不适合面试：

1. 会生成重复组合
2. 依赖 `set` 事后去重
3. 没有体现回溯题常用的同层去重写法

---

## 解法 2：回溯 + 同层去重

### 思路

先排序：

```python
candidates.sort()
```

然后用 `start` 控制下一层从哪里开始选。

每层循环：

```python
for i in range(start, len(candidates)):
```

如果当前数字和同一层前一个数字相同，就跳过：

```python
if i > start and candidates[i] == candidates[i - 1]:
    continue
```

选择当前数字后，下一层从 `i + 1` 开始：

```python
backtrack(i + 1, remain - num)
```

因为 Q40 每个数字只能使用一次。

### 代码

```python
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        ans = []
        path = []

        def backtrack(start: int, remain: int) -> None:
            if remain == 0:
                ans.append(path[:])
                return

            if remain < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                num = candidates[i]
                path.append(num)
                backtrack(i + 1, remain - num)
                path.pop()

        backtrack(0, target)
        return ans
```

### 什么叫同层去重？

看这个例子：

```
candidates = [1, 1, 2, 5]
target = 6
```

排序后还是：

```
[1, 1, 2, 5]
```

第一层可以选择：

```
第一个 1
第二个 1
2
5
```

第一层选第一个 `1` 后，后面可以生成：

```
[1, 5]
```

如果第一层再选第二个 `1`，也会生成：

```
[1, 5]
```

这就是重复。

所以在同一层里，第二个 `1` 要跳过。

对应代码：

```python
if i > start and candidates[i] == candidates[i - 1]:
    continue
```

这里的 `i > start` 表示：

```
当前数字不是这一层的第一个候选
```

只有同一层才跳过重复。

### 为什么不能直接写 `candidates[i] == candidates[i - 1]`？

因为不同层的重复数字是可以使用的。

比如：

```
candidates = [1, 1, 6]
target = 8
```

答案里可以有：

```
[1, 1, 6]
```

当第一层选了第一个 `1` 后，第二层是可以选第二个 `1` 的。

所以不能看到重复数字就无脑跳过。

正确规则是：

```
同一层重复，跳过
不同层重复，可以选
```

---

## 解法 3：排序 + 回溯 + 去重 + 剪枝 ⭐ 面试推荐

### 思路

在解法 2 的基础上加剪枝。

因为数组已经排序，如果当前数字已经大于 `remain`：

```python
if num > remain:
    break
```

那么后面的数字也一定更大，不可能凑出答案，可以直接停止当前循环。

### 代码

```python
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        ans = []
        path = []

        def backtrack(start: int, remain: int) -> None:
            if remain == 0:
                ans.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                num = candidates[i]
                if num > remain:
                    break

                path.append(num)
                backtrack(i + 1, remain - num)
                path.pop()

        backtrack(0, target)
        return ans
```

### 为什么先去重，再判断 `num > remain`？

这两句顺序写成下面这样最自然：

```python
if i > start and candidates[i] == candidates[i - 1]:
    continue

num = candidates[i]
if num > remain:
    break
```

先处理同层重复候选，再看当前数字是否超过 `remain`。

实际这题里因为排序后重复数字相等，先判断 `num > remain` 通常也能工作。但按逻辑分层来说，先去重再剪枝更清楚。

### 为什么这里递归传 `i + 1`？

因为 Q40 每个数字只能使用一次。

选择了下标 `i` 的数字后，下一层必须从后面的下标开始：

```python
backtrack(i + 1, remain - num)
```

这和 Q39 正好相反：

```python
# Q39：当前数字可以重复用
backtrack(i, remain - num)

# Q40：当前数字只能用一次
backtrack(i + 1, remain - num)
```

### 复杂度

搜索树仍然是指数级。

最坏情况下，每个数字都有选或不选两种可能，所以时间复杂度可以粗略写：

```
O(2^n * n)
```

其中复制答案时，每个组合最多长度为 `n`。

空间复杂度主要由返回结果决定。设答案数量为 `A`，平均组合长度为 `L`：

```
O(A * L)
```

如果不算返回结果，递归栈和 `path` 最多是：

```
O(n)
```

### 为什么它最适合面试？

因为它覆盖了 Q40 的三个核心点：

1. 排序，让重复数字相邻，也支持 `num > remain` 剪枝
2. `i > start` 跳过同一层重复数字
3. 递归传 `i + 1`，保证每个下标只能用一次

面试时可以这样讲：

> 我先排序。回溯时用 `path` 表示当前组合，用 `remain` 表示还差多少。每一层从 `start` 开始枚举，保证不会回头选前面的数。同一层如果遇到相同数字，跳过，避免重复组合。因为每个数字只能使用一次，所以递归时传 `i + 1`。如果当前数字大于 `remain`，后面数字更大，直接 break。

---

## 最终推荐

面试最推荐写 **解法 3：排序 + 回溯 + 同层去重 + 剪枝**。

核心代码：

```python
for i in range(start, len(candidates)):
    if i > start and candidates[i] == candidates[i - 1]:
        continue

    num = candidates[i]
    if num > remain:
        break

    path.append(num)
    backtrack(i + 1, remain - num)
    path.pop()
```

重点记住：

```
Q39 可重复选：递归传 i
Q40 不可重复选：递归传 i + 1
Q40 有重复数字：同层重复要跳过
```
