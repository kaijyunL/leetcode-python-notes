# LeetCode 19. 删除链表的倒数第 N 个结点（Remove Nth Node From End of List）解析

## 题目描述

给你一个链表的头节点 `head`，以及一个整数 `n`。

题目要求你删除链表的：

```text
倒数第 n 个节点
```

并返回删除后的链表头节点。

例如：

```text
head = 1 -> 2 -> 3 -> 4 -> 5, n = 2
```

倒数第 `2` 个节点是 `4`，所以删除后结果是：

```text
1 -> 2 -> 3 -> 5
```

---

## 先理解这题在考什么

这题表面上是在“删除一个节点”，但真正考的是：

```text
怎么在只用链表顺序遍历的前提下，定位到“倒数第 n 个节点的前一个节点”
```

注意，链表删除一个节点时，我们真正需要操作的是：

```text
目标节点的前驱节点
```

因为删除动作本质是：

```python
prev.next = prev.next.next
```

所以这题最关键的不是“找到倒数第 `n` 个节点本身”，而是：

```text
找到它前面的那个节点
```

一旦这个点想清楚，这题就会顺很多。

---

## 为什么这题里 `dummy` 特别重要

这题最麻烦的边界情况是：

```text
要删除的正好是头节点
```

比如：

```text
head = 1 -> 2, n = 2
```

要删的就是 `1`。

如果没有前驱节点，删除逻辑就得单独分支处理。

所以这题里我们特别喜欢先造一个哑节点：

```text
dummy -> head
```

这样一来：

- 原来的头节点也有“前驱”了
- 删除头节点和删除中间节点的写法完全统一
- 最后统一返回 `dummy.next`

这就是为什么这题的面试主推写法几乎都会配上 `dummy`。

---

## 方法一：两次遍历统计长度

### 思路

最直观的想法是先把“倒数”改写成“正数”。

如果链表总长度是 `length`，那么：

```text
倒数第 n 个 = 正数第 length - n + 1 个
```

而我们真正需要的是它的前驱节点，也就是：

```text
正数第 length - n 个节点
```

所以做法就是：

1. 第一遍遍历，算出链表长度 `length`
2. 第二遍从 `dummy` 出发，走 `length - n` 步
3. 此时停下的位置就是待删除节点的前驱
4. 执行删除

---

### 代码

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        prev = dummy
        for _ in range(length - n):
            prev = prev.next

        prev.next = prev.next.next
        return dummy.next
```

---

### 为什么可行

因为一旦链表长度确定下来，“倒数第 `n` 个”就不再抽象了，它只是一个普通的位置换算问题。

这个方法很适合建立第一直觉。

---

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

虽然走了两遍，但总步数仍然是线性的。

---

### 它的不足

这个方法的问题不在于不能做，而在于：

```text
没有直接用到这题最核心的“固定间距双指针”思想
```

所以如果面试官继续追问“一趟遍历能不能做”，你还是要回到方法二。

---

## 方法二：哑节点 + 快慢指针固定间距（面试主推）

### 核心思路

这题最经典的做法是让两个指针之间保持固定距离。

做法是：

1. `fast` 和 `slow` 都从 `dummy` 出发
2. 先让 `fast` 单独走 `n` 步
3. 此时 `fast` 和 `slow` 之间已经拉开了固定间距
4. 然后让它们一起往前走，直到 `fast.next` 为 `None`
5. 此时 `slow` 正好停在目标节点的前驱位置

这题最值得记的一句话就是：

```text
让快指针先走 n 步，再一起走；当快指针到尾部时，慢指针刚好停在倒数第 n 个节点的前一个位置
```

---

## 为什么这个固定间距是对的

假设：

```text
head = 1 -> 2 -> 3 -> 4 -> 5, n = 2
```

开始时：

```text
dummy -> 1 -> 2 -> 3 -> 4 -> 5
fast = dummy
slow = dummy
```

先让 `fast` 走 `2` 步后：

```text
fast 在 2
slow 还在 dummy
```

然后一起走：

- `fast` 到 `3`，`slow` 到 `1`
- `fast` 到 `4`，`slow` 到 `2`
- `fast` 到 `5`，`slow` 到 `3`

这时 `fast.next` 已经是 `None`，说明 `fast` 到尾了。

而 `slow` 正好停在 `3`，它的下一个节点就是 `4`：

```text
3 -> 4 -> 5
```

所以删掉 `4` 正好符合题意。

---

### 面试代码

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
```

---

## 为什么这个方法最适合面试

如果这题你只记一种写法，就记这一种。

### 1. 一趟定位，思路最巧

它不用先数长度，而是直接通过：

```text
制造固定间距
```

把“倒数第 `n` 个”这个条件变成了可操作的同步移动问题。

### 2. `dummy` 让边界统一

无论删的是：

- 头节点
- 中间节点
- 尾节点

写法都一样，不需要额外特殊判断。

### 3. 是很多链表题的通用母题

这题不只是单独一道题，它会反复训练你：

```text
双指针维持固定距离
```

这个思路在链表、数组、滑窗题里都非常常见。

### 4. 复杂度最优

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

这就是题目最标准、最推荐现场手写的版本。

---

### 容易出错的地方

### 1. 忘了从 `dummy` 出发

如果直接从 `head` 出发，删除头节点时会很别扭。

而从：

```text
dummy -> head
```

开始，逻辑会统一很多。

### 2. 快指针先走的步数和循环条件不配套

我这里采用的是：

```python
for _ in range(n):
    fast = fast.next

while fast.next:
    fast = fast.next
    slow = slow.next
```

这套搭配的结果是：

```text
slow 最终停在待删除节点的前驱
```

如果你改成别的写法，比如让 `fast` 先走 `n + 1` 步，那后面的循环条件也要一起改。

### 3. 删除动作写错

删除不是：

```python
slow = slow.next
```

而是：

```python
slow.next = slow.next.next
```

因为我们要改的是链表连接关系。

---

### 面试里怎么讲

你可以这样解释：

```text
我会先加一个 dummy 节点，让删除头节点和删除普通节点的逻辑统一。然后用两个指针都从 dummy 出发，让 fast 先走 n 步，和 slow 拉开固定距离。接着让它们一起移动，直到 fast 到达尾节点。由于间距一直保持不变，这时 slow 就正好停在倒数第 n 个节点的前一个位置。我再执行 slow.next = slow.next.next 完成删除。这样时间复杂度是 O(n)，额外空间复杂度是 O(1)。
```

这就是这题最标准的讲法。

---

## 方法三：不使用 `dummy` 的双指针变体

### 思路

这也是双指针，只不过不再加哑节点。

做法是：

1. `fast` 和 `slow` 都从 `head` 出发
2. 先让 `fast` 走 `n` 步
3. 如果这时 `fast` 已经是 `None`，说明要删除的正好是头节点
4. 否则继续同步移动，直到 `fast.next` 为 `None`
5. 此时 `slow` 停在目标节点前驱，执行删除

---

### 代码

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        fast = head
        slow = head

        for _ in range(n):
            fast = fast.next

        if fast is None:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
```

---

### 为什么可行

本质上它和方法二是同一个思路，仍然是在用：

```text
固定间距双指针
```

只是因为少了 `dummy`，所以“删头节点”这个边界必须自己手动补一个判断。

---

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

---

### 它适合什么时候学

它适合作为：

- 帮你真正理解 `dummy` 到底帮你省掉了什么
- 看懂别人题解里的无哑节点写法
- 对比“统一逻辑”和“少一个节点辅助”之间的取舍

但如果你现在只准备记一个版本：

```text
还是优先记方法二
```

---

## 三种方法的关系

这题三种做法的递进关系很清楚：

- **方法一**：先数长度，再把倒数位置换成正数位置
- **方法二**：用 `dummy` + 固定间距双指针一次定位，这是面试主推
- **方法三**：去掉 `dummy`，保留核心双指针思想，但要自己处理删头节点

这题最值得抓住的一句话是：

```text
删除倒数第 n 个节点，真正要找的是它前面的那个节点；最优做法是让两个指针保持固定距离
```

只要这句话真正想通，方法二就会很自然。

---

## 复杂度总结

| 方法 | 时间复杂度 | 空间复杂度 | 评价 |
| --- | --- | --- | --- |
| 方法一：两次遍历统计长度 | `O(n)` | `O(1)` | 最直观，适合建立第一感觉 |
| 方法二：哑节点 + 快慢指针固定间距 | `O(n)` | `O(1)` | 面试主推 |
| 方法三：不使用 `dummy` 的双指针变体 | `O(n)` | `O(1)` | 有助于理解 `dummy` 的作用 |

---

## 总结

这题最重要的不是背公式，而是想清楚两件事：

```text
1. 删除节点时，真正需要找到的是前驱节点
2. “倒数第 n 个”最自然的做法，是让两个指针保持固定间距
```

如果你现在只准备记一个版本：

```text
就记方法二：哑节点 + 快慢指针固定间距
```
