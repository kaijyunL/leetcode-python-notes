# LeetCode 117 - 填充每个节点的下一个右侧节点指针 II（Populating Next Right Pointers in Each Node II）

## 题目

给你一棵二叉树的根节点 `root`。

每个节点有四个字段：

```text
val
left
right
next
```

要求把每个节点的 `next` 指向它右侧相邻的节点。

如果右侧没有节点，就指向 `None`。

例如：

```text
        1
      /   \
     2     3
    / \     \
   4   5     7
```

连接后：

```text
第 1 层：1 -> None
第 2 层：2 -> 3 -> None
第 3 层：4 -> 5 -> 7 -> None
```

---

## 先说结论

第 117 题是第 116 题的升级版。

第 116 题是：

```text
完美二叉树
```

第 117 题是：

```text
普通二叉树
```

所以第 116 题里这类写法不能直接照搬：

```python
node.left.next = node.right
node.right.next = node.next.left
```

因为第 117 题里：

```text
node.left 可能不存在
node.right 可能不存在
node.next.left 也可能不存在
```

从第一性原理出发，真正自然的解法是：

1. BFS 队列：一层一层遍历，把同层节点连起来
2. O(1) 空间迭代：用当前层的 `next` 遍历当前层，用 `dummy + nxt` 连接下一层，**最适合面试**

这题不需要硬凑一个递归找右侧节点的复杂版本。

普通二叉树的结构不整齐，递归版会把“找下一个可连接孩子”写得很绕，面试和复习都不如 `dummy + nxt` 迭代清晰。

---

## 这题本质是什么

第 117 题和第 116 题本质一样：

```text
把每一层从左到右串成 next 链表
```

区别是：

```text
116：下一层节点位置非常规律
117：下一层节点位置不规律
```

所以第 117 题不能依赖：

```text
左孩子一定存在
右孩子一定存在
相邻父节点的左孩子一定存在
```

它需要一个更通用的动作：

```text
扫描当前层时，遇到下一层的孩子，就把它接到“已经接好的最后一个孩子”后面。
```

这就是 `dummy + nxt` 的作用。

---

## 最容易错的地方

### 1. 把 116 的最优解直接搬过来

第 116 题可以写：

```python
while leftmost.left:
```

因为完美二叉树只要不是叶子，`left` 一定存在。

第 117 题不行。

例如：

```text
    1
     \
      2
```

根节点没有左孩子，但下一层仍然存在。

所以第 117 题不能用 `leftmost.left` 判断是否继续。

### 2. 只处理左孩子，漏掉右孩子

普通二叉树里，节点可能只有右孩子。

所以扫描当前层时必须分别判断：

```python
if cur.left:
    ...
if cur.right:
    ...
```

### 3. 不知道下一层从哪里开始

第 116 题下一层最左节点一定是：

```python
leftmost.left
```

第 117 题不一定。

所以我们用：

```python
dummy.next
```

表示下一层的第一个节点。

处理完当前层后：

```python
cur = dummy.next
```

进入下一层。

---

## 解法一：BFS 队列

对应文件：

```text
10_二叉树/17_q117/solution_1_bfs_queue.py
```

### 思路

最直观的方法还是层序遍历。

每一层从左到右处理。

用 `prev` 记录当前层的前一个节点：

```python
prev = None
```

每弹出一个节点 `node`：

```python
if prev:
    prev.next = node
prev = node
```

这样同一层就能被串起来。

孩子仍然按 `left -> right` 加入队列：

```python
if node.left:
    queue.append(node.left)
if node.right:
    queue.append(node.right)
```

### 为什么这个方法很适合做起点

这个方法完全符合第一性原理：

```text
既然要连接同一层，那就先一层一层拿节点。
```

而且它和第 102、103、107、199 的 BFS 模板一致：

```python
level_size = len(queue)
```

所以它很适合用来理解题目。

### 为什么它不是最终最优

BFS 队列需要额外空间：

```text
O(w)
```

其中 `w` 是树的最大宽度。

第 117 题的进阶目标仍然是：

```text
O(1) 额外空间
```

所以面试里可以先说 BFS，但最终推荐写解法二。

### 复杂度

- 时间复杂度：`O(n)`，每个节点访问一次
- 空间复杂度：`O(w)`，队列最多保存一层节点

---

## 解法二：O(1) 空间迭代 + dummy/nxt

对应文件：

```text
10_二叉树/17_q117/solution_2_iterative_dummy.py
```

## 这是最适合面试的方法

如果面试里写第 117 题，我最推荐这一版。

原因是：

1. 它满足常量级额外空间
2. 它能处理普通二叉树，不依赖完美结构
3. 它是第 116 题 O(1) 思想的通用升级
4. 它的模板稳定：`cur` 扫当前层，`dummy/nxt` 连接下一层

一句话总结：

```text
沿着当前层的 next 往右走；遇到下一层孩子，就接到 dummy 后面这条临时链上。
```

---

### 从第一性原理推导

假设当前层已经可以通过 `next` 横向移动。

我们用：

```python
cur
```

遍历当前层。

完整模板是：

```python
cur = root

while cur:
    dummy = Node(0)
    nxt = dummy

    while cur:
        if cur.left:
            nxt.next = cur.left
            nxt = nxt.next

        if cur.right:
            nxt.next = cur.right
            nxt = nxt.next

        cur = cur.next

    cur = dummy.next
```

每处理一层，先准备：

```python
dummy = Node(0)
nxt = dummy
```

这里要注意：

```text
dummy 不是当前层节点
nxt 也不是当前层节点
```

它们只是临时工具，用来把下一层的孩子从左到右接起来。

刚开始下一层还没有接任何真实节点，所以：

```text
dummy.next is None
nxt 指向 dummy
```

扫描当前层的每个节点 `cur`。

如果 `cur.left` 存在，就把它接到 `nxt` 后面：

```python
nxt.next = cur.left
nxt = nxt.next
```

这两行的意思是：

```text
nxt.next = cur.left：把 cur.left 接到下一层临时链后面
nxt = nxt.next：nxt 移到刚接上的 cur.left
```

如果 `cur.right` 存在，也做同样的事：

```python
nxt.next = cur.right
nxt = nxt.next
```

然后当前层继续往右走：

```python
cur = cur.next
```

当前层处理完以后：

```python
cur = dummy.next
```

这里的 `dummy.next` 才是下一层真正的第一个节点。

如果这一层没有任何孩子，那么 `dummy.next` 还是 `None`，循环自然结束。

---

### 为什么 dummy 好用

如果不用 `dummy`，你需要额外判断：

```text
下一层第一个孩子是谁？
已经接好的最后一个孩子是谁？
```

比如：

```text
如果还没有第一个孩子，就先记录下一层入口
如果已经有孩子了，就把新孩子接到上一个孩子后面
```

这当然也能写，但分支更多。

`dummy` 的作用是给下一层放一个临时起点：

```text
所有下一层孩子都接到 nxt 后面
nxt 每次移动到刚接上的孩子
最后 dummy.next 就是下一层第一个真实节点
```

它不是树里的真实节点，只是临时辅助节点。

每一层只创建一个 `dummy`，处理完这一层就丢掉。

所以额外空间仍然是：

```text
O(1)
```

---

### 为什么叫 nxt

这里的 `nxt` 不是当前层，也不是树里的特殊节点。

它表示：

```text
下一层这条临时链上，当前已经接好的最后一个节点
```

名字叫 `nxt`，是为了提醒自己：

```text
我正在处理 next 指针，正在拼下一层
```

很多链表模板会把这个变量叫 `tail`。

但这题不是把整棵二叉树变成一条链表，所以用 `tail` 容易让人误会。

这份笔记用 `nxt`，保留 `dummy` 模板，但减少链表术语带来的绕感。

---

### 和第 116 题的关系

第 116 题可以利用完美二叉树写：

```python
node.left.next = node.right
node.right.next = node.next.left
```

第 117 题不能这么写。

第 117 题更通用的写法是：

```text
扫描当前层，遇到下一层孩子，就把它接到 nxt 后面。
```

所以第 117 题可以反过来理解第 116：

```text
116 是结构规整时的特化版本
117 是普通二叉树下的通用版本
```

### 复杂度

- 时间复杂度：`O(n)`，每个节点访问一次
- 空间复杂度：`O(1)`，只使用常量个指针

---

## 面试推荐

第 117 题最适合面试的方法是：

```text
O(1) 空间迭代 + dummy/nxt
```

面试时可以这样讲：

```text
这题是第 116 题的升级版，但它不是完美二叉树，所以不能假设 left、right、next.left 都存在。
我用 cur 沿着当前层已有的 next 指针横向遍历。
遍历当前层时，用 dummy 作为下一层临时链的起点，nxt 指向当前已经接好的最后一个下一层孩子。
如果 cur.left 存在，就 nxt.next = cur.left，然后 nxt = nxt.next。
如果 cur.right 存在，也做同样的事。
当前层走完后，dummy.next 就是下一层第一个真实节点，于是 cur = dummy.next。
循环直到没有下一层。
整个过程不用队列，只用 cur、dummy、nxt 这些指针。
```

复杂度：

```text
每个节点最多访问一次，时间复杂度 O(n)。
只使用常量个指针，空间复杂度 O(1)。
```

---

## 和第 116 题的区别

可以这样记：

```text
116：完美二叉树，可以直接连接固定位置
117：普通二叉树，必须动态收集下一层孩子
```

第 116 题核心连接：

```python
node.left.next = node.right
node.right.next = node.next.left
```

第 117 题核心连接：

```python
nxt.next = child
nxt = nxt.next
```

所以：

```text
116 利用结构规律
117 扫当前层，动态连接下一层
```

---

## 推荐记忆顺序

1. 先从 BFS 理解目标：

```text
同一层从左到右连 next
```

2. 再记住第 117 题不能依赖完美结构：

```text
孩子可能缺失，下一层第一个节点不固定
```

3. 最后记住 `dummy + nxt` 模板：

```python
dummy = Node(0)
nxt = dummy
```

含义是：

```text
准备开始连接下一层
```

每遇到一个下一层孩子 `child`：

```python
nxt.next = child
nxt = nxt.next
```

当前层结束后：

```python
cur = dummy.next
```

---

## 本题文件

```text
10_二叉树/17_q117/solution.md
10_二叉树/17_q117/solution_1_bfs_queue.py
10_二叉树/17_q117/solution_2_iterative_dummy.py
```
