# LeetCode 114 - 二叉树展开为链表（Flatten Binary Tree to Linked List）

## 题目

给你一棵二叉树的根节点 `root`，请你把它展开为一个单链表。

展开后的链表要求：

```text
1. 使用原来的 TreeNode 节点
2. 每个节点的 left 都要变成 None
3. 每个节点的 right 指向链表里的下一个节点
4. 链表顺序必须等于二叉树的前序遍历顺序
```

例如：

```text
原树：

      1
     / \
    2   5
   / \   \
  3   4   6

展开后：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

展开后的右指针链表是：

```text
[1, 2, 3, 4, 5, 6]
```

这正好是原树的前序遍历：

```text
根 -> 左 -> 右
```

---

## 先说结论

第 114 题的本质是：

```text
把二叉树按前序遍历顺序，原地改造成一条只走 right 的链表。
```

从简单到最优，推荐掌握三种写法：

1. 前序遍历收集节点，再统一重连：最直观，适合理解
2. 递归原地展开：不用额外节点数组，适合理解递归关系
3. 迭代原地改指针：`O(1)` 额外空间，**最适合面试**

解法一好懂，但额外用了一个列表。

解法二比较优雅，但递归栈最坏 `O(n)`。

解法三不需要递归栈，不需要额外列表，是这题面试最推荐的写法。

---

## 这题本质是什么

题目说“展开为链表”，但它不是普通链表题。

它真正要求的是：

```text
把前序遍历结果写回原树的 right 指针上。
```

以前序遍历为例：

```text
      1
     / \
    2   5
   / \   \
  3   4   6
```

前序遍历结果是：

```text
[1, 2, 3, 4, 5, 6]
```

所以最终结构必须是：

```text
1 -> 2 -> 3 -> 4 -> 5 -> 6
```

用二叉树指针表示就是：

```text
1.right = 2
2.right = 3
3.right = 4
4.right = 5
5.right = 6

所有节点的 left = None
```

---

## 最容易错的地方

### 1. 展开顺序是前序，不是中序或后序

展开后的顺序必须是：

```text
根 -> 左 -> 右
```

比如节点 `1` 的左子树 `2, 3, 4` 必须排在右子树 `5, 6` 前面。

### 2. 不能创建新节点

题目要求原地修改。

可以使用额外列表保存节点引用，但不能重新创建一批新节点来拼链表。

### 3. 每个节点的 left 都要置空

展开后必须满足：

```python
node.left is None
```

只改 `right` 不清空 `left`，结构就不符合题意。

---

## 解法一：前序遍历收集节点 + 统一重连

对应文件：

```text
10_二叉树/25_q114/solution_1_preorder_list.py
```

### 思路

最直观的方法是分两步：

1. 先做一次前序遍历，把节点按顺序放进列表
2. 再按列表顺序，把这些节点改成右链表

前序遍历：

```text
根 -> 左 -> 右
```

所以对于这棵树：

```text
      1
     / \
    2   5
   / \   \
  3   4   6
```

节点列表就是：

```text
[1, 2, 3, 4, 5, 6]
```

然后重连：

```text
1.right = 2
2.right = 3
3.right = 4
4.right = 5
5.right = 6
```

同时每个节点：

```text
left = None
```

### 对应代码

核心代码是：

```python
nodes = []

def preorder(node):
    if not node:
        return

    nodes.append(node)
    preorder(node.left)
    preorder(node.right)

for i in range(1, len(nodes)):
    prev = nodes[i - 1]
    cur = nodes[i]
    prev.left = None
    prev.right = cur
```

最后一个节点也要清理：

```python
nodes[-1].left = None
nodes[-1].right = None
```

### 为什么它不是面试最优

这个方法非常适合理解题目，因为它把“前序顺序”和“重连指针”拆开了。

但它额外用了一个列表保存所有节点：

```text
nodes
```

所以空间复杂度是 `O(n)`。

面试时可以先讲这个方法，但最终建议写解法三。

### 复杂度

- 时间复杂度：`O(n)`，每个节点遍历一次，重连一次
- 空间复杂度：`O(n)`，节点列表和递归栈

---

## 解法二：递归原地展开

对应文件：

```text
10_二叉树/25_q114/solution_2_recursive.py
```

### 思路

递归原地展开的核心是：

```text
先把左子树展开成链表
再把右子树展开成链表
最后把左链表插到 root 和右链表之间
```

对于当前节点 `root`：

```text
原来：

      root
      /  \
   left  right

展开 left 后：

left -> ...

展开 right 后：

right -> ...

最后改成：

root -> left链表 -> right链表
```

因为最终顺序是前序：

```text
root -> 左子树 -> 右子树
```

所以左链表必须接在 `root.right`，原来的右链表要接到左链表的尾部。

### 用例子看一层指针怎么改

还是这棵树：

```text
      1
     / \
    2   5
   / \   \
  3   4   6
```

假设递归已经把左右子树展开好了：

```text
左子树展开后：
2 -> 3 -> 4

右子树展开后：
5 -> 6
```

当前节点 `1` 要变成：

```text
1 -> 2 -> 3 -> 4 -> 5 -> 6
```

所以要做三件事：

1. 先保存原来的右子树：

```python
right = root.right
```

2. 把左链表接到右边：

```python
root.right = root.left
root.left = None
```

3. 找到左链表尾巴，把原来的右链表接上：

```python
tail = root.right
while tail.right:
    tail = tail.right
tail.right = right
```

### 递归顺序

代码会先递归处理：

```python
self.flatten(root.left)
self.flatten(root.right)
```

然后再处理当前节点的拼接。

这个顺序有点像后序处理：

```text
先让左右子树变好，再处理当前节点
```

但最终链表顺序仍然是前序：

```text
root -> 左 -> 右
```

### 复杂度

- 时间复杂度：最坏 `O(n^2)`
- 空间复杂度：`O(h)`，递归栈

为什么最坏是 `O(n^2)`？

因为每个节点都可能要向右找一次左链表尾巴：

```python
while tail.right:
    tail = tail.right
```

如果树退化得比较极端，反复找尾巴会累计很多次。

这个方法适合理解递归改指针，但不是最优面试写法。

---

## 解法三：迭代原地展开

对应文件：

```text
10_二叉树/25_q114/solution_3_iterative.py
```

## 这是最适合面试的方法

如果面试里写第 114 题，最推荐这一版。

原因是：

1. 它不创建新节点
2. 它不使用额外节点列表
3. 它不用递归，避免递归栈
4. 它只通过指针调整完成原地展开

复杂度是：

```text
时间复杂度 O(n)
额外空间复杂度 O(1)
```

---

### 核心想法

对于当前节点 `cur`，如果它没有左子树：

```text
cur.left is None
```

那它本来就不需要处理，直接往右走：

```python
cur = cur.right
```

如果它有左子树，说明最终链表里：

```text
左子树整条链必须排在右子树前面
```

也就是：

```text
cur -> 左子树 -> 右子树
```

所以要把原来的右子树，接到左子树最右边的尾巴后面。

### 当前节点如何改指针

假设当前节点是 `cur`：

```text
      cur
      / \
   left  right
```

第一步：找到左子树里最右边的节点。

这个节点叫 `predecessor`：

```python
predecessor = cur.left
while predecessor.right:
    predecessor = predecessor.right
```

为什么找左子树最右边？

因为展开后的结构里，左子树这条链要接在 `cur` 后面。

而原来的右子树要接到左子树链表的最后。

第二步：把原来的右子树接到 `predecessor.right`：

```python
predecessor.right = cur.right
```

第三步：把左子树搬到右边：

```python
cur.right = cur.left
cur.left = None
```

这样当前节点就处理好了。

最后继续往右走：

```python
cur = cur.right
```

---

### 用例子完整走一遍

原树：

```text
      1
     / \
    2   5
   / \   \
  3   4   6
```

当前节点 `cur = 1`。

`1` 有左子树 `2`，所以要处理。

先找 `1` 的左子树里最右边的节点：

```text
左子树是：

    2
   / \
  3   4

最右边节点是 4
```

也就是：

```text
predecessor = 4
```

把 `1` 原来的右子树 `5 -> 6` 接到 `4.right`：

```text
    2
   / \
  3   4
       \
        5
         \
          6
```

然后把 `1.left` 搬到 `1.right`，并清空 `1.left`：

```text
1
 \
  2
 / \
3   4
     \
      5
       \
        6
```

此时 `1` 已经满足：

```text
1.left = None
1.right = 2
```

接着 `cur = cur.right`，也就是来到 `2`。

---

当前节点 `cur = 2`。

`2` 有左子树 `3`。

找 `2` 左子树里最右边的节点：

```text
predecessor = 3
```

把 `2` 原来的右子树 `4 -> 5 -> 6` 接到 `3.right`：

```text
3.right = 4
```

再把 `2.left` 搬到 `2.right`，清空 `2.left`：

```text
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

后面节点都没有左子树了，只要一路往右走。

最终结果：

```text
1 -> 2 -> 3 -> 4 -> 5 -> 6
```

---

### 为什么这个方法是 O(n)

这段代码看起来有一个嵌套循环：

```python
while cur:
    if cur.left:
        predecessor = cur.left
        while predecessor.right:
            predecessor = predecessor.right
        ...
    cur = cur.right
```

但整体仍然是 `O(n)`。

原因是：

```text
每条右指针在调整过程中只会被沿着走有限次。
```

更直观地说，每次找到 `predecessor` 后，都会把一整段左子树搬到右边。

搬完之后，当前节点的左子树会被清空：

```python
cur.left = None
```

这个节点以后不会再因为左子树被重复处理。

所以所有节点整体只会被处理常数次，时间复杂度是 `O(n)`。

### 对应代码

```python
cur = root

while cur:
    if cur.left:
        predecessor = cur.left

        while predecessor.right:
            predecessor = predecessor.right

        predecessor.right = cur.right
        cur.right = cur.left
        cur.left = None

    cur = cur.right
```

这段代码的意义是：

```text
如果当前节点有左子树，就把左子树插到当前节点和右子树之间。
```

也就是：

```text
cur -> left -> right
```

这正好符合前序展开顺序：

```text
根 -> 左 -> 右
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

---

## 面试推荐

第 114 题最适合面试的方法是：

```text
迭代原地展开
```

面试时可以这样讲：

```text
展开后的顺序其实就是前序遍历顺序：根、左、右。
对当前节点 cur 来说，如果它有左子树，那么最终左子树应该排在右子树前面。
所以我先找到 cur 左子树里最右边的节点 predecessor。
然后把 cur 原来的右子树接到 predecessor.right。
接着把 cur.left 搬到 cur.right，并把 cur.left 置空。
这样 cur 这一层就变成了 根 -> 左 -> 右 的链式结构。
最后 cur 往右移动，继续处理下一个节点。
整个过程只改原树指针，不创建新节点，额外空间 O(1)。
```

---

## 推荐记忆顺序

1. 先记住展开顺序：

```text
展开后就是前序遍历：根 -> 左 -> 右
```

2. 再记住当前节点的目标结构：

```text
cur -> 左子树 -> 右子树
```

3. 最后记住三步改指针：

```python
predecessor.right = cur.right
cur.right = cur.left
cur.left = None
```

---

## 本题文件

```text
10_二叉树/25_q114/solution.md
10_二叉树/25_q114/solution_1_preorder_list.py
10_二叉树/25_q114/solution_2_recursive.py
10_二叉树/25_q114/solution_3_iterative.py
```
