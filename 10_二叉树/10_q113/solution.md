# LeetCode 113 - 路径总和 II（Path Sum II）

## 题目

给你一棵二叉树的根节点 `root` 和一个整数 `targetSum`。

返回所有从根节点到叶子节点的路径，使得每条路径上的节点值之和都等于 `targetSum`。

叶子节点是指：

```text
没有左孩子，也没有右孩子的节点
```

例如：

```text
        5
       / \
      4   8
     /   / \
    11  13  4
   /  \    / \
  7    2  5   1
```

如果 `targetSum = 22`，答案是：

```text
[
  [5, 4, 11, 2],
  [5, 8, 4, 5]
]
```

---

## 先说结论

第 113 题是第 112 题的进阶版。

第 112 题只问：

```text
是否存在一条路径
```

第 113 题要求：

```text
返回所有满足条件的路径
```

所以第 113 题不能只传一个“还差多少”，还必须维护当前路径 `path`。

从第一性原理出发，真正自然的解法是：

1. 朴素暴力：先枚举所有根到叶路径，再过滤路径和
2. DFS 回溯：边走边维护路径和路径剩余目标，**最适合面试**
3. 迭代栈：把当前节点、剩余目标、路径一起入栈

---

## 这题本质是什么

题目问的是：

```text
所有 root -> leaf 且路径和等于 targetSum 的路径
```

关键有三个：

1. 路径必须从根节点开始
2. 路径必须到叶子节点结束
3. 要返回路径本身，而不只是 `True / False`

所以这题比第 112 题多了一个核心动作：

```text
维护 path
```

每进入一个节点，就把它加入 `path`。

每离开一个节点，就把它从 `path` 中移除。

这就是回溯。

---

## 最容易错的地方

### 1. 中途满足 targetSum 不能直接加入答案

必须走到叶子节点才能判断。

比如：

```text
    1
   /
  2
 /
3
```

如果 `targetSum = 3`，路径 `1 -> 2` 的和是 `3`。

但 `2` 不是叶子，所以不能加入答案。

### 2. 加入答案时必须复制 path

错误写法：

```python
ans.append(path)
```

正确写法：

```python
ans.append(path[:])
```

原因是 `path` 是一个会继续变化的列表。

如果直接把 `path` 放进 `ans`，后续 `path.pop()` 会影响已经保存的答案。

所以必须保存当前路径的快照。

这里用 `path[:]`，和回溯模板里的写法保持一致。

---

## 解法一：朴素暴力枚举路径

对应文件：

```text
10_二叉树/10_q113/solution_1_bruteforce.py
```

### 思路

最直观的想法是分两步：

1. 先找出所有根到叶路径
2. 再筛选出路径和等于 `targetSum` 的路径

比如所有路径是：

```text
[5, 4, 11, 7]
[5, 4, 11, 2]
[5, 8, 13]
[5, 8, 4, 5]
[5, 8, 4, 1]
```

再逐条计算和，留下和为 `22` 的路径：

```text
[5, 4, 11, 2]
[5, 8, 4, 5]
```

### 为什么它不适合面试主写

这个方法很直观，但会做一些不必要的事：

1. 保存所有路径，即使很多路径根本不满足条件
2. 每条路径到最后再 `sum(path)`，有重复计算
3. 内存占用更大

它适合作为第一性原理的起点，但不是面试首选。

### 复杂度

- 时间复杂度：`O(n * h)`，生成路径和计算路径和都与路径长度相关
- 空间复杂度：`O(n * h)`，最坏情况下保存大量路径

---

## 解法二：DFS 回溯

对应文件：

```text
10_二叉树/10_q113/solution_2_backtracking.py
```

## 这是最适合面试的方法

如果面试里写第 113 题，我最推荐写 DFS 回溯。

原因是：

1. 它直接表达了“根到叶路径”的搜索过程
2. 它只维护当前路径，不需要先保存所有路径
3. 它用剩余目标值避免反复 `sum(path)`
4. 它是很多二叉树路径题的通用模板

一句话总结：

```text
进入节点时选择它，离开节点时撤销它；走到叶子时判断是否满足 targetSum。
```

---

### 从第一性原理推导

定义一个 DFS 函数：

```python
def dfs(node, remain):
```

含义是：

```text
当前走到 node，这条路径还需要凑出 remain
```

进入节点时：

```python
path.append(node.val)
```

如果当前节点是叶子节点：

```python
if node.left is None and node.right is None:
```

就判断：

```python
node.val == remain
```

如果成立，把当前路径复制进答案：

```python
ans.append(path[:])
```

如果不是叶子，就继续递归左右子树：

```python
next_remain = remain - node.val
dfs(node.left, next_remain)
dfs(node.right, next_remain)
```

最后离开当前节点时撤销选择：

```python
path.pop()
```

---

### 为什么要回溯

`path` 表示当前从根走到当前节点的路径。

当我们从一个节点返回父节点时，这个节点就不应该继续留在 `path` 里。

比如走完：

```text
5 -> 4 -> 11 -> 2
```

返回到 `11` 后，接下来可能要探索别的方向。

如果不 `pop()`，路径里还会残留 `2`，后面的路径就乱了。

所以回溯的本质是：

```text
选择 -> 递归 -> 撤销选择
```

对应代码：

```python
path.append(node.val)
...
path.pop()
```

---

### 为什么 ans.append(path[:])

这是本题最容易踩的 Python 坑。

`path` 是同一个列表对象，会随着递归继续变化。

如果写：

```python
ans.append(path)
```

保存进去的是同一个列表引用。

后面 `path.pop()` 时，`ans` 里面的路径也会跟着变。

所以必须写：

```python
ans.append(path[:])
```

保存当前这一刻的路径快照。

### 复杂度

- 时间复杂度：`O(n * h)`，每个节点访问一次，复制答案路径需要路径长度
- 空间复杂度：`O(h)`，不计返回结果；递归栈和当前路径长度都与树高相关

---

## 解法三：迭代栈

对应文件：

```text
10_二叉树/10_q113/solution_3_iterative_stack.py
```

### 思路

递归回溯保存了三个信息：

```text
当前节点
剩余目标值
当前路径
```

迭代版就把这三个信息一起放进栈：

```text
(node, remain, path)
```

每次弹出一个状态：

1. 如果当前节点是叶子，并且 `node.val == remain`，加入答案
2. 否则把左右孩子和更新后的路径入栈

核心代码：

```python
stack = [(root, targetSum, [root.val])]

while stack:
    node, remain, path = stack.pop()

    if node.left is None and node.right is None and node.val == remain:
        ans.append(path)

    next_remain = remain - node.val
    if node.right:
        stack.append((node.right, next_remain, path + [node.right.val]))
    if node.left:
        stack.append((node.left, next_remain, path + [node.left.val]))
```

### 什么时候写迭代版

如果面试官追问非递归，就写这一版。

默认情况下，递归回溯更自然、更省路径复制次数。

### 复杂度

- 时间复杂度：`O(n * h)`，路径拼接会复制列表
- 空间复杂度：`O(n * h)`，栈中可能保存多条路径

---

## 面试推荐

第 113 题最适合面试的方法是：

```text
DFS 回溯
```

面试时可以这样讲：

```text
我用 DFS 从根节点往叶子节点搜索。
path 维护当前路径，remain 表示当前路径还需要凑出的目标值。
进入一个节点时，把节点值加入 path。
如果当前节点是叶子，并且 node.val == remain，
说明当前 root-to-leaf 路径满足要求，把 path[:] 加入答案。
然后递归搜索左右子树。
递归结束后，需要 path.pop() 撤销当前节点，
保证回到父节点时 path 恢复到进入当前节点前的状态。
```

复杂度：

```text
每个节点访问一次，但每次保存答案时要复制路径。
时间复杂度 O(n * h)，空间复杂度 O(h)，不计返回结果。
```

---

## 和第 112 题的关系

第 112 题：

```text
只问是否存在路径
```

所以可以只传 `remain`，不保存完整路径。

第 113 题：

```text
要返回所有路径
```

所以必须维护 `path`，并在找到答案时复制路径。

可以这样记：

```text
112：存在性判断，用 DFS + remain
113：输出所有路径，用 DFS + remain + path + 回溯
```

---

## 推荐记忆顺序

1. 先记住路径要求：

```text
root -> leaf
```

2. 再记住回溯结构：

```text
path.append(node.val)
dfs(...)
path.pop()
```

3. 最后记住 Python 细节：

```text
ans.append(path[:])
```

---

## 本题文件

```text
10_二叉树/10_q113/solution.md
10_二叉树/10_q113/solution_1_bruteforce.py
10_二叉树/10_q113/solution_2_backtracking.py
10_二叉树/10_q113/solution_3_iterative_stack.py
```
