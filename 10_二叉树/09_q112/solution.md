# LeetCode 112 - 路径总和（Path Sum）

## 题目

给你一棵二叉树的根节点 `root` 和一个整数 `targetSum`。

判断这棵树中是否存在一条从根节点到叶子节点的路径，使得路径上所有节点值的和等于 `targetSum`。

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
   /  \      \
  7    2      1
```

如果 `targetSum = 22`，返回：

```text
True
```

因为存在路径：

```text
5 -> 4 -> 11 -> 2
```

路径和是：

```text
5 + 4 + 11 + 2 = 22
```

---

## 先说结论

这题不需要为了凑方法写很多花样。

从第一性原理出发，真正自然的解法是：

1. 朴素暴力：枚举所有根到叶路径，逐条计算路径和
2. 递归 DFS：一路把 `targetSum` 往下减，**最适合面试**
3. 迭代栈：递归思想的非递归版本

本题最重要的点是：

```text
必须走到叶子节点，才能判断路径和是否满足要求。
```

不能在中途发现当前和等于 `targetSum` 就直接返回。

---

## 这题本质是什么

题目问的是：

```text
有没有一条 root -> leaf 的路径，使得路径和等于 targetSum
```

关键有两个：

1. 路径必须从根节点开始
2. 路径必须到叶子节点结束

所以 DFS 很自然。

每往下走一层，就把当前节点值从目标值里减掉。

比如目标是 `22`：

```text
走到 5 后，还需要 17
走到 4 后，还需要 13
走到 11 后，还需要 2
走到 2 后，还需要 0
```

如果此时节点 `2` 是叶子节点，就说明找到了一条合法路径。

---

## 最容易错的地方

错误写法是：

```python
if targetSum == 0:
    return True
```

这个判断很危险。

因为题目要求的是：

```text
根节点到叶子节点
```

不是中途任意一段路径。

看这个例子：

```text
    1
   /
  2
 /
3
```

如果 `targetSum = 3`，路径 `1 -> 2` 的和确实是 `3`。

但 `2` 不是叶子节点，所以答案应该是：

```text
False
```

合法路径必须继续走到 `3`。

所以正确判断应该发生在叶子节点：

```python
if root.left is None and root.right is None:
    return root.val == targetSum
```

---

## 解法一：朴素暴力枚举路径

对应文件：

```text
10_二叉树/09_q112/solution_1_bruteforce.py
```

### 思路

最直观的想法是：

```text
把所有 root -> leaf 路径都找出来
然后逐条计算路径和
```

比如这棵树：

```text
        5
       / \
      4   8
     /   / \
    11  13  4
   /  \      \
  7    2      1
```

可以枚举出一些根到叶路径：

```text
5 -> 4 -> 11 -> 7
5 -> 4 -> 11 -> 2
5 -> 8 -> 13
5 -> 8 -> 4 -> 1
```

然后在叶子节点处，计算当前路径和是否等于 `targetSum`。

这就是最朴素、最直接的思路。

### 为什么它不适合面试主写

它的缺点很明显：

1. 需要维护整条路径
2. 需要在叶子节点重新计算路径和
3. 本质上只是把“存在性判断”做成了“完整枚举”

所以它适合理解题意，但不适合作为面试首选。

### 复杂度

- 时间复杂度：`O(n * h)`，最坏情况下退化到 `O(n^2)`
- 空间复杂度：`O(h)`，路径长度和递归栈都和树高相关

---

## 解法二：递归 DFS

对应文件：

```text
10_二叉树/09_q112/solution_2_recursive.py
```

## 这是最适合面试的方法

如果面试里写第 112 题，我最推荐写递归 DFS。

原因是：

1. 它直接表达了“从根到叶”的路径结构
2. 代码短，现场手写稳定
3. 可以找到一条路径后立刻返回
4. 不需要保存完整路径，只保存剩余目标值

一句话总结：

```text
每走到一个节点，就从 targetSum 里减掉 node.val；
走到叶子时，看剩余目标是否刚好等于叶子值。
```

---

### 从第一性原理推导

当前节点是 `root`，目标和是 `targetSum`。

如果 `root` 是空：

```text
不存在路径
```

返回：

```python
False
```

如果 `root` 是叶子节点：

```text
这条路径已经结束
```

这时判断：

```python
root.val == targetSum
```

如果当前节点不是叶子，就继续往左右子树找。

因为当前节点已经被选进路径，所以后续路径需要凑出的和变成：

```text
targetSum - root.val
```

于是递归代码是：

```python
remain = targetSum - root.val
return (
    self.hasPathSum(root.left, remain)
    or self.hasPathSum(root.right, remain)
)
```

这里用 `or`，因为只要存在一条合法路径就可以。

---

### 为什么不需要 path 数组

朴素想法可能会保存整条路径：

```text
[5, 4, 11, 2]
```

然后到叶子时计算总和。

但这题只问是否存在，不要求返回路径。

所以不需要保存路径本身。

只需要保存：

```text
还差多少
```

这就是递归里传递 `targetSum - root.val` 的原因。

### 复杂度

- 时间复杂度：`O(n)`，最坏情况下每个节点访问一次
- 空间复杂度：`O(h)`，递归调用栈高度

---

## 解法三：迭代栈

对应文件：

```text
10_二叉树/09_q112/solution_3_iterative_stack.py
```

### 思路

递归版本质是在保存两个信息：

```text
当前节点
走到当前节点时还剩多少目标值
```

迭代版用栈手动保存这两个信息：

```text
(node, remain)
```

初始：

```text
(root, targetSum)
```

每次弹出一个节点：

1. 如果它是叶子，判断 `node.val == remain`
2. 如果不是叶子，把左右孩子和新的剩余目标入栈

新的剩余目标是：

```text
remain - node.val
```

核心代码：

```python
stack = [(root, targetSum)]

while stack:
    node, remain = stack.pop()

    if node.left is None and node.right is None and node.val == remain:
        return True

    next_remain = remain - node.val
    if node.right:
        stack.append((node.right, next_remain))
    if node.left:
        stack.append((node.left, next_remain))
```

### 什么时候写迭代版

如果面试官追问：

```text
能不能不用递归？
```

就写这一版。

默认情况下，递归 DFS 更直接。

### 复杂度

- 时间复杂度：`O(n)`，最坏情况下访问所有节点
- 空间复杂度：`O(h)`，栈里保存待访问节点

---

## 面试推荐

第 112 题最适合面试的方法是：

```text
递归 DFS
```

面试时可以这样讲：

```text
我从根节点开始 DFS。
每经过一个节点，就把它的值从 targetSum 中减掉。
如果走到叶子节点，说明一条 root-to-leaf 路径结束了，
此时只需要判断叶子节点的值是否等于当前剩余目标。
如果不是叶子节点，就继续递归查找左子树或右子树。
只要任意一边返回 True，就说明存在合法路径。
```

复杂度：

```text
最坏情况下访问每个节点一次，时间复杂度 O(n)。
递归栈深度等于树高，空间复杂度 O(h)。
```

---

## 和第 113 题的关系

第 112 题只问：

```text
是否存在路径
```

所以只需要返回 `True / False`，不需要保存路径。

第 113 题会问：

```text
返回所有满足条件的路径
```

那时就必须用回溯维护 `path` 数组。

所以第 112 题可以理解为第 113 题的简化版。

---

## 推荐记忆顺序

1. 先记住路径要求：

```text
root -> leaf
```

2. 再记住叶子判断：

```text
left is None and right is None
```

3. 最后记住递归写法：

```text
走过当前节点后，目标值变成 targetSum - root.val
```

---

## 本题文件

```text
10_二叉树/09_q112/solution.md
10_二叉树/09_q112/solution_1_bruteforce.py
10_二叉树/09_q112/solution_2_recursive.py
10_二叉树/09_q112/solution_3_iterative_stack.py
```
