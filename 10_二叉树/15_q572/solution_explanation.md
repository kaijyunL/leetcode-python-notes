# LeetCode 572 - 另一棵树的子树（Subtree of Another Tree）

## 题目

给你两棵二叉树 `root` 和 `subRoot`，判断 `subRoot` 是否是 `root` 的子树。

`subRoot` 是 `root` 的子树，必须满足：

1. `root` 中存在一个节点，作为这棵子树的根节点
2. 从这个节点开始，整棵树的结构和值都与 `subRoot` 完全相同

例如：

```text
root:             subRoot:
      3                 4
     / \               / \
    4   5             1   2
   / \
  1   2
```

返回：

```text
True
```

因为 `root` 中以节点 `4` 为根的整棵子树，与 `subRoot` 完全相同。

再看：

```text
root:             subRoot:
      3                 4
     / \               / \
    4   5             1   2
   / \
  1   2
 /
0
```

返回：

```text
False
```

因为 `root` 中虽然有节点 `4`，但以它为根的子树比 `subRoot` 多了节点 `0`，结构不相同。

---

## 先说结论

这题的本质是两个动作：

```text
1. 在 root 中寻找可能的起点
2. 从每个起点开始，判断两棵树是否完全相同
```

按由浅入深的顺序：

1. 方法一：遍历每个节点，暴力比较整棵树
2. 方法二：递归 DFS，拆出 `is_same_tree` 判断两棵树是否相同，**面试推荐**
3. 方法三：前序序列化 + KMP，把树匹配转成序列匹配

面试时优先写方法二。方法三复杂度更优，但需要同时讲清楚序列化和 KMP，手写成本更高。

---

## 这题最核心的区别

### 不是找一个值相同的节点

下面这棵树中，`root` 里有节点 `4`：

```text
    3
   /
  4
 /
1
```

但下面的 `subRoot`：

```text
  4
 / \
1   2
```

不是它的子树，因为 `root` 中节点 `4` 没有右孩子 `2`。

所以不能只判断：

```python
root.val == subRoot.val
```

必须从这个候选节点开始，把左右子树也全部比较。

### 不是只比较一条路径

树的子树要求的是完整结构：

```text
节点值相同
左孩子结构相同
右孩子结构相同
空孩子位置也相同
```

例如：

```text
    4          4
   /            \
  1              1
```

这两棵树的节点值都可以遍历出 `[4, 1]`，但结构不同，所以不能认为它们相同。

---

## 解法一：遍历候选节点 + 暴力比较

对应文件：

```text
10_二叉树/15_q572/solution_1_bruteforce.py
```

### 思路

先遍历 `root` 的每个节点，把每个节点都当成候选的子树根：

```text
当前节点是不是 subRoot 的根？
如果是，继续完整比较两棵树
如果不是，继续看左子树和右子树
```

完整比较时需要同时判断：

```text
当前节点值是否相同
左子树是否相同
右子树是否相同
```

### 递归关系

```text
visit(node) =
    is_same_tree(node, subRoot)
    或 visit(node.left)
    或 visit(node.right)
```

### 复杂度

设 `root` 有 `n` 个节点，`subRoot` 有 `m` 个节点：

- 时间复杂度：`O(n * m)`
- 空间复杂度：`O(h)`，递归深度取决于树高

这个方法和方法二的核心逻辑相同，只是把辅助函数放在 `isSubtree` 内部，更偏向最直观的暴力展开。

---

## 解法二：递归 DFS（面试推荐）

对应文件：

```text
10_二叉树/15_q572/solution_2_recursive.py
```

### 函数职责

这里有两个递归函数，它们负责不同的事情。

#### `isSubtree(root, subRoot)`

含义是：

```text
subRoot 是否出现在当前 root 子树中
```

它负责寻找候选起点：

```python
if self.is_same_tree(root, subRoot):
    return True

return (
    self.isSubtree(root.left, subRoot)
    or self.isSubtree(root.right, subRoot)
)
```

也就是：

```text
当前节点可以匹配
或者左子树中存在匹配
或者右子树中存在匹配
```

#### `is_same_tree(first, second)`

含义是：

```text
以 first 和 second 为根的两棵树是否完全相同
```

判断顺序：

```python
if first is None and second is None:
    return True

if first is None or second is None:
    return False

if first.val != second.val:
    return False

return self.is_same_tree(first.left, second.left) and self.is_same_tree(
    first.right, second.right
)
```

### 为什么需要两个函数

因为题目包含两个不同问题：

```text
isSubtree：去哪里找？
is_same_tree：找到一个位置后，是否完全相同？
```

例如：

```text
        3
       / \
      4   5
     / \
    1   2
```

`isSubtree(3, subRoot)` 会依次尝试：

```text
以 3 为起点比较
以 4 为起点比较
以 1 为起点比较
以 2 为起点比较
以 5 为起点比较
```

当尝试到 `4` 时，才由 `is_same_tree(4, subRoot)` 负责验证 `4` 的左右结构和值。

### 边界条件

```python
if subRoot is None:
    return True
```

空树通常被认为是任何树的子树。

```python
if root is None:
    return False
```

此时 `subRoot` 已经不是空树，但 `root` 中没有任何节点可以匹配。

### 复杂度

设 `root` 有 `n` 个节点，`subRoot` 有 `m` 个节点：

- 时间复杂度：`O(n * m)`
- 空间复杂度：`O(h_root + h_subRoot)`，来自两层递归调用

最坏情况下，会对 `root` 中的多个节点分别比较一遍 `subRoot`。

### 面试表达

可以这样说：

```text
我把问题拆成两个递归动作。外层 DFS 遍历 root 中的每个节点，寻找可能的子树根；对每个候选节点，调用 is_same_tree 同步比较两棵树的结构和值。只有当前节点值相同，并且左右子树都相同，才能判定匹配。空的 subRoot 直接返回 true，空的 root 返回 false。
```

---

## 解法三：前序序列化 + KMP

对应文件：

```text
10_二叉树/15_q572/solution_3_serialization_kmp.py
```

### 思路

把两棵树都做带空节点标记的前序遍历：

```text
节点：记录节点值
空节点：记录 #
```

例如：

```text
    4
   / \
  1   2
```

序列化为：

```text
[4, 1, #, #, 2, #, #]
```

然后判断：

```text
subRoot 的序列，是否是 root 序列中的连续子序列
```

### 为什么必须记录 `#`

如果不记录空节点，下面两棵树都会得到：

```text
[4, 1]
```

但它们结构不同：

```text
    4          4
   /            \
  1              1
```

加入空节点后：

```text
[4, 1, #, #, #]
[4, #, 1, #, #]
```

序列就不同了。

### 为什么使用 KMP

序列化后问题变成：

```text
在 root 序列中查找 subRoot 序列
```

直接使用普通子串查找，最坏情况下可能重复比较；KMP 使用前缀表跳过已经确认过的部分，把匹配过程降为线性。

### 复杂度

设 `root` 有 `n` 个节点，`subRoot` 有 `m` 个节点：

- 序列化：`O(n + m)`
- KMP 匹配：`O(n + m)`
- 总时间复杂度：`O(n + m)`
- 空间复杂度：`O(n + m)`

### 面试取舍

方法三的渐进复杂度更好，但面试中不一定优先写，原因是：

1. 需要处理空节点标记
2. 需要解释为什么序列匹配等价于子树匹配
3. 还要现场写 KMP 前缀表

除非面试官明确追问复杂度优化，否则方法二更容易正确、清楚地完成。

---

## 三种方法对比

| 方法 | 核心思路 | 时间复杂度 | 空间复杂度 | 面试建议 |
|---|---|---:|---:|---|
| 方法一 | 遍历候选节点 + 比较 | `O(nm)` | `O(h)` | 用来建立直觉 |
| 方法二 | DFS 寻找起点 + `is_same_tree` | `O(nm)` | `O(h_root + h_subRoot)` | **主推** |
| 方法三 | 序列化 + KMP | `O(n+m)` | `O(n+m)` | 进阶优化 |

## 最后记忆

这题可以记成一句话：

```text
先在 root 中找候选根，再从候选根开始判断两棵树是否完全相同。
```

判断完全相同必须同时满足：

```text
当前值相同
左子树相同
右子树相同
空节点位置也相同
```
