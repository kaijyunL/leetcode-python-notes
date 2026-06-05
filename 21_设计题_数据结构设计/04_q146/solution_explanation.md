# LeetCode 146. LRU 缓存（LRU Cache）解析

## 题目描述

设计一个满足 **LRU（Least Recently Used，最近最少使用）** 规则的缓存结构 `LRUCache`，支持：

```python
LRUCache(capacity)
get(key)
put(key, value)
```

规则如下：

- `get(key)`：如果 `key` 存在，返回对应的值；否则返回 `-1`
- `put(key, value)`：如果 `key` 已存在，就更新它的值；如果不存在，就插入这个键值对
- 当缓存容量超过 `capacity` 时，要删除 **最近最少使用** 的那个键

并且题目要求：

```text
get 和 put 都必须做到 O(1)
```

---

## 先理解题意

这题不是单纯让你“存键值对”，而是让你维护两件事：

```text
1. key -> value 的映射
2. 每个 key 的最近使用顺序
```

其中“使用”包括两种情况：

- 调用了 `get(key)` 并且这个 key 存在
- 调用了 `put(key, value)`，无论是更新旧 key 还是插入新 key

只要一个 key 被使用了，它就应该变成：

```text
最近使用过的 key
```

而当容量满了，就要淘汰：

```text
最久没有被使用的 key
```

所以这题本质在考：

```text
如何一边 O(1) 查 key，一边 O(1) 维护“最近使用顺序”？
```

---

## 用例子先建立直觉

假设：

```text
capacity = 2
```

执行下面操作：

```text
put(1, 1)
put(2, 2)
get(1)
put(3, 3)
get(2)
put(4, 4)
get(1)
get(3)
get(4)
```

过程如下。

### 1. put(1, 1)

缓存里放入 `1`：

```text
[1]
```

### 2. put(2, 2)

缓存变成：

```text
[1, 2]
```

这里如果从左到右表示“越左越久没用，越右越新”，那么：

- `1` 更久没用
- `2` 是最近使用的

### 3. get(1)

返回 `1`，同时 `1` 被访问了，所以它应该变成最近使用：

```text
[2, 1]
```

### 4. put(3, 3)

容量已满，要插入 `3`，就必须删掉最久没用的那个，也就是 `2`：

```text
[1, 3]
```

### 5. get(2)

`2` 已被淘汰，所以返回：

```text
-1
```

### 6. put(4, 4)

当前缓存是：

```text
[1, 3]
```

最久没用的是 `1`，所以删掉它，再加入 `4`：

```text
[3, 4]
```

### 7. get(1)

返回：

```text
-1
```

### 8. get(3)

返回 `3`，并把 `3` 移到最近使用位置。

### 9. get(4)

返回 `4`。

---

## 方法一：哈希表 + 列表维护顺序

### 思路

最直接的想法是维护两个结构：

- 一个哈希表 `cache`，记录 `key -> value`
- 一个列表 `order`，记录使用顺序

比如：

```text
order = [2, 1, 4]
```

表示：

- `2` 最久没用
- `4` 最近刚用过

那么：

- `get(key)` 成功时，先返回值，再把这个 `key` 从列表中删掉并放到末尾
- `put(key, value)` 时：
  - 如果 key 已存在，更新值，并把它移动到末尾
  - 如果 key 不存在，就插入；若容量满了，先删除列表头部对应的 key

---

### 代码

```python
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
            return

        if len(self.cache) == self.capacity:
            lru_key = self.order.pop(0)
            del self.cache[lru_key]

        self.cache[key] = value
        self.order.append(key)
```

---

### 为什么可行

因为：

- 哈希表能正确存值
- 列表能维护“谁更久没用、谁最近刚用过”
- 每次访问或更新时，都把这个 key 挪到列表末尾

逻辑上完全正确。

---

### 为什么不满足题目要求

问题出在列表操作：

```python
self.order.remove(key)
self.order.pop(0)
```

这两个都不是 `O(1)`：

- `remove(key)` 先找 key，再删除，最坏 `O(n)`
- `pop(0)` 会导致后面的元素整体左移，最坏 `O(n)`

所以这个方法虽然能做对，但达不到题目要求。

---

### 复杂度

- `get`：最坏 `O(n)`
- `put`：最坏 `O(n)`
- 空间复杂度：`O(n)`

---

## 方法二：哈希表 + 双向链表（面试主推）

### 先想清楚题目真正需要什么

题目要求 `get` 和 `put` 都是 `O(1)`。

这意味着我们必须同时做到：

```text
1. O(1) 根据 key 找到对应节点
2. O(1) 把某个节点从“原位置”摘掉
3. O(1) 把某个节点放到“最近使用位置”
4. O(1) 删除“最久没用”的节点
```

其中：

- 第 1 点适合用哈希表
- 第 2、3、4 点适合用双向链表

所以最经典的组合就是：

```text
哈希表 + 双向链表
```

---

## 双向链表里每个节点存什么

每个节点至少要存：

- `key`
- `value`
- `prev`
- `next`

为什么节点里一定要存 `key`？

因为当容量满了、要删除最久没用节点时，我们会先从链表里拿到这个节点；但删掉哈希表时需要：

```python
del cache[node.key]
```

所以节点里不能只存 `value`，还得存自己的 `key`。

---

## 链表顺序怎么定义

我们约定：

- 靠近头部的是 **更久没用的**
- 靠近尾部的是 **最近刚用过的**

这样就很自然：

- `get` 或 `put` 某个 key 后，把它移动到尾部
- 容量满时，删除头部后面的那个真实节点

为了让边界处理更简单，我们一般会加两个哨兵节点：

- `dummy_head`
- `dummy_tail`

链表大致长这样：

```text
dummy_head <-> 最久没用 ... 最近刚用过 <-> dummy_tail
```

这样做的好处是：

```text
插入和删除时不用专门判断空链表、头节点、尾节点
```

面试里这是非常稳的写法。

---

## 两个核心小操作

## 1. 删除一个节点

如果某个节点已经在链表里，要把它摘掉，只需要改它前后节点的指针：

```python
prev_node.next = next_node
next_node.prev = prev_node
```

这就是双向链表最重要的优势：

```text
已知节点位置时，删除是 O(1)
```

---

## 2. 把节点放到尾部

尾部代表“最近使用”。

如果要把某个节点插入到 `dummy_tail` 前面，只要把它挂到：

```text
原来的最后一个真实节点 和 dummy_tail 之间
```

这也是固定指针修改，所以是 `O(1)`。

---

## get(key) 怎么做

### 情况 1：key 不存在

直接返回：

```text
-1
```

### 情况 2：key 存在

先通过哈希表拿到节点，然后：

1. 把这个节点从原位置删除
2. 再把它插到链表尾部
3. 返回它的值

为什么要“删掉再插入”？

因为一次成功的 `get` 也算一次“使用”，所以它必须变成最近使用的节点。

---

## put(key, value) 怎么做

### 情况 1：key 已存在

这时不是新增，而是更新：

1. 修改节点的 `value`
2. 把这个节点移动到尾部

因为更新也算一次使用。

### 情况 2：key 不存在

这时要新建节点，并把它放到尾部。

然后看容量是否超了：

- 如果没超，结束
- 如果超了，就删除链表头部后面的那个真实节点

为什么删头部后面的节点？

因为我们定义了：

```text
头部方向 = 最久没用
尾部方向 = 最近刚用过
```

所以头部第一个真实节点就是 LRU 节点。

---

## 面试代码

```python
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.dummy_head = Node(0, 0)
        self.dummy_tail = Node(0, 0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def _remove_node(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_tail(self, node: Node) -> None:
        last_node = self.dummy_tail.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.dummy_tail
        self.dummy_tail.prev = node

    def _move_to_tail(self, node: Node) -> None:
        self._remove_node(node)
        self._add_to_tail(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_tail(node)
            return

        node = Node(key, value)
        self.cache[key] = node
        self._add_to_tail(node)

        if len(self.cache) > self.capacity:
            lru_node = self.dummy_head.next
            self._remove_node(lru_node)
            del self.cache[lru_node.key]
```

---

## 上面代码里最容易写错的点

这题面试里最容易错的，不是大方向，而是细节。

### 1. `_add_to_tail` 的指针顺序

插入一个节点时，必须把四条关系接完整：

- `last_node.next = node`
- `node.prev = last_node`
- `node.next = dummy_tail`
- `dummy_tail.prev = node`

少写一条，链表就断了。

### 2. 删除节点后，哈希表也要同步删

淘汰 LRU 节点时，不能只把链表节点删掉，还要：

```python
del self.cache[lru_node.key]
```

否则哈希表里会留下脏数据。

### 3. 更新已有 key 时不要重复创建节点

如果 `key` 已经存在：

- 应该更新原节点的值
- 再把原节点移到尾部

而不是重新建一个同 key 的节点，否则链表和哈希表关系会乱。

### 4. 为什么哨兵节点特别有用

如果没有 `dummy_head` 和 `dummy_tail`，你每次删头节点、插尾节点时都要额外处理：

- 空链表
- 只有一个节点
- 删除头节点
- 删除尾节点

边界会一下子变多。

加哨兵后，插入删除都统一成“处理中间节点”，面试里明显更稳。

---

## 用例子完整走一遍

假设：

```text
capacity = 2
```

执行：

```text
put(1, 1)
put(2, 2)
get(1)
put(3, 3)
```

我们用链表表示顺序：

```text
head <-> ... <-> tail
```

其中越靠左越久没用，越靠右越新。

### 1. put(1, 1)

插到尾部：

```text
head <-> 1 <-> tail
```

哈希表：

```text
{1: node1}
```

### 2. put(2, 2)

插到尾部：

```text
head <-> 1 <-> 2 <-> tail
```

现在 `1` 更久没用，`2` 更新。

### 3. get(1)

访问 `1` 后，`1` 要移到尾部：

```text
head <-> 2 <-> 1 <-> tail
```

返回：

```text
1
```

### 4. put(3, 3)

先插入 `3`：

```text
head <-> 2 <-> 1 <-> 3 <-> tail
```

这时容量超过 2，要删除最左边真实节点 `2`：

```text
head <-> 1 <-> 3 <-> tail
```

同时从哈希表删掉 `2`。

这就是 LRU 的全过程。

---

## 复杂度分析

## 方法一：哈希表 + 列表

- `get`：最坏 `O(n)`
- `put`：最坏 `O(n)`
- 空间复杂度：`O(n)`

## 方法二：哈希表 + 双向链表

- `get`：`O(1)`
- `put`：`O(1)`
- 空间复杂度：`O(n)`

为什么方法二真的是 `O(1)`？

因为：

- 通过哈希表找节点是 `O(1)`
- 双向链表删除已知节点是 `O(1)`
- 双向链表尾插是 `O(1)`
- 删除头部第一个真实节点也是 `O(1)`

整个过程中没有线性扫描。

---

## 为什么这个方法最适合面试

这题最适合面试的方法就是：

```text
哈希表 + 双向链表
```

原因有三个。

### 1. 它是标准正解

这题核心要求就是 `get` 和 `put` 都 `O(1)`，而最经典、最标准的设计就是这个组合。

### 2. 它正好体现了“组合数据结构”的能力

这题不是在考某个 API，而是在考你能不能把：

- 哈希表的快定位
- 双向链表的快删除 / 快插入

拼成一个完整结构。

这是设计题里非常典型的考法。

### 3. 它的代码虽然比暴力法长一点，但逻辑最稳

真正的主线很清楚：

```text
哈希表定位节点
访问后移到尾部
超容量时删头部第一个真实节点
```

只要这三句讲顺，面试官通常就能确认你是真的理解了。

---

## 面试里怎么讲

你可以直接这样说：

```text
我用哈希表把 key 映射到双向链表节点，这样可以 O(1) 找到某个 key 对应的位置。
双向链表负责维护使用顺序，越靠头部表示越久没使用，越靠尾部表示最近使用。

当 get 命中或者 put 更新某个 key 时，我都会把对应节点移到链表尾部。
当插入新 key 导致容量超限时，我就删除链表头部后面的第一个真实节点，也就是最近最少使用的节点，并同步从哈希表中删掉。

这样 get 和 put 都是 O(1)。
```

这就是这题最标准的面试表达。

---

## 总结

| 方法 | `get` | `put` | 空间 | 评价 |
| --- | --- | --- | --- | --- |
| 方法一：哈希表 + 列表 | `O(n)` | `O(n)` | `O(n)` | 好想，但不达标 |
| 方法二：哈希表 + 双向链表 | `O(1)` | `O(1)` | `O(n)` | 面试主推 |

最重要的一句话是：

```text
LRU 不是单纯的字典题，关键是既要 O(1) 找到 key，又要 O(1) 调整“最近使用顺序”，所以必须把哈希表和双向链表结合起来。
```
