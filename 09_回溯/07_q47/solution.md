# LeetCode 47 — 全排列 II（Permutations II）

## 题目

给定一个可包含重复数字的数组 `nums`，返回所有不重复的全排列。

返回顺序不限。

### 示例

```
输入: nums = [1, 1, 2]
输出:
[
  [1, 1, 2],
  [1, 2, 1],
  [2, 1, 1]
]
```

---

## 和 Q46 的区别

Q46 全排列：

```
nums 中没有重复数字
```

所以只需要用 `used` 数组防止同一个下标重复使用。

Q47 全排列 II：

```
nums 中可能有重复数字
```

比如：

```
nums = [1, 1, 2]
```

两个 `1` 虽然下标不同，但数值相同。如果不做去重，会生成重复排列。

所以 Q47 是：

```
Q46 的 used 数组模板 + 排序 + 同层去重
```

---

## 核心难点

Q47 最关键的一句是：

```python
if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
    continue
```

这句的意思是：

```
如果当前数字和前一个数字相同，并且前一个相同数字在当前路径里没有被使用，
说明当前数字是在同一层里作为重复候选出现，应该跳过。
```

先不要急着背，先理解为什么。

---

## 为什么要先排序？

排序后，相同数字才会挨在一起。

比如：

```
[1, 2, 1]
```

排序后：

```
[1, 1, 2]
```

这样才能通过：

```python
nums[i] == nums[i - 1]
```

判断当前数字是否和前一个数字重复。

---

## 什么叫同层去重？

以：

```
nums = [1, 1, 2]
```

为例。

第一层要决定排列的第 1 个位置，可以选：

```
第一个 1
第二个 1
2
```

如果第一层先选第一个 `1`，可以生成：

```
[1, 1, 2]
[1, 2, 1]
```

如果第一层再选第二个 `1`，也会生成同样的：

```
[1, 1, 2]
[1, 2, 1]
```

所以在同一层里，第二个 `1` 要跳过。

---

## 为什么是 `not used[i - 1]`？

判断：

```python
not used[i - 1]
```

表示：

```
前一个相同数字没有在当前路径里
```

这说明当前数字和前一个相同数字处在同一层的候选关系里。

这时要跳过当前数字，避免重复排列。

### 例子 1：同一层，应该跳过

```
nums = [1, 1, 2]
path = []
used = [False, False, False]
```

第一层循环：

```
i = 0 -> 选第一个 1
i = 1 -> 第二个 1
```

当 `i = 1` 时：

```python
nums[1] == nums[0]
used[0] == False
```

说明第一个 `1` 没在当前路径中，第二个 `1` 是同一层重复候选。

所以跳过第二个 `1`。

### 例子 2：不同层，不能跳过

```
path = [1]
used = [True, False, False]
```

现在已经选了第一个 `1`，下一层可以选第二个 `1`，这样才能得到：

```
[1, 1, 2]
```

当下一层 `i = 1` 时：

```python
nums[1] == nums[0]
used[0] == True
```

因为前一个 `1` 已经在当前路径里，说明第二个 `1` 不是同一层重复候选，而是合法的下一层选择。

所以不能跳过。

这就是为什么条件是：

```python
not used[i - 1]
```

---

## 解法一览

| 解法 | 思路 | 时间复杂度 | 空间复杂度 | 是否推荐面试 |
|---|---|---|---|---|
| 1. 暴力排列 + set 去重 | 先生成所有排列，再用 set 去重 | O(n * n!) | O(n * n!) | 只适合理解 |
| 2. 回溯 + used + 同层去重 | 排序后，用 `used` 和去重条件避免重复分支 | O(n * n!) | O(n * n!) | **面试推荐 ✅** |
| 3. 原地交换 + 每层 set 去重 | 每个位置用 set 避免放入重复数字 | O(n * n!) | O(n * n!) | 进阶写法 |

---

## 解法 1：暴力排列 + set 去重

### 思路

先按 Q46 的方式生成所有排列。

因为 `nums` 有重复数字，所以会生成重复排列。

比如：

```
nums = [1, 1, 2]
```

两个 `1` 交换位置后，排列看起来完全一样。

所以可以把每个排列转成元组放进 `set`：

```python
seen.add(tuple(path))
```

最后再转回列表。

### 代码

```python
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        seen = set()
        path = []
        used = [False] * len(nums)

        def backtrack() -> None:
            if len(path) == len(nums):
                seen.add(tuple(path))
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
        return [list(item) for item in seen]
```

### 评价

这个方法能得到正确答案，但不推荐面试。

原因是它没有避免重复搜索，而是先生成重复排列，再用 `set` 去重。重复数字越多，浪费越明显。

---

## 解法 2：回溯 + used + 同层去重 ⭐ 面试推荐

### 思路

先排序：

```python
nums.sort()
```

再沿用 Q46 的排列模板：

```python
used = [False] * len(nums)
```

区别是循环里多一条去重判断：

```python
if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
    continue
```

完整代码：

```python
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
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

                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                path.append(nums[i])
                used[i] = True
                backtrack()
                used[i] = False
                path.pop()

        backtrack()
        return ans
```

### 去重条件怎么记？

可以这样读：

```python
i > 0
```

当前数字不是第一个数字。

```python
nums[i] == nums[i - 1]
```

当前数字和前一个数字相同。

```python
not used[i - 1]
```

前一个相同数字没有被当前路径使用，说明当前数字是同一层重复候选。

所以：

```python
continue
```

跳过当前数字。

### 递归树理解

排序后：

```
nums = [1, 1, 2]
```

递归树大致是：

```
[]
├── 选第一个 1
│   ├── 选第二个 1
│   │   └── [1, 1, 2]
│   └── 选 2
│       └── [1, 2, 1]
├── 第二个 1 跳过
└── 选 2
    └── [2, 1, 1]
```

最终结果：

```
[[1, 1, 2], [1, 2, 1], [2, 1, 1]]
```

### 复杂度

最坏情况下没有重复元素，一共有：

```
n!
```

个排列。

每个排列复制一次，长度为 `n`。

时间复杂度：

```
O(n * n!)
```

空间复杂度包含返回结果：

```
O(n * n!)
```

如果不算返回结果，`path`、`used` 和递归栈是：

```
O(n)
```

### 为什么它最适合面试？

因为它是在 Q46 标准排列模板上的最小升级。

Q46：

```python
if used[i]:
    continue
```

Q47：

```python
if used[i]:
    continue

if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
    continue
```

面试时可以这样讲：

> 我先排序，让相同数字相邻。排列问题每一层都从所有数字中选，用 `used` 防止同一个下标重复使用。对于重复数字，如果前一个相同数字没有被使用，说明当前数字是在同一层重复出现的候选，跳过它，避免重复排列。

---

## 解法 3：原地交换 + 每层 set 去重

### 思路

原地交换版本也可以处理重复。

每一层确定一个位置 `first`。

这一层用一个 `seen` 集合记录：

```
这个位置已经放过哪些数字
```

如果当前数字这一层已经放过，就跳过。

### 代码

```python
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def backtrack(first: int) -> None:
            if first == len(nums):
                ans.append(nums[:])
                return

            seen = set()
            for i in range(first, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])

                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack(0)
        return ans
```

### 评价

这个写法也很好，而且不需要 `used` 数组。

但它会原地修改数组，对刚开始练回溯的人不如 `used` 数组版直观。

面试里如果你已经很熟悉交换法，可以写这个；否则更推荐解法 2。

---

## 最终推荐

面试最推荐写 **解法 2：回溯 + used + 同层去重**。

核心代码：

```python
if used[i]:
    continue

if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
    continue
```

重点记住：

```
Q46：没有重复数字，只需要 used
Q47：有重复数字，先排序，再加同层去重
```
