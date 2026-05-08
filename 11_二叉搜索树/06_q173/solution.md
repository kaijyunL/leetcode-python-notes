# LeetCode 173 - 二叉搜索树迭代器

## 题目

设计一个二叉搜索树迭代器 `BSTIterator`，它需要支持：

```text
BSTIterator(root)  初始化迭代器
next()             返回 BST 中当前最小的还未访问节点的值
hasNext()          如果迭代器中还有节点，返回 True，否则返回 False
```

要求：

```text
next() 和 hasNext() 的平均时间复杂度都应该接近 O(1)
```

---

## 先抓住这题的本质

这题表面上是在“设计一个迭代器”，但本质还是 BST 的中序遍历。

BST 的中序遍历顺序是：

```text
左 -> 根 -> 右
```

而 BST 的性质决定了：

```text
中序遍历结果一定是升序
```

所以这题要做的事情其实就是：

```text
把 BST 按升序一个一个吐出来
```

关键是：

```text
不能每次 next() 都重新从根遍历
```

否则就太慢了。

---

## 解法总览

我们按“从简单到最优”的顺序来理解：

1. 先把整棵树中序遍历出来，存到数组里
2. 用栈懒加载中序遍历，边走边输出

其中最适合面试的是：

```text
解法二：栈懒加载中序遍历
```

因为它：

1. 真正利用了 BST 中序有序的性质
2. `next()` 和 `hasNext()` 都很自然
3. 不需要一次性把所有节点都存下来
4. 是这题最经典、最稳的写法

---

## 解法一：先中序遍历整棵树，存成数组

对应文件：

```text
11_二叉搜索树/06_q173/solution_1_flatten.py
```

### 思路

这个方法最直接：

1. 构造迭代器时，先把整个 BST 做一次中序遍历
2. 把结果存到数组里
3. `next()` 就返回数组当前下标对应的值
4. `hasNext()` 就判断下标有没有越界

### 为什么这样做是对的

因为 BST 的中序遍历是升序，所以提前把所有值都排好序存起来，后面就可以直接按顺序返回。

### 代码

```python
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        """
        解法1：先展开成中序数组
        时间复杂度：初始化 O(n)，next / hasNext 都是 O(1)
        空间复杂度：O(n)
        """
        self.values: list[int] = []
        self.index = 0

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inorder(node.left)
            self.values.append(node.val)
            inorder(node.right)

        inorder(root)

    def next(self) -> int:
        val = self.values[self.index]
        self.index += 1
        return val

    def hasNext(self) -> bool:
        return self.index < len(self.values)
```

### 复杂度

```text
时间复杂度：
初始化 O(n)
next() O(1)
hasNext() O(1)

空间复杂度：O(n)
```

### 优缺点

优点：

```text
实现简单，几乎不会写错
```

缺点：

```text
初始化时要把所有节点都存起来，空间比较大
```

所以这个方法适合帮助你快速理解题意，但不是这题最优的面试写法。

---

## 解法二：栈懒加载中序遍历

对应文件：

```text
11_二叉搜索树/06_q173/solution_2_stack_iterator.py
```

## 这是最适合面试的解法

它的核心思想是：

```text
不一次性遍历整棵树，
而是把“当前还没访问到的最左路径”压到栈里，
每次 next() 只处理一个节点。
```

这其实就是把递归中序遍历改写成了手动维护栈。

---

## 先理解中序遍历怎么“懒加载”

中序遍历是：

```text
一路往左走
左边走到底后，访问当前节点
然后转向右子树
```

如果把这个过程模拟成代码，就会发现：

1. 左边走到底之前，沿途的节点都要先压栈
2. 弹栈时访问当前节点
3. 然后把右子树的左边路径再压栈

这样每次 `next()` 都只是推进一小步，而不是从头遍历整棵树。

---

## 栈里存的是什么

栈里存的是：

```text
当前还没有被访问，但未来一定要访问的节点
```

更准确一点说：

```text
栈顶永远是当前最小的“未访问节点”之一
```

这就是为什么每次 `next()` 都可以直接弹栈拿到下一个值。

---

## 初始化时做什么

初始化时，我们只做一件事：

```text
把根节点一路向左的路径全部压栈
```

因为 BST 的最小值一定在最左边，所以这条链路上的节点就是当前最先可能被访问的节点。

---

## next() 怎么写

`next()` 分两步：

1. 弹出栈顶，这个节点就是当前访问的节点
2. 如果它有右子树，就把右子树的最左路径压栈

为什么要处理右子树？

因为中序遍历的顺序是：

```text
左 -> 根 -> 右
```

当前节点访问完后，下一批应该访问的就是它右子树里的最左节点。

---

## hasNext() 怎么写

很简单：

```text
只要栈不空，就说明还有节点没访问
```

所以：

```python
return bool(stack)
```

---

## 代码

```python
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        """
        解法2：栈懒加载中序遍历
        时间复杂度：初始化 O(h)，next / hasNext 均摊 O(1)
        空间复杂度：O(h)
        """
        self.stack: list[TreeNode] = []
        self._push_left(root)

    def _push_left(self, node: Optional[TreeNode]) -> None:
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return bool(self.stack)
```

---

## 用例子手动走一遍

还是看这棵树：

```text
      7
     / \
    3   15
       /  \
      9   20
```

### 初始化

把最左路径压栈：

```text
stack = [7, 3]
```

这时栈顶是 `3`，所以第一个 `next()` 应该返回 `3`。

### 第一次 next()

弹出 `3`：

```text
返回 3
```

`3` 没有右子树，所以栈还是：

```text
stack = [7]
```

### 第二次 next()

弹出 `7`：

```text
返回 7
```

`7` 的右子树是 `15`，把 `15` 的最左路径压栈：

```text
stack = [15, 9]
```

### 第三次 next()

弹出 `9`：

```text
返回 9
```

### 后面继续

依次会得到：

```text
15, 20
```

整体输出就是：

```text
3, 7, 9, 15, 20
```

正好是 BST 的升序序列。

---

## 复杂度

```text
时间复杂度：
初始化 O(h)
next() 均摊 O(1)
hasNext() O(1)

空间复杂度：O(h)
```

其中 `h` 是树高。

对于平衡 BST，`h = O(log n)`。

---

## 两种解法怎么选

### 学习顺序

建议按这个顺序掌握：

1. 先理解“整棵树中序展开成数组”
2. 再掌握“栈懒加载中序遍历”

### 面试顺序

面试里建议这样表达：

1. 先说明 BST 的中序遍历是升序
2. 如果每次都重新遍历整棵树，太慢
3. 所以可以用栈模拟中序遍历
4. 初始化时把根到最左节点的路径压栈
5. 每次 `next()` 弹出栈顶节点，再处理它的右子树
6. `hasNext()` 只需要判断栈是否为空

这样会显得你的思路很完整，而且能自然说明为什么它是均摊 O(1)。

---

## 面试表达模板

你可以直接这样说：

```text
这题本质上是把 BST 按中序遍历的顺序依次输出。
因为 BST 的中序遍历是升序，所以 next() 就应该返回当前最小的未访问节点。

最直接的方法是先把整棵树中序遍历到数组里，
这样 next() 和 hasNext() 都是 O(1)，但空间是 O(n)。

更好的做法是用栈模拟中序遍历，
初始化时把根到最左节点的路径压栈，
每次 next() 弹出栈顶节点，
然后把它右子树的最左路径继续压栈。

这样 hasNext() 只要看栈是否为空，
next() 也能做到均摊 O(1)，空间是 O(h)。
```

---

## 总结

这题真正考的不是“会不会写一个迭代器”，而是：

```text
你能不能把 BST 的中序有序性，转化成一个可持续输出的迭代结构。
```

所以你要记住这两层：

1. 数组预处理法帮助你理解题意
2. 栈懒加载中序遍历是这题最适合面试的主力写法
