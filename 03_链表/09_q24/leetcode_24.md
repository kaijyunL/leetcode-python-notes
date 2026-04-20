# LeetCode 24 - 两两交换链表中的节点

## 题目描述

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。  
你**必须**在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

**示例 1：**
```
输入：head = [1,2,3,4]
输出：[2,1,4,3]
```

**示例 2：**
```
输入：head = []
输出：[]
```

**示例 3：**
```
输入：head = [1]
输出：[1]
```

**约束条件：**
- 链表中节点的数目在范围 `[0, 100]` 内
- `0 <= Node.val <= 100`

---

## 🧠 解题思路总览

| 方法 | 思路 | 时间复杂度 | 空间复杂度 |
|------|------|-----------|-----------|
| 方法一：值交换（伪暴力） | 直接交换相邻节点的值 | O(n) | O(1) |
| 方法二：迭代（指针重连） | 用哑节点，迭代重连每对节点 | O(n) | O(1) |
| 方法三：递归 | 递归处理每一对节点 | O(n) | O(n) 栈空间 |

> **注意**：题目要求只能交换节点，不能修改节点值。因此方法一在严格意义上不符合题意，但帮助理解问题。

---

## 方法一：值交换（伪暴力）

### 💡 思路

最直观的想法：不改变指针结构，直接把相邻两个节点的 **值** 互换。  
虽然违反了题目要求（实际面试/提交中不可用），但有助于理解题意。

### 图解

```
原始链表：  1 → 2 → 3 → 4
交换值后：  2 → 1 → 4 → 3
```

节点结构没变，只是内部 `val` 值换了。

### 代码

```python
def swapPairs_v1(head):
    cur = head
    while cur and cur.next:
        # 直接交换相邻两个节点的值
        cur.val, cur.next.val = cur.next.val, cur.val
        # 跳过已处理的两个节点，移到下一对
        cur = cur.next.next
    return head
```

### ⚠️ 缺点
- **违反题目规则**：题目明确要求不能修改节点内部的值
- 仅用于理解题意，不可在实战中使用

---

## 方法二：迭代（哑节点 + 指针重连）⭐ 推荐

### 💡 思路

用一个**哑节点（dummy node）** 作为链表头部的前驱，然后用 `prev` 指针追踪每对节点的前驱，逐对进行指针重连。

每次迭代处理 `(first, second)` 这一对节点时：
1. 让 `first.next` 指向 `second.next`（接好出口）
2. 让 `second.next` 指向 `first`（内部交换）
3. 让 `prev.next` 指向 `second`（连回主链）
4. `prev` 移动到 `first`（交换后 first 在后面），继续下一对

### 图解（以 1→2→3→4 为例）

```
初始状态（哑节点 dummy = 0）：
dummy → 1 → 2 → 3 → 4
  ↑
 prev

第一次迭代（处理 1, 2）：
  first = 1, second = 2

  步骤1: first.next = second.next(3)
  步骤2: second.next = first(1)
  步骤3: prev.next = second(2)

  结果: dummy → 2 → 1 → 3 → 4
                     ↑
                    prev

第二次迭代（处理 3, 4）：
  first = 3, second = 4

  结果: dummy → 2 → 1 → 4 → 3
```

### 代码

```python
def swapPairs_v2(head):
    # 创建哑节点，简化边界处理（无需对头节点特殊处理）
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy  # prev 始终指向待交换对的前一个节点

    while prev.next and prev.next.next:
        # 定位待交换的两个节点
        first = prev.next        # 第一个节点
        second = prev.next.next  # 第二个节点

        # 三步完成指针重连（倒序连接，逻辑更清晰）
        first.next = second.next  # 步骤1: first 跳过 second
        second.next = first       # 步骤2: second 连回 first
        prev.next = second        # 步骤3: 前驱连接到 second

        # prev 移动到下一对的前驱位置（交换后 first 排在后面）
        prev = first

    return dummy.next  # 哑节点的下一个就是新头节点
```

### ✅ 优势
- 完全符合题意（只重连指针，不修改值）
- 时间 O(n)，空间 O(1)
- 逻辑清晰，容易调试

---

## 方法三：递归

### 💡 思路

将链表看作：**当前对（head, head.next）** + **剩余链表**。

递归地处理 `head.next.next` 之后的部分，再把当前这对节点交换并拼接上去。

**递归定义**：
- `swapPairs(head)` = 交换 `head` 和 `head.next`，并将 `head.next.next` 之后的结果（递归返回）接在 `head` 后面

### 图解

```
swapPairs(1 → 2 → 3 → 4)
  ├── second = 2
  ├── 递归处理 swapPairs(3 → 4) → 返回 4 → 3
  ├── 1.next = (4 → 3)
  ├── 2.next = 1
  └── 返回 2 → 1 → 4 → 3
```

### 递归树

```
swapPairs(1→2→3→4)
    └── swapPairs(3→4)
            └── swapPairs(None) → 返回 None
        3.next = None, 4.next = 3 → 返回 4→3
    1.next = 4→3, 2.next = 1 → 返回 2→1→4→3
```

### 代码

```python
def swapPairs_v3(head):
    # 递归终止条件：链表为空或只有一个节点时，无需交换
    if not head or not head.next:
        return head

    # 记录当前对的第二个节点（交换后会成为新的头）
    second = head.next

    # 递归处理 second 之后的链表，并将结果连到 head 后面
    head.next = swapPairs_v3(second.next)

    # 把 second 指向 head，完成当前对的交换
    second.next = head

    # 返回当前对的新头（原来的第二个节点）
    return second
```

### ⚠️ 注意
- 调用栈深度为 O(n/2)，即 O(n) 空间
- 代码简洁优雅，但对于极长链表可能栈溢出

---

## 总结对比

| 方法 | 符合题意 | 时间复杂度 | 空间复杂度 | 适用场景 |
|------|--------|-----------|-----------|---------|
| 值交换（暴力） | ❌ 不符合 | O(n) | O(1) | 仅供理解题意 |
| 迭代（哑节点） | ✅ | O(n) | O(1) | **面试/竞赛推荐** |
| 递归 | ✅ | O(n) | O(n) | 代码简洁，递归练习 |

### 🎯 核心收获

1. **哑节点技巧**：在链表头部插入哑节点，可以统一对头节点和普通节点的处理，避免大量边界判断。
2. **三指针交换模式**：`prev → first → second → rest` 这种三步重连是链表节点交换的通用模板。
3. **递归思维**：将链表问题分解为"当前处理 + 递归后续"，是递归解链表题的经典思路。

---

## 相关题目推荐

- [LeetCode 25 - K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/)（本题的进阶）
- [LeetCode 206 - 反转链表](https://leetcode.cn/problems/reverse-linked-list/)（基础）
- [LeetCode 92 - 反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/)（进阶）
