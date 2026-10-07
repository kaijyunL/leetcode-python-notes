# LeetCode 226 - 翻转二叉树（Invert Binary Tree）

## 题目

给定一棵二叉树，翻转它，并返回翻转后的根节点。

翻转的意思是：

```text
每个节点的左子树和右子树互换
```

例如：

```text
原树：                 翻转后：
      4                      4
     / \                    / \
    2   7                  7   2
   / \ / \                / \ / \
  1  3 6  9              9  6 3  1
```

输入可以写成层序数组：

```text
输入：[4, 2, 7, 1, 3, 6, 9]
输出：[4, 7, 2, 9, 6, 3, 1]
```

## 先建立直觉

翻转一棵树，不是只交换根节点的左右孩子。

```text
交换根节点的左右子树
交换左子树内部的左右子树
交换右子树内部的左右子树
```

也就是：

```text
每到一个节点，就交换它的 left 和 right
然后继续处理它的两个孩子
```

把一个节点看成一个“开关”：

```text
翻转前：node.left  -> 左边
         node.right -> 右边

翻转后：node.left  -> 原来的右边
         node.right -> 原来的左边
```

空节点没有左右子树，不需要处理。

## 从递归关系推导

站在当前节点 `root` 上，只需要问三个问题：

1. 当前节点是空节点吗？如果是，直接返回 `None`。
2. 当前节点的左右子树要不要交换？要。
3. 交换之后，两个子树内部要不要继续翻转？要。

所以递归结构就是：

```python
if root is None:
    return None

root.left, root.right = root.right, root.left
self.invertTree(root.left)
self.invertTree(root.right)
return root
```

这里的顺序很重要：先交换，再递归处理交换后的左右子树。

例如原来：

```text
root.left  = A
root.right = B
```

交换以后：

```text
root.left  = B
root.right = A
```

接下来递归处理的就是 `B` 和 `A`，也就是翻转后的两个子树位置。

## 用 `n = 3` 展开递归

原树：

```text
    2
   / \
  1   3
```

进入：

```text
invertTree(2)
```

当前：

```text
root = 2
root.left = 1
root.right = 3
```

先交换：

```text
root.left = 3
root.right = 1
```

树变成：

```text
    2
   / \
  3   1
```

然后继续执行：

```text
invertTree(3)
```

节点 `3` 没有孩子，交换前后没有变化；继续递归它的左右孩子：

```text
invertTree(None) -> 返回 None
invertTree(None) -> 返回 None
```

回到节点 `2`，继续执行：

```text
invertTree(1)
```

节点 `1` 也没有孩子，同样返回。

最终得到：

```text
    2
   / \
  3   1
```

这里要注意：递归返回后，程序不是从头开始，而是回到调用递归的下一行继续执行。

## `n = 4` 的递归层级

原树：

```text
      4
     / \
    2   7
   / \ / \
  1  3 6  9
```

递归层级可以画成：

```text
F0: invertTree(4)
├── 先交换 4 的左右子树
│   当前变成：
│       4
│      / \
│     7   2
│
├── F1: invertTree(7)
│   ├── 交换 7 的左右子树：9、6
│   ├── invertTree(9)
│   │   ├── invertTree(None)
│   │   └── invertTree(None)
│   └── invertTree(6)
│       ├── invertTree(None)
│       └── invertTree(None)
│
└── F1: invertTree(2)
    ├── 交换 2 的左右子树：3、1
    ├── invertTree(3)
    │   ├── invertTree(None)
    │   └── invertTree(None)
    └── invertTree(1)
        ├── invertTree(None)
        └── invertTree(None)
```

注意这里的关键顺序：

```text
F0 先交换 4
F0 递归处理交换后的左孩子 7
F1 处理完 7 后返回 F0
F0 再递归处理交换后的右孩子 2
```

每一层都重复同一个动作：

```text
交换当前节点的左右孩子
递归处理左孩子
递归处理右孩子
返回当前节点
```

## 解法一览

| 解法 | 思路 | 时间复杂度 | 空间复杂度 | 是否推荐面试 |
|---|---|---|---|---|
| 1. 递归 DFS | 每个节点交换左右孩子，再递归处理子树 | `O(n)` | `O(h)` | **最适合面试 ✅** |
| 2. 显式栈迭代 | 用栈模拟递归，弹出节点后交换左右孩子 | `O(n)` | `O(h)` | 迭代补充 |

其中：

```text
n：节点总数
h：树的高度
```

## 解法 1：递归 DFS（面试推荐）

对应文件：

```text
10_二叉树/05_q226/solution_1_recursive.py
```

代码：

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
```

### 为什么面试推荐递归？

因为题目本身就是一个递归定义：

```text
翻转整棵树
= 交换根节点的左右子树
  + 翻转左子树
  + 翻转右子树
```

代码短，状态也简单：当前函数只需要关注当前节点。它不需要保存额外的路径、深度或全局变量。

### 复杂度

每个节点都会被访问一次，并且只做一次左右交换：

```text
时间复杂度：O(n)
```

递归调用栈的最大深度等于树高：

```text
空间复杂度：O(h)
```

平衡树的 `h` 大约是 `log n`，退化成链表时 `h = n`。

## 解法 2：显式栈迭代

对应文件：

```text
10_二叉树/05_q226/solution_2_iterative_stack.py
```

递归版本中，系统调用栈帮我们保存“之后还要处理哪些节点”。迭代版本用自己的 `stack` 保存这些节点：

```python
if root is None:
    return None

stack = [root]

while stack:
    node = stack.pop()
    node.left, node.right = node.right, node.left

    if node.left:
        stack.append(node.left)
    if node.right:
        stack.append(node.right)

return root
```

每次从栈中取出一个节点：

```text
交换它的左右孩子
把两个孩子放入栈
继续处理栈中的节点
```

这里交换之后再入栈，所以入栈的是交换后的左右子树；两者最终都会被处理，顺序不影响结果。

## 递归和迭代的对应关系

递归版本：

```python
交换当前节点
递归处理左子树
递归处理右子树
```

迭代版本：

```python
弹出当前节点
交换当前节点
把左右子树压入 stack
```

两种写法做的是同一件事：每个节点只交换一次。

## 常见错误

### 1. 只交换根节点

错误思路：

```python
root.left, root.right = root.right, root.left
return root
```

这只能交换根节点，根节点下面的子树内部还没有翻转。

### 2. 交换后使用旧变量导致处理错误

下面这种写法容易把同一个新子树处理两次：

```python
root.left = self.invertTree(root.right)
root.right = self.invertTree(root.left)
```

第一行执行后，`root.left` 已经变成翻转后的原右子树，第二行再处理 `root.left` 就不是原来的左子树了。

安全写法是先整体交换：

```python
root.left, root.right = root.right, root.left
```

再递归处理两个孩子。

### 3. 忘记处理空树

```python
if root is None:
    return None
```

空树没有节点可以交换，应该直接返回。

## 最终推荐

面试时优先写递归 DFS：

```python
def invertTree(self, root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root
```

向面试官解释：

> 我按节点处理。当前节点为空时直接返回；否则交换它的左右子树，再递归翻转交换后的两个子树。每个节点访问一次，所以时间复杂度是 `O(n)`，递归栈空间是 `O(h)`。
