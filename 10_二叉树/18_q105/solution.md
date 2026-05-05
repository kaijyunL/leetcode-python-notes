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
left_size = root_inorder_index - inorder_left
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

### 先把四个下标翻译成人话

解法一是直接切数组：

```text
当前子树的 preorder
当前子树的 inorder
```

解法二不切数组，只用下标表示这两段范围。

```python
def build(pre_left, pre_right, in_left, in_right):
```

这四个参数的意思是：

```text
preorder[pre_left ... pre_right] 表示当前子树的前序遍历
inorder[in_left ... in_right] 表示当前子树的中序遍历
```

注意这里不是 Python 切片语法，而是左闭右闭区间。

如果非要换成 Python 真切片，它应该是：

```text
preorder[pre_left : pre_right + 1]
inorder[in_left : in_right + 1]
```

比如：

```text
preorder[0 ... 4] 等价于 Python 的 preorder[0:5]
preorder[2 ... 4] 等价于 Python 的 preorder[2:5]
inorder[2 ... 4]  等价于 Python 的 inorder[2:5]
```

也就是说，方法二其实还是在做解法一那件事：

```text
根据当前子树的前序片段和中序片段，构造当前子树
```

只是它没有真的创建新数组。

---

### 用例子走一遍

还是看这个例子：

```text
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]
```

第一次调用是：

```python
build(0, 4, 0, 4)
```

意思是：

```text
preorder[0 ... 4] 和 inorder[0 ... 4] 构造整棵树
```

把它真的展开就是：

```text
preorder[0 ... 4] = [3, 9, 20, 15, 7]
inorder[0 ... 4]  = [9, 3, 15, 20, 7]
```

也就是：

```text
当前这次递归，要用完整的 preorder 和完整的 inorder 构造整棵树。
```

当前前序区间的第一个数就是根：

```python
root_val = preorder[0]  # 3
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

### 为什么前序区间可以这样切

前序顺序是：

```text
根 -> 左子树 -> 右子树
```

现在根已经占了 `pre_left` 这个位置。

如果左子树有 `left_size` 个节点，那么前序里根后面的 `left_size` 个位置，一定都属于左子树。

所以左子树的前序区间是：

```text
pre_left + 1 到 pre_left + left_size
```

右子树就从左子树后面开始：

```text
pre_left + left_size + 1 到 pre_right
```

套到例子里：

```text
preorder = [3, 9, 20, 15, 7]
            ^  ^  ^       ^
            根 左  右子树范围

根节点：preorder[0] = 3
左子树前序：preorder[1 ... 1] = [9]
右子树前序：preorder[2 ... 4] = [20, 15, 7]
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
root.left = build(1, 1, 0, 0)
root.right = build(2, 4, 2, 4)
```

翻译成人话：

```text
用 preorder[1 ... 1] 和 inorder[0 ... 0] 构造左子树
用 preorder[2 ... 4] 和 inorder[2 ... 4] 构造右子树
```

把它真的展开：

```text
左子树：
preorder[1 ... 1] = [9]
inorder[0 ... 0]  = [9]

右子树：
preorder[2 ... 4] = [20, 15, 7]
inorder[2 ... 4]  = [15, 20, 7]
```

也就是说，第一层递归把完整数组拆成了：

```text
整棵树：
preorder[0 ... 4] = [3, 9, 20, 15, 7]
inorder[0 ... 4]  = [9, 3, 15, 20, 7]

左子树：
preorder[1 ... 1] = [9]
inorder[0 ... 0]  = [9]

右子树：
preorder[2 ... 4] = [20, 15, 7]
inorder[2 ... 4]  = [15, 20, 7]
```

右子树还会继续递归：

```python
build(2, 4, 2, 4)
```

这次的当前子树片段是：

```text
preorder[2 ... 4] = [20, 15, 7]
inorder[2 ... 4]  = [15, 20, 7]
```

这段的根是：

```python
root_val = preorder[2]  # 20
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

右子树里的左子树和右子树继续拆成：

```text
20 的左子树：
preorder[3 ... 3] = [15]
inorder[2 ... 2]  = [15]

20 的右子树：
preorder[4 ... 4] = [7]
inorder[4 ... 4]  = [7]
```

把这几次递归汇总成表格，就是：

| 调用 | 当前 preorder 范围 | 实际拿到的 preorder | 当前 inorder 范围 | 实际拿到的 inorder | 根节点 |
| --- | --- | --- | --- | --- | --- |
| `build(0, 4, 0, 4)` | `preorder[0 ... 4]` | `[3, 9, 20, 15, 7]` | `inorder[0 ... 4]` | `[9, 3, 15, 20, 7]` | `3` |
| `build(1, 1, 0, 0)` | `preorder[1 ... 1]` | `[9]` | `inorder[0 ... 0]` | `[9]` | `9` |
| `build(2, 4, 2, 4)` | `preorder[2 ... 4]` | `[20, 15, 7]` | `inorder[2 ... 4]` | `[15, 20, 7]` | `20` |
| `build(3, 3, 2, 2)` | `preorder[3 ... 3]` | `[15]` | `inorder[2 ... 2]` | `[15]` | `15` |
| `build(4, 4, 4, 4)` | `preorder[4 ... 4]` | `[7]` | `inorder[4 ... 4]` | `[7]` | `7` |

所以不要把 `pre_left`、`pre_right` 想成抽象变量。

它们就是在说：

```text
这次递归，只看 preorder 的哪一段。
```

`in_left`、`in_right` 也是同理：

```text
这次递归，只看 inorder 的哪一段。
```

这就是方法二的全部逻辑。

---

### 对应到代码

递归停止条件：

```python
if pre_left > pre_right:
    return None
```

意思是当前前序区间里已经没有节点了。

这个情况通常出现在“某个节点没有左子树或右子树”的时候。

比如上面的例子里，`9` 是一个叶子节点。

构造 `9` 的调用是：

```python
build(1, 1, 0, 0)
```

这次只包含一个节点：

```text
preorder[1 ... 1] = [9]
inorder[0 ... 0]  = [9]
```

所以：

```python
root_val = preorder[1]  # 9
root_inorder_index = 0
left_size = root_inorder_index - in_left
          = 0 - 0
          = 0
```

接下来代码还是会尝试构造 `9` 的左子树：

```python
root.left = build(
    pre_left + 1,
    pre_left + left_size,
    in_left,
    root_inorder_index - 1,
)
```

把数字代进去：

```python
root.left = build(2, 1, 0, -1)
```

这里 `pre_left = 2`，`pre_right = 1`。

也就是：

```text
preorder[2 ... 1]
```

这个范围左边界已经超过右边界，说明里面没有任何节点。

所以：

```python
if pre_left > pre_right:
    return None
```

就会返回 `None`，表示 `9` 没有左子树。

`9` 的右子树也是一样：

```python
root.right = build(2, 1, 1, 0)
```

这里同样是 `pre_left = 2`，`pre_right = 1`，所以也返回 `None`。

这就是叶子节点的左右子树怎么变成空的。

当前根节点：

```python
root_val = preorder[pre_left]
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
    pre_left + 1,
    pre_left + left_size,
    in_left,
    root_inorder_index - 1,
)
root.right = build(
    pre_left + left_size + 1,
    pre_right,
    root_inorder_index + 1,
    in_right,
)
```

如果只记一句话，就记这个：

```text
中序负责告诉我们左子树有多大；
前序根据这个大小切出左子树和右子树。
```

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
left_size = root_inorder_index - in_left
```

---

## 本题文件

```text
10_二叉树/18_q105/solution.md
10_二叉树/18_q105/solution_1_slice.py
10_二叉树/18_q105/solution_2_index_hash.py
```
