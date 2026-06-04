# LeetCode 380. O(1) 时间插入、删除和获取随机元素（Insert Delete GetRandom O(1)）解析

## 题目描述

设计一个数据结构 `RandomizedSet`，支持下面三个操作，并且要求它们的**平均时间复杂度都是 `O(1)`**：

```python
RandomizedSet()
insert(val)
remove(val)
getRandom()
```

含义分别是：

- `insert(val)`：如果 `val` 不存在，插入并返回 `True`；否则返回 `False`
- `remove(val)`：如果 `val` 存在，删除并返回 `True`；否则返回 `False`
- `getRandom()`：从当前集合中**等概率**返回一个元素

题目保证：调用 `getRandom()` 时，集合里至少有一个元素。

---

## 先理解题意

这题表面上像普通集合题，但要求其实很苛刻：

```text
1. 要能判重
2. 要能删除指定值
3. 要能随机等概率取一个值
4. 上面三个操作都尽量做到 O(1)
```

单看其中一个要求都不难，但三个一起满足就不那么直接了。

最关键的矛盾在这里：

```text
- 哈希表 / 哈希集合：查找、插入、删除很快
- 数组：按下标随机取值很快
```

所以这题的本质就是：

```text
怎么把“哈希表的快查找”和“数组的快随机访问”结合起来？
```

---

## 方法一：直接用数组模拟

### 思路

最直接的想法就是用一个列表存所有元素：

- `insert` 前先判断元素是否已经在列表里
- `remove` 时直接调用删除
- `getRandom` 时用 `random.choice`

### 代码

```python
import random


class RandomizedSet:
    def __init__(self):
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.nums:
            return False
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.nums:
            return False
        self.nums.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
```

### 为什么可行

因为列表里确实保存了当前所有元素：

- 判重可以做
- 删除可以做
- 随机返回也可以做

功能上完全没问题。

### 但为什么不满足题目要求

问题在于复杂度：

- `val in self.nums` 是线性查找，`O(n)`
- `self.nums.remove(val)` 也是先找位置再删，`O(n)`

所以这个方法虽然能做出来，但不满足题目要求的平均 `O(1)`。

### 复杂度

- `insert`：`O(n)`
- `remove`：`O(n)`
- `getRandom`：`O(1)`
- 空间复杂度：`O(n)`

---

## 方法二：数组 + 哈希表记录下标（面试主推）

### 先想一半：为什么只用哈希表不够

如果只用哈希表或集合：

- `insert`：快
- `remove`：快
- 判重：快

但 `getRandom()` 麻烦。

因为哈希表不是按连续下标存储的，我们没法像数组那样：

```python
nums[random_index]
```

如果你每次为了随机返回，临时把集合转成列表：

```python
random.choice(list(my_set))
```

那这一步就会变成 `O(n)`，题目要求就被破坏了。

所以一定要保留一个数组，专门负责：

```text
O(1) 随机取元素
```

---

## 核心难点：数组怎么做到 O(1) 删除

数组尾部追加是 `O(1)`，这个没问题。

但数组删除指定元素通常不行，因为删中间元素会导致后面的元素整体左移。

比如：

```text
nums = [10, 20, 30, 40]
```

如果要删掉 `20`，普通做法会变成：

```text
[10, 30, 40]
```

这一步需要搬移元素，不是 `O(1)`。

所以这题真正的关键就在于：

```text
如何在数组里 O(1) 删除某个元素？
```

答案是：

```text
不要真的“中间删除并搬移”，而是把它和最后一个元素交换，再删尾巴。
```

---

## 交换到末尾再删除

假设：

```text
nums = [10, 20, 30, 40]
```

现在要删除 `20`。

### 第一步：先找到 `20` 的下标

如果我们有一个哈希表：

```text
index_map = {
    10: 0,
    20: 1,
    30: 2,
    40: 3,
}
```

那么能立刻知道：

```text
20 的下标是 1
```

### 第二步：拿到数组最后一个元素

```text
last_val = 40
```

### 第三步：把最后一个元素覆盖到待删除位置

把 `40` 放到下标 `1`：

```text
nums = [10, 40, 30, 40]
```

### 第四步：更新 `40` 在哈希表里的下标

因为 `40` 现在从原来的下标 `3` 变成了下标 `1`，所以要改成：

```text
index_map[40] = 1
```

### 第五步：弹出数组最后一个位置

```text
nums.pop()
```

结果变成：

```text
nums = [10, 40, 30]
```

### 第六步：删掉 `20` 的哈希记录

```text
del index_map[20]
```

这样整个删除过程就完成了，而且没有发生整段搬移。

---

## 数据结构怎么设计

我们维护两个东西：

### 1. `self.nums`

一个数组，保存当前所有元素。

作用：

```text
支持 O(1) 随机取值
```

### 2. `self.index_map`

一个哈希表，记录：

```text
元素值 -> 它在 nums 里的下标
```

作用：

```text
支持 O(1) 判断元素是否存在
支持 O(1) 找到要删除元素的位置
```

这两个结构必须始终保持一致。

---

## 三个操作分别怎么做

## 1. insert(val)

### 思路

先查哈希表：

- 如果已经存在，返回 `False`
- 如果不存在，就追加到数组尾部，并记录它的下标

### 过程

```python
if val in self.index_map:
    return False

self.nums.append(val)
self.index_map[val] = len(self.nums) - 1
return True
```

### 为什么是 O(1)

- 哈希表查重：平均 `O(1)`
- 数组尾插：`O(1)`
- 哈希表记录下标：平均 `O(1)`

---

## 2. remove(val)

### 思路

先查是否存在。

如果不存在，直接返回 `False`。

如果存在：

1. 找到它的下标
2. 取出数组最后一个元素
3. 用最后一个元素覆盖待删位置
4. 更新最后一个元素的新下标
5. 弹出数组尾部
6. 删除哈希表中 `val` 的记录

### 代码骨架

```python
if val not in self.index_map:
    return False

remove_index = self.index_map[val]
last_val = self.nums[-1]

self.nums[remove_index] = last_val
self.index_map[last_val] = remove_index

self.nums.pop()
del self.index_map[val]

return True
```

### 这里为什么即使删的是最后一个元素也没问题

比如：

```text
nums = [10, 20, 30]
删 30
```

这时：

- `remove_index = 2`
- `last_val = 30`

执行：

```python
self.nums[2] = 30
self.index_map[30] = 2
self.nums.pop()
del self.index_map[30]
```

虽然看起来像“自己覆盖自己”，但逻辑完全没问题。

所以这一版写法有一个优点：

```text
不需要专门区分“删除的是不是最后一个元素”
```

面试里这样写通常最稳。

---

## 3. getRandom()

### 思路

因为所有元素都在数组 `self.nums` 里，所以直接随机返回一个下标对应的值即可。

```python
return random.choice(self.nums)
```

### 为什么满足等概率

因为数组里的每个元素都只出现一次，`random.choice` 会等概率选择数组里的每一个位置。

位置等概率，元素也就等概率。

---

## 用例子完整走一遍

假设执行顺序如下：

```text
insert(1)
remove(2)
insert(2)
getRandom()
remove(1)
insert(2)
getRandom()
```

### 初始状态

```text
nums = []
index_map = {}
```

### 1. insert(1)

追加到数组尾部：

```text
nums = [1]
index_map = {1: 0}
```

返回：

```text
True
```

### 2. remove(2)

`2` 不存在。

返回：

```text
False
```

### 3. insert(2)

追加到尾部：

```text
nums = [1, 2]
index_map = {1: 0, 2: 1}
```

返回：

```text
True
```

### 4. getRandom()

可能返回 `1`，也可能返回 `2`。

### 5. remove(1)

当前：

```text
nums = [1, 2]
index_map = {1: 0, 2: 1}
```

删除 `1`：

- `remove_index = 0`
- `last_val = 2`
- 用 `2` 覆盖位置 `0`
- 更新 `2` 的下标为 `0`
- 弹出尾部
- 删除 `1` 的映射

结果：

```text
nums = [2]
index_map = {2: 0}
```

返回：

```text
True
```

### 6. insert(2)

`2` 已存在。

返回：

```text
False
```

### 7. getRandom()

现在集合里只有 `2`，所以只能返回：

```text
2
```

---

## 面试代码

```python
import random


class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False

        self.nums.append(val)
        self.index_map[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False

        remove_index = self.index_map[val]
        last_val = self.nums[-1]

        self.nums[remove_index] = last_val
        self.index_map[last_val] = remove_index

        self.nums.pop()
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
```

---

## 复杂度分析

## 方法一：直接用数组模拟

- `insert`：`O(n)`
- `remove`：`O(n)`
- `getRandom`：`O(1)`
- 空间复杂度：`O(n)`

## 方法二：数组 + 哈希表记录下标

- `insert`：平均 `O(1)`
- `remove`：平均 `O(1)`
- `getRandom`：`O(1)`
- 空间复杂度：`O(n)`

这里哈希表操作说“平均 `O(1)`”，是因为哈希冲突的极端情况通常不作为面试主讨论点。

---

## 为什么这个方法最适合面试

这题最适合面试的方法就是：

```text
数组 + 哈希表 + 删除时和末尾交换
```

原因有三个：

### 1. 完全满足题意

三个操作都能做到平均 `O(1)`。

### 2. 思路有代表性

这题考的不是单一 API，而是：

```text
把两种数据结构的优点拼起来
```

这是设计题里很常见的能力。

### 3. 代码短，而且容易讲清楚

真正的关键点只有一个：

```text
删除时不要做数组中间删除，改成“末尾元素补位 + pop”
```

只要把这句话讲清楚，整题就通了。

---

## 面试里怎么讲

你可以直接这样解释：

```text
我用一个数组保存所有元素，这样 getRandom 可以 O(1) 随机取值。

再用一个哈希表记录每个元素在数组中的下标，这样 insert 时可以 O(1) 判重，remove 时也能 O(1) 找到待删除元素的位置。

删除时我不用真的把数组中间元素删掉，而是把最后一个元素放到待删位置，再弹出数组尾部，同时更新这个最后一个元素在哈希表里的下标。

这样 insert、remove、getRandom 三个操作都能做到平均 O(1)。
```

这就是这题最标准、最稳的说法。

---

## 总结

| 方法 | `insert` | `remove` | `getRandom` | 空间 | 评价 |
| --- | --- | --- | --- | --- | --- |
| 方法一：直接数组模拟 | `O(n)` | `O(n)` | `O(1)` | `O(n)` | 好想，但不达标 |
| 方法二：数组 + 哈希表 | 平均 `O(1)` | 平均 `O(1)` | `O(1)` | `O(n)` | 面试主推 |

最重要的一句话是：

```text
数组负责随机访问，哈希表负责定位下标；删除时用末尾元素补位，这样就避免了数组中间删除的线性搬移。
```
