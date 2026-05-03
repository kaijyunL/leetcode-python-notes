# LeetCode 77 — 组合（Combinations）

## 题目

给定两个整数 `n` 和 `k`，返回范围 `[1, n]` 中所有可能的 `k` 个数的组合。

返回顺序不限。

### 示例

```
输入: n = 4, k = 2
输出:
[
  [1, 2],
  [1, 3],
  [1, 4],
  [2, 3],
  [2, 4],
  [3, 4]
]
```

---

## 和 Q78 的关系

Q78 子集是：

```
给 nums，返回所有长度的子集
```

比如：

```
nums = [1, 2, 3]
```

要返回：

```
长度 0: []
长度 1: [1], [2], [3]
长度 2: [1,2], [1,3], [2,3]
长度 3: [1,2,3]
```

Q77 组合是：

```
只返回长度为 k 的子集
```

比如：

```
n = 4, k = 2
```

只要长度为 2 的组合：

```
[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]
```

所以 Q77 可以理解为：

```
在 [1, 2, ..., n] 里，只找长度为 k 的子集
```

---

## 核心规则

组合不关心顺序。

也就是说：

```
[1, 2]
```

和：

```
[2, 1]
```

是同一个组合，只能出现一次。

所以回溯时，每次选完一个数，下一层只能从它后面的数字继续选。

这就是 `start` 的作用：

```python
backtrack(i + 1)
```

---

## 解法一览

| 解法 | 思路 | 时间复杂度 | 空间复杂度 | 是否推荐面试 |
|---|---|---|---|---|
| 1. 暴力枚举 | 枚举所有子集，只保留长度为 k 的 | O(n * 2^n) | O(k * C(n,k)) | 只适合理解 |
| 2. 普通回溯 | 只构造长度为 k 的路径 | O(k * C(n,k)) | O(k * C(n,k)) | 可以写 |
| 3. 回溯 + 剪枝 | 提前停止不可能凑够 k 个数的分支 | O(k * C(n,k)) | O(k * C(n,k)) | **面试推荐 ✅** |

> `C(n,k)` 表示从 `n` 个数中选 `k` 个数的组合数量。因为必须返回所有组合，所以结果本身就有 `C(n,k)` 个。

---

## 解法 1：暴力枚举

### 思路

把 `[1, 2, ..., n]` 的所有子集都枚举出来，然后只保留长度为 `k` 的子集。

比如：

```
n = 4, k = 2
```

所有子集有：

```
[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3], ...
```

只保留长度为 2 的：

```
[1,2], [1,3], [2,3], [1,4], [2,4], [3,4]
```

这可以用位掩码实现。

每个二进制位表示一个数字选不选：

```
0000 -> []
0011 -> [1, 2]
0101 -> [1, 3]
1111 -> [1, 2, 3, 4]
```

### 代码

```python
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []

        for mask in range(1 << n):
            path = []
            for i in range(n):
                if mask & (1 << i):
                    path.append(i + 1)

            if len(path) == k:
                ans.append(path)

        return ans
```

### 复杂度

一共有 `2^n` 个子集状态，每个状态都要检查 `n` 个位置。

时间复杂度：

```
O(n * 2^n)
```

返回结果有 `C(n,k)` 个，每个长度为 `k`。

空间复杂度：

```
O(k * C(n,k))
```

如果算临时路径，额外还有 `O(k)`。

### 评价

这个方法能帮助理解“组合是固定长度的子集”，但面试不推荐。

原因是它枚举了大量没用的子集，比如 `k = 2` 时，长度为 0、1、3、4 的子集都被白白生成了。

---

## 解法 2：普通回溯

### 思路

直接只构造长度为 `k` 的组合。

回溯变量：

| 变量 | 含义 |
|---|---|
| `ans` | 存放所有组合 |
| `path` | 当前正在构造的组合 |
| `start` | 当前这一层可以从哪个数字开始选 |

当 `path` 长度等于 `k` 时，说明已经得到一个合法组合：

```python
if len(path) == k:
    ans.append(path[:])
    return
```

循环从 `start` 到 `n`：

```python
for num in range(start, n + 1):
```

选择当前数字：

```python
path.append(num)
```

下一层只能从 `num + 1` 开始：

```python
backtrack(num + 1)
```

撤销选择：

```python
path.pop()
```

### 代码

```python
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []
        path = []

        def backtrack(start: int) -> None:
            if len(path) == k:
                ans.append(path[:])
                return

            for num in range(start, n + 1):
                path.append(num)
                backtrack(num + 1)
                path.pop()

        backtrack(1)
        return ans
```

### 以 `n = 4, k = 2` 为例

递归树大致是：

```
[]
├── [1]
│   ├── [1, 2]
│   ├── [1, 3]
│   └── [1, 4]
├── [2]
│   ├── [2, 3]
│   └── [2, 4]
├── [3]
│   └── [3, 4]
└── [4]
```

最后 `[4]` 这一支没有办法再凑够 2 个数，所以不会产生答案。

这也引出了解法 3 的剪枝。

---

## 解法 3：回溯 + 剪枝 ⭐ 面试推荐

### 思路

普通回溯已经能正确做出来，但它会进入一些明显不可能成功的分支。

比如：

```
n = 4, k = 2
```

第一层如果选择 `4`：

```
path = [4]
```

后面已经没有数字了，不可能凑出长度为 2 的组合。

所以第一层根本不需要让 `num` 取到 `4`。

### 剪枝条件怎么推？

假设当前已经选了：

```python
len(path)
```

个数字。

还需要：

```python
remaining = k - len(path)
```

个数字。

如果当前循环选择 `num`，那么可选范围是：

```
num, num + 1, ..., n
```

一共有：

```
n - num + 1
```

个数字。

为了能凑够 `remaining` 个数字，必须满足：

```
n - num + 1 >= remaining
```

移项：

```
num <= n - remaining + 1
```

所以循环最大只需要到：

```python
n - remaining + 1
```

Python 的 `range` 右边界不包含，所以写成：

```python
range(start, n - remaining + 2)
```

这就是剪枝版里最重要的一句。

### 例子

```
n = 4, k = 2
path = []
remaining = 2
```

第一层最多从哪里开始选？

```
num <= n - remaining + 1
num <= 4 - 2 + 1
num <= 3
```

所以第一层只需要尝试：

```
1, 2, 3
```

不需要尝试 `4`，因为 `[4]` 后面没有数字能凑成长度 2。

如果已经选了 `[1]`：

```
path = [1]
remaining = 1
```

此时：

```
num <= 4 - 1 + 1 = 4
```

下一层可以尝试：

```
2, 3, 4
```

这就是正确的。

### 代码

```python
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []
        path = []

        def backtrack(start: int) -> None:
            if len(path) == k:
                ans.append(path[:])
                return

            remaining = k - len(path)
            for num in range(start, n - remaining + 2):
                path.append(num)
                backtrack(num + 1)
                path.pop()

        backtrack(1)
        return ans
```

### 复杂度

一共有 `C(n,k)` 个答案，每个答案复制一次，长度是 `k`。

时间复杂度通常写：

```
O(k * C(n,k))
```

空间复杂度包含返回结果：

```
O(k * C(n,k))
```

如果不算返回结果，递归栈和 `path` 最多长度为 `k`：

```
O(k)
```

### 为什么它最适合面试？

因为它体现了组合题最核心的回溯模板：

```python
path.append(num)
backtrack(num + 1)
path.pop()
```

同时也体现了剪枝意识：

```python
remaining = k - len(path)
for num in range(start, n - remaining + 2):
```

面试时可以这样讲：

1. 组合不关心顺序，所以选了 `num` 后，下一层从 `num + 1` 开始
2. `path` 表示当前组合
3. 当 `len(path) == k` 时，加入答案
4. 如果剩余数字数量不够凑满 `k`，这条分支不用搜索
5. 所以循环右边界可以剪到 `n - remaining + 1`

这就是 Q77 最标准、最推荐的写法。

---

## 最终推荐

面试最推荐写 **解法 3：回溯 + 剪枝**。

它是在 Q78 子集模板上的变化：

```python
if len(path) == k:
    ans.append(path[:])
    return
```

并且比普通回溯多了一个非常实用的剪枝：

```python
remaining = k - len(path)
for num in range(start, n - remaining + 2):
```

掌握这题后，后面的组合总和类题目会顺很多。
