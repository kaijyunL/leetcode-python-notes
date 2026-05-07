# LeetCode 235 - 二叉搜索树的最近公共祖先

## 题目

给定一个二叉搜索树 `BST` ，找到该树中两个指定节点 `p` 和 `q` 的最近公共祖先。

最近公共祖先（LCA, Lowest Common Ancestor）的定义是：

```text
对于有根树 T 的两个节点 p、q，
最近公共祖先表示为一个节点 x，
满足 x 是 p、q 的祖先，
并且 x 的深度尽可能大。
```

题目还特别说明：

```text
一个节点也可以是它自己的祖先。
```

---

## 先抓住这题的本质

BST 最重要的性质是：

```text
左子树所有节点值 < 根节点值 < 右子树所有节点值
```

这个性质会直接决定我们怎么找最近公共祖先。

对于当前节点 `root`：

1. 如果 `p.val` 和 `q.val` 都比 `root.val` 小，答案一定在左子树
2. 如果 `p.val` 和 `q.val` 都比 `root.val` 大，答案一定在右子树
3. 如果一个在左边，一个在右边，或者其中一个就是当前节点，那当前节点就是最近公共祖先

整道题最核心的一句话就是：

```text
BST 中，第一个把 p 和 q “分开”的节点，
或者第一次碰到 p / q 本身的那个节点，
就是最近公共祖先。
```

---

## 解法总览

我们按“从简单暴力到最优”的顺序来理解：

1. 记录从根到 `p`、`q` 的路径，再比较最后一个公共节点
2. 利用 BST 性质：递归查找分叉点
3. 利用 BST 性质：迭代查找分叉点

其中最适合面试的是：

```text
解法三：利用 BST 性质的迭代写法
```

因为它：

1. 真正用上了 BST 的有序性质
2. 代码短，逻辑非常直接
3. 不需要额外路径数组
4. 不依赖递归栈，过程更稳

---

## 解法一：分别找路径，再比较最后一个公共节点

对应文件：

```text
11_二叉搜索树/04_q235/solution_1_path_compare.py
```

### 思路

这个方法先不利用 BST 的性质，直接按普通二叉树来做。

步骤是：

1. 找到从根节点到 `p` 的路径
2. 找到从根节点到 `q` 的路径
3. 从前往后比较两条路径
4. 最后一个相同的节点，就是最近公共祖先

### 为什么这样做是对的

因为从根往下走时：

1. 两条路径前面重合的部分，表示它们有共同祖先
2. 一旦开始分开，说明已经走到了分叉点下面
3. 所以“最后一个还相同的节点”，一定就是最近公共祖先

### 代码

```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self,
        root: Optional[TreeNode],
        p: TreeNode,
        q: TreeNode,
    ) -> TreeNode:
        path_p = []
        path_q = []

        def find_path(
            node: Optional[TreeNode],
            target: TreeNode,
            path: list[TreeNode],
        ) -> bool:
            if not node:
                return False

            path.append(node)

            if node == target:
                return True

            if find_path(node.left, target, path) or find_path(node.right, target, path):
                return True

            path.pop()
            return False

        find_path(root, p, path_p)
        find_path(root, q, path_q)

        ancestor = root
        for node_p, node_q in zip(path_p, path_q):
            if node_p != node_q:
                break
            ancestor = node_p

        return ancestor
```

### 复杂度

```text
时间复杂度：O(n)
空间复杂度：O(n)
```

### 优缺点

优点：

```text
非常直观，容易想到
```

缺点：

```text
没有利用 BST 性质
还要额外保存两条路径
```

所以这个方法适合用来建立“最近公共祖先”的基本理解，但不是这题最好的解法。

---

## 解法二：利用 BST 性质递归查找分叉点

对应文件：

```text
11_二叉搜索树/04_q235/solution_2_bst_recursive.py
```

### 思路

现在开始真正利用 BST 的性质。

假设当前在节点 `root`：

1. 如果 `p.val` 和 `q.val` 都小于 `root.val`，说明它们都在左子树里
2. 如果 `p.val` 和 `q.val` 都大于 `root.val`，说明它们都在右子树里
3. 否则，说明它们在当前节点两侧，或者其中一个就是当前节点

第三种情况出现时：

```text
当前节点就是最近公共祖先
```

### 代码

```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self,
        root: Optional[TreeNode],
        p: TreeNode,
        q: TreeNode,
    ) -> TreeNode:
        low = min(p.val, q.val)
        high = max(p.val, q.val)

        if root.val > high:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < low:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
```

### 为什么这个判断非常关键

这里的本质是：

```text
只要 p 和 q 还在同一侧，
最近公共祖先就不可能是当前节点，
必须继续往那一侧走。
```

而一旦当前节点的值落在 `[low, high]` 之间：

```text
low <= root.val <= high
```

就说明：

1. 当前节点正好把 `p` 和 `q` 分在两边
2. 或者当前节点就是 `p` / `q` 之一

这两种情况都意味着：

```text
当前节点就是答案
```

### 复杂度

```text
时间复杂度：O(h)
空间复杂度：O(h)
```

如果 BST 平衡，`h = O(log n)`；
如果 BST 退化成链表，最坏 `h = O(n)`。

---

## 解法三：利用 BST 性质迭代查找分叉点

对应文件：

```text
11_二叉搜索树/04_q235/solution_3_bst_iterative.py
```

## 这是最适合面试的解法

它和递归版的核心逻辑完全一样：

```text
如果 p 和 q 都在当前节点左边，就往左走
如果 p 和 q 都在当前节点右边，就往右走
否则当前节点就是答案
```

只是把递归改成了迭代。

它最适合面试，是因为：

1. 逻辑直接，没有多余结构
2. 清楚展示你理解了 BST 的性质
3. 空间复杂度更好，不用递归栈
4. 写起来短，而且不容易错

---

## 先把“分叉点”这个概念想明白

对 BST 来说，最近公共祖先本质上就是：

```text
从根往下走时，第一个让 p 和 q 不再位于同一侧的节点
```

为什么？

因为：

1. 如果 `p`、`q` 都比当前节点小，那它们一定都在左边
2. 如果 `p`、`q` 都比当前节点大，那它们一定都在右边
3. 只有当它们不再同时落在同一边时，当前节点才可能成为它们共同的“最低汇合点”

这就是“分叉点”的含义。

---

## 一共有三种判断情况

设：

```python
low = min(p.val, q.val)
high = max(p.val, q.val)
```

这样就不需要关心 `p` 和 `q` 谁大谁小。

然后对于当前节点 `cur`：

### 情况一：`cur.val > high`

说明：

```text
p 和 q 都比 cur 小
```

那它们一定都在左子树里，所以：

```python
cur = cur.left
```

### 情况二：`cur.val < low`

说明：

```text
p 和 q 都比 cur 大
```

那它们一定都在右子树里，所以：

```python
cur = cur.right
```

### 情况三：`low <= cur.val <= high`

这时有两种可能：

1. `p` 和 `q` 分别在 `cur` 两侧
2. `cur` 本身就是 `p` 或 `q`

无论哪种情况，`cur` 都是最近公共祖先。

所以直接：

```python
return cur
```

---

## 为什么“一个节点可以是它自己的祖先”很重要

看这个例子：

```text
    6
   / \
  2   8
 / \
0   4
   / \
  3   5
```

如果：

```text
p = 2
q = 4
```

当我们走到节点 `2` 时：

```text
low = 2
high = 4
cur.val = 2
```

满足：

```text
low <= cur.val <= high
```

此时当前节点 `2` 本身就是 `p`，而 `q` 在它的子树里。

根据题意：

```text
一个节点可以是它自己的祖先
```

所以答案就是 `2`，而不是再往下走。

这也是为什么“落在区间里就直接返回”这个判断是完整正确的。

---

## 用例子手动走一遍

看这棵 BST：

```text
        6
      /   \
     2     8
    / \   / \
   0   4 7   9
      / \
     3   5
```

### 例子一：`p = 2, q = 8`

设：

```text
low = 2
high = 8
```

一开始：

```text
cur = 6
```

判断：

```text
6 不大于 8
6 不小于 2
所以 2 <= 6 <= 8
```

说明：

```text
p 和 q 已经分在当前节点两侧
```

所以答案直接是：

```text
6
```

### 例子二：`p = 2, q = 4`

设：

```text
low = 2
high = 4
```

第一步：

```text
cur = 6
6 > 4
```

说明 `p` 和 `q` 都在左边，所以：

```python
cur = cur.left = 2
```

第二步：

```text
cur = 2
2 不大于 4
2 不小于 2
所以 2 <= 2 <= 4
```

这说明当前节点已经是分叉点，或者就是 `p` / `q` 本身。

因此答案就是：

```text
2
```

---

## 代码

```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self,
        root: Optional[TreeNode],
        p: TreeNode,
        q: TreeNode,
    ) -> TreeNode:
        low = min(p.val, q.val)
        high = max(p.val, q.val)
        cur = root

        while cur:
            if cur.val > high:
                cur = cur.left
            elif cur.val < low:
                cur = cur.right
            else:
                return cur
```

---

## 复杂度

```text
时间复杂度：O(h)
空间复杂度：O(1)
```

其中 `h` 是树高。

如果是平衡 BST，时间复杂度通常是：

```text
O(log n)
```

最坏退化成链表时才会到：

```text
O(n)
```

---

## 三种解法怎么选

### 学习顺序

建议按这个顺序掌握：

1. 先理解“路径比较法”，建立最近公共祖先的基本概念
2. 然后学会“BST 递归分叉点判断”
3. 最后把它写成“BST 迭代版”，作为主力解法

### 面试顺序

面试里建议这样表达：

1. 先说明 BST 的有序性质决定了查找方向
2. 如果 `p`、`q` 都在同一侧，就继续往那一侧走
3. 第一次出现“不在同一侧”时，当前节点就是最近公共祖先
4. 这个过程可以递归写，也可以迭代写

这样会显得你的思路很完整，而且能体现你会“从通用思路升级到针对性最优解法”。

---

## 面试表达模板

你可以直接这样说：

```text
这题的关键是 BST 的有序性质。
如果 p 和 q 都比当前节点小，答案一定在左子树；
如果都比当前节点大，答案一定在右子树；
否则当前节点就是最近公共祖先。

所以我们只需要从根开始不断往下走，
找到第一个把 p 和 q 分开的节点即可。

BST 版本的递归和迭代都可以这么做，
但迭代写法更简洁，空间复杂度还能做到 O(1)。
```

---

## 总结

这题真正考的不是“LCA 会不会写”，而是：

```text
你能不能根据 BST 的性质，
把路径类思路优化成只沿一条路径查找的 O(h) 思路。
```

所以要记住这几个层次：

1. 路径比较法能帮助你理解什么叫最近公共祖先
2. BST 版的关键是判断 `p`、`q` 是否都在当前节点同一侧
3. 迭代版是这题最适合面试的主力写法
