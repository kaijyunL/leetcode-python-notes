# LeetCode 95 - 不同的二叉搜索树 II

## 题目

给你一个整数 `n` ，请你生成并返回所有由 `n` 个节点组成且节点值从 `1` 到 `n` 互不相同的不同二叉搜索树。

返回答案的顺序不限。

例如：

```text
输入：n = 3
输出：5 棵不同的 BST
```

---

## 这题和第 96 题是什么关系

第 96 题问的是：

```text
一共有多少种
```

第 95 题问的是：

```text
把每一种都真正构造出来
```

所以可以这样理解：

```text
96 是计数版
95 是生成版
```

第 96 题里我们写的是：

```text
左子树方案数 × 右子树方案数
```

而第 95 题里要做的是：

```text
把左子树的每一种可能，和右子树的每一种可能，逐个配对拼出来
```

也就是说，这题本质上是把第 96 题里的“乘法”，真的展开成一组一组树。

---

## 这题本质在考什么

核心只有一句话：

```text
枚举每个数字做根节点，
递归生成所有左子树，
递归生成所有右子树，
然后做笛卡尔积组合。
```

为什么这样做是对的？

因为 BST 满足：

```text
左子树所有值 < 根节点 < 右子树所有值
```

所以如果当前根节点选 `root`：

```text
左子树只能从 [left, root - 1] 里构造
右子树只能从 [root + 1, right] 里构造
```

左右子树各自所有可能都求出来后，再两两组合，就是以 `root` 为根的全部答案。

---

## 一个最重要的递归函数

为了把问题抽象清楚，我们定义：

```text
build(left, right) = 用区间 [left, right] 内的数字，能生成的所有 BST
```

那么：

1. 如果 `left > right`，说明这边没有节点
2. 空树也要作为一种合法结果返回
3. 所以此时返回：

```text
[None]
```

注意这里必须是：

```text
列表里放一个 None
```

而不能是空列表 `[]`。

因为我们后面要做左右子树组合。

比如某个根节点没有左子树，但有右子树时：

```text
左边要提供 1 种“空树方案”
右边提供若干真实树方案
```

这样两边才能正常做配对。

---

## 解法总览

我们按“从简单暴力到最优”的顺序来理解：

1. 全排列插入 BST + 序列化去重：最暴力，适合建立直觉
2. 分治递归生成：直接利用 BST 性质，**最适合面试**
3. 记忆化搜索：缓存区间结果，减少重复生成

这题和第 96 题不一样。

第 96 题最适合面试的是 DP。

但第 95 题最适合面试的主答案其实是：

```text
分治递归生成
```

因为它最贴合题目本身，也最容易把“BST 的定义”直接翻译成代码。

---

## 解法一：全排列插入 BST + 去重

对应文件：

```text
11_二叉搜索树/09_q95/solution_1_permutations_dedup.py
```

### 思路

最容易想到的暴力法是：

1. 枚举 `1 ~ n` 的所有排列
2. 按排列顺序依次插入 BST
3. 得到一棵树
4. 用序列化结果去重

例如 `n = 3`：

```text
[1, 2, 3] -> 一棵偏右的树
[1, 3, 2] -> 另一棵树
[2, 1, 3] -> 一棵平衡树
...
```

但要注意：

```text
不同插入顺序，可能生成同一棵 BST
```

所以必须去重。

### 代码

```python
from itertools import permutations
from typing import Dict, List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        unique_trees: Dict[str, TreeNode] = {}

        for order in permutations(range(1, n + 1)):
            root = None
            for value in order:
                root = self.insert(root, value)

            key = self.serialize(root)
            if key not in unique_trees:
                unique_trees[key] = root

        return list(unique_trees.values())
```

### 复杂度

```text
时间复杂度：非常高，接近 O(n! * n)
空间复杂度：很高
```

### 为什么不适合作为主答案

因为它根本没有抓住这题最核心的 BST 结构性质。

它只是：

```text
把所有插入顺序都试一遍，再去重
```

这更像一个“纯暴力保底思路”。

---

## 解法二：分治递归生成

对应文件：

```text
11_二叉搜索树/09_q95/solution_2_divide_conquer.py
```

## 最适合面试的方法

这是这题最推荐的主答案。

原因是：

```text
1. 直接利用 BST 的定义
2. 递归结构非常自然
3. 思路和代码一一对应，表达清楚
4. 是这题最经典的标准解法
```

### 先定义递归含义

我们写一个函数：

```text
build(left, right)
```

表示：

```text
用闭区间 [left, right] 内的所有数字，构造出的全部 BST
```

例如：

```text
build(1, 3)
```

表示用 `1, 2, 3` 生成所有 BST。

### base case 是什么

如果：

```text
left > right
```

说明这个区间没有数字可用。

这时要返回：

```text
[None]
```

而不是 `[]`。

这是整题最容易写错的地方之一。

为什么？

因为我们后面要枚举：

```text
for left_tree in left_trees:
    for right_tree in right_trees:
```

如果一边为空树，它也应该提供一种合法选择，否则组合数会被错误清空。

### 状态转移怎么想

对于区间 `[left, right]`，我们枚举每个 `root_val` 做根节点：

```text
root_val = left, left+1, ..., right
```

一旦根节点固定：

```text
左子树只能来自 [left, root_val - 1]
右子树只能来自 [root_val + 1, right]
```

于是：

```text
left_trees = build(left, root_val - 1)
right_trees = build(root_val + 1, right)
```

然后把左右两边所有可能两两组合：

```text
for left_tree in left_trees:
    for right_tree in right_trees:
        root = TreeNode(root_val)
        root.left = left_tree
        root.right = right_tree
        ans.append(root)
```

这就是：

```text
“左边每一种” × “右边每一种”
```

在第 95 题里的真实展开方式。

### 用 `n = 3` 手推一遍

要求：

```text
build(1, 3)
```

#### 1. 根节点取 `1`

左区间：

```text
build(1, 0) = [None]
```

右区间：

```text
build(2, 3)
```

右边会生成两棵树，所以根为 `1` 时能拼出两棵树。

#### 2. 根节点取 `2`

左区间：

```text
build(1, 1)
```

右区间：

```text
build(3, 3)
```

左右各只有一种，所以根为 `2` 时只有一棵树。

#### 3. 根节点取 `3`

和根为 `1` 对称，也会得到两棵树。

所以总数：

```text
2 + 1 + 2 = 5
```

### 代码

```python
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def build(left: int, right: int) -> List[Optional[TreeNode]]:
            if left > right:
                return [None]

            trees = []
            for root_val in range(left, right + 1):
                left_trees = build(left, root_val - 1)
                right_trees = build(root_val + 1, right)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(root_val)
                        root.left = left_tree
                        root.right = right_tree
                        trees.append(root)

            return trees

        return build(1, n)
```

### 复杂度

这题是“生成所有答案”的题，所以复杂度一定和输出规模强相关。

常见写法记作：

```text
时间复杂度：O(n * Cn)
空间复杂度：O(n * Cn)
```

其中 `Cn` 是第 `n` 个卡特兰数，也就是答案数量级。

你可以把它简单理解成：

```text
答案本来就有这么多棵树，
所以不可能比“把这些树生成出来”更便宜太多。
```

### 面试怎么讲最稳

你可以这样表达：

```text
1. 定义 build(left, right) 返回区间内所有 BST
2. 枚举每个值作为根节点
3. 递归生成所有左子树和所有右子树
4. 把左右结果做笛卡尔积组合
5. 当 left > right 时返回 [None]，表示空树也是一种合法选择
```

如果你把这 5 句讲清楚，这题基本就稳了。

---

## 解法三：记忆化搜索

对应文件：

```text
11_二叉搜索树/09_q95/solution_3_memoization.py
```

### 思路

在上面的分治递归中，同一个区间会被反复求解。

例如：

```text
build(1, 2)
build(2, 3)
build(1, 1)
```

这些区间可能在不同路径里多次出现。

所以我们可以用缓存：

```text
memo[(left, right)] = 这个区间对应的所有 BST
```

这样如果某个区间已经算过，就不用重新生成。

### 一个实现细节

如果直接把缓存里的树对象原样返回：

```text
不同答案之间可能共享同一棵子树对象
```

LeetCode 判题本身通常不受影响，但从“每棵答案树彼此独立”的角度看，不够严谨。

所以这个版本里会在取缓存时做一次深拷贝。

### 代码

```python
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        memo = {}

        def clone(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            return TreeNode(node.val, clone(node.left), clone(node.right))

        def build(left: int, right: int) -> List[Optional[TreeNode]]:
            if left > right:
                return [None]

            key = (left, right)
            if key in memo:
                return [clone(tree) for tree in memo[key]]

            trees = []
            for root_val in range(left, right + 1):
                left_trees = build(left, root_val - 1)
                right_trees = build(root_val + 1, right)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(root_val)
                        root.left = left_tree
                        root.right = right_tree
                        trees.append(root)

            memo[key] = [clone(tree) for tree in trees]
            return trees

        return build(1, n)
```

### 复杂度

```text
时间复杂度：仍然和输出规模同阶，常记作 O(n * Cn)
空间复杂度：O(n * Cn)
```

它的优势不在于把复杂度从指数变成线性，而在于：

```text
减少同一区间的重复递归构造
```

---

## 三种方法对比

| 方法 | 时间复杂度 | 空间复杂度 | 是否推荐做面试主答案 |
| --- | --- | --- | --- |
| 全排列插入 + 去重 | 非常高，接近 O(n! * n) | 很高 | 不推荐 |
| 分治递归生成 | O(n * Cn) | O(n * Cn) | **最推荐** |
| 记忆化搜索 | O(n * Cn) | O(n * Cn) | 可以作为优化补充 |

---

## 一句话总结

这题最核心的一句话是：

```text
枚举根节点后，递归生成所有左子树和所有右子树，再把左右结果逐个配对组合。
```

如果是面试：

```text
主答案讲分治递归；
如果面试官继续追问重复子问题，再补记忆化。
```
