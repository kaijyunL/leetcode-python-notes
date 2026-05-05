# LeetCode 106 - 从中序与后序遍历序列构造二叉树（Construct Binary Tree from Inorder and Postorder Traversal）

## 题目

给你两个整数数组：

```text
inorder：二叉树的中序遍历
postorder：二叉树的后序遍历
```

请构造并返回这棵二叉树。

题目保证：

```text
树中没有重复元素
inorder 和 postorder 都来自同一棵树
```

例如：

```text
inorder   = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
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

第 106 题和第 105 题是镜像关系。

第 105 题用的是：

```text
前序 + 中序
```

第 106 题用的是：

```text
中序 + 后序
```

两题共同点是：

```text
都靠中序确定左右子树范围
```

不同点是根节点的位置：

```text
前序：根在当前前序区间的最左边
后序：根在当前后序区间的最右边
```

所以第 106 题的核心只有一句话：

```text
后序遍历最后一个元素是根节点；
中序遍历里根节点左边是左子树，右边是右子树。
```

从简单到最优，推荐掌握两种写法：

1. 递归 + 数组切片：最直观，适合理解题目
2. 递归 + 哈希表 + 下标边界：避免反复切片和查找，**最适合面试**

---

## 这题本质是什么

先看两种遍历的顺序。

中序遍历：

```text
左子树 -> 根 -> 右子树
```

后序遍历：

```text
左子树 -> 右子树 -> 根
```

所以后序遍历能告诉我们：

```text
当前子树的根是谁
```

中序遍历能告诉我们：

```text
根的左边有哪些节点属于左子树
根的右边有哪些节点属于右子树
```

构造二叉树时，每一层递归都做同一件事：

```text
1. 从后序最后一个元素找到根
2. 在中序里找到这个根的位置
3. 根据中序位置切出左子树和右子树
4. 递归构造左右子树
```

---

## 最容易错的地方

### 1. 后序的根在最后，不是在最前

当前子树的根是：

```python
root_val = postorder[-1]
```

如果使用下标边界，就是：

```python
root_val = postorder[post_right]
```

### 2. 仍然要靠中序计算左子树大小

中序里根左边的节点个数，就是左子树大小：

```python
left_size = root_inorder_index - in_left
```

这个 `left_size` 用来切后序区间。

### 3. 后序区间切法容易反

后序顺序是：

```text
左子树 -> 右子树 -> 根
```

所以根占了 `post_right` 这个位置。

如果左子树有 `left_size` 个节点，那么：

```text
左子树后序：post_left 到 post_left + left_size - 1
右子树后序：post_left + left_size 到 post_right - 1
```

这里最容易错的是右子树的结尾：

```text
post_right - 1
```

因为 `post_right` 已经被根节点占用了。

---

## 解法一：递归 + 数组切片

对应文件：

```text
10_二叉树/19_q106/solution_1_slice.py
```

### 思路

最直观的方法是直接把数组切开。

后序最后一个值是根：

```python
root_val = postorder[-1]
```

在中序里找到根的位置：

```python
root_inorder_index = inorder.index(root_val)
```

中序左边就是左子树：

```python
left_inorder = inorder[:root_inorder_index]
```

中序右边就是右子树：

```python
right_inorder = inorder[root_inorder_index + 1:]
```

左子树节点个数是：

```python
left_size = len(left_inorder)
```

因为后序顺序是：

```text
左子树 -> 右子树 -> 根
```

所以后序里：

```python
postorder[:left_size]
```

是左子树。

```python
postorder[left_size:-1]
```

是右子树。

最后一个元素 `postorder[-1]` 是根，不再传给子树。

然后递归构造：

```python
root.left = buildTree(left_inorder, left_postorder)
root.right = buildTree(right_inorder, right_postorder)
```

### 用例子看切片

```text
inorder   = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
```

后序最后一个元素是根：

```text
root_val = 3
```

`3` 在中序里的位置是：

```text
inorder = [9, 3, 15, 20, 7]
             ^
      root_inorder_index = 1
```

所以：

```text
左子树 inorder = [9]
右子树 inorder = [15, 20, 7]
```

左子树大小：

```python
left_size = 1
```

于是后序也能切开：

```text
左子树 postorder = [9]
右子树 postorder = [15, 7, 20]
根节点 root = 3
```

这就递归拆成了：

```text
root.left  用 inorder=[9], postorder=[9] 构造
root.right 用 inorder=[15, 20, 7], postorder=[15, 7, 20] 构造
```

### 为什么它不是面试最优

这个方法最适合理解题意。

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
10_二叉树/19_q106/solution_2_index_hash.py
```

## 这是最适合面试的方法

如果面试里写第 106 题，最推荐这一版。

原因是：

1. 它保留了解法一的递归分治思想
2. 它用哈希表把中序定位从 `O(n)` 优化到 `O(1)`
3. 它用下标边界代替切片，避免创建新数组
4. 它和第 105 题完全对称，掌握一题就能迁移到另一题

一句话总结：

```text
用 postorder[post_right] 找根；
用 inorder_map 找根在中序的位置；
用 left_size 切分左右子树的下标范围。
```

---

### 先把四个下标翻译成人话

解法一是直接切数组：

```text
当前子树的 inorder
当前子树的 postorder
```

解法二不切数组，只用下标表示这两段范围。

```python
def build(in_left, in_right, post_left, post_right):
```

这四个参数的意思是：

```text
inorder[in_left ... in_right] 表示当前子树的中序遍历
postorder[post_left ... post_right] 表示当前子树的后序遍历
```

注意这里不是 Python 切片语法，而是左闭右闭区间。

如果换成 Python 真切片，就是：

```text
inorder[in_left : in_right + 1]
postorder[post_left : post_right + 1]
```

比如：

```text
inorder[0 ... 4]   等价于 Python 的 inorder[0:5]
postorder[0 ... 4] 等价于 Python 的 postorder[0:5]
postorder[1 ... 3] 等价于 Python 的 postorder[1:4]
```

---

### 用例子走一遍

还是看这个例子：

```text
inorder   = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
```

第一次调用是：

```python
build(0, 4, 0, 4)
```

意思是：

```text
inorder[0 ... 4] 和 postorder[0 ... 4] 构造整棵树
```

把它展开就是：

```text
inorder[0 ... 4]   = [9, 3, 15, 20, 7]
postorder[0 ... 4] = [9, 15, 7, 20, 3]
```

当前后序区间的最后一个数就是根：

```python
root_val = postorder[4]  # 3
```

然后去中序里找 `3` 的位置：

```text
inorder = [9, 3, 15, 20, 7]
              ^
          root_inorder_index = 1
```

中序的特点是：

```text
左子树 -> 根 -> 右子树
```

所以 `3` 左边的 `[9]` 是左子树，右边的 `[15, 20, 7]` 是右子树。

左子树有几个节点？

```python
left_size = root_inorder_index - in_left
          = 1 - 0
          = 1
```

这就是 `left_size` 的含义：

```text
左子树节点个数
```

---

### 为什么后序区间可以这样切

后序顺序是：

```text
左子树 -> 右子树 -> 根
```

现在根已经占了 `post_right` 这个位置。

如果左子树有 `left_size` 个节点，那么后序里最前面的 `left_size` 个位置属于左子树。

所以左子树的后序区间是：

```text
post_left 到 post_left + left_size - 1
```

右子树紧跟在左子树后面，并且根节点前面结束：

```text
post_left + left_size 到 post_right - 1
```

套到例子里：

```text
postorder = [9, 15, 7, 20, 3]
             ^  ^       ^   ^
             左  右子树范围 根

根节点：postorder[4] = 3
左子树后序：postorder[0 ... 0] = [9]
右子树后序：postorder[1 ... 3] = [15, 7, 20]
```

中序区间更直接：

```text
左子树中序：in_left 到 root_inorder_index - 1
右子树中序：root_inorder_index + 1 到 in_right
```

套到例子里：

```text
inorder = [9, 3, 15, 20, 7]
           ^  ^  ^       ^
           左 根  右子树范围

左子树中序：inorder[0 ... 0] = [9]
右子树中序：inorder[2 ... 4] = [15, 20, 7]
```

所以两次递归就是：

```python
root.left = build(0, 0, 0, 0)
root.right = build(2, 4, 1, 3)
```

翻译成人话：

```text
用 inorder[0 ... 0] 和 postorder[0 ... 0] 构造左子树
用 inorder[2 ... 4] 和 postorder[1 ... 3] 构造右子树
```

把它展开：

```text
左子树：
inorder[0 ... 0]   = [9]
postorder[0 ... 0] = [9]

右子树：
inorder[2 ... 4]   = [15, 20, 7]
postorder[1 ... 3] = [15, 7, 20]
```

右子树继续递归：

```python
build(2, 4, 1, 3)
```

这次的当前子树片段是：

```text
inorder[2 ... 4]   = [15, 20, 7]
postorder[1 ... 3] = [15, 7, 20]
```

这段的根是：

```python
root_val = postorder[3]  # 20
```

`20` 在当前中序片段里的位置是：

```text
inorder = [9, 3, 15, 20, 7]
                  ^   ^
              in_left root_inorder_index
                 2       3
```

所以：

```python
left_size = root_inorder_index - in_left
          = 3 - 2
          = 1
```

`20` 的左右子树继续拆成：

```text
20 的左子树：
inorder[2 ... 2]   = [15]
postorder[1 ... 1] = [15]

20 的右子树：
inorder[4 ... 4]   = [7]
postorder[2 ... 2] = [7]
```

把这几次递归汇总成表格，就是：

| 调用 | 当前 inorder 范围 | 实际拿到的 inorder | 当前 postorder 范围 | 实际拿到的 postorder | 根节点 |
| --- | --- | --- | --- | --- | --- |
| `build(0, 4, 0, 4)` | `inorder[0 ... 4]` | `[9, 3, 15, 20, 7]` | `postorder[0 ... 4]` | `[9, 15, 7, 20, 3]` | `3` |
| `build(0, 0, 0, 0)` | `inorder[0 ... 0]` | `[9]` | `postorder[0 ... 0]` | `[9]` | `9` |
| `build(2, 4, 1, 3)` | `inorder[2 ... 4]` | `[15, 20, 7]` | `postorder[1 ... 3]` | `[15, 7, 20]` | `20` |
| `build(2, 2, 1, 1)` | `inorder[2 ... 2]` | `[15]` | `postorder[1 ... 1]` | `[15]` | `15` |
| `build(4, 4, 2, 2)` | `inorder[4 ... 4]` | `[7]` | `postorder[2 ... 2]` | `[7]` | `7` |

所以不要把四个下标想成抽象变量。

它们就是在说：

```text
这次递归，只看 inorder 的哪一段，以及 postorder 的哪一段。
```

---

### 递归停止条件为什么是 post_left > post_right

代码里会写：

```python
if post_left > post_right:
    return None
```

意思是当前后序区间里已经没有节点了。

这种情况通常出现在“某个节点没有左子树或右子树”的时候。

比如 `9` 是叶子节点。

构造 `9` 的调用是：

```python
build(0, 0, 0, 0)
```

这次只包含一个节点：

```text
inorder[0 ... 0]   = [9]
postorder[0 ... 0] = [9]
```

所以：

```python
root_val = postorder[0]  # 9
root_inorder_index = 0
left_size = root_inorder_index - in_left
          = 0 - 0
          = 0
```

接下来代码还是会尝试构造 `9` 的左子树：

```python
root.left = build(
    in_left,
    root_inorder_index - 1,
    post_left,
    post_left + left_size - 1,
)
```

把数字代进去：

```python
root.left = build(0, -1, 0, -1)
```

这里 `post_left = 0`，`post_right = -1`。

也就是：

```text
postorder[0 ... -1]
```

这个范围左边界已经超过右边界，说明里面没有任何节点。

所以：

```python
if post_left > post_right:
    return None
```

就会返回 `None`，表示 `9` 没有左子树。

`9` 的右子树也是一样：

```python
root.right = build(1, 0, 0, -1)
```

这里同样是 `post_left = 0`，`post_right = -1`，所以也返回 `None`。

---

### 对应到代码

递归停止条件：

```python
if post_left > post_right:
    return None
```

当前根节点：

```python
root_val = postorder[post_right]
root = TreeNode(root_val)
```

根在中序里的位置：

```python
root_inorder_index = inorder_map[root_val]
```

左子树节点个数：

```python
left_size = root_inorder_index - in_left
```

递归构造左右子树：

```python
root.left = build(
    in_left,
    root_inorder_index - 1,
    post_left,
    post_left + left_size - 1,
)
root.right = build(
    root_inorder_index + 1,
    in_right,
    post_left + left_size,
    post_right - 1,
)
```

如果只记一句话，就记这个：

```text
中序负责告诉我们左子树有多大；
后序根据这个大小切出左子树和右子树，并且最后一个位置留给根。
```

### 复杂度

- 时间复杂度：`O(n)`，每个节点创建一次，哈希表定位根是 `O(1)`
- 空间复杂度：`O(n)`，哈希表和递归栈

---

## 面试推荐

第 106 题最适合面试的方法是：

```text
递归 + 哈希表 + 下标边界
```

面试时可以这样讲：

```text
后序遍历的最后一个元素一定是当前子树的根。
中序遍历中，根左边是左子树，根右边是右子树。
我先用哈希表记录每个值在中序中的位置，这样能 O(1) 找到根的位置。
递归函数用 inorder 和 postorder 的左右边界表示当前子树范围，不做数组切片。
每次根据根在中序中的位置计算 left_size。
然后用 left_size 切出左子树和右子树在后序、中序中的范围。
```

复杂度：

```text
每个节点只处理一次，时间复杂度 O(n)。
哈希表 O(n)，递归栈最坏 O(n)，空间复杂度 O(n)。
```

---

## 和第 105 题的关系

第 105 题：

```text
preorder + inorder
```

根的位置是：

```text
preorder[pre_left]
```

第 106 题：

```text
inorder + postorder
```

根的位置是：

```text
postorder[post_right]
```

两题共同点：

```text
都用 inorder 找根的位置
都用 left_size 切分左右子树
都推荐用哈希表 + 下标边界
```

---

## 推荐记忆顺序

1. 先记住遍历性质：

```text
inorder：左 -> 根 -> 右
postorder：左 -> 右 -> 根
```

2. 再记住当前根：

```python
root_val = postorder[post_right]
```

3. 最后记住后序区间切法：

```python
root.left = build(
    in_left,
    root_inorder_index - 1,
    post_left,
    post_left + left_size - 1,
)
root.right = build(
    root_inorder_index + 1,
    in_right,
    post_left + left_size,
    post_right - 1,
)
```

---

## 本题文件

```text
10_二叉树/19_q106/solution.md
10_二叉树/19_q106/solution_1_slice.py
10_二叉树/19_q106/solution_2_index_hash.py
```
