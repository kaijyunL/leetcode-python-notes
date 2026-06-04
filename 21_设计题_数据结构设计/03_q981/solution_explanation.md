# LeetCode 981. 基于时间的键值存储（Time Based Key-Value Store）解析

## 题目描述

设计一个时间维度上的键值存储 `TimeMap`，支持下面两个操作：

```python
TimeMap()
set(key, value, timestamp)
get(key, timestamp)
```

含义是：

- `set(key, value, timestamp)`：在时间 `timestamp` 时，把 `key` 的值设为 `value`
- `get(key, timestamp)`：返回在时间 `timestamp` 时，`key` 对应的值

这里的“在时间 `timestamp` 时的值”并不是只找**恰好等于** `timestamp` 的记录，而是要找：

```text
时间 <= timestamp 的最近一次赋值
```

如果这样的记录不存在，就返回空字符串 `""`。

题目还给了一个非常关键的条件：

```text
所有 set 的 timestamp 都是严格递增的
```

这个条件会直接决定最优解法。

---

## 先理解题意

这题最容易误解的点是 `get`。

比如：

```text
set("foo", "bar", 1)
set("foo", "bar2", 4)
```

那么：

```text
get("foo", 1) -> "bar"
get("foo", 3) -> "bar"
get("foo", 4) -> "bar2"
get("foo", 5) -> "bar2"
```

为什么 `get("foo", 3)` 也是 `"bar"`？

因为时间 `3` 时，最近一次且不超过 `3` 的赋值发生在时间 `1`。

所以这题本质上是在问：

```text
对于每个 key，如何快速找到“不大于目标时间的最后一个版本”？
```

---

## 先抓住题目的关键条件

题目说：

```text
所有 set 的 timestamp 严格递增
```

这意味着：

- 后来的写入时间一定比前面大
- 对同一个 `key` 来说，它的历史记录天然就是按时间递增排列的

也就是说，我们根本不需要额外排序。

这很重要，因为一旦每个 `key` 的历史记录天然有序，就可以考虑：

```text
二分查找
```

但在上二分之前，我们先看一个更直观的做法。

---

## 方法一：按 key 存所有版本，get 时从后往前找

### 思路

我们可以用一个哈希表：

```text
key -> [(timestamp1, value1), (timestamp2, value2), ...]
```

由于时间是递增写入的，所以：

- `set` 时直接追加到列表尾部
- `get` 时从后往前找第一个 `timestamp <= target` 的记录

为什么从后往前？

因为我们要找的是：

```text
不超过目标时间的最近一次赋值
```

“最近一次”天然就更靠后，所以倒着找最顺手。

---

### 代码

```python
class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        for current_timestamp, current_value in reversed(self.store[key]):
            if current_timestamp <= timestamp:
                return current_value

        return ""
```

---

### 为什么可行

假设：

```text
foo -> [(1, "bar"), (4, "bar2"), (6, "bar3")]
```

如果查：

```text
get("foo", 5)
```

倒着看：

- `(6, "bar3")`：6 > 5，不行
- `(4, "bar2")`：4 <= 5，返回 `"bar2"`

逻辑完全正确。

---

### 复杂度

设某个 `key` 一共存了 `m` 条记录。

- `set`：`O(1)`，因为只是尾部追加
- `get`：最坏 `O(m)`，因为可能要从后扫到前
- 空间复杂度：`O(n)`，`n` 是所有版本总数

这个方法已经不难写了，但 `get` 还不够快。

---

## 方法二：按 key 存时间序列 + 二分查找（面试主推）

### 核心思路

方法一慢在哪里？

慢在：

```text
get 时要线性扫描
```

但我们前面已经知道，每个 `key` 的历史记录本来就是按时间递增的。

既然有序，就没必要线性找，应该直接二分。

`get(key, timestamp)` 真正要找的是：

```text
最后一个 timestamp <= 目标 timestamp 的位置
```

这就是一个非常标准的“找右侧边界”问题。

---

## 为什么是“找最后一个 <= timestamp”

继续看例子：

```text
foo -> [(1, "bar"), (4, "bar2"), (6, "bar3")]
```

如果查：

```text
get("foo", 5)
```

你不是要找“最接近 5 的时间”，而是要找：

```text
所有 <= 5 的时间里，最大的那个
```

也就是：

```text
1, 4 里选最大的 -> 4
```

所以返回 `"bar2"`。

这就是“右边界”的本质。

---

## 二分过程怎么想

我们对某个 `key` 的版本列表做二分。

假设：

```text
records = [(1, "bar"), (4, "bar2"), (6, "bar3")]
目标时间 = 5
```

我们维护：

- `left`
- `right`
- `answer`

其中：

```text
answer 表示当前找到的、满足 timestamp <= 目标时间 的最好答案
```

### 第一次

```text
left = 0, right = 2
mid = 1
records[1][0] = 4
```

因为：

```text
4 <= 5
```

说明下标 `1` 这个位置是一个合法答案。

但我们还不能立刻停，因为右边可能还有更靠后、也仍然 <= 5 的时间。

所以：

```text
先把 answer 记成 "bar2"
然后继续去右边找
```

即：

```text
left = mid + 1
```

### 第二次

```text
left = 2, right = 2
mid = 2
records[2][0] = 6
```

因为：

```text
6 > 5
```

说明这个时间太晚了，不合法。

所以只能去左边找：

```text
right = mid - 1
```

循环结束，最终 `answer = "bar2"`。

---

## 面试代码

```python
class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        records = self.store[key]
        left = 0
        right = len(records) - 1
        answer = ""

        while left <= right:
            mid = (left + right) // 2
            current_timestamp, current_value = records[mid]

            if current_timestamp <= timestamp:
                answer = current_value
                left = mid + 1
            else:
                right = mid - 1

        return answer
```

---

## 为什么这段二分写法是对的

关键就在这两句：

```python
if current_timestamp <= timestamp:
    answer = current_value
    left = mid + 1
```

为什么不是直接返回？

因为当前这个位置虽然合法，但我们想找的是：

```text
最靠右的合法位置
```

所以只要当前时间 `<= target`，就先记住它，然后继续往右找，看能不能找到更晚、但仍然不超过目标时间的记录。

而如果：

```python
current_timestamp > timestamp
```

说明这个位置已经太靠后了，右边只会更大，更不可能合法，所以必须往左收缩。

这个逻辑一定要讲清楚，这是这题二分的核心。

---

## 用例子完整走一遍

执行顺序：

```text
set("foo", "bar", 1)
set("foo", "bar2", 4)
get("foo", 1)
get("foo", 3)
get("foo", 4)
get("foo", 5)
```

### 1. set("foo", "bar", 1)

```text
store = {
    "foo": [(1, "bar")]
}
```

### 2. set("foo", "bar2", 4)

```text
store = {
    "foo": [(1, "bar"), (4, "bar2")]
}
```

### 3. get("foo", 1)

找最后一个 `<= 1` 的时间。

答案是时间 `1`，返回：

```text
"bar"
```

### 4. get("foo", 3)

找最后一个 `<= 3` 的时间。

- 时间 `1` 合法
- 时间 `4` 不合法

所以返回：

```text
"bar"
```

### 5. get("foo", 4)

找最后一个 `<= 4` 的时间。

答案就是时间 `4`，返回：

```text
"bar2"
```

### 6. get("foo", 5)

找最后一个 `<= 5` 的时间。

- 时间 `4` 合法
- 后面没有更大的合法时间

所以返回：

```text
"bar2"
```

---

## 复杂度分析

设某个 `key` 的历史版本数为 `m`。

### 方法一：倒序线性扫描

- `set`：`O(1)`
- `get`：`O(m)`
- 空间复杂度：`O(n)`

### 方法二：二分查找

- `set`：`O(1)`
- `get`：`O(log m)`
- 空间复杂度：`O(n)`

其中：

- `m` 表示某个 key 自己的版本数
- `n` 表示所有 key 的总版本数

---

## 为什么它最适合面试

最适合面试的方法就是：

```text
哈希表存 key -> 历史版本列表
每个列表按时间天然有序
get 时二分查找最后一个 <= timestamp 的位置
```

原因是：

### 1. 完全利用了题目给的关键条件

题目专门告诉你：

```text
timestamp 严格递增
```

这不是废话，而是在提示你：

```text
可以直接 append，并且可以二分
```

### 2. 代码短、逻辑稳

没有复杂数据结构，不需要平衡树，不需要额外排序。

### 3. 面试官最想看的就是这个思维过程

你能不能从：

```text
“要找最近且不超过目标时间的版本”
```

一步走到：

```text
“有序列表里找最后一个 <= target，用二分做右边界”
```

这是这题真正的考点。

---

## 面试里怎么讲

你可以直接这样说：

```text
我用一个哈希表把每个 key 映射到它的历史版本列表。
因为题目保证 set 的 timestamp 严格递增，所以每个 key 的列表天然按时间有序，set 时直接 append 就行。

get 的时候，我要找的是最后一个 timestamp <= 查询时间 的版本。
因为列表有序，所以可以在这个 key 对应的列表里做二分查找。
只要当前时间 <= target，我就先记录这个值，并继续往右找更靠后的合法答案；如果当前时间 > target，就往左收缩。
这样 set 是 O(1)，get 是 O(log m)。
```

这就是最标准的面试表达。

---

## 总结

| 方法 | `set` | `get` | 空间 | 评价 |
| --- | --- | --- | --- | --- |
| 方法一：倒序线性扫描 | `O(1)` | `O(m)` | `O(n)` | 好写，但查询慢 |
| 方法二：有序列表 + 二分查找 | `O(1)` | `O(log m)` | `O(n)` | 面试主推 |

最重要的一句话是：

```text
这题的关键不是“存住历史值”，而是“利用时间递增，让每个 key 的版本列表天然有序，然后二分找最后一个不超过目标时间的版本”。
```