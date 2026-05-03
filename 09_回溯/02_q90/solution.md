# LeetCode 90 — 子集 II（Subsets II）

## 题目

给你一个整数数组 `nums`，其中可能包含重复元素。请返回该数组所有可能的子集。

要求结果中不能包含重复子集，返回顺序不限。

### 示例

```
输入: nums = [1, 2, 2]
输出: [[], [1], [1,2], [1,2,2], [2], [2,2]]
```

---

## 和 Q78 的区别

Q78 的数组元素互不相同：

```
[1, 2, 3]
```

所以直接枚举所有子集即可。

Q90 的数组可能有重复元素：

```
[1, 2, 2]
```

如果还用 Q78 的普通回溯，会出现重复答案：

```
第一个 2 组成 [2]
第二个 2 也组成 [2]
```

但结果里只能保留一个 `[2]`。

所以 Q90 的核心是：

```
先排序，再在同一层跳过重复数字
```

排序后，相同数字会挨在一起：

```
[1, 2, 2]
```

这样才能判断：

```python
if i > start and nums[i] == nums[i - 1]:
    continue
```

这句的含义是：

```
在同一层递归里，如果当前数字和前一个数字相同，就跳过当前数字
```

---

## 解法一览

| 解法 | 思路 | 时间复杂度 | 空间复杂度 | 是否推荐面试 |
|---|---|---|---|---|
| 1. 暴力枚举 + set 去重 | 先生成所有子集，再用 set 去重 | O(n * 2^n) | O(n * 2^n) | 只适合理解 |
| 2. 迭代扩展 + 去重范围 | 重复数字只扩展上一轮新增子集 | O(n * 2^n) | O(n * 2^n) | 可以掌握 |
| 3. 回溯 + 同层去重 | 排序后，在同一层跳过重复数字 | O(n * 2^n) | O(n * 2^n) | **面试推荐 ✅** |

> 返回所有子集本身就需要指数级空间，所以这题的重点不是把复杂度降到多项式，而是正确处理重复元素。

---

## 解法 1：暴力枚举 + set 去重

### 思路

最直接的想法是：

1. 按 Q78 的方式枚举所有子集
2. 把每个子集转成元组，放进 `set` 去重
3. 最后再转回列表

因为列表不能直接放进 `set`，所以要先转成元组：

```python
tuple(subset)
```

为了让重复子集长得一样，需要先排序：

```python
nums.sort()
```

比如：

```
nums = [1, 2, 2]
```

普通枚举可能得到：

```
[]
[1]
[2]
[1, 2]
[2]
[1, 2]
[2, 2]
[1, 2, 2]
```

用 `set` 后，重复的 `[2]`、`[1, 2]` 会被去掉。

### 代码

```python
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        seen = set()
        n = len(nums)

        for mask in range(1 << n):
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            seen.add(tuple(subset))

        return [list(subset) for subset in seen]
```

### 复杂度

总共有 `2^n` 个选择状态，每个状态最多构造长度为 `n` 的子集。

时间复杂度：

```
O(n * 2^n)
```

空间复杂度：

```
O(n * 2^n)
```

### 评价

这个方法容易理解，但不推荐面试写。

原因是它没有从生成过程避免重复，而是先产生重复，再用 `set` 补救。面试官一般更希望看到你能在回溯过程中主动去重。

---

## 解法 2：迭代扩展 + 去重范围

### 思路

Q78 的迭代扩展是：

```
每来一个数字，就把它加到所有已有子集后面
```

但 Q90 有重复数字。如果当前数字和前一个数字相同，就不能再扩展所有旧子集，否则会重复。

关键规则：

```
如果当前数字是第一次出现，扩展所有已有子集
如果当前数字和前一个数字相同，只扩展上一轮新增的子集
```

以 `nums = [1, 2, 2]` 为例：

初始：

```
ans = [[]]
```

处理 `1`，它第一次出现，扩展所有已有子集：

```
新增: [1]
ans = [[], [1]]
```

处理第一个 `2`，它第一次出现，扩展所有已有子集：

```
新增: [2], [1, 2]
ans = [[], [1], [2], [1, 2]]
```

处理第二个 `2`，它和前一个数字相同，只扩展上一轮新增的部分：

```
上一轮新增: [2], [1, 2]
新增: [2, 2], [1, 2, 2]
ans = [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
```

这样就不会重复生成 `[2]` 和 `[1, 2]`。

### 代码

```python
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = [[]]
        start = 0

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                extend_from = start
            else:
                extend_from = 0

            start = len(ans)

            for j in range(extend_from, start):
                ans.append(ans[j] + [num])

        return ans
```

### 复杂度

时间复杂度：

```
O(n * 2^n)
```

空间复杂度：

```
O(n * 2^n)
```

### 评价

这个方法写起来也不难，适合补充理解。

但它的变量 `start` 和 `extend_from` 需要解释清楚，否则不如回溯法直观。

---

## 解法 3：回溯 + 同层去重 ⭐ 面试推荐

### 思路

这是 Q78 回溯模板的升级版。

Q78 的核心代码是：

```python
for i in range(start, len(nums)):
    path.append(nums[i])
    backtrack(i + 1)
    path.pop()
```

Q90 只需要在这个循环里加一条去重判断：

```python
if i > start and nums[i] == nums[i - 1]:
    continue
```

完整含义：

```python
def backtrack(start):
    ans.append(path[:])

    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]:
            continue

        path.append(nums[i])
        backtrack(i + 1)
        path.pop()
```

### 为什么必须先排序？

因为只有排序后，相同元素才会挨在一起。

比如：

```
[2, 1, 2]
```

如果不排序，两个 `2` 不挨着，就没法用：

```python
nums[i] == nums[i - 1]
```

判断重复。

排序后：

```
[1, 2, 2]
```

重复元素相邻，就能在同一层跳过。

### 什么叫“同一层去重”？

以 `nums = [1, 2, 2]` 为例。

第一层从下标 `0` 开始，可以选择：

```
1
2
2
```

这两个 `2` 在同一层。如果第一层已经用第一个 `2` 开头生成过所有子集，那么第一层再用第二个 `2` 开头就会重复，所以要跳过。

也就是：

```python
if i > start and nums[i] == nums[i - 1]:
    continue
```

这里的 `i > start` 非常关键。

它表示：

```
当前不是这一层的第一个选择
```

只有在同一层里，才跳过重复数字。

### 为什么不是所有重复数字都跳过？

因为 `[2, 2]` 是合法子集。

如果看见第二个 `2` 就无脑跳过，那 `[2, 2]` 就生成不了了。

正确逻辑是：

```
同一层的重复选择要跳过
不同层的重复选择可以保留
```

例如：

```
path = [2]
```

进入下一层后，第二个 `2` 是可以继续选的，这样才能得到：

```
[2, 2]
```

所以判断条件必须是：

```python
if i > start and nums[i] == nums[i - 1]:
    continue
```

而不是：

```python
if nums[i] == nums[i - 1]:
    continue
```

### 递归树理解

排序后：

```
nums = [1, 2, 2]
```

递归树大致是：

```
[]
├── [1]
│   ├── [1, 2]
│   │   └── [1, 2, 2]
│   └── 第二个 2 跳过
├── [2]
│   └── [2, 2]
└── 第二个 2 跳过
```

最终结果：

```
[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
```

### 代码

```python
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        path = []

        def backtrack(start: int) -> None:
            ans.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return ans
```

### 复杂度

排序需要：

```
O(n log n)
```

回溯最多生成 `2^n` 个子集，每次加入答案时复制 `path`，最多 `O(n)`。

总时间复杂度：

```
O(n log n + n * 2^n)
```

通常写作：

```
O(n * 2^n)
```

空间复杂度：

```
O(n * 2^n)
```

如果不算返回结果，递归栈和 `path` 是：

```
O(n)
```

### 为什么它最适合面试？

因为这题是回溯去重的第一道核心题。

面试官想看的不是你用 `set` 把重复答案删掉，而是你能不能在搜索过程中避免重复分支。

你可以这样讲：

1. 先排序，让相同数字相邻
2. `path` 表示当前子集，`start` 表示下一轮从哪里开始选
3. 每次进入递归，当前 `path` 都是一个合法子集，加入答案
4. 在同一层循环里，如果当前数字和前一个数字相同，跳过
5. 选择当前数字，递归到下一层，回来后撤销选择

核心代码就是：

```python
if i > start and nums[i] == nums[i - 1]:
    continue
```

这句要解释清楚：

```
i > start：说明当前数字不是这一层的第一个候选
nums[i] == nums[i - 1]：说明它和同层前一个候选重复
continue：跳过，避免生成重复子集
```

---

## 最终推荐

面试最推荐写 **解法 3：回溯 + 同层去重**。

它是在 Q78 回溯模板上的自然升级：

```python
nums.sort()

if i > start and nums[i] == nums[i - 1]:
    continue
```

这套去重逻辑后面会反复出现，比如：

- Q40 Combination Sum II
- Q47 Permutations II
- 其他需要“排序 + 跳过重复分支”的回溯题
