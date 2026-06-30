# LeetCode 148. 排序链表（Sort List）解析

## 题目描述

给你一个链表的头节点 `head`，请你把这条链表按升序排好，并返回排序后的头节点。

例如：

```text
4 -> 2 -> 1 -> 3
```

排序后变成：

```text
1 -> 2 -> 3 -> 4
```

再比如：

```text
-1 -> 5 -> 3 -> 4 -> 0
```

排序后变成：

```text
-1 -> 0 -> 3 -> 4 -> 5
```

这题的关键不只是“把链表排好”，而是要尽量做到：

```text
时间复杂度 O(n log n)
```

而且题目还会进一步追问：

```text
能不能做到常数级额外空间
```

所以这题不是普通排序题，而是：

```text
链表上的归并排序核心题
```

---

## 先理解这题到底在考什么

很多人一看到“排序链表”，会本能想到：

- 把值拿出来放进数组
- 数组排序
- 再写回链表

这个方法当然能做对，但它没有真正练到链表排序最核心的能力。

`148` 真正想考的是：

```text
当数据结构是链表时，怎样利用链表“容易拆分、容易合并”的特点，把排序做到 O(n log n)
```

所以这题真正的主线不是“借数组”，而是：

```text
分成两半 -> 分别排好 -> 再把两条有序链表合并起来
```

这就是归并排序。

---

## 为什么链表特别适合归并排序

这是这题最该想通的一点。

数组做归并排序时，虽然也很好理解，但常常需要额外数组来辅助合并。

而链表不一样。

对于链表来说：

### 1. 拆成两半很自然

你只需要用快慢指针找到中点，再把中点前后断开，就能得到两条子链表。

### 2. 合并两条有序链表也很自然

这其实就是 `21` 题：

```text
每次比较两条链表当前头节点，谁小就先接谁
```

### 3. 不需要像数组那样搬动元素

链表排序本质上是：

```text
调整节点之间的 next 指针
```

而不是把大量元素搬来搬去。

所以对链表来说，最适合的高效排序方法通常就是：

```text
归并排序
```

这也是为什么：

- `147`：链表插入排序，作为排序入门
- `148`：链表归并排序，作为真正高效排序主线

---

## 这题和 `147`、`21` 的关系

这题非常适合和前两题一起理解。

### 和 `147` 的关系

`147` 练的是：

```text
维护有序部分，把当前节点插回正确位置
```

那是链表排序的入门过程题。

但如果题目追求真正高效的排序复杂度，主线就会变成 `148`：

```text
归并排序链表，做到 O(n log n)
```

所以可以这样记：

- **`147`**：练链表插入排序思想
- **`148`**：练链表高效排序主线

### 和 `21` 的关系

`148` 的“治”其实就是 `21`：

```text
把两条已经有序的链表重新合成一条更长的有序链表
```

所以如果你 `21` 很熟，`148` 的 merge 部分会非常顺。

---

## 方法一：收集值后排序再覆盖回链表

### 思路

最直观的保底方法是：

1. 遍历链表，把所有值收集到数组
2. 对数组排序
3. 再遍历原链表，把排序后的值依次写回去

例如：

```text
4 -> 2 -> 1 -> 3
```

先收集出：

```text
[4, 2, 1, 3]
```

排序后：

```text
[1, 2, 3, 4]
```

再覆盖回原链表即可。

---

### 代码

```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        cur = head

        while cur:
            values.append(cur.val)
            cur = cur.next

        values.sort()

        cur = head
        for value in values:
            cur.val = value
            cur = cur.next

        return head
```

---

### 为什么可行

因为数组排序后，值的升序关系已经正确了。

把这些值重新写回链表，最终链表的值序自然也就是升序的。

---

### 复杂度

- 时间复杂度：`O(n log n)`
- 空间复杂度：`O(n)`

---

### 它的不足

这个方法只是保底能做，但不是真正值得主记的版本。

因为：

### 1. 没有真正练到链表排序

它本质上还是在借助数组排序。

### 2. 没满足常数空间方向

额外数组要用 `O(n)` 空间。

### 3. 没抓住这题真正价值

这题真正值得练的是：

```text
链表如何通过“拆分 + 合并”完成高效排序
```

所以主线还是方法二、方法三。

---

## 方法二：自顶向下归并排序（面试主推）

### 核心思路

这题最标准、最值得先掌握的版本，就是自顶向下归并排序。

整体过程就三步：

1. 用快慢指针把链表拆成左右两半
2. 递归地把左右两半分别排好
3. 把两条有序链表合并起来

也就是：

```text
大问题拆成两个更小的“排序链表”问题，最后再 merge
```

这就是典型分治。

---

## 为什么这个思路很自然

因为“排序一条链表”这件事，天然可以转化成：

```text
如果我已经能把左半边排好，也能把右半边排好，那整个问题就只剩下“合并两个有序链表”
```

而“合并两个有序链表”你其实已经在 `21` 里做过了。

所以 `148` 最核心的一句话是：

```text
148 题 = 找中点拆分 + 递归排序 + 21 题合并有序链表
```

这句话一旦想通，方法二就会很顺。

---

## 用例子走一遍

假设：

```text
4 -> 2 -> 1 -> 3
```

### 第 1 层拆分

先拆成两半：

```text
4 -> 2
1 -> 3
```

### 第 2 层继续拆分

左边继续拆：

```text
4
2
```

右边继续拆：

```text
1
3
```

这时每条链表长度都是 `1`，天然有序。

### 开始合并

先合并左边：

```text
4 和 2  ->  2 -> 4
```

再合并右边：

```text
1 和 3  ->  1 -> 3
```

最后合并：

```text
2 -> 4
1 -> 3
```

得到：

```text
1 -> 2 -> 3 -> 4
```

这就是完整的归并排序过程。

---

### 面试代码

```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def merge(
        self,
        left: Optional[ListNode],
        right: Optional[ListNode],
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        tail.next = left if left else right
        return dummy.next
```

---

### 为什么可行

因为它满足归并排序的不变式：

```text
只要左右两半已经有序，merge 以后整段就有序
```

而递归会一直把链表拆到长度为 `0` 或 `1`，这些子问题天然有序。

于是从下往上每一层合并都正确，最终整条链表就会有序。

---

### 复杂度

- 时间复杂度：`O(n log n)`
- 空间复杂度：`O(log n)`

这里的空间复杂度主要来自递归调用栈。

---

### 为什么它最适合先记

如果这题你先只准备记一种写法，我建议先记方法二。

### 1. 它最能体现这题本质

这题的核心不是“怎么写迭代细节”，而是：

```text
归并排序为什么适合链表
```

方法二把这条主线讲得最清楚。

### 2. 它最容易和 `21`、`147` 串起来

- 和 `147` 对比：为什么 `148` 更高效
- 和 `21` 连接：merge 这一步怎么做

知识结构非常完整。

### 3. 现场表达最自然

你可以很顺地讲出：

```text
我先找中点拆成两半，分别递归排序，再把两条有序链表合并
```

这个叙述非常清楚。

---

### 容易出错的地方

### 1. 找到中点后忘了断开

也就是忘了：

```python
slow.next = None
```

如果不断开，左右两半其实还是连在一起，递归会出问题。

### 2. 中点位置没选好

这里常见写法是：

```python
slow = head
fast = head.next
```

这样偶数长度时，`slow` 会停在左中点，方便用：

```python
mid = slow.next
slow.next = None
```

把链表稳定拆成左右两半。

### 3. merge 后忘了把剩余部分接上

循环结束后，左右两边最多只剩一边还有节点。

一定别忘了：

```python
tail.next = left if left else right
```

---

## 方法三：自底向上归并排序（严格满足常数额外空间）

### 核心思路

如果你想进一步满足：

```text
不使用递归，尽量做到真正常数级额外空间
```

那就可以写成自底向上的归并排序。

它和方法二本质完全一样，仍然是在做 merge sort；区别只是：

- **方法二**：递归地先拆到最小，再往上合并
- **方法三**：直接从长度为 `1` 的有序段开始，逐轮向上合并

步长变化是：

```text
1 -> 2 -> 4 -> 8 -> ...
```

也就是说：

### 第 1 轮

每次合并两个长度为 `1` 的有序段，得到长度为 `2` 的有序段。

### 第 2 轮

每次合并两个长度为 `2` 的有序段，得到长度为 `4` 的有序段。

### 第 3 轮

每次合并两个长度为 `4` 的有序段……

直到步长覆盖整条链表。

---

## 为什么它更难写

因为方法三虽然没有递归，但链表操作细节更多：

- 你要手动把当前链表切成 `left` 和 `right`
- 你要记住下一段从哪里继续处理
- 你要在每次 merge 后把结果重新接回总链表
- 你还要拿到 merge 后这段链表的尾巴，方便继续拼接

所以它的难点不在思路，而在：

```text
链表切段和回接细节很多
```

---

### 面试代码

```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        dummy = ListNode(0, head)
        step = 1

        while step < length:
            prev = dummy
            cur = dummy.next

            while cur:
                left = cur
                right = self.split(left, step)
                cur = self.split(right, step)
                merged_head, merged_tail = self.merge(left, right)
                prev.next = merged_head
                prev = merged_tail

            step *= 2

        return dummy.next

    def split(self, head: Optional[ListNode], size: int) -> Optional[ListNode]:
        if head is None:
            return None

        for _ in range(size - 1):
            if head.next is None:
                break
            head = head.next

        second = head.next
        head.next = None
        return second

    def merge(
        self,
        left: Optional[ListNode],
        right: Optional[ListNode],
    ) -> tuple[Optional[ListNode], Optional[ListNode]]:
        dummy = ListNode(0)
        tail = dummy

        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        tail.next = left if left else right
        while tail.next:
            tail = tail.next

        return dummy.next, tail
```

---

### 为什么可行

因为每一轮开始时，我们都能保证：

```text
当前链表由很多个长度为 step 的有序段组成
```

那这一轮把相邻两个长度为 `step` 的有序段 merge 之后，
就能得到很多个长度为 `2 * step` 的有序段。

步长不断翻倍，最终整条链表就会变成一个完整有序段。

---

### 复杂度

- 时间复杂度：`O(n log n)`
- 空间复杂度：`O(1)`

这里不算递归栈，因为它根本没有递归。

---

### 它适合什么时候记

它更适合在你已经真正理解方法二以后，再往前补。

因为方法三的难度不是算法思想更高级，而是：

```text
同样的归并排序思想，被你用纯链表迭代细节手写出来了
```

如果你现在只准备记一个最稳的版本：

```text
还是优先记方法二：自顶向下归并排序
```

如果面试官继续追问“能不能做到真正常数额外空间”，再补方法三会很漂亮。

---

## 三种方法的关系

这题三种做法的递进关系很清楚：

- **方法一**：先借数组把值排好，再写回链表，属于保底做法
- **方法二**：真正的链表归并排序主线，最值得先掌握，也是面试主推
- **方法三**：把同样的归并排序写成迭代版，严格满足常数额外空间方向

这题最值得抓住的一句话是：

```text
148 题的本质，不是“排序链表”四个字，而是“把排序问题拆成：找中点拆分 + 递归/迭代归并 + 合并两个有序链表”
```

一旦这句话真正想通，方法二和方法三都会自然很多。

---

## 复杂度总结

| 方法 | 时间复杂度 | 空间复杂度 | 评价 |
| --- | --- | --- | --- |
| 方法一：收集值后排序再覆盖回链表 | `O(n log n)` | `O(n)` | 最直观，但没有真正练到链表排序 |
| 方法二：自顶向下归并排序 | `O(n log n)` | `O(log n)` | 面试主推，最适合理解和手写 |
| 方法三：自底向上归并排序 | `O(n log n)` | `O(1)` | 进阶最优，严格满足常数空间方向 |

---

## 总结

这题最重要的，不是死记某份代码，而是先建立这个理解：

```text
链表最适合的高效排序方法通常是归并排序，因为链表很容易拆成两半，也很容易把两条有序链表重新合并
```

如果你现在只准备记一个版本：

```text
就记方法二：自顶向下归并排序
```

如果你已经完全掌握方法二，再把：

```text
方法三：自底向上归并排序
```

作为“常数额外空间进阶版”补上，这题就算真正吃透了。
