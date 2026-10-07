# LeetCode 543 - 二叉树的直径（Diameter of Binary Tree）

## 题目

给定一棵二叉树，返回这棵树的直径。

直径是树中任意两个节点之间最长的路径长度，长度按边数计算。

例如：

```text
      1
     / \
    2   3
   / \
  4   5
```

最长路径是：

```text
4 -> 2 -> 1 -> 3
```

经过 3 条边，所以答案是：

```text
3
```

注意：题目求的是边数，不是节点数。

```text
4 -> 2 -> 1 -> 3
节点数：4
边数：3
```

## 先理解“经过当前节点的路径”

直径可能经过根节点，也可能完全在某个子树内部。

以节点 `1` 为例，如果最长路径经过 `1`，它一定是：

```text
左子树最深节点 -> 1 -> 右子树最深节点
```

所以，经过当前节点的最长路径长度是：

```text
左子树高度 + 右子树高度
```

这里的高度按边数理解：

```text
空节点高度 = 0
叶子节点向下的高度 = 0
```

但代码通常让 `height(None) = 0`、叶子返回 `1`，这表示的是节点层数。此时如果直接计算：

```python
left_height + right_height
```

得到的正好仍然是经过当前节点的边数，因为左右两边的“当前节点那一层”没有被加进去。

例如：

```text
      1
     / \
    2   3
```

代码计算：

```text
height(2) = 1
height(3) = 1
经过 1 的直径 = 1 + 1 = 2
```

路径 `2 -> 1 -> 3` 确实有 2 条边。

## 直径不一定经过根节点

这是本题最容易漏掉的地方。

```text
          1
         /
        2
       / \
      4   5
         / \
        6   7
```

整棵树的直径可能完全位于左子树内部，例如：

```text
4 -> 2 -> 5 -> 6
```

因此不能只计算：

```python
height(root.left) + height(root.right)
```

必须同时考虑：

```text
经过当前节点的最长路径
左子树内部的直径
右子树内部的直径
```

最终答案是所有节点的“经过该节点的最长路径”中的最大值。

## 解法一览

| 解法 | 思路 | 时间复杂度 | 空间复杂度 | 是否推荐面试 |
|---|---|---|---|---|
| 1. 自顶向下递归 | 每个节点计算左右高度，再计算子树直径 | 最坏 `O(n^2)` | `O(h)` | 适合理解 |
| 2. 后序 DFS | 一次返回高度，同时更新全局直径 | `O(n)` | `O(h)` | **面试推荐 ✅** |

其中：

```text
n：节点总数
h：树高
```

## 解法 1：自顶向下递归

对应文件：

```text
10_二叉树/10_q543/solution_1_top_down.py
```

### 思路

站在当前节点 `root` 上：

1. 计算左子树高度
2. 计算右子树高度
3. 得到经过当前节点的直径：`left_height + right_height`
4. 递归计算左子树内部的直径
5. 递归计算右子树内部的直径
6. 取三者最大值

代码：

```python
def diameterOfBinaryTree(self, root):
    if root is None:
        return 0

    left_height = self.height(root.left)
    right_height = self.height(root.right)

    current_diameter = left_height + right_height
    subtree_diameter = max(
        self.diameterOfBinaryTree(root.left),
        self.diameterOfBinaryTree(root.right),
    )

    return max(current_diameter, subtree_diameter)
```

### 为什么会重复计算？

例如计算根节点的直径时，先完整计算了一遍左子树高度。

接着递归进入左子树，又会重新计算左子树下面的高度。

同一批节点被多次访问，所以最坏时间复杂度是：

```text
O(n^2)
```

这个方法适合用来理解“直径要比较三种情况”，但不适合作为最终面试答案。

## 解法 2：后序 DFS（面试推荐）

对应文件：

```text
10_二叉树/10_q543/solution_2_postorder.py
```

### 关键转变：一次递归返回两个结果中的一个

每个节点需要参与两件事：

```text
1. 告诉父节点：我这棵子树有多高
2. 更新答案：经过我自己的路径是否刷新了全局最大直径
```

递归函数只能直接 `return` 一个值，所以让它返回最重要、父节点还需要的信息：

```text
当前子树的高度
```

直径用外部变量 `ans` 保存，因为它是整棵树的全局答案。

### 为什么必须后序？

当前节点的直径需要：

```python
left_height + right_height
```

所以必须先知道左子树和右子树的高度，再处理当前节点：

```python
left_height = height(node.left)
right_height = height(node.right)
ans = max(ans, left_height + right_height)
```

这就是后序顺序：

```text
左子树 -> 右子树 -> 当前节点
```

### 代码

```python
ans = 0

def height(node):
    nonlocal ans

    if node is None:
        return 0

    left_height = height(node.left)
    right_height = height(node.right)

    ans = max(ans, left_height + right_height)

    return 1 + max(left_height, right_height)

height(root)
return ans
```

### 用例走一遍

以这棵树为例：

```text
      1
     / \
    2   3
   / \
  4   5
```

调用：

```text
height(1)
```

先进入左子树：

```text
height(2)
```

再进入 `2` 的左子树：

```text
height(4)
```

节点 `4` 的左右孩子都是空：

```text
left_height = 0
right_height = 0
ans = max(0, 0 + 0) = 0
return 1 + max(0, 0) = 1
```

回到节点 `2` 后，再处理右子树 `5`：

```text
height(5) = 1
```

此时节点 `2` 得到：

```text
left_height = 1
right_height = 1
ans = max(0, 1 + 1) = 2
return 1 + max(1, 1) = 2
```

这里 `ans = 2` 对应路径：

```text
4 -> 2 -> 5
```

回到节点 `1` 后处理右子树 `3`：

```text
height(3) = 1
```

节点 `1` 得到：

```text
left_height = 2
right_height = 1
ans = max(2, 2 + 1) = 3
return 1 + max(2, 1) = 3
```

最终：

```text
ans = 3
```

对应路径：

```text
4 -> 2 -> 1 -> 3
```

### `return` 和 `ans` 分别表示什么？

这是本题最关键的区分：

```python
return 1 + max(left_height, right_height)
```

返回给父节点的是：

```text
当前节点向下能提供的最长单边高度
```

当前节点只能选择左边或右边的一条路继续向上，不能同时把左右两边都交给父节点。

而：

```python
ans = max(ans, left_height + right_height)
```

记录的是：

```text
以当前节点为拐点，左右两边拼起来的完整路径
```

所以：

```text
return：给父节点使用的一条边向下路径
ans：当前节点作为拐点时的完整路径
```

### 复杂度

每个节点只访问一次：

```text
时间复杂度：O(n)
```

递归调用栈最多达到树高：

```text
空间复杂度：O(h)
```

## 面试推荐

面试最推荐方法二：后序 DFS。

面试时可以这样解释：

> 我用后序 DFS 计算每棵子树的高度。对当前节点，左子树高度加右子树高度就是经过当前节点的最长路径，用它更新全局答案。然后向父节点返回 `1 + max(left_height, right_height)`，因为父节点只能选择当前节点的一侧继续延伸。每个节点访问一次，时间复杂度 `O(n)`，递归栈空间 `O(h)`。

## 常见错误

### 1. 把直径当成高度

高度是一条从当前节点向下的单边路径；直径可以从左子树经过当前节点连接到右子树。

```text
高度：当前节点 -> 某个后代
直径：左侧后代 -> 当前节点 -> 右侧后代
```

### 2. 只计算经过根节点的路径

直径可能完全位于某个子树中，所以必须在每个节点更新 `ans`。

### 3. 把节点数当成直径

题目返回边数。`left_height + right_height` 在当前高度定义下正好得到边数，不需要再加 1。
