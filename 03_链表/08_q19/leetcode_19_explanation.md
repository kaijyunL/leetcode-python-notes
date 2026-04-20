LeetCode 第19题 **“删除链表的倒数第 N 个结点” (Remove Nth Node From End of List)** 是一道非常经典的链表操作题。

要解决链表中的问题，有一个非常常用的技巧叫作 **哑节点（Dummy Node）**。在我们开始每种解法之前，先理解它很有帮助。
> **💡 哑节点（Dummy Node）有什么用？**
> 如果我们要删除的是链表的**头节点**，处理起来往往会有很多特殊的边界条件。为了避免这些麻烦，我们可以在真正的头节点之前人为地添加一个“哑节点”。这样一来，即使要删除的是头节点，它也有了“前驱节点”，所有节点的删除逻辑就统一了。最后只需要返回 `dummy.next` 即可。

下面我将以 Python 为例，按照**从基础暴力到最优解法**的顺序，一步步带你解析。

---

### 解法一：两次遍历（基础计算长度法）

这是最直观、也是最容易想到的办法。所谓“倒数第 `n` 个”，如果能够知道链表的总长度 `L`，它其实就是“正数第 `L - n + 1` 个”。
既然我们要删除它，我们就需要找到它**前面的那个节点**，也就是“正数第 `L - n` 个”节点。

#### 步骤说明：
1. 第一次遍历：从头走到尾，统计链表的总长度 `length`。
2. 第二次遍历：从哑节点开始走 `length - n` 步，找到要删除节点的前一个节点。
3. 执行删除操作：把前一个节点的 `next` 指向它的下下一个节点。

#### 代码实现：

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 创建一个哑节点，并将其 next 指向头节点
        dummy = ListNode(0, head)
        
        # 第一次遍历：统计链表长度
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
            
        # 第二次遍历：找到要删除且节点的前驱节点
        # 它在正数第 length - n 个位置（由于有 dummy，所以刚好走 length - n 步）
        current = dummy
        for _ in range(length - n):
            current = current.next
            
        # 执行删除操作：跨过当前节点的 next 节点
        current.next = current.next.next
        
        # dummy.next 指向的始终是真正的（可能被更新了的）头节点
        return dummy.next
```
**复杂度分析：**
- 时间复杂度：$O(L)$，其中 $L$ 是链表长度。走了两趟。
- 空间复杂度：$O(1)$，只用了几个指针变量。

---

### 解法二：使用栈（空间换时间）

有时候我们会被要求不用获取链表长度去得到倒数第 `N` 个节点。我们可以利用“栈”先进后出的特性，完美契合“倒数”这个概念。

#### 步骤说明：
1. 从哑节点开始遍历链表，依次将遇到的每一个节点压入栈（Stack）中。
2. 链表遍历完成后，我们将栈顶元素连续弹出 `n` 次。
3. 弹出 `n` 次后，现在**栈顶的节点**就是我们要删除节点的前一个节点（前驱节点）。
4. 执行删除操作。

#### 代码实现：

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        stack = []
        
        # 第一次遍历：将包括 dummy 在内的所有节点压入栈中
        current = dummy
        while current:
            stack.append(current)
            current = current.next
            
        # 弹出栈顶的 n 个元素，这些是倒数的那 n 个节点
        for _ in range(n):
            stack.pop()
            
        # 此时栈顶剩下的节点，就是要删除节点的前驱节点
        prev = stack[-1]
        
        # 执行删除
        prev.next = prev.next.next
        
        return dummy.next
```
**复杂度分析：**
- 时间复杂度：$O(L)$，遍历一遍压栈，遍历一遍弹栈。
- 空间复杂度：$O(L)$，因为借用了一个栈，把链表所有的节点都存进去了。

---

### 解法三：双指针 / 快慢指针（一趟遍历最优解）

这是这道题面试时面试官最想看到的优雅解法！
在不知道链表长度的情况下，我们怎么只能遍历一次就找到倒数第 `n` 个节点呢？答案是造一个“尺子”或者说保持一段**固定距离**。

#### 步骤说明：
1. 采用两个指针 `fast` 和 `slow`，一开始都指向哑节点。
2. 让 `fast` 指针先单独往前走 `n` 步。此时 `fast` 和 `slow` 之间相差了 `n` 步。
3. 然后同时移动 `fast` 和 `slow`（每次各走一步），直到 `fast` 走到了链表的最后一个节点。
4. 因为 `fast` 和 `slow` 之间始终隔着 `n` 步的距离，当 `fast` 到底时，`slow` 刚好停在**倒数第 `n` 个节点的前面一个节点**。
5. 此时修改 `slow.next` 执行删除即可。

#### 代码实现：

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        
        # 初始化快慢指针
        fast = dummy
        slow = dummy
        
        # 1. 让快指针先走 n 步
        for _ in range(n):
            fast = fast.next
            
        # 2. 快慢指针一起走，直到快指针的下一个是没有节点（到达末尾）
        # 这样能保证 slow 刚好停在要删除的节点的前一个！
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        # 3. 此时 slow 停在了要删除节点的前驱，执行删除
        slow.next = slow.next.next
        
        return dummy.next
```
**复杂度分析：**
- 时间复杂度：$O(L)$。这次只有 `fast` 指针完整地遍历了一次链表（One Pass），效率最高。
- 空间复杂度：$O(1)$。只创建了两个指针 `fast` 和 `slow`。

---

### 进阶思考：可以不设置 Dummy 节点吗？

答案是：**可以**，但是代码会多出一个“特殊情况处理”。

如果不使用哑节点，我们需要直接从 `head` 开始操作。这时候会面临一个尴尬的问题：**我们要删除倒数第 N 个，但它的前面可能没有任何节点（也就是我们要删除的是头节点自己）。**

#### 不带 Dummy 的逻辑：
1. `fast` 和 `slow` 都从 `head` 出发。
2. `fast` 先走 `n` 步。
3. **关键判断**：如果 `fast` 走完 `n` 步后已经变成了 `None`，说明链表的总长度正好是 `n`。我们要删除的倒数第 `n` 个就是第一个节点（头节点）。此时直接返回 `head.next` 即可。
4. 如果 `fast` 没变空，我们就同步移动 `fast` 和 `slow`，直到 `fast.next` 为空。
5. 此时 `slow` 停在目标节点的前驱，执行删除。

#### 代码实现：
```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        
        # 1. 快指针先走 n 步
        for _ in range(n):
            fast = fast.next
            
        # 2. 如果 fast 走空了，说明要删的是头节点
        if not fast:
            return head.next
            
        # 3. 正常同步走
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        # 4. 删除
        slow.next = slow.next.next
        
        return head
```

---

### 总结
1. **第一次遍历法**是基础，锻炼把题目翻译成最朴素代码逻辑的能力。
2. **栈解法**属于发散性思维，巧妙利用了数据结构特性来解决抽象问题。
3. **快慢指针**是链表类问题（特别是寻找中间节点、环形链表判断等）的**终极杀手锏**。
4. **哑节点（Dummy Node）**的作用是**统一逻辑**。如果不加它，删除中间和尾部节点的逻辑是一样的，但删除头部节点需要单独写一个 `if` 判断。为了代码的简洁性，在处理链表删除/修改头部的题目时，一般都优先考虑加一个哑节点。
