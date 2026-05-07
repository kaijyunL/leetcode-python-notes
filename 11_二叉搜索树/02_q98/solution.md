# LeetCode 98 - 验证二叉搜索树

## 题目

给你一个二叉树的根节点 `root` ，判断其是否是一个有效的二叉搜索树（BST）。

二叉搜索树要求：

```text
1. 节点左子树只包含小于当前节点的数
2. 节点右子树只包含大于当前节点的数
3. 左右子树也必须分别是二叉搜索树
```

注意这里是：

```text
严格小于 / 严格大于
```

也就是说，重复值不允许出现在 BST 中。

---

## 这题最容易踩的坑

很多人一开始会写成：

```python
if node.left and node.left.val >= node.val:
    return False
if node.right and node.right.val <= node.val:
    return False
```

这个思路不够，因为它只检查了：

```text
当前节点 和 它的直接孩子
```

但 BST 的约束其实是：

```text
整棵左子树都要小于当前节点
整棵右子树都要大于当前节点
```

例如这棵树：

```text
    5
   / \
  1   4
     / \
    3   6
```

节点 `4` 的左孩子 `3` 确实小于 `4`，右孩子 `6` 也大于 `4`。

但整棵树仍然不是 BST，因为：

```text
3 在 5 的右子树里，却小于 5
```

所以这题的关键不是“父子关系”，而是“整棵子树的合法范围”。

---

## 解法总览

我们按“从简单暴力到最优”的顺序来理解：

1. 暴力递归：每个节点都去检查左子树最大值、右子树最小值
2. 中序遍历 + 存数组：利用 BST 中序遍历严格递增
3. 递归传上下界：直接维护每个节点允许落入的范围

其中最适合面试的是：

```text
解法三：递归传上下界
```

因为它最能体现你对 BST 定义的真正理解，而且时间、空间都很好。

---

## 解法一：暴力递归检查子树最值

对应文件：

```text
11_二叉搜索树/02_q98/solution_1_bruteforce.py
```

### 思路

对每个节点 `node`：

1. 找到左子树里的最大值 `left_max`
2. 找到右子树里的最小值 `right_min`
3. 判断：

```text
left_max < node.val < right_min
```

4. 再递归判断左右子树本身是不是 BST

### 为什么可行

因为 BST 定义本来就是：

```text
左子树所有值 < 根节点 < 右子树所有值
```

这个方法是最“硬查”的方式，直接把定义翻译成代码。

### 代码

```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def get_min(node: Optional[TreeNode]) -> float:
            if not node:
                return float("inf")
            return min(node.val, get_min(node.left), get_min(node.right))

        def get_max(node: Optional[TreeNode]) -> float:
            if not node:
                return float("-inf")
            return max(node.val, get_max(node.left), get_max(node.right))

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return True

            if get_max(node.left) >= node.val:
                return False
            if get_min(node.right) <= node.val:
                return False

            return dfs(node.left) and dfs(node.right)

        return dfs(root)
```

### 复杂度

```text
时间复杂度：最坏 O(n^2)
空间复杂度：O(h)
```

其中 `h` 是树高。

### 为什么慢

因为每到一个节点，我们都要重新遍历它的整棵左子树或右子树去找最值。

这就会出现大量重复计算。

### 适合什么时候掌握

这个方法适合拿来“入门理解定义”，但不适合作为面试主答案。

---

## 解法二：中序遍历 + 存数组

对应文件：

```text
11_二叉搜索树/02_q98/solution_2_inorder.py
```

### 思路

BST 的一个核心性质是：

```text
中序遍历结果一定严格递增
```

所以我们可以：

1. 对整棵树做中序遍历
2. 把结果存到数组里
3. 检查数组是否严格递增

如果严格递增，就是 BST；否则不是。

### 为什么可行

因为中序遍历顺序是：

```text
左 -> 根 -> 右
```

而 BST 恰好满足：

```text
左边都比根小，右边都比根大
```

所以中序遍历出来的序列一定从小到大排列。

反过来，如果一棵二叉树的中序序列不是严格递增，那它一定不是 BST。

### 代码

```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        for i in range(1, len(values)):
            if values[i] <= values[i - 1]:
                return False

        return True
```

### 复杂度

```text
时间复杂度：O(n)
空间复杂度：O(n)
```

### 优点

这个方法非常直观，也很常见。

### 缺点

缺点在于：

```text
需要额外数组保存所有节点值
```

虽然时间已经是最优，但空间还可以再优化。

---

## 解法三：递归传上下界

对应文件：

```text
11_二叉搜索树/02_q98/solution_3_bounds.py
```

### 这是最适合面试的解法

原因有三个：

1. 它直接对应 BST 的定义，而不是“顺便利用某个性质”
2. 时间复杂度是 `O(n)`
3. 额外空间只需要递归栈 `O(h)`，比存整条中序数组更省

---

## 先理解“范围”这件事

我们不要只盯着“当前节点和父节点”的大小关系，而要看：

```text
当前节点允许出现在哪个数值范围内
```

例如根节点是 `5`：

```text
root = 5
```

那么：

1. 左子树所有节点都必须 `< 5`
2. 右子树所有节点都必须 `> 5`

如果走到右子树里的某个节点，比如 `4`，那它虽然可能小于它自己的父节点或和父节点关系看起来没问题，但它只要：

```text
不大于 5
```

就已经违法了。

所以每个节点都不只是受“父节点”约束，而是受“从根走到它这一整条路径上的所有边界”约束。

---

## 递归怎么设计

我们定义函数：

```python
dfs(node, lower, upper)
```

含义是：

```text
当前节点 node 的值，必须严格落在 (lower, upper) 这个范围里
```

也就是：

```text
lower < node.val < upper
```

然后分三步：

### 第一步：当前节点为空

空树当然是合法 BST：

```python
if not node:
    return True
```

### 第二步：当前值越界

如果当前节点不在合法范围里，直接返回 `False`：

```python
if lower is not None and node.val <= lower:
    return False
if upper is not None and node.val >= upper:
    return False
```

### 第三步：递归左右子树

对于左子树：

```text
它的上界变成当前节点值 node.val
```

因为左子树所有节点都必须小于当前节点。

对于右子树：

```text
它的下界变成当前节点值 node.val
```

因为右子树所有节点都必须大于当前节点。

所以递归是：

```python
return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(
            node: Optional[TreeNode],
            lower: Optional[int],
            upper: Optional[int],
        ) -> bool:
            if not node:
                return True

            if lower is not None and node.val <= lower:
                return False
            if upper is not None and node.val >= upper:
                return False

            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

        return dfs(root, None, None)
```

---

## 用例子走一遍

以这棵非法树为例：

```text
    5
   / \
  1   4
     / \
    3   6
```

### 根节点 5

调用：

```python
dfs(5, None, None)
```

说明 `5` 没有上下界限制，合法。

### 左子树 1

调用：

```python
dfs(1, None, 5)
```

说明 `1` 必须小于 `5`，它满足。

### 右子树 4

调用：

```python
dfs(4, 5, None)
```

说明 `4` 必须大于 `5`。

但 `4 <= 5`，立刻返回 `False`。

这正是这题最关键的地方：

```text
4 虽然是 5 的右孩子，但它本身已经不满足 > 5
```

更深层的节点也同理，都会继承祖先传下来的限制。

---

## 复杂度

```text
时间复杂度：O(n)
空间复杂度：O(h)
```

其中：

1. `n` 是节点总数，每个节点只访问一次
2. `h` 是树高，递归栈深度最多是树高

平衡树时 `h = O(log n)`，极端退化链表时 `h = O(n)`。

---

## 三种解法怎么选

### 如果你在自己学习

建议顺序：

1. 先理解暴力法，吃透 BST 定义
2. 再理解中序递增这个性质
3. 最后掌握上下界递归，这样会真正融会贯通

### 如果你在面试

建议这样答：

1. 先说“不能只看父子关系，要看整棵子树范围”
2. 先口头提一下中序遍历严格递增
3. 主答用“递归传上下界”

这样会显得你：

```text
既知道性质，也真正理解定义
```

---

## 面试表达模板

你可以直接这样说：

```text
这题不能只比较当前节点和左右孩子，因为 BST 的要求是：
左子树所有节点都要小于根，右子树所有节点都要大于根。

所以我会在递归里给每个节点传一个合法范围 (lower, upper)。
当前节点必须满足 lower < node.val < upper。

递归到左子树时，上界收紧为当前节点值；
递归到右子树时，下界收紧为当前节点值。

这样每个节点只访问一次，时间复杂度 O(n)，空间复杂度是递归栈 O(h)。
```

---

## 总结

这题真正考的是：

```text
你是否理解 BST 的约束是“整棵子树范围”，而不是“局部父子比较”
```

从学习路径上看：

1. 暴力法最容易想到
2. 中序法最直观
3. 上下界法最适合面试，也最能体现理解深度

如果你把第三种方法真正想明白，后面很多 BST 题都会顺很多。
