# LeetCode 703. 数据流中的第 K 大元素（Kth Largest Element in a Stream）解析

## 题目描述

设计一个类 `KthLargest`，支持：

```python
KthLargest(k, nums)
add(val)
```

其中：

- 初始化时给定整数 `k` 和初始数组 `nums`
- `add(val)` 表示把新数字加入数据流
- 每次调用 `add` 后，返回当前数据流中的第 `k` 大元素

例如：

```text
k = 3
nums = [4, 5, 8, 2]

add(3)  -> 4
add(5)  -> 5
add(10) -> 5
add(9)  -> 8
add(4)  -> 8
```

---

## 先理解题意

这题要注意两点：

```text
1. 数据是不断加入的
2. 每次要的是“第 k 大”，不是最大值
```

比如：

```text
k = 3
当前数字: [2, 4, 5, 8]
第 3 大是 4
```

如果再加入一个 `10`：

```text
[2, 4, 5, 8, 10]
第 3 大变成 5
```

所以核心问题是：

```text
如何在不断插入数字时，始终快速拿到第 k 大？
```

---

## 方法一：每次都排序

### 思路

最直接的想法：

```text
把所有数字都存下来
每次 add 后重新排序
返回倒数第 k 个
```

### 代码

```python
class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums[:]

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]
```

### 评价

优点：

```text
非常直观，最好想到。
```

缺点：

```text
每次 add 都要整体排序。
```

复杂度：

- `add`：`O(n log n)`
- 空间复杂度：`O(n)`

这显然不够好。

---

## 方法二：始终维护有序数组

### 思路

如果数组一直有序，就不需要每次重新全排。

可以在插入时用二分找到位置，再把元素插进去。

Python 可以用：

```python
bisect.insort
```

### 代码

```python
from bisect import insort


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        insort(self.nums, val)
        return self.nums[-self.k]
```

### 评价

这个方法比方法一好，因为：

```text
不再重复做整段排序。
```

但问题还在：

```text
插入时虽然位置能二分找到，但数组元素还是要整体搬移。
```

复杂度：

- `add`：`O(n)`
- 空间复杂度：`O(n)`

还能继续优化。

---

## 方法三：固定大小的小顶堆（面试主推）

### 核心思路

要求“第 `k` 大”，其实不需要保存所有数字的完整顺序。

我们只需要关心：

```text
当前最大的 k 个数是谁
```

如果我们始终维护一个大小为 `k` 的集合：

```text
这个集合里放当前最大的 k 个数
```

那么：

```text
这个集合里最小的那个数
就是整个数据流里的第 k 大
```

这就是小顶堆的用法。

---

## 为什么是“小顶堆”

假设：

```text
k = 3
数据流里最大的 3 个数是 [5, 8, 10]
```

如果用小顶堆保存它们：

```text
堆顶 = 5
```

而 `5` 恰好就是：

```text
第 3 大
```

所以：

```text
堆里保留最大的 k 个数
堆顶就是答案
```

---

## add(val) 时怎么维护

维护规则只有两步。

### 1. 先把新值放进堆

```python
heappush(heap, val)
```

### 2. 如果堆大小超过 k，就弹出最小值

```python
if len(heap) > k:
    heappop(heap)
```

为什么弹最小值？

因为我们只想保留：

```text
最大的 k 个数
```

一旦数量超过 `k`，最小的那个一定不可能再是“最大的 k 个数”之一，所以直接踢掉。

这样最终堆里剩下的永远是：

```text
当前最大的 k 个数
```

堆顶就是第 `k` 大。

---

## 初始化时为什么也用同样逻辑

初始化时不是把 `nums` 直接全堆化然后完事，而是也按同样规则逐个加入：

```python
for num in nums:
    heappush(heap, num)
    if len(heap) > k:
        heappop(heap)
```

这样初始化结束后，堆的含义和后续 `add` 完全一致：

```text
堆里始终只保留最大的 k 个数
```

这样逻辑最统一，面试里也最好讲。

---

## 用例子走一遍

### 初始

```text
k = 3
nums = [4, 5, 8, 2]
```

依次加入：

- 加 4：堆 `[4]`
- 加 5：堆 `[4, 5]`
- 加 8：堆 `[4, 5, 8]`
- 加 2：堆变 4 个数，弹最小值 2，堆还是 `[4, 5, 8]`

所以初始化后：

```text
堆里是最大的 3 个数：[4, 5, 8]
堆顶 4 就是第 3 大
```

### add(3)

加入后：

```text
[3, 4, 5, 8]
```

超过 3 个，弹最小值 3：

```text
[4, 5, 8]
```

返回：

```text
4
```

### add(10)

加入后：

```text
[4, 5, 8, 10]
```

弹最小值 4：

```text
[5, 8, 10]
```

返回：

```text
5
```

---

## 面试代码

```python
from heapq import heappop, heappush


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []

        for num in nums:
            heappush(self.heap, num)
            if len(self.heap) > self.k:
                heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]
```

---

## 复杂度

设堆大小最多为 `k`。

### 初始化

初始数组长度是 `n`。

每次插入堆，堆大小最多只到 `k + 1`，所以：

- 初始化：`O(n log k)`

### add

每次 `add` 最多做一次入堆、一次出堆：

- `add`：`O(log k)`

### 空间复杂度

堆里最多只保留 `k` 个元素：

- 空间复杂度：`O(k)`

---

## 为什么它最适合面试

因为这题最关键的思维转换就是：

```text
第 k 大 ≠ 需要维护全局有序
第 k 大 = 只需要维护最大的 k 个数
```

一旦想到这一步：

```text
最大的 k 个数 + 取其中最小值
```

自然就对应：

```text
大小固定为 k 的小顶堆
```

这个思路短、稳、复杂度也最好。

---

## 面试里怎么讲

可以直接这样说：

```text
我维护一个大小最多为 k 的小顶堆。

堆里始终保存当前数据流中最大的 k 个数。
如果新数加入后堆大小超过 k，就弹出最小值。
这样最后堆顶就是这 k 个数里最小的那个，也就是整个数据流里的第 k 大元素。
```

这个解释非常标准。

---

## 总结

| 方法 | `add` | 空间 | 评价 |
| --- | --- | --- | --- |
| 方法一：每次排序 | `O(n log n)` | `O(n)` | 最直观，但太慢 |
| 方法二：有序数组 | `O(n)` | `O(n)` | 比全排序好，但插入仍慢 |
| 方法三：固定大小小顶堆 | `O(log k)` | `O(k)` | 面试主推 |

最适合面试的是：

```text
固定大小为 k 的小顶堆
```

真正要记住的一句话是：

```text
堆里保留最大的 k 个数，堆顶就是第 k 大。
```
