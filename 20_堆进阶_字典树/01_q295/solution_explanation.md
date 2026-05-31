# LeetCode 295. 数据流的中位数（Find Median from Data Stream）解析

## 题目描述

设计一个数据结构，支持两个操作：

```python
addNum(num)
findMedian()
```

其中：

- `addNum(num)`：从数据流中加入一个整数
- `findMedian()`：返回当前所有数字的中位数

中位数定义：

```text
如果数字个数是奇数，中位数是排序后中间那个数
如果数字个数是偶数，中位数是排序后中间两个数的平均值
```

例子：

```text
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2.0
```

---

## 先理解题意

这题不是一次性给你一个数组，让你求中位数。

它是一个**动态数据流**：

```text
数字一个一个进来
每次都可能问当前中位数
```

如果每次问中位数时再排序，当然能做，但会很慢。

真正要优化的是：

```text
如何在不断插入数字的同时，快速拿到中间位置的数？
```

---

## 方法一：每次查询时排序

### 思路

最直接的做法：

```text
addNum 时直接 append
findMedian 时临时排序，再取中间
```

### 代码

```python
class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        nums = sorted(self.nums)
        n = len(nums)
        mid = n // 2

        if n % 2 == 1:
            return float(nums[mid])
        return (nums[mid - 1] + nums[mid]) / 2.0
```

### 评价

这个方法非常直观。

缺点也明显：

```text
每次 findMedian 都要重新排序
```

如果调用很多次 `findMedian`，会非常慢。

复杂度：

- `addNum`：`O(1)`
- `findMedian`：`O(n log n)`
- 空间复杂度：`O(n)`

下一步自然想到：

```text
能不能一直维护一个有序数组？
```

---

## 方法二：维护有序数组

### 思路

如果数组始终有序，那么找中位数就是 `O(1)`。

问题变成：

```text
每次插入新数字时，把它放到正确位置。
```

Python 可以用：

```python
bisect.insort
```

它会把数字插入到有序数组中的正确位置。

### 代码

```python
from bisect import insort


class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        insort(self.nums, num)

    def findMedian(self) -> float:
        n = len(self.nums)
        mid = n // 2

        if n % 2 == 1:
            return float(self.nums[mid])
        return (self.nums[mid - 1] + self.nums[mid]) / 2.0
```

### 评价

这个方法比方法一更适合频繁查询：

```text
findMedian 很快，因为数组已经有序。
```

但插入会慢：

```text
插入位置可以二分找到，但真正插入时，后面的元素要整体搬移。
```

所以：

- `addNum`：`O(n)`
- `findMedian`：`O(1)`
- 空间复杂度：`O(n)`

还能再优化插入吗？

中位数只关心“中间”，不需要维护整个数组完全有序。

这就引出双堆。

---

## 方法三：双堆 / 对顶堆（面试主推）

### 核心思路

中位数只和中间位置有关。

我们可以把所有数字分成两半：

```text
左半边：较小的一半
右半边：较大的一半
```

如果能快速拿到：

```text
左半边最大值
右半边最小值
```

那中位数就很好求。

所以用两个堆：

```text
small：最大堆，保存较小的一半
large：最小堆，保存较大的一半
```

Python 只有最小堆，所以最大堆用负数模拟：

```text
small 里存 -num
small[0] 的相反数就是左半边最大值
```

### 维护两个不变量

双堆能正确工作的关键是两个不变量：

```text
1. small 中的所有数 <= large 中的所有数
2. len(small) == len(large) 或 len(small) == len(large) + 1
```

也就是说：

```text
左半边可以和右半边一样多
左半边也可以多一个
但右半边不能更多
```

为什么让左半边可以多一个？

这样当总数是奇数时，中位数就是左半边最大值：

```text
-small[0]
```

当总数是偶数时，中位数就是：

```text
(左半边最大值 + 右半边最小值) / 2
```

也就是：

```text
(-small[0] + large[0]) / 2
```

### addNum 怎么维护不变量

代码采用一个很稳的写法：

```python
heappush(self.small, -num)
heappush(self.large, -heappop(self.small))

if len(self.large) > len(self.small):
    heappush(self.small, -heappop(self.large))
```

分三步看。

#### 第一步：先放进 small

```python
heappush(self.small, -num)
```

先假设新数属于左半边。

#### 第二步：把 small 的最大值挪到 large

```python
heappush(self.large, -heappop(self.small))
```

`small` 是最大堆，堆顶代表左半边最大值。

把它挪到 `large`，可以保证：

```text
small 留下来的数不会比 large 里的数更大
```

也就是维护了：

```text
small 中的所有数 <= large 中的所有数
```

#### 第三步：如果 large 更多，就挪一个回来

```python
if len(self.large) > len(self.small):
    heappush(self.small, -heappop(self.large))
```

我们希望：

```text
small 的数量 >= large 的数量
```

如果 `large` 多了，就把 `large` 里最小的那个挪回 `small`。

这样既维持了大小关系，也维持了数量平衡。

### 用 `[1, 2, 3]` 走一遍

#### 加入 1

```text
small = [1]
large = []
```

中位数：

```text
1
```

#### 加入 2

先放左边，再把左边最大值挪到右边：

```text
small = [1]
large = [2]
```

两边一样多，中位数：

```text
(1 + 2) / 2 = 1.5
```

#### 加入 3

先放左边，左边最大值会被挪到右边，之后右边多了，再挪最小值回来：

```text
small = [1, 2]
large = [3]
```

左边多一个，中位数：

```text
2
```

### 面试代码

```python
from heapq import heappop, heappush


class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)
        heappush(self.large, -heappop(self.small))

        if len(self.large) > len(self.small):
            heappush(self.small, -heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        return (-self.small[0] + self.large[0]) / 2.0
```

### 复杂度

- `addNum`：`O(log n)`
- `findMedian`：`O(1)`
- 空间复杂度：`O(n)`

### 面试里怎么讲

可以这样说：

```text
我把数据流分成左右两半。

左半边保存较小的一半，用最大堆，这样能快速拿到左边最大值。
右半边保存较大的一半，用最小堆，这样能快速拿到右边最小值。

我维护两个不变量：
1. 左半边所有数都 <= 右半边所有数
2. 左半边数量等于右半边，或者比右半边多 1

这样如果总数是奇数，中位数就是左半边最大值；
如果总数是偶数，中位数就是两个堆顶的平均值。

插入时先放左边，再把左边最大值挪到右边，保证大小关系；
如果右边数量更多，再把右边最小值挪回左边，保证数量平衡。
```

---

## 总结

| 方法 | `addNum` | `findMedian` | 空间 | 评价 |
| --- | --- | --- | --- | --- |
| 方法一：查询时排序 | `O(1)` | `O(n log n)` | `O(n)` | 最直观，但查询慢 |
| 方法二：有序数组 | `O(n)` | `O(1)` | `O(n)` | 思路自然，但插入慢 |
| 方法三：双堆 | `O(log n)` | `O(1)` | `O(n)` | 面试主推 |

最适合面试的是 **方法三：双堆 / 对顶堆**。

真正要记住的是：

```text
中位数只需要中间两个边界：
左半边最大值 + 右半边最小值。
```
