# LeetCode 102 - 二叉树的层序遍历（Binary Tree Level Order Traversal）

## 题目

给你一棵二叉树的根节点 `root`，返回它的层序遍历结果。

层序遍历就是：

```text
从上到下，一层一层访问；
每一层从左到右访问。
```

例如：

```text
      3
     / \
    9  20
       / \
      15  7
```

返回：

```text
[
  [3],
  [9, 20],
  [15, 7]
]
```

---

## 先说结论

第 102 题是二叉树 BFS 的核心模板题。

从第一性原理出发，真正自然的解法是：

1. 朴素 DFS 分组：递归时带上深度 `depth`，按层放入答案
2. BFS 队列：一层一层处理，**最适合面试**
3. DFS 递归补充：同样按深度分组，但写得更模板化

严格说，DFS 分组也能做到 `O(n)`。

但这题题目本身就是：

```text
一层一层遍历
```

所以 BFS 队列是最自然、最适合面试的写法。

---

## 这题本质是什么

题目要求的结果不是一个扁平列表：

```text
[3, 9, 20, 15, 7]
```

而是按层分组：

```text
[[3], [9, 20], [15, 7]]
```

所以核心问题是：

```text
怎么知道哪些节点属于同一层？
```

BFS 的答案是：

```text
队列里当前已有的节点数量，就是这一层的节点数量。
```

也就是：

```python
level_size = len(queue)
```

然后只处理这 `level_size` 个节点。

处理完它们，这一层就结束了。

---

## 最容易错的地方

### 1. 忘记固定当前层长度

错误写法常见于：

```python
while queue:
    node = queue.popleft()
    ...
```

这样只能得到普通 BFS 顺序，很难自然分层。

正确做法是：

```python
level_size = len(queue)
for _ in range(level_size):
    node = queue.popleft()
```

因为在处理当前层时，会把下一层节点加入队列。

如果不先固定 `level_size`，当前层和下一层就会混在一起。

### 2. 空树返回空列表

如果 `root is None`，答案是：

```text
[]
```

不是：

```text
[[]]
```

---

## 解法一：朴素 DFS 按深度分组

对应文件：

```text
10_二叉树/12_q102/solution_1_dfs_group.py
```

### 思路

最直观的分组想法是：

```text
每个节点都知道自己在第几层
然后把它放到 ans[depth] 里
```

根节点深度是 `0`。

左孩子和右孩子深度都是：

```text
depth + 1
```

所以递归时多传一个 `depth`：

```python
dfs(node, depth)
```

如果第一次来到某一层，答案里还没有这一层的列表，就先创建：

```python
if depth == len(ans):
    ans.append([])
```

然后加入当前节点：

```python
ans[depth].append(node.val)
```

### 为什么它不是面试首选

这个方法也很好，也能 `O(n)`。

但题目叫“层序遍历”，面试官通常期待你写 BFS 队列。

DFS 分组适合作为补充，说明你理解：

```text
层 = depth
```

### 复杂度

- 时间复杂度：`O(n)`，每个节点访问一次
- 空间复杂度：`O(h)`，递归调用栈高度，不计返回结果

---

## 解法二：BFS 队列

对应文件：

```text
10_二叉树/12_q102/solution_2_bfs.py
```

## 这是最适合面试的方法

如果面试里写第 102 题，我最推荐写 BFS 队列。

原因是：

1. 它和“层序遍历”的定义完全一致
2. `level_size = len(queue)` 这个模板非常重要
3. 后续 107、103、199、116、117 都会复用它
4. 代码结构稳定，现场手写不容易乱

一句话总结：

```text
队列保存待访问节点；每轮先固定当前层节点数，再处理这一层。
```

---

### 从第一性原理推导

初始时，队列里只有根节点：

```python
queue = deque([root])
```

此时队列里的所有节点就是第 1 层。

处理这一层之前，先记录数量：

```python
level_size = len(queue)
```

然后循环 `level_size` 次：

```python
for _ in range(level_size):
    node = queue.popleft()
```

每弹出一个节点：

1. 把它的值加入当前层列表
2. 如果有左孩子，左孩子入队
3. 如果有右孩子，右孩子入队

这一轮结束时，当前层处理完了。

刚刚入队的孩子们，正好就是下一层。

---

### 为什么必须先取 level_size

看这棵树：

```text
      3
     / \
    9  20
```

开始时：

```text
queue = [3]
```

处理 `3` 的时候，会把 `9` 和 `20` 加入队列。

如果不提前固定这一层的大小，就可能把 `9`、`20` 也当成当前层继续处理。

所以必须：

```python
level_size = len(queue)
```

这行代码的含义是：

```text
现在队列里这些节点，就是当前层。
后面新加进来的，是下一层。
```

### BFS 模板

```python
ans = []
queue = deque([root])

while queue:
    level = []
    level_size = len(queue)

    for _ in range(level_size):
        node = queue.popleft()
        level.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    ans.append(level)
```

这就是二叉树层序题最重要的模板。

### 复杂度

- 时间复杂度：`O(n)`，每个节点访问一次
- 空间复杂度：`O(w)`，队列最多保存一层节点

---

## 解法三：DFS 递归补充

对应文件：

```text
10_二叉树/12_q102/solution_3_dfs_recursive.py
```

### 思路

这其实和解法一是同一种思想，只是写成更常见的递归模板。

递归函数：

```python
dfs(node, depth)
```

每个节点根据 `depth` 放进对应层。

先访问左子树，再访问右子树，就能保证同一层内从左到右。

### 什么时候用 DFS 写

如果题目不是标准层序遍历，而是要求你按深度收集一些信息，DFS 也很好用。

例如：

```text
每层最大值
每层最右节点
每个深度的节点和
```

但第 102 题本身，BFS 更贴合。

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(h)`，递归调用栈高度，不计返回结果

---

## 面试推荐

第 102 题最适合面试的方法是：

```text
BFS 队列
```

面试时可以这样讲：

```text
层序遍历天然适合 BFS。
我用队列保存当前待访问的节点。
每一轮 while 循环代表一层。
进入这一层时，先用 level_size = len(queue) 固定当前层节点数。
然后只弹出这 level_size 个节点，把它们的值加入 level，
并把它们的左右孩子加入队列。
这一轮结束后，level 就是当前层结果，加入 ans。
队列中剩下的节点就是下一层。
```

复杂度：

```text
每个节点访问一次，时间复杂度 O(n)。
队列最多保存一层节点，空间复杂度 O(w)。
```

---

## 和后续层序题的关系

第 102 题是后面几道题的基础模板：

```text
107：层序遍历后反转结果
103：每一层根据方向决定是否反转
199：每层只取最后一个节点
116 / 117：按层连接 next 指针
```

所以这题一定要把 BFS 模板写熟。

---

## 推荐记忆顺序

1. 先记住层序的本质：

```text
一层一层处理
```

2. 再记住关键代码：

```python
level_size = len(queue)
```

3. 最后记住循环含义：

```text
while queue 的每一轮，处理一整层
```

---

## 本题文件

```text
10_二叉树/12_q102/solution.md
10_二叉树/12_q102/solution_1_dfs_group.py
10_二叉树/12_q102/solution_2_bfs.py
10_二叉树/12_q102/solution_3_dfs_recursive.py
```

