# LeetCode 92. 反转链表 II（Reverse Linked List II）解析

## 题目描述

给你一个链表的头节点 `head`，以及两个整数 `left` 和 `right`。

请你把链表中从位置 `left` 到位置 `right` 的那一段反转，并返回反转后的链表。

这里的下标是：

```text
从 1 开始计数
```

例如：

```text
head = 1 -> 2 -> 3 -> 4 -> 5
left = 2, right = 4
```

反转区间 `[2, 4]` 后，结果是：

```text
1 -> 4 -> 3 -> 2 -> 5
```

注意，这题不是整条链表都反转，而是：

```text
只反转中间的一小段
```

---

## 先理解这题在考什么

这题表面上是在“区间反转”，但真正考的是：

```text
你会不会把整段反转链表的能力，收缩成只处理某一段局部链表
```

所以它和 `206` 的关系非常直接：

- `206`：反转整条链表
- `92`：只反转 `[left, right]` 这一段

也就是说，这题的核心不是一个全新技巧，而是：

```text
先把反转区间定位出来，再把 206 的反转逻辑套到这段区间上
```

这也是为什么它常被看成 `206` 的直接升级版。

---

## 为什么这题里 `dummy` 特别重要

这题最麻烦的边界情况是：

```text
left = 1
```

也就是说，反转区间从头节点就开始了。

比如：

```text
1 -> 2 -> 3 -> 4
left = 1, right = 3
```

反转后新头节点会变成 `3`。

如果不加一个统一的前驱节点，代码很容易写出特殊分支。

所以这题里特别推荐先加：

```text
dummy -> head
```

这样一来：

- 原来的头节点也有前驱了
- `left = 1` 和普通情况完全统一
- 最后统一返回 `dummy.next`

这也是为什么这题的主流写法几乎都会带 `dummy`。

---

## 方法一：收集节点到数组后区间重连

### 思路

最直观的保底方法是：

1. 先把链表节点顺序收集到数组里
2. 把数组中 `[left - 1, right - 1]` 这一段反转
3. 再按新的节点顺序重新连接整条链表

例如：

```text
1 -> 2 -> 3 -> 4 -> 5
```

收集成数组是：

```text
[1, 2, 3, 4, 5]
```

如果 `left = 2, right = 4`，那就把中间这一段改成：

```text
[1, 4, 3, 2, 5]
```

然后重新把这些节点按顺序连起来。

---

### 代码

```python
class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int,
    ) -> Optional[ListNode]:
        if head is None or left == right:
            return head

        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        nodes[left - 1:right] = reversed(nodes[left - 1:right])

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None

        return nodes[0]
```

---

### 为什么可行

因为数组让“区间反转”这件事变得非常直观。

一旦数组中的节点顺序已经变成目标顺序，后面只要把 `next` 重新连起来，得到的链表自然就是答案。

---

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

---

### 它的不足

这个方法虽然好懂，但最大的问题是：

```text
没有真正练到链表原地反转区间的能力
```

而这题最值得掌握的，恰恰就是如何在不借数组的情况下直接改指针。

所以面试里更推荐方法二。

---

## 方法二：哑节点 + 局部套用 206 反转模板（面试主推）

### 核心思路

这题最自然的想法就是：

```text
先找到要反转的那一段，再把 206 的反转逻辑只用在这一段上
```

整个过程分成 4 步：

1. 用 `dummy` 和指针找到反转区间前驱 `before_start`
2. 记住区间起点 `start`
3. 在长度为 `right - left + 1` 的这段上，套用 `206` 的局部反转
4. 反转后把前后两段重新接好

你可以把它看成：

```text
原链表 = 前半段 + 待反转区间 + 后半段
```

我们做的事就是：

```text
只把中间那段翻过来，再把三段重新拼回去
```

---

## 为什么它和 206 几乎是同一道题

回忆一下 `206` 的核心循环：

```text
保存 next -> 反转当前指针 -> prev 前进 -> cur 前进
```

在这题里，区别只有两个：

### 1. 反转起点不同

`206` 是从 `head` 开始反转整条链表。  
而 `92` 是从区间起点 `start` 开始，只反转固定长度。

### 2. 反转结束后要“缝合”回原链表

因为这里只反转中间一段，所以反转后还要做两次连接：

- `before_start.next = prev`
- `start.next = cur`

所以这题最该记住的一句话就是：

```text
92 题本质上就是：先定位区间，再把 206 模板局部执行一遍，最后把前后接回去
```

---

## 用例子走一遍

假设：

```text
head = 1 -> 2 -> 3 -> 4 -> 5
left = 2, right = 4
```

加上哑节点后：

```text
dummy -> 1 -> 2 -> 3 -> 4 -> 5
```

### 第 1 步：找到区间前驱

`left = 2`，所以区间起点是 `2`。  
它前面的节点就是：

```text
before_start = 1
```

于是：

```text
start = before_start.next = 2
```

### 第 2 步：局部反转长度为 3 的区间

因为：

```text
right - left + 1 = 3
```

所以只反转这 3 个节点：

```text
2 -> 3 -> 4
```

按 `206` 的方式反转后，会变成：

```text
4 -> 3 -> 2
```

此时：

- `prev` 指向 `4`，也就是反转后新区间头
- `cur` 指向 `5`，也就是区间后面的第一个节点
- `start` 还指向原来的 `2`，它现在变成了区间尾

### 第 3 步：接回原链表

把前面和中间接起来：

```text
before_start.next = prev
```

得到：

```text
1 -> 4 -> 3 -> 2
```

再把中间和后面接起来：

```text
start.next = cur
```

最终得到：

```text
1 -> 4 -> 3 -> 2 -> 5
```

---

### 面试代码

```python
class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int,
    ) -> Optional[ListNode]:
        if head is None or left == right:
            return head

        dummy = ListNode(0, head)
        before_start = dummy
        for _ in range(left - 1):
            before_start = before_start.next

        start = before_start.next
        prev = None
        cur = start

        for _ in range(right - left + 1):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        start.next = cur
        before_start.next = prev
        return dummy.next
```

---

## 为什么这个方法最适合面试

如果这题你只记一种写法，就记这一种。

### 1. 和 206 衔接最顺

它不是硬记新区间技巧，而是直接复用你已经掌握的：

```text
链表反转模板
```

对于刷题和面试记忆都非常友好。

### 2. 真正练到了“局部反转”

这题的本质不只是反转，而是：

```text
在原链表中只改一段，并把它重新缝合回去
```

方法二把这个过程讲得最清楚。

### 3. 复杂度优秀

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

这就是题目最标准、最推荐现场手写的版本。

### 4. 变量语义清楚

这里的几个关键变量都特别好解释：

- `before_start`：反转区间前驱
- `start`：反转区间旧头，反转后会变尾
- `prev`：局部反转后的新区间头
- `cur`：区间后面的续接点

面试时你能把这几个变量讲顺，基本就稳了。

---

### 容易出错的地方

### 1. 忘了区间长度是 `right - left + 1`

这里不是反转到链表结束，而是：

```text
只反转固定个数的节点
```

所以循环次数必须写成：

```python
for _ in range(right - left + 1):
```

### 2. 忘了最后两次“缝合”

局部反转做完后，一定要把前后接回去：

```python
start.next = cur
before_start.next = prev
```

少任何一个，链表都会断掉。

### 3. 把 `start` 和 `before_start` 混了

- `before_start` 是区间外面的前驱节点
- `start` 是区间第一个节点

反转后：

- `before_start` 负责接新区间头
- `start` 负责接区间后半段

这两个角色不要混。

---

### 面试里怎么讲

你可以这样解释：

```text
这题可以看成 206 反转链表的区间版。我先用 dummy 节点统一 left=1 的边界情况，然后找到反转区间前驱 before_start，再把区间起点记成 start。接着我只在长度为 right-left+1 的这段链表上执行一次 206 的反转模板。反转完成后，prev 会指向新区间头，cur 会指向区间后面的续接点。最后我用 before_start.next = prev 和 start.next = cur 把前后重新接回去。这样时间复杂度 O(n)，额外空间复杂度 O(1)。
```

这就是这题最标准、也最容易讲清楚的说法。

---

## 方法三：哑节点 + 头插法区间反转（补充理解）

### 思路

这也是经典做法，而且写起来很短。

它的想法不是先完整反转那一段，而是：

```text
不断把区间里的下一个节点，抽出来插到区间最前面
```

假设当前有：

```text
pre -> curr -> nxt -> ...
```

每次都把 `nxt` 从后面拿出来，插到 `pre` 后面。

这样连续做 `right - left` 次之后，区间就反转好了。

---

## 用例子走一遍

还是：

```text
1 -> 2 -> 3 -> 4 -> 5
left = 2, right = 4
```

先找到：

- `pre = 1`
- `curr = 2`

### 第 1 次头插

把 `3` 从 `2` 后面抽出来，插到 `1` 后面：

```text
1 -> 3 -> 2 -> 4 -> 5
```

### 第 2 次头插

再把 `4` 从 `2` 后面抽出来，插到 `1` 后面：

```text
1 -> 4 -> 3 -> 2 -> 5
```

区间反转完成。

---

### 代码

```python
class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int,
    ) -> Optional[ListNode]:
        if head is None or left == right:
            return head

        dummy = ListNode(0, head)
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next

        curr = pre.next
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt

        return dummy.next
```

---

### 为什么可行

因为每次都在做一件固定的事：

```text
把区间中的下一个节点，搬到区间最前面
```

连续搬运后，区间的相对顺序就被反转了。

---

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

---

### 它适合什么时候学

它适合作为：

- 看懂官方题解里常见的头插法写法
- 练习局部指针搬运
- 对比“完整局部反转”和“逐个头插”两种思路

但如果你现在只准备记一个版本：

```text
还是优先记方法二
```

因为它和 `206` 的关系更直观，讲起来也更顺。

---

## 三种方法的关系

这题三种做法的递进关系很清楚：

- **方法一**：先把节点收集出来，再在数组里完成区间反转
- **方法二**：定位区间后，直接局部复用 `206` 反转模板，这是面试主推
- **方法三**：通过头插法逐个搬运节点完成区间反转

这题最值得抓住的一句话是：

```text
92 题不是新题型，它本质上就是“先定位区间，再局部执行一次 206 的反转模板”
```

只要这句话真正想通，方法二就会非常自然。

---

## 复杂度总结

| 方法 | 时间复杂度 | 空间复杂度 | 评价 |
| --- | --- | --- | --- |
| 方法一：收集节点到数组后区间重连 | `O(n)` | `O(n)` | 直观保底，但没练到原地反转 |
| 方法二：哑节点 + 局部套用 206 反转模板 | `O(n)` | `O(1)` | 面试主推 |
| 方法三：哑节点 + 头插法区间反转 | `O(n)` | `O(1)` | 有助于理解局部搬运，但不如方法二直观 |

---

## 总结

这题最重要的不是死记区间反转套路，而是想清楚：

```text
整条链表反转你已经会了，现在只是先把区间找出来，再把 206 的逻辑局部用一遍
```

如果你现在只准备记一个版本：

```text
就记方法二：哑节点 + 局部套用 206 反转模板
```
