# LeetCode 101 - 对称二叉树（Symmetric Tree）

## 题目

给你一棵二叉树的根节点 `root`，判断它是否轴对称。

所谓轴对称，就是以根节点为中心，左子树和右子树互为镜像。

例如：

```text
        1
       / \
      2   2
     / \ / \
    3  4 4  3
```

这棵树是对称的，返回：

```text
True
```

再看这个例子：

```text
        1
       / \
      2   2
       \   \
        3   3
```

这棵树不是对称的，因为结构不镜像，返回：

```text
False
```

---

## 先说结论

这题和第 100 题“相同的树”非常像。

第 100 题比较的是：

```text
同位置是否相同
```

第 101 题比较的是：

```text
镜像位置是否相同
```

从第一性原理出发，真正自然的解法是：

1. 层序序列化后判断每层是否回文：直观但不推荐面试主写
2. 递归 DFS：同步比较镜像节点，**最适合面试**
3. 迭代队列：递归思想的非递归版本

---

## 这题本质是什么

判断一棵树是否对称，其实是在判断：

```text
root.left 和 root.right 是否互为镜像
```

那么，什么叫两棵树互为镜像？

假设当前比较的两个节点是 `left` 和 `right`。

它们互为镜像需要满足：

1. `left` 和 `right` 都为空：镜像成立
2. `left` 和 `right` 只有一个为空：结构不镜像
3. `left.val == right.val`
4. `left.left` 要和 `right.right` 镜像
5. `left.right` 要和 `right.left` 镜像

写成递归公式就是：

```text
isMirror(left, right) =
    True                                      left 和 right 都为空
    False                                     left 和 right 只有一个为空
    left.val == right.val
      and isMirror(left.left, right.right)
      and isMirror(left.right, right.left)    left 和 right 都非空
```

这就是第 101 题最核心的公式。

---

## 朴素思路：按层看是否回文

对应文件：

```text
10_二叉树/07_q101/solution_1_level_order.py
```

### 思路

从直觉上看，对称树每一层从左到右读，应该是回文的。

例如：

```text
        1
       / \
      2   2
     / \ / \
    3  4 4  3
```

每一层分别是：

```text
[1]
[2, 2]
[3, 4, 4, 3]
```

都是回文。

所以可以做层序遍历，并且把空节点也记录进去。

### 为什么必须记录 None

如果不记录空节点，下面这棵树可能被误判：

```text
        1
       / \
      2   2
       \   \
        3   3
```

第二层值是：

```text
[2, 2]
```

第三层如果不记录空节点，看到的是：

```text
[3, 3]
```

看起来像回文，但结构其实不对称。

必须记录成：

```text
[None, 3, None, 3]
```

这样才能看出它不是回文。

### 为什么它不适合面试主写

这个方法直观，但不是最推荐面试写法。

原因是：

1. 要维护每一层列表
2. 需要特别处理空节点
3. 比递归镜像判断更绕
4. 容易在“是否继续加入空节点”上写复杂

所以它适合理解直觉：

```text
对称树的每一层看起来应该左右对称
```

但面试主写递归更稳。

### 复杂度

- 时间复杂度：`O(n)`，需要遍历节点和必要的空位
- 空间复杂度：`O(w)`，队列和每层列表最多与树宽相关

---

## 解法 2：递归 DFS

对应文件：

```text
10_二叉树/07_q101/solution_2_recursive.py
```

## 这是最适合面试的方法

如果面试里写第 101 题，我最推荐写递归 DFS。

原因是：

1. 它直接表达“镜像”的定义
2. 代码短，现场手写稳定
3. 可以遇到不对称的位置立刻返回
4. 和第 100 题形成非常好的对比

一句话总结：

```text
对称不是左左比右左，而是外侧比外侧、内侧比内侧。
```

也就是：

```text
left.left  对  right.right
left.right 对  right.left
```

---

### 从第一性原理推导

我们要判断整棵树是否对称。

根节点自己在中轴线上，不需要和别人比较。

真正要比较的是：

```text
root.left 和 root.right 是否镜像
```

于是定义一个辅助函数：

```python
def is_mirror(left, right):
```

它负责判断两个节点代表的子树是否互为镜像。

先处理空节点：

```python
if left is None and right is None:
    return True

if left is None or right is None:
    return False
```

然后比较当前节点值：

```python
if left.val != right.val:
    return False
```

最后比较镜像方向：

```python
return (
    is_mirror(left.left, right.right)
    and is_mirror(left.right, right.left)
)
```

注意这里不是：

```python
is_mirror(left.left, right.left)
```

因为那是在比较同方向，不是镜像方向。

---

### 和第 100 题的区别

第 100 题 Same Tree 比较的是：

```text
p.left  对 q.left
p.right 对 q.right
```

第 101 题 Symmetric Tree 比较的是：

```text
left.left  对 right.right
left.right 对 right.left
```

也就是说：

```text
100 是同侧比较
101 是交叉比较
```

把这句话记住，这题就很稳。

### 复杂度

- 时间复杂度：`O(n)`，最坏情况下每个节点访问一次
- 空间复杂度：`O(h)`，递归调用栈高度

---

## 解法 3：迭代队列

对应文件：

```text
10_二叉树/07_q101/solution_3_iterative_queue.py
```

### 思路

递归版每次比较一对镜像节点：

```text
(left, right)
```

迭代版也一样，只是用队列保存这些待比较的节点对。

队列里放：

```text
(node1, node2)
```

每次弹出一对节点：

1. 两个都为空：继续
2. 只有一个为空：返回 `False`
3. 值不同：返回 `False`
4. 值相同：按镜像方向入队

镜像方向入队是关键：

```text
node1.left  对 node2.right
node1.right 对 node2.left
```

核心代码：

```python
queue = deque([(root.left, root.right)])

while queue:
    left, right = queue.popleft()

    if left is None and right is None:
        continue
    if left is None or right is None:
        return False
    if left.val != right.val:
        return False

    queue.append((left.left, right.right))
    queue.append((left.right, right.left))
```

### 什么时候写迭代版

如果面试官追问：

```text
能不能不用递归？
```

就写这一版。

默认情况下，递归 DFS 更适合优先写。

### 复杂度

- 时间复杂度：`O(n)`，最坏情况下访问所有节点
- 空间复杂度：`O(w)`，队列最多保存一层节点对

---

## 面试推荐

第 101 题最适合面试的方法是：

```text
递归 DFS
```

面试时可以这样讲：

```text
一棵树是否对称，等价于它的左子树和右子树是否互为镜像。
我定义 is_mirror(left, right) 来同步比较两个镜像位置。
如果两个节点都为空，说明当前结构对称。
如果只有一个为空，结构不对称。
如果两个节点值不同，也不对称。
否则继续比较外侧 left.left 和 right.right，
以及内侧 left.right 和 right.left。
两个方向都成立，才说明当前两棵子树镜像。
```

复杂度：

```text
最坏情况下访问每个节点一次，时间复杂度 O(n)。
递归栈高度等于树高，空间复杂度 O(h)。
```

---

## 推荐记忆顺序

1. 先记住对称的本质：

```text
左子树和右子树互为镜像
```

2. 再记住比较方向：

```text
外侧：left.left  vs right.right
内侧：left.right vs right.left
```

3. 和第 100 题对比：

```text
100：同侧比较
101：交叉比较
```

---

## 本题文件

```text
10_二叉树/07_q101/solution.md
10_二叉树/07_q101/solution_1_level_order.py
10_二叉树/07_q101/solution_2_recursive.py
10_二叉树/07_q101/solution_3_iterative_queue.py
```

