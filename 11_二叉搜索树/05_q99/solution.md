# LeetCode 99 - 恢复二叉搜索树

## 题目

给你一棵二叉搜索树，它的两个节点值被错误地交换了，请你恢复这棵树。

要求你：

```text
不改变树的结构，只恢复被交换的两个节点
```

---

## 先抓住这题的本质

BST 的中序遍历结果本来应该是严格递增的。

但是现在有两个节点被交换了，所以中序序列里一定会出现“逆序”的情况。

例如本来应该是：

```text
1, 2, 3, 4, 5
```

如果把 `2` 和 `4` 交换后，可能变成：

```text
1, 4, 3, 2, 5
```

这里就出现了逆序：

```text
4 > 3
3 > 2
```

这道题的核心就是：

```text
在中序遍历过程中找出那两个错位的节点，然后把它们的值交换回来
```

---

## 解法总览

我们按“从简单暴力到最优”的顺序来理解：

1. 中序遍历收集所有值，排序后重写回树
2. 中序遍历找出错位的两个节点，再交换它们的值
3. Morris 中序遍历，做到 O(1) 额外空间

其中最适合面试的是：

```text
解法二：中序遍历找出错位的两个节点
```

因为它直接利用了 BST 的中序有序性质，而且不需要额外数组。

---

## 解法一：中序遍历 + 排序后重写

对应文件：

```text
11_二叉搜索树/05_q99/solution_1_inorder_sort.py
```

### 思路

这个方法先不考虑“怎么定位错位节点”，而是直接把 BST 当成普通二叉树：

1. 中序遍历整棵树，把所有节点值收集到数组
2. 对数组排序
3. 再做一次中序遍历，把排好序的值依次写回去

因为 BST 的中序遍历本来应该是升序，所以排序后的数组就是正确答案。

### 代码

```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        values = []

        def inorder_collect(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inorder_collect(node.left)
            values.append(node.val)
            inorder_collect(node.right)

        def inorder_write(node: Optional[TreeNode], index: list[int]) -> None:
            if not node:
                return
            inorder_write(node.left, index)
            node.val = values[index[0]]
            index[0] += 1
            inorder_write(node.right, index)

        inorder_collect(root)
        values.sort()
        inorder_write(root, [0])
```

### 复杂度

```text
时间复杂度：O(n log n)
空间复杂度：O(n)
```

### 优缺点

优点：

```text
简单直接，几乎不会写错
```

缺点：

```text
没有利用“只交换了两个节点”这个关键信息
空间也比较大
```

所以这个方法适合入门理解，不适合作为面试主答案。

---

## 解法二：中序遍历找出两个错位节点

对应文件：

```text
11_二叉搜索树/05_q99/solution_2_inorder_find_swapped.py
```

## 这是最适合面试的解法

它利用了一个非常关键的观察：

```text
BST 的中序遍历本来应该严格递增
```

如果有两个节点被交换了，那么中序序列里一定会出现逆序对。

### 逆序对长什么样

假设中序遍历时依次访问到：

```text
1, 4, 3, 2, 5
```

这里会出现：

```text
4 > 3
3 > 2
```

这说明：

1. `4` 是一个异常大的值，应该属于后面
2. `2` 是一个异常小的值，应该属于前面

所以我们要找的就是：

```text
第一个“太大”的节点 + 最后一个“太小”的节点
```

然后交换它们的值即可。

---

## 为什么只要找两个节点

这题只交换了两个节点的值，所以中序序列的异常通常表现为：

1. 一次逆序，说明两个交换节点相邻
2. 两次逆序，说明两个交换节点不相邻

无论哪种情况：

```text
第一个逆序里前面的那个节点，是较大的错节点
最后一个逆序里后面的那个节点，是较小的错节点
```

这两个节点就是答案。

---

## 递归中序的判断逻辑

中序遍历时维护三个东西：

1. `prev`：上一个访问的节点
2. `first`：第一次发现逆序时的大节点
3. `second`：每次发现逆序时更新的小节点

遍历到当前节点 `cur` 时：

```text
如果 prev.val > cur.val，
说明出现逆序
```

此时：

1. 如果 `first` 还没找到，就把 `first` 记成 `prev`
2. 把 `second` 记成 `cur`

然后继续遍历。

为什么 `second` 要反复更新？

因为如果有两次逆序，最后一个逆序里的小节点才是最终真正该交换的那个节点。

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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = None
        second = None
        prev = None

        def inorder(node: Optional[TreeNode]) -> None:
            nonlocal first, second, prev
            if not node:
                return

            inorder(node.left)

            if prev and prev.val > node.val:
                if first is None:
                    first = prev
                second = node

            prev = node

            inorder(node.right)

        inorder(root)

        if first and second:
            first.val, second.val = second.val, first.val
```

---

## 用例子手动走一遍

看这个 BST：

```text
    3
   / \
  1   4
     /
    2
```

如果把 `2` 和 `3` 交换后，树变成：

```text
    2
   / \
  1   4
     /
    3
```

中序遍历结果是：

```text
1, 2, 3, 4
```

这个例子里如果交换的是根和叶子，逆序会出现在不同位置。

再看一个更典型的例子：

```text
    3
   / \
  1   4
     /
    2
```

中序遍历应该是：

```text
1, 2, 3, 4
```

但现在变成了：

```text
1, 3, 2, 4
```

遍历过程：

1. 先访问 `1`
2. 再访问 `3`
3. 然后访问 `2`

此时发现：

```text
3 > 2
```

于是：

1. `first = 3`
2. `second = 2`

遍历结束后交换它们，就恢复了 BST。

---

## 复杂度

```text
时间复杂度：O(n)
空间复杂度：O(h)
```

其中 `h` 是树高。

如果 BST 平衡，则空间一般是：

```text
O(log n)
```

---

## 解法三：Morris 中序遍历

对应文件：

```text
11_二叉搜索树/05_q99/solution_3_morris.py
```

### 思路

这一版和解法二的核心思路完全一样：

```text
还是中序遍历，还是找 first / second
```

区别只在于：

```text
不用递归，也不用显式栈
```

而是通过 Morris 遍历在树上临时建立“线索”来完成中序遍历。

### 为什么它能做到 O(1) 空间

因为它利用了树上原本空着的指针位置，临时把前驱节点和当前节点连起来，遍历完再恢复。

所以它的额外空间是常数级。

---

## Morris 版本怎么理解

对于当前节点 `cur`：

1. 如果 `cur.left` 为空，直接访问当前节点，然后走到右子树
2. 如果 `cur.left` 不为空，就去找左子树中最右边的节点 `pred`
3. 如果 `pred.right` 为空，说明还没建立过线索，就让 `pred.right = cur`，然后往左走
4. 如果 `pred.right == cur`，说明左子树已经处理完了，就把线索断开，访问当前节点，再往右走

这样就能不借助栈完成中序遍历。

### 代码

```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = None
        second = None
        prev = None
        cur = root

        while cur:
            if not cur.left:
                if prev and prev.val > cur.val:
                    if first is None:
                        first = prev
                    second = cur
                prev = cur
                cur = cur.right
            else:
                pred = cur.left
                while pred.right and pred.right != cur:
                    pred = pred.right

                if not pred.right:
                    pred.right = cur
                    cur = cur.left
                else:
                    pred.right = None
                    if prev and prev.val > cur.val:
                        if first is None:
                            first = prev
                        second = cur
                    prev = cur
                    cur = cur.right

        if first and second:
            first.val, second.val = second.val, first.val
```

### 复杂度

```text
时间复杂度：O(n)
空间复杂度：O(1)
```

---

## 哪个最适合面试

最适合面试的是：

```text
解法二：中序遍历找出两个错位节点
```

原因很简单：

1. 它直接抓住了 BST 中序有序这个本质
2. 代码比 Morris 更稳，不容易写崩
3. 时间是 O(n)，空间是 O(h)，已经足够好
4. 面试里通常优先考虑“清晰且正确”的解法，而不是强行上最难的 Morris

Morris 可以作为加分项提一下，但不建议作为第一主解。

---

## 面试表达模板

你可以直接这样说：

```text
这题的核心是 BST 的中序遍历应该严格递增。
如果有两个节点被交换了，中序序列里一定会出现逆序对。

我只需要在中序遍历过程中记录：
第一个逆序里前面的那个较大节点 first，
以及每次逆序里后面的那个较小节点 second。

如果两个交换节点相邻，只会出现一次逆序；
如果不相邻，会出现两次逆序，
但 first 仍然是第一次逆序中的大节点，
second 需要更新成最后一次逆序中的小节点。

最后交换 first 和 second 的值即可恢复 BST。
```

---

## 总结

这题真正考的是：

```text
你能不能从 BST 的中序有序性里，直接定位出那两个被交换的节点。
```

所以你要记住这三层：

1. 暴力重写能帮助你理解“恢复”到底在做什么
2. 中序找错位节点是这题的主力方法，也是最适合面试的版本
3. Morris 是空间最优版，属于进阶加分项
