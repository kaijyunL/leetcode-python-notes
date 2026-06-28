# LeetCode 24. 两两交换链表中的节点（Swap Nodes in Pairs）解析

## 题目描述

给你一个链表的头节点 `head`，请你把其中相邻的两个节点两两交换，并返回交换后的链表头节点。

题目还特别强调了一点：

```text
不能修改节点内部的值，只能真正交换节点
```

例如：

```text
1 -> 2 -> 3 -> 4
```

交换后应该得到：

```text
2 -> 1 -> 4 -> 3
```

注意，如果链表长度是奇数，最后那个单独剩下的节点保持不动。

例如：

```text
1 -> 2 -> 3
```

交换后是：

```text
2 -> 1 -> 3
```

---

## 先理解这题在考什么

这题表面上是在“交换相邻节点”，但真正考的是：

```text
你会不会在链表里安全地改一小段指针关系
```

它本质上是在训练一种非常重要的能力：

- 找到当前要处理的一小段链表
- 只改这一小段的连接关系
- 再把它重新接回主链

所以这题和 `206` 反转链表其实是同一类指针题：

```text
本质都是在改 next 指针的指向
```

只不过 `206` 是整段反转，`24` 是每两个节点交换一次。

---

## 为什么这题里 `dummy` 特别好用

这题最麻烦的地方是：

```text
第一对节点交换以后，链表头节点会变
```

比如：

```text
1 -> 2 -> 3 -> 4
```

交换第一对以后，新头节点会变成 `2`，不是原来的 `1`。

如果没有一个统一的前驱节点，代码就会不断碰到“头节点要不要单独处理”的问题。

所以这题里加一个：

```text
dummy -> head
```

会非常舒服，因为这样：

- 第一对节点也有前驱了
- 中间各对节点的写法和第一对完全统一
- 最后直接返回 `dummy.next`

这也是为什么面试里最稳的版本几乎都会带 `dummy`。

---

## 方法一：收集节点到数组后两两重连

### 思路

最直观、同时又符合题意的保底做法是：

1. 先把所有链表节点按顺序收集到数组里
2. 每次按两个一组交换数组中的相邻节点位置
3. 再按照新顺序把这些节点重新连起来

例如：

```text
1 -> 2 -> 3 -> 4
```

收集成数组后是：

```text
[1, 2, 3, 4]
```

两两交换位置后变成：

```text
[2, 1, 4, 3]
```

再把这些节点重新串起来即可。

---

### 代码

```python
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        for i in range(0, len(nodes) - 1, 2):
            nodes[i], nodes[i + 1] = nodes[i + 1], nodes[i]

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None

        return nodes[0]
```

---

### 为什么可行

因为数组让“交换相邻两个位置”变得非常直接。

一旦数组中的节点顺序已经变成目标顺序，后面只要按这个顺序把 `next` 重新连起来，得到的链表自然就是答案。

---

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

---

### 它的不足

这个方法能做，但最大问题是：

```text
它没有直接训练链表原地改指针的能力
```

而这题真正最值得练的，就是如何在链表上原地交换一对节点。

所以更推荐的方法是方法二。

---

## 方法二：哑节点 + 迭代指针重连（面试主推）

### 核心思路

每次只处理当前的一对节点。

假设当前局部结构是：

```text
prev -> first -> second -> next_pair
```

我们想把它改成：

```text
prev -> second -> first -> next_pair
```

这其实只需要改 3 条指针：

1. `first.next = second.next`
2. `second.next = first`
3. `prev.next = second`

改完以后，这一对就交换完成了。

然后让 `prev` 移动到交换后的 `first`，继续处理下一对。

这题最关键的画面就是：

```text
prev -> first -> second -> next_pair
            ↓
prev -> second -> first -> next_pair
```

---

## 为什么这个思路能想到

因为题目每次只要求交换：

```text
相邻两个节点
```

这说明你不需要整段反转，也不需要一次看很远。

你只要每次盯住一小段固定结构：

```text
前驱 + 两个待交换节点 + 下一段起点
```

把这 4 个位置的关系改对就行。

这和 `206` 的共同点就在于：

```text
核心不是背结果，而是想清楚 next 指针应该重新指向谁
```

---

## 用例子走一遍

假设链表是：

```text
1 -> 2 -> 3 -> 4
```

加上哑节点以后：

```text
dummy -> 1 -> 2 -> 3 -> 4
prev = dummy
```

### 第 1 轮

当前这对是：

```text
prev -> 1 -> 2 -> 3
```

也就是：

- `first = 1`
- `second = 2`

按顺序改指针：

1. `first.next = second.next`，也就是 `1 -> 3`
2. `second.next = first`，也就是 `2 -> 1`
3. `prev.next = second`，也就是 `dummy -> 2`

于是整条链表变成：

```text
dummy -> 2 -> 1 -> 3 -> 4
```

然后把 `prev` 移到 `1`。

### 第 2 轮

现在处理：

```text
1 -> 3 -> 4
```

也就是：

- `first = 3`
- `second = 4`

同样三步改完后，得到：

```text
dummy -> 2 -> 1 -> 4 -> 3
```

最后返回 `dummy.next`，答案就是：

```text
2 -> 1 -> 4 -> 3
```

---

### 面试代码

```python
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first

        return dummy.next
```

---

## 为什么这个方法最适合面试

如果这题你只记一种写法，就记这一种。

### 1. 完全符合题意

它没有交换节点值，而是真正交换了节点位置。

### 2. `dummy` 让边界统一

不管是第一对节点，还是中间某一对，处理方式都一样。

### 3. 真正练到了链表指针能力

这题最重要的收获不是“会做一道题”，而是会处理这种局部重连结构：

```text
prev -> a -> b -> next
```

这是后面很多链表题都会继续用到的能力。

### 4. 复杂度最好

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

这是这题最标准、最推荐现场手写的版本。

---

### 容易出错的地方

### 1. 改指针顺序写乱

这题最怕的是还没把后续节点记住，就先把链断掉。

所以最好固定成同一套写法，不要临场乱改顺序。

### 2. `prev` 没移动到正确位置

一对节点交换完成后：

```text
second 在前，first 在后
```

所以下一轮的前驱应该更新成：

```python
prev = first
```

不是 `second`。

### 3. 循环条件少写了一个 `next`

必须保证当前至少还有两个节点才能交换，所以要写：

```python
while prev.next and prev.next.next:
```

如果只判断一个节点是否存在，可能就会在取第二个节点时出错。

---

### 面试里怎么讲

你可以这样解释：

```text
我会先加一个 dummy 节点，把头节点交换和普通位置交换统一处理。然后每次关注一小段固定结构 prev -> first -> second -> next_pair，把它改成 prev -> second -> first -> next_pair。具体只需要三步指针重连：first.next 指向后续节点，second.next 指回 first，prev.next 指向 second。做完后让 prev 移到 first，继续处理下一对。这样每个节点只访问常数次，时间复杂度 O(n)，额外空间复杂度 O(1)。
```

这就是这题最标准的讲法。

---

## 方法三：递归两两交换（补充理解）

### 思路

递归的想法是：

```text
先交换当前这一对，再递归处理后面的链表
```

假设当前是：

```text
head -> second -> rest
```

那么交换后这一对应该变成：

```text
second -> head
```

而 `head` 后面接的，不是原来的 `rest`，而是：

```text
递归处理 rest 之后得到的新头
```

所以写法就会很自然：

1. 先记住第二个节点 `second`
2. 递归处理 `second.next` 后面的部分
3. 把递归结果接到 `head.next`
4. 再让 `second.next = head`
5. 返回 `second`

---

### 代码

```python
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head
        return second
```

---

### 为什么可行

因为每一层递归都在做同一件事：

```text
交换当前这两个节点，然后把剩余部分交给下一层
```

问题结构完全一致，所以可以自然递归下去。

---

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

这里的额外空间来自递归调用栈。

---

### 它适合什么时候学

它适合作为：

- 练习链表递归写法
- 理解“当前一对 + 剩余链表”这种拆分方式
- 帮你从递归角度理解迭代版本在做什么

但如果你现在只准备记一个版本：

```text
还是优先记方法二
```

---

## 三种方法的关系

这题三种做法的递进关系很清楚：

- **方法一**：先把节点收集出来，再按目标顺序重连
- **方法二**：真正原地处理每一对节点，这是面试主推
- **方法三**：把“交换当前对 + 处理后续”写成递归表达

这题最值得抓住的一句话是：

```text
每次只看一小段 prev -> first -> second -> next_pair，把它改成 prev -> second -> first -> next_pair
```

只要这句话你能讲顺，这题就基本掌握了。

---

## 复杂度总结

| 方法 | 时间复杂度 | 空间复杂度 | 评价 |
| --- | --- | --- | --- |
| 方法一：收集节点到数组后两两重连 | `O(n)` | `O(n)` | 直观保底，但没练到原地改指针 |
| 方法二：哑节点 + 迭代指针重连 | `O(n)` | `O(1)` | 面试主推 |
| 方法三：递归两两交换 | `O(n)` | `O(n)` | 有助于理解，但现场不如迭代稳 |

---

## 总结

这题最重要的不是记住“三步交换公式”，而是想清楚：

```text
链表交换节点，本质上就是把一小段局部结构重新接好
```

如果你现在只准备记一个版本：

```text
就记方法二：哑节点 + 迭代指针重连
```
