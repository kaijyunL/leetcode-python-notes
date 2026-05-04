# LeetCode 105 - 从前序与中序遍历序列构造二叉树（Construct Binary Tree from Preorder and Inorder Traversal）

## 题目

给你两个整数数组：

```text
preorder：二叉树的前序遍历
inorder：二叉树的中序遍历
```

请构造并返回这棵二叉树。

题目保证：

```text
树中没有重复元素
preorder 和 inorder 都来自同一棵树
```

例如：

```text
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]
```

构造出的树是：

```text
      3
     / \
    9  20
       / \
      15  7
```

---

## 先说结论

第 105 题是典型的二叉树分治题。

从第一性原理出发，真正自然的解法是：

1. 递归 + 数组切片：最直观，适合理解题目
2. 递归 + 哈希表 + 下标边界：避免反复切片和查找，**最适合面试**

这题不需要为了凑方法写很多花样。

核心只有一句话：

```text
前序遍历第一个元素是根节点；
中序遍历里根节点左边是左子树，右边是右子树。
```

---

## 这题本质是什么

先看两种遍历的顺序。

前序遍历：

```text
根 -> 左子树 -> 右子树
```

中序遍历：

```text
左子树 -> 根 -> 右子树
```

所以前序遍历能告诉我们：

```text
当前子树的根是谁
```

中序遍历能告诉我们：

```text
根的左边有哪些节点属于左子树
根的右边有哪些节点属于右子树
```

把这两件事合起来，就能递归构造整棵树。

---

## 最容易错的地方

### 1. 只知道根，不知道左右子树长度

前序第一个元素是根：

```python
root_val = preorder[0]
```

但接下来要知道前序里哪些属于左子树，哪些属于右子树。

这个长度来自中序：

```python
left_size = root_index - inorder_left
```

`left_size` 是这题最关键的变量。

### 2. 下标边界容易写乱

面试最优写法不用切片，所以会有四个边界：

```text
pre_left, pre_right
in_left, in_right
```

我建议统一使用左闭右闭区间：

```text
[pre_left, pre_right]
[in_left, in_right]
```

空区间就是：

```python
if pre_left > pre_right:
    return None
```

### 3. 不能有重复元素

这题能用哈希表定位根在中序里的位置，是因为题目保证：

```text
节点值不重复
```

如果有重复值，只靠前序和中序就不能唯一确定树。

---

## 解法一：递归 + 数组切片

对应文件：

```text
10_二叉树/18_q105/solution_1_slice.py
```

### 思路

最直观的方法是直接把数组切开。

前序第一个值是根：

```python
root_val = preorder[0]
```

在中序里找到根的位置：

```python
root_index = inorder.index(root_val)
```

中序左边就是左子树：

```python
left_inorder = inorder[:root_index]
```

中序右边就是右子树：

```python
right_inorder = inorder[root_index + 1:]
```

左子树节点个数是：

```python
left_size = len(left_inorder)
```

所以前序里：

```python
preorder[1:1 + left_size]
```

是左子树。

```python
preorder[1 + left_size:]
```

是右子树。

然后递归构造：

```python
root.left = buildTree(left_preorder, left_inorder)
root.right = buildTree(right_preorder, right_inorder)
```

### 为什么它不是面试最优

这个方法非常适合理解题目。

但它有两个额外开销：

1. `inorder.index(root_val)` 每次都要线性查找
2. 数组切片会创建新数组

所以在链状树最坏情况下，时间复杂度会退化到：

```text
O(n^2)
```

面试时可以先讲这个思路，但最终建议写解法二。

### 复杂度

- 时间复杂度：最坏 `O(n^2)`
- 空间复杂度：最坏 `O(n^2)`，切片会创建新数组

---

## 解法二：递归 + 哈希表 + 下标边界

对应文件：

```text
10_二叉树/18_q105/solution_2_index_hash.py
```

## 这是最适合面试的方法

如果面试里写第 105 题，我最推荐这一版。

原因是：

1. 它保留了解法一的递归分治思想
2. 它用哈希表把中序定位从 `O(n)` 优化到 `O(1)`
3. 它用下标边界代替切片，避免创建新数组
4. 它是第 106 题的基础模板

一句话总结：

```text
用 preorder[pre_left] 找根；
用 inorder_map 找根在中序的位置；
用 left_size 切分左右子树的下标范围。
```

---

### 从第一性原理推导

我们定义递归函数：

```python
def build(pre_left, pre_right, in_left, in_right):
```

含义是：

```text
用 preorder[pre_left:pre_right] 和 inorder[in_left:in_right] 这一段构造当前子树
```

这里实际使用左闭右闭区间：

```text
preorder[pre_left ... pre_right]
inorder[in_left ... in_right]
```

如果前序区间为空：

```python
if pre_left > pre_right:
    return None
```

当前子树根节点一定是：

```python
root_val = preorder[pre_left]
```

创建根节点：

```python
root = TreeNode(root_val)
```

找到根在中序里的位置：

```python
root_index = inorder_map[root_val]
```

左子树节点个数：

```python
left_size = root_index - in_left
```

于是左子树对应的前序区间是：

```text
pre_left + 1 到 pre_left + left_size
```

左子树对应的中序区间是：

```text
in_left 到 root_index - 1
```

右子树对应的前序区间是：

```text
pre_left + left_size + 1 到 pre_right
```

右子树对应的中序区间是：

```text
root_index + 1 到 in_right
```

所以代码是：

```python
root.left = build(
    pre_left + 1,
    pre_left + left_size,
    in_left,
    root_index - 1,
)
root.right = build(
    pre_left + left_size + 1,
    pre_right,
    root_index + 1,
    in_right,
)
```

---

### 为什么 left_size 是关键

前序遍历是：

```text
根 -> 左子树 -> 右子树
```

当前根占了一个位置：

```text
pre_left
```

所以左子树从：

```text
pre_left + 1
```

开始。

但左子树到哪里结束？

这就要靠中序里左子树的节点个数。

如果：

```python
left_size = root_index - in_left
```

那么左子树在前序里的最后一个位置就是：

```text
pre_left + left_size
```

这就是 105 题下标写法的核心。

---

### 复杂度

- 时间复杂度：`O(n)`，每个节点创建一次，哈希表定位根是 `O(1)`
- 空间复杂度：`O(n)`，哈希表和递归栈

---

## 面试推荐

第 105 题最适合面试的方法是：

```text
递归 + 哈希表 + 下标边界
```

面试时可以这样讲：

```text
前序遍历的第一个元素一定是当前子树的根。
中序遍历中，根左边是左子树，根右边是右子树。
我先用哈希表记录每个值在中序中的位置，这样能 O(1) 找到根的位置。
递归函数用 preorder 和 inorder 的左右边界表示当前子树范围，不做数组切片。
每次根据根在中序中的位置计算 left_size，
再用 left_size 切出左子树和右子树在前序、中序中的范围。
```

复杂度：

```text
每个节点只处理一次，时间复杂度 O(n)。
哈希表 O(n)，递归栈最坏 O(n)，空间复杂度 O(n)。
```

---

## 和第 106 题的关系

第 105 题：

```text
前序 + 中序
```

前序的特点是：

```text
根在当前前序区间的最左边
```

第 106 题：

```text
中序 + 后序
```

后序的特点是：

```text
根在当前后序区间的最右边
```

两题共同点是：

```text
都靠中序确定左右子树范围
```

---

## 推荐记忆顺序

1. 先记住遍历性质：

```text
preorder：根 -> 左 -> 右
inorder：左 -> 根 -> 右
```

2. 再记住当前根：

```python
root_val = preorder[pre_left]
```

3. 最后记住左右子树长度：

```python
left_size = root_index - in_left
```

---

## 本题文件

```text
10_二叉树/18_q105/solution.md
10_二叉树/18_q105/solution_1_slice.py
10_二叉树/18_q105/solution_2_index_hash.py
```
