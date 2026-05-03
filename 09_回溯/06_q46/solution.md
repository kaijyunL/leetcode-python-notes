# LeetCode 46 — 全排列（Permutations）

## 题目

给定一个不含重复数字的数组 `nums`，返回它的所有可能排列。

返回顺序不限。

### 示例

```
输入: nums = [1, 2, 3]
输出:
[
  [1, 2, 3],
  [1, 3, 2],
  [2, 1, 3],
  [2, 3, 1],
  [3, 1, 2],
  [3, 2, 1]
]
```

---

## 和组合/子集的区别

前面几题是子集、组合：

```
[1, 2]
```

和：

```
[2, 1]
```

在组合题里是同一个结果。

但在排列题里，它们是两个不同结果。

所以排列题不能用 `start` 限制“只能往后选”。

排列题每一层都要从所有数字里选，只是不能重复使用已经在 `path` 里的数字。

这就是 Q46 的核心：

```
每一层从所有数字中选一个还没用过的数字
```

---

## 核心理解

如果：

```
nums = [1, 2, 3]
```

第一位可以选：

```
1, 2, 3
```

如果第一位选了 `1`，第二位可以选：

```
2, 3
```

如果第二位选了 `2`，第三位只能选：

```
3
```

得到：

```
[1, 2, 3]
```

然后回退，第二位改选 `3`：

```
[1, 3, 2]
```

这就是典型的回溯：

```
做选择 -> 递归 -> 撤销选择
```

---

## 解法一览

| 解法 | 思路 | 时间复杂度 | 空间复杂度 | 是否推荐面试 |
|---|---|---|---|---|
| 1. 递归复制剩余列表 | 每层选择一个数，把剩余数字传给下一层 | O(n * n!) | O(n * n!) | 适合理解 |
| 2. 回溯 + used 数组 | 每层从所有数字里选还没用过的数 | O(n * n!) | O(n * n!) | **面试最推荐 ✅** |
| 3. 原地交换回溯 | 通过交换把数字放到当前位置 | O(n * n!) | O(n * n!) | 进阶写法 |

> 一共有 `n!` 个排列，每个排列长度是 `n`，所以保存答案本身就需要 `O(n * n!)`。

---

## 解法 1：递归复制剩余列表

### 思路

用两个列表：

| 变量 | 含义 |
|---|---|
| `path` | 当前已经选好的排列前缀 |
| `remaining` | 当前还没使用的数字 |

每次从 `remaining` 中选一个数字加入 `path`，然后把剩下的数字传给下一层。

比如：

```
path = [1]
remaining = [2, 3]
```

下一层可以选 `2` 或 `3`。

### 代码

```python
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def dfs(path: list[int], remaining: list[int]) -> None:
            if not remaining:
                ans.append(path[:])
                return

            for i, num in enumerate(remaining):
                dfs(path + [num], remaining[:i] + remaining[i + 1:])

        dfs([], nums)
        return ans
```

### 评价

这个方法很好理解，但不推荐作为最终面试写法。

原因是：

```python
path + [num]
remaining[:i] + remaining[i + 1:]
```

每次递归都会创建新列表，额外拷贝比较多。

它适合作为理解排列搜索树的第一步。

---

## 解法 2：回溯 + used 数组 ⭐ 面试最推荐

### 思路

用：

```python
used = [False] * len(nums)
```

记录每个数字是否已经被当前路径使用。

每一层都从头遍历 `nums`：

```python
for i in range(len(nums)):
```

如果 `nums[i]` 已经用过，就跳过：

```python
if used[i]:
    continue
```

如果没用过，就加入 `path`：

```python
path.append(nums[i])
used[i] = True
```

递归回来后撤销：

```python
used[i] = False
path.pop()
```

### 为什么不需要 `start`？

因为排列关心顺序。

组合题用 `start` 是为了避免：

```
[1, 2]
[2, 1]
```

这种重复组合。

但排列题里：

```
[1, 2]
[2, 1]
```

本来就是两个不同排列。

所以排列题不能限制只能往后选，而是每一层都从所有数字里选，只跳过已经用过的数字。

### 代码

```python
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        path = []
        used = [False] * len(nums)

        def backtrack() -> None:
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                path.append(nums[i])
                used[i] = True
                backtrack()
                used[i] = False
                path.pop()

        backtrack()
        return ans
```

### 以 `[1, 2, 3]` 为例

递归树大致是：

```
[]
├── [1]
│   ├── [1, 2]
│   │   └── [1, 2, 3]
│   └── [1, 3]
│       └── [1, 3, 2]
├── [2]
│   ├── [2, 1]
│   │   └── [2, 1, 3]
│   └── [2, 3]
│       └── [2, 3, 1]
└── [3]
    ├── [3, 1]
    │   └── [3, 1, 2]
    └── [3, 2]
        └── [3, 2, 1]
```

最后得到 6 个排列：

```
3! = 6
```

### 复杂度

排列数量是：

```
n!
```

每个排列复制一次，长度为 `n`。

时间复杂度：

```
O(n * n!)
```

返回结果需要保存 `n!` 个排列，每个长度为 `n`。

空间复杂度：

```
O(n * n!)
```

如果不算返回结果，`path`、`used` 和递归栈都是 `O(n)`。

### 为什么它最适合面试？

因为这版最清楚地表达了排列模板：

1. 每一层都遍历所有数字
2. 用 `used` 防止同一个下标重复使用
3. `path` 长度等于 `nums` 长度时加入答案
4. 递归后撤销选择

而且这版可以自然升级到 Q47 Permutations II：

```python
if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
    continue
```

所以 Q46 最建议先把 `used` 数组版写熟。

---

## 解法 3：原地交换回溯

### 思路

还有一种写法是不使用 `used` 数组，而是通过交换，把某个数字放到当前位置。

假设当前要确定下标 `first` 的数字。

我们可以把 `first` 后面的每个数字都交换到 `first`：

```python
for i in range(first, len(nums)):
    nums[first], nums[i] = nums[i], nums[first]
    backtrack(first + 1)
    nums[first], nums[i] = nums[i], nums[first]
```

当 `first == len(nums)` 时，说明所有位置都确定好了。

### 代码

```python
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def backtrack(first: int) -> None:
            if first == len(nums):
                ans.append(nums[:])
                return

            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack(0)
        return ans
```

### 评价

这个方法的好处是不用额外的 `used` 数组。

但它会原地修改 `nums`，理解成本比 `used` 数组版高一点。

如果面试官喜欢原地交换，这个写法也很好；但对刷题学习和后续 Q47 去重排列来说，`used` 数组版更直观。

---

## 最终推荐

面试最推荐写 **解法 2：回溯 + used 数组**。

核心代码：

```python
for i in range(len(nums)):
    if used[i]:
        continue

    path.append(nums[i])
    used[i] = True
    backtrack()
    used[i] = False
    path.pop()
```

重点记住：

```
子集/组合：用 start，避免顺序重复
排列：不用 start，用 used，允许不同顺序成为不同答案
```
