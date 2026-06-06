# LeetCode 238. 除自身以外数组的乘积（Product of Array Except Self）解析

## 题目描述

给定一个整数数组 `nums`，返回一个数组 `answer`，其中：

```text
answer[i] = nums 中除了 nums[i] 之外，其余所有元素的乘积
```

例如：

```text
nums = [1, 2, 3, 4]
```

结果是：

```text
[24, 12, 8, 6]
```

因为：

- `answer[0] = 2 * 3 * 4 = 24`
- `answer[1] = 1 * 3 * 4 = 12`
- `answer[2] = 1 * 2 * 4 = 8`
- `answer[3] = 1 * 2 * 3 = 6`

题目还有一个关键限制：

```text
不能使用除法
```

并且要求时间复杂度尽量做到：

```text
O(n)
```

---

## 先理解这题最关键的一句话

对于位置 `i` 来说，除了自己以外的乘积，其实可以拆成两部分：

```text
左边所有数的乘积 × 右边所有数的乘积
```

也就是：

```text
answer[i] = left_product[i] * right_product[i]
```

这就是这题真正的核心。

不是去想：

```text
怎么把整个数组乘起来再除掉自己
```

而是去想：

```text
每个位置的答案，都等于“左积 × 右积”
```

一旦这句话想明白，这题就顺了。

---

## 方法一：暴力枚举每个位置

### 思路

最直接的想法是：

```text
对于每个 i，我都重新遍历一遍数组，把除了 nums[i] 以外的数都乘起来
```

比如 `i = 2`，那就把：

```text
nums[0] * nums[1] * nums[3] * nums[4] ...
```

都乘一遍。

---

### 代码

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        for i in range(n):
            product = 1
            for j in range(n):
                if i != j:
                    product *= nums[j]
            answer[i] = product

        return answer
```

---

### 为什么可行

因为它完全按照题意来做。

对每个位置 `i`，都老老实实把“除自己以外的元素”乘起来，所以结果一定正确。

---

### 为什么会慢

问题在于：

- 外层要枚举每个位置 `i`
- 内层又要重新扫一遍整个数组

所以总操作次数是：

```text
O(n^2)
```

数组一长就会慢。

---

### 复杂度

- 时间复杂度：`O(n^2)`
- 空间复杂度：`O(1)`（不算返回数组）

---

## 方法二：前缀积数组 + 后缀积数组

### 核心思路

既然答案等于：

```text
左边乘积 × 右边乘积
```

那我们就干脆提前把这两部分都算出来。

定义：

- `prefix[i]`：`nums[i]` 左边所有元素的乘积
- `suffix[i]`：`nums[i]` 右边所有元素的乘积

那么：

```text
answer[i] = prefix[i] * suffix[i]
```

---

### `prefix` 和 `suffix` 分别表示什么

假设：

```text
nums = [1, 2, 3, 4]
```

那么：

### `prefix`

`prefix[i]` 表示 `i` 左边所有数的乘积。

所以：

- `prefix[0] = 1`，因为左边没有数
- `prefix[1] = 1`
- `prefix[2] = 1 * 2 = 2`
- `prefix[3] = 1 * 2 * 3 = 6`

得到：

```text
prefix = [1, 1, 2, 6]
```

### `suffix`

`suffix[i]` 表示 `i` 右边所有数的乘积。

所以：

- `suffix[3] = 1`，因为右边没有数
- `suffix[2] = 4`
- `suffix[1] = 3 * 4 = 12`
- `suffix[0] = 2 * 3 * 4 = 24`

得到：

```text
suffix = [24, 12, 4, 1]
```

于是：

- `answer[0] = 1 * 24 = 24`
- `answer[1] = 1 * 12 = 12`
- `answer[2] = 2 * 4 = 8`
- `answer[3] = 6 * 1 = 6`

最终得到：

```text
[24, 12, 8, 6]
```

---

### 面试代码

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        answer = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            answer[i] = prefix[i] * suffix[i]

        return answer
```

---

### 为什么可行

因为：

- `prefix[i]` 已经把左边乘积准备好了
- `suffix[i]` 已经把右边乘积准备好了

而题目要求的正好就是这两部分相乘。

所以对每个 `i`：

```text
answer[i] = prefix[i] * suffix[i]
```

一定成立。

---

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

这里的空间复杂度主要来自 `prefix` 和 `suffix` 两个辅助数组。

---

## 方法三：把前缀积直接写进答案数组，再用一个变量维护后缀积（面试主推）

### 核心思路

方法二已经很不错了，但还可以继续优化。

关键观察是：

```text
我们其实不一定要把 suffix 整个数组都存下来
```

因为我们从右往左扫的时候，可以用一个变量 `right_product` 动态维护：

```text
当前位置右边所有元素的乘积
```

这样就能做到：

1. 第一遍从左往右，把每个位置的前缀积直接写进 `answer`
2. 第二遍从右往左，用 `right_product` 把右边乘积补进去

---

### 这段代码到底在干什么

假设：

```text
nums = [1, 2, 3, 4]
```

### 第一步：先把前缀积写进 `answer`

开始时：

```text
answer = [1, 1, 1, 1]
```

然后从左往右：

- `i = 1` 时，`answer[1] = answer[0] * nums[0] = 1 * 1 = 1`
- `i = 2` 时，`answer[2] = answer[1] * nums[1] = 1 * 2 = 2`
- `i = 3` 时，`answer[3] = answer[2] * nums[2] = 2 * 3 = 6`

这时：

```text
answer = [1, 1, 2, 6]
```

也就是：

```text
answer[i] 里先放好了左边乘积
```

### 第二步：从右往左补上右边乘积

先设：

```text
right_product = 1
```

因为最右边那个位置右边没有数，所以右乘积一开始是 `1`。

然后从右往左：

#### `i = 3`

- 当前 `answer[3] = 6`
- `answer[3] *= right_product = 6 * 1 = 6`
- 然后更新 `right_product *= nums[3] = 1 * 4 = 4`

现在：

```text
answer = [1, 1, 2, 6]
right_product = 4
```

#### `i = 2`

- 当前 `answer[2] = 2`
- `answer[2] *= right_product = 2 * 4 = 8`
- 然后更新 `right_product *= nums[2] = 4 * 3 = 12`

现在：

```text
answer = [1, 1, 8, 6]
right_product = 12
```

#### `i = 1`

- 当前 `answer[1] = 1`
- `answer[1] *= right_product = 1 * 12 = 12`
- 然后更新 `right_product *= nums[1] = 12 * 2 = 24`

现在：

```text
answer = [1, 12, 8, 6]
right_product = 24
```

#### `i = 0`

- 当前 `answer[0] = 1`
- `answer[0] *= right_product = 1 * 24 = 24`
- 然后更新 `right_product *= nums[0] = 24 * 1 = 24`

最终：

```text
answer = [24, 12, 8, 6]
```

---

### 面试代码

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer
```

---

### 为什么这个方法最适合面试

因为它有三个优点。

### 1. 思路其实还是“左积 × 右积”

它不是新的思路，只是把方法二继续压缩空间。

所以讲起来很顺：

```text
我先用 answer 存左积，再从右往左用一个变量补右积
```

### 2. 代码不复杂

虽然是空间优化版，但代码仍然很自然。

没有特别难写的边界，也没有花哨技巧。

### 3. 复杂度漂亮

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`（不算返回数组）

这正是题目最希望看到的答案。

---

### 这题关于 0 的情况，要不要单独分类讨论？

这题一个容易担心的地方是：

```text
如果数组里有 0 怎么办？
```

其实这个前后缀乘积做法：

```text
不需要单独特判 0
```

它会自然算对。

比如：

```text
nums = [-1, 1, 0, -3, 3]
```

最后结果是：

```text
[0, 0, 9, 0, 0]
```

因为除了 `nums[2] = 0` 这个位置外，别的位置在“除自己以外的乘积”里都会乘到这个 `0`，所以结果自然是 `0`。

而位置 `2` 的答案，则是其他非零元素的乘积：

```text
(-1) * 1 * (-3) * 3 = 9
```

所以这也是前后缀思路很稳的地方。

---

## 面试里可以怎么讲

你可以这样说：

```text
对于每个位置 i，答案其实等于它左边所有数的乘积乘上右边所有数的乘积。

所以我先从左往右，把每个位置左边的乘积存进 answer。
再从右往左，用一个变量维护当前右边乘积，把它乘到 answer[i] 上。

这样就能在 O(n) 时间内完成，并且除了返回数组外只用了一个额外变量。
```

如果你先写出方法二，再优化到方法三，层次会更完整。

---

## 总结

| 方法 | 时间复杂度 | 空间复杂度 | 评价 |
| --- | --- | --- | --- |
| 方法一：暴力枚举 | `O(n^2)` | `O(1)` | 直观，但太慢 |
| 方法二：前缀积数组 + 后缀积数组 | `O(n)` | `O(n)` | 很容易想到 |
| 方法三：前缀积写入答案数组 + 右乘积变量 | `O(n)` | `O(1)` | 面试主推 |

这题最重要的一句话就是：

```text
answer[i] = 左边所有数的乘积 × 右边所有数的乘积
```

只要这句话真正想清楚，代码基本就能自己推出来。
