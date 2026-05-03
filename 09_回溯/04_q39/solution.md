# LeetCode 39 — 组合总和（Combination Sum）

## 题目

给你一个无重复元素的整数数组 `candidates` 和一个目标整数 `target`。

找出 `candidates` 中所有可以使数字和为 `target` 的不同组合。

每个数字可以被选择无限次。

返回顺序不限。

### 示例

```
输入: candidates = [2, 3, 6, 7], target = 7
输出: [[2, 2, 3], [7]]
```

解释：

```
2 + 2 + 3 = 7
7 = 7
```

---

## 和 Q77 的关系

Q77 是：

```
从 1 到 n 中选 k 个数
每个数只能选一次
目标是长度等于 k
```

Q39 是：

```
从 candidates 中选若干个数
每个数可以重复选
目标是和等于 target
```

所以 Q39 的终止条件不再是：

```python
len(path) == k
```

而是：

```python
remain == 0
```

其中 `remain` 表示距离 `target` 还差多少。

---

## 核心规则

组合题不关心顺序。

比如：

```
[2, 2, 3]
```

和：

```
[2, 3, 2]
```

是同一个组合，不能重复出现。

所以仍然需要 `start` 控制选择范围，避免回头选前面的数。

但是 Q39 允许同一个数字重复选，所以选了 `candidates[i]` 后，下一层还能继续从 `i` 开始：

```python
backtrack(i, remain - candidates[i])
```

不是：

```python
backtrack(i + 1, remain - candidates[i])
```

这就是 Q39 和 Q77 最关键的区别。

---

## 解法一览

| 解法 | 思路 | 时间复杂度 | 空间复杂度 | 是否推荐面试 |
|---|---|---|---|---|
| 1. 暴力回溯 | 每次从所有数字里选，用排序后的元组去重 | 指数级 | 指数级 | 只适合理解 |
| 2. 标准回溯 | 用 `start` 避免顺序重复，允许重复选当前数 | 指数级 | 指数级 | 可以写 |
| 3. 排序 + 回溯 + 剪枝 | 当前数字超过 `remain` 就停止循环 | 指数级 | 指数级 | **面试推荐 ✅** |

> 组合总和类题目通常很难写成精确的简单复杂度。面试里更重要的是说明：搜索树是指数级，递归深度最多约为 `target / min(candidates)`。

---

## 解法 1：暴力回溯 + set 去重

### 思路

最暴力的想法是：

```
每一层都可以选任意 candidate
```

这样会产生顺序重复：

```
[2, 2, 3]
[2, 3, 2]
[3, 2, 2]
```

它们其实是同一个组合。

为了去重，可以在找到答案时排序后转成元组，放进 `set`：

```python
seen.add(tuple(sorted(path)))
```

这个方法能做出来，但不推荐，因为它先生成重复答案，再靠 `set` 补救。

### 代码

```python
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        seen = set()
        path = []

        def backtrack(total: int) -> None:
            if total == target:
                seen.add(tuple(sorted(path)))
                return

            if total > target:
                return

            for num in candidates:
                path.append(num)
                backtrack(total + num)
                path.pop()

        backtrack(0)
        return [list(item) for item in seen]
```

### 评价

这个方法的问题很明显：

1. 会产生大量顺序重复
2. 每次找到答案还要排序
3. 没有体现组合题的 `start` 思想

所以它只适合理解“为什么需要避免重复排列”，不适合面试。

---

## 解法 2：标准回溯

### 思路

使用 `start` 控制每一层从哪里开始选。

这样能避免：

```
[2, 3, 2]
[3, 2, 2]
```

这种顺序重复。

核心代码：

```python
for i in range(start, len(candidates)):
    num = candidates[i]
    path.append(num)
    backtrack(i, remain - num)
    path.pop()
```

注意递归传的是：

```python
backtrack(i, remain - num)
```

而不是：

```python
backtrack(i + 1, remain - num)
```

因为 Q39 允许重复使用当前数字。

比如选择了 `2` 之后，下一层还可以继续选 `2`：

```
[2]
[2, 2]
[2, 2, 2]
```

### 为什么用 `remain`？

也可以用 `total` 记录当前路径的和。

但 `remain` 更适合这题：

```python
remain = target - 当前路径总和
```

当：

```python
remain == 0
```

说明刚好凑到目标。

当：

```python
remain < 0
```

说明已经超过目标，不需要继续。

### 代码

```python
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        path = []

        def backtrack(start: int, remain: int) -> None:
            if remain == 0:
                ans.append(path[:])
                return

            if remain < 0:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                path.append(num)
                backtrack(i, remain - num)
                path.pop()

        backtrack(0, target)
        return ans
```

### 以 `[2, 3, 6, 7], target = 7` 为例

递归过程的一部分：

```
[]
├── [2]
│   ├── [2, 2]
│   │   ├── [2, 2, 2]  remain = 1
│   │   └── [2, 2, 3]  remain = 0，加入答案
│   └── [2, 3]         remain = 2
├── [3]
├── [6]
└── [7]                remain = 0，加入答案
```

答案：

```
[[2, 2, 3], [7]]
```

---

## 解法 3：排序 + 回溯 + 剪枝 ⭐ 面试推荐

### 思路

在标准回溯的基础上，先排序：

```python
candidates.sort()
```

这样当当前数字已经大于 `remain` 时，后面的数字也一定更大，不可能凑出答案，可以直接停止循环：

```python
if num > remain:
    break
```

这比标准回溯里的：

```python
if remain < 0:
    return
```

更早剪掉无效分支。

### 代码

```python
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        ans = []
        path = []

        def backtrack(start: int, remain: int) -> None:
            if remain == 0:
                ans.append(path[:])
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                if num > remain:
                    break

                path.append(num)
                backtrack(i, remain - num)
                path.pop()

        backtrack(0, target)
        return ans
```

### 为什么 `break` 可以，不是 `continue`？

因为数组已经排序。

如果当前：

```python
num > remain
```

那么后面的数字只会更大：

```python
candidates[i + 1] >= num
```

所以后面也不可能选，直接 `break` 停止当前循环。

如果没有排序，就不能用 `break`。

### 为什么递归还是传 `i`？

因为当前数字可以重复使用。

例如：

```python
candidates = [2, 3, 6, 7]
target = 7
```

选择 `2` 后，下一层仍然可以继续选择 `2`：

```python
path = [2]
backtrack(i, 5)
```

这样才能得到：

```python
[2, 2, 3]
```

如果写成：

```python
backtrack(i + 1, remain - num)
```

就表示当前数字不能再用了，那就变成 Q40 的规则，不是 Q39。

### 复杂度

搜索树是指数级。

递归最大深度约为：

```
target / min(candidates)
```

如果不算返回结果，递归栈和 `path` 的额外空间也是：

```
O(target / min(candidates))
```

返回结果需要存储所有合法组合，设答案数量为 `A`，平均组合长度为 `L`，则结果空间是：

```
O(A * L)
```

面试里可以简单说：

```
时间复杂度是指数级，空间复杂度主要由递归深度和答案数量决定
```

### 为什么它最适合面试？

因为它直接体现了组合总和题的三个关键点：

1. `start` 控制顺序，避免 `[2,3,2]` 这种重复排列
2. 递归传 `i`，表示当前数字可以重复使用
3. 排序后用 `num > remain` 剪枝

面试时可以这样讲：

> 我先排序。回溯时用 `path` 表示当前组合，用 `remain` 表示还差多少到 target。每次从 `start` 开始枚举，保证组合不重复。因为同一个数字可以重复使用，所以递归时传 `i`。如果当前数字已经大于 `remain`，后面数字更大，直接 break。

---

## 最终推荐

面试最推荐写 **解法 3：排序 + 回溯 + 剪枝**。

核心代码是：

```python
for i in range(start, len(candidates)):
    num = candidates[i]
    if num > remain:
        break

    path.append(num)
    backtrack(i, remain - num)
    path.pop()
```

重点记住：

```
Q39 可重复选，所以递归传 i
Q40 不可重复选，所以递归传 i + 1
```
