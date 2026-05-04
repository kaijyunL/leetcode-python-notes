# LeetCode 116 - 填充每个节点的下一个右侧节点指针（Populating Next Right Pointers in Each Node）

## 题目

给你一棵完美二叉树：

```text
所有叶子节点都在同一层
每个非叶子节点都有两个孩子
```

每个节点除了 `left` 和 `right`，还有一个 `next` 指针。

要求把每个节点的 `next` 指向它右侧相邻的节点。

如果右侧没有节点，就指向 `None`。

例如：

```text
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
```

连接后：

```text
第 1 层：1 -> None
第 2 层：2 -> 3 -> None
第 3 层：4 -> 5 -> 6 -> 7 -> None
```

---

## 先说结论

第 116 题也是层序系列题，但它比 102、103、107、199 更进一步：

```text
前面几题是返回一个答案列表
第 116 题是直接修改节点的 next 指针
```

从第一性原理出发，真正自然的解法是：

1. BFS 队列：一层一层遍历，把同层节点连起来
2. 递归连接相邻节点：把“同一个节点的两个孩子”和“相邻两个节点之间的孩子”都连上
3. O(1) 空间迭代：利用已经建立好的 `next` 指针遍历下一层，**最适合面试**

这题真正的重点是：

```text
完美二叉树这个条件可以让我们不用队列，也能找到下一层的相邻节点。
```

所以如果面试里只写 BFS，能过题，但没有完全体现第 116 题的核心。

最推荐的面试写法是：

```text
从每一层最左节点开始，利用当前层的 next 指针横向移动；
一边移动，一边连接下一层的 next 指针。
```

---

## 这题本质是什么

题目要做的事情是：

```text
把每一层的节点从左到右串起来
```

第 102 题是：

```text
每一层收集成 list
```

第 116 题是：

```text
每一层通过 next 指针串起来
```

所以它本质上仍然是：

```text
按层处理节点
```

只是结果不再是 `ans.append(level)`，而是：

```python
prev.next = node
```

---

## 最容易错的地方

### 1. 忘记这是完美二叉树

第 116 题的 O(1) 解法依赖这个条件：

```text
每个非叶子节点一定有 left 和 right
```

所以可以安全地写：

```python
node.left.next = node.right
```

也可以通过：

```python
node.next.left
```

找到 `node` 在同一层右侧相邻节点的左孩子。

也就是说，如果当前层里有：

```text
node -> node.next
```

那么下一层里，`node.right` 右边紧挨着的节点就是：

```python
node.next.left
```

这个条件到了第 117 题就不成立了。

### 2. 只连了同一个 node 下面的两个孩子

只写：

```python
node.left.next = node.right
```

是不够的。

还必须连接相邻两个 `node` 之间的孩子：

```python
node.right.next = node.next.left
```

例如：

```text
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
```

`5.next` 应该指向 `6`。

这就是 `node.right` 到 `node.next.left` 的连接。

### 3. O(1) 迭代时层与层不要混

外层循环控制“从哪一层开始连接下一层”。

内层循环沿着当前层的 `next` 横向移动。

也就是：

```text
leftmost 控制当前层最左节点
node 沿当前层 next 往右走
```

---

## 解法一：BFS 队列

对应文件：

```text
10_二叉树/16_q116/solution_1_bfs_queue.py
```

### 思路

最直观的方法还是层序遍历。

每一层从左到右处理。

在同一层里，用 `prev` 记录前一个节点：

```python
prev = None
```

每弹出一个当前节点 `node`：

```python
if prev:
    prev.next = node
prev = node
```

这样同一层就被串起来了。

### 和第 102 题的关系

第 102 题是：

```python
level.append(node.val)
```

第 116 题 BFS 版是：

```python
prev.next = node
```

模板还是：

```python
level_size = len(queue)
```

只是处理当前节点的动作变了。

### 为什么它不是最优

BFS 队列很好理解，也能通过。

但它需要额外队列空间。

题目进阶要求通常希望你做到：

```text
只使用常量级额外空间
```

所以 BFS 是理解起点，不是第 116 题最核心的面试写法。

### 复杂度

- 时间复杂度：`O(n)`，每个节点访问一次
- 空间复杂度：`O(w)`，队列最多保存一层节点

---

## 解法二：递归连接相邻节点

对应文件：

```text
10_二叉树/16_q116/solution_2_recursive_pair.py
```

### 思路

这题也可以从“连接相邻节点”这个角度理解。

定义一个函数：

```python
connect_two(node1, node2)
```

含义是：

```text
把 node1.next 指向 node2
并继续处理它们下面的相邻关系
```

对于两个相邻节点 `node1` 和 `node2`，需要做三件事：

```python
node1.next = node2
```

连接 `node1` 自己的两个孩子：

```python
connect_two(node1.left, node1.right)
```

连接 `node2` 自己的两个孩子：

```python
connect_two(node2.left, node2.right)
```

连接相邻两个节点之间的孩子：

```python
connect_two(node1.right, node2.left)
```

最后从根节点的左右孩子开始：

```python
connect_two(root.left, root.right)
```

### 这个方法的价值

它能很好地帮助你理解第 116 题最关键的两类连接：

```text
同一个节点内部：left -> right
相邻两个节点之间：node1.right -> node2.left
```

不过递归会使用调用栈。

如果面试官严格要求 O(1) 额外空间，还是写解法三。

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(h)`，递归调用栈高度

---

## 解法三：O(1) 空间迭代

对应文件：

```text
10_二叉树/16_q116/solution_3_iterative_o1.py
```

## 这是最适合面试的方法

如果面试里写第 116 题，我最推荐这一版。

原因是：

1. 它符合题目进阶要求：常量级额外空间
2. 它真正利用了完美二叉树的结构
3. 它为第 117 题做铺垫
4. 它能清楚区分“层内横向移动”和“连接下一层”

一句话总结：

```text
当前层已经被 next 串起来后，就可以用当前层去连接下一层。
```

---

### 从第一性原理推导

先看这棵树：

```text
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
```

第一层只有 `1`。

我们可以直接通过 `1` 连接第二层：

```python
1.left.next = 1.right
```

也就是：

```text
2 -> 3
```

第二层连好以后，就可以利用：

```text
2.next == 3
```

从 `2` 横向走到 `3`。

当处理节点 `2` 时：

```python
2.left.next = 2.right
```

得到：

```text
4 -> 5
```

并且因为 `2.next` 是 `3`，所以还能连接：

```python
2.right.next = 2.next.left
```

得到：

```text
5 -> 6
```

当处理节点 `3` 时：

```python
3.left.next = 3.right
```

得到：

```text
6 -> 7
```

这样第三层也连好了。

---

### 两个指针分别干什么

代码里有两个核心变量：

```python
leftmost = root
```

表示当前层最左边的节点。

只要 `leftmost.left`，说明下一层还存在，需要继续连接。

内层循环：

```python
node = leftmost
while node:
```

表示沿着当前层已经建立好的 `next` 指针从左往右走。

处理每个 `node` 时，连接下一层两类关系。

第一类：连接同一个 `node` 的两个孩子：

```python
node.left.next = node.right
```

第二类：连接 `node` 和 `node.next` 之间的孩子：

```python
if node.next:
    node.right.next = node.next.left
```

当前层处理完以后，移动到下一层最左节点：

```python
leftmost = leftmost.left
```

---

### 为什么是 O(1) 空间

这版没有使用队列。

它只用了几个指针：

```text
leftmost
node
```

这些变量数量不会随着节点数量增加。

所以额外空间是：

```text
O(1)
```

注意：返回的树本身不算额外空间。

### 复杂度

- 时间复杂度：`O(n)`，每个非叶子节点被处理一次
- 空间复杂度：`O(1)`，只使用常量个指针

---

## 面试推荐

第 116 题最适合面试的方法是：

```text
O(1) 空间迭代
```

面试时可以这样讲：

```text
这题是完美二叉树，所以每个非叶子节点都有 left 和 right。
我从当前层最左节点 leftmost 开始。
当前层已经可以通过 next 指针横向遍历。
对当前层每个 node，我连接下一层的两个关系：
第一，node.left.next = node.right，这是同一个 node 的两个孩子之间的连接。
第二，如果 node.next 存在，node.right.next = node.next.left，
这里的 node.next 表示当前节点在同一层右侧相邻的节点，
所以 node.next.left 就是下一层里 node.right 右侧相邻的节点。
处理完整层后，leftmost = leftmost.left，进入下一层。
整个过程不用队列，只用常量个指针。
```

复杂度：

```text
每个节点最多处理一次，时间复杂度 O(n)。
只用了 leftmost 和 node 这几个指针，空间复杂度 O(1)。
```

---

## 和第 117 题的关系

第 116 题：

```text
完美二叉树
```

所以可以放心使用：

```python
node.left
node.right
node.next.left  # node 在同一层右侧相邻节点的左孩子
```

第 117 题：

```text
普通二叉树
```

左右孩子可能不存在。

所以第 117 题不能直接照搬这一版，需要用更通用的“虚拟头节点”方式处理下一层。

---

## 推荐记忆顺序

1. 先从 BFS 理解目标：

```text
同一层从左到右连 next
```

2. 再记住完美二叉树的两类连接：

```text
node.left.next = node.right
node.right.next = node.next.left
```

3. 最后记住 O(1) 迭代的两层循环：

```text
leftmost 控制当前层
node 沿 next 横向移动
```

---

## 本题文件

```text
10_二叉树/16_q116/solution.md
10_二叉树/16_q116/solution_1_bfs_queue.py
10_二叉树/16_q116/solution_2_recursive_pair.py
10_二叉树/16_q116/solution_3_iterative_o1.py
```
