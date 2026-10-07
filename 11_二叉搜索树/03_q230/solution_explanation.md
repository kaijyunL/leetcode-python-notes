# LeetCode 230 - 二叉搜索树中第 K 小的元素

## 题目

给定一个二叉搜索树的根节点 `root` ，和一个整数 `k` ，请你设计一个算法查找其中第 `k` 小的元素。

题目保证：

```text
1 <= k <= 二叉搜索树中的节点数
```

---

## 先抓住这题的本质

这题表面上是在找“第 `k` 小”。

但它真正考的是你是否知道：

```text
二叉搜索树（BST）的中序遍历结果是升序序列
```

中序遍历顺序是：

```text
左 -> 根 -> 右
```

而 BST 的性质是：

```text
左子树所有值 < 根节点 < 右子树所有值
```

所以中序遍历出来，一定是从小到大。

也就是说：

```text
第 k 小的元素
= 中序遍历序列里的第 k 个元素
```

这就是整道题最核心的一句话。

---

## 解法总览

我们按“从简单暴力到最优”的顺序来理解：

1. 暴力法：遍历整棵树，收集所有值后排序
2. 中序遍历 + 存数组：直接利用 BST 的有序性质
3. 递归中序 + 计数提前返回：边遍历边计数，不存整条数组
4. 迭代中序 + 消耗 k 提前返回：把递归过程改写成显式栈

其中最适合面试的是：

```text
解法四：迭代中序 + 消耗 k 提前返回
```

因为它：

1. 真正利用了 BST 的性质
2. 不需要额外保存所有节点值
3. 可以在找到第 `k` 个节点时立刻返回

---

## 解法一：遍历全部节点 + 排序

对应文件：

```text
11_二叉搜索树/03_q230/solution_1_bruteforce_sort.py
```

### 思路

这个方法先不利用 BST 的性质，直接把它当作普通二叉树处理。

步骤是：

1. 遍历整棵树，把所有节点值放进数组
2. 对数组排序
3. 返回排序后第 `k - 1` 个元素

### 代码

```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            values.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        values.sort()
        return values[k - 1]
```

### 复杂度

```text
时间复杂度：O(n log n)
空间复杂度：O(n)
```

### 优缺点

优点是：

```text
非常好想，几乎不会写错
```

缺点是：

```text
完全没用上 BST 的性质
```

所以这个方法更适合拿来当“保底思路”，不适合作为面试主答案。

---

## 解法二：中序遍历 + 存数组

对应文件：

```text
11_二叉搜索树/03_q230/solution_2_inorder_array.py
```

### 思路

既然 BST 的中序遍历是升序，那我们直接：

1. 中序遍历整棵树
2. 把遍历结果放入数组
3. 返回数组第 `k - 1` 个元素

### 代码

```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)
        return values[k - 1]
```

### 为什么这个方法正确

因为中序遍历的访问顺序天然就是从小到大。

例如这棵 BST：

```text
    5
   / \
  3   6
 / \
2   4
/
1
```

它的中序遍历结果是：

```text
[1, 2, 3, 4, 5, 6]
```

所以：

```text
第 3 小 = 3
第 5 小 = 5
```

### 复杂度

```text
时间复杂度：O(n)
空间复杂度：O(n)
```

### 这个方法比暴力法好在哪

因为它不需要额外排序了。

排序那一步从：

```text
O(n log n)
```

变成了：

```text
直接 O(n)
```

### 不足

它还是会把所有节点都存进数组。

但实际上我们只想要：

```text
第 k 个
```

所以空间还能继续优化，而且还可以提前返回。

---

## 解法三：递归中序 + 计数提前返回

对应文件：

```text
11_二叉搜索树/03_q230/solution_3_recursive_inorder.py
```

### 思路

这个方法和“中序遍历 + 存数组”本质上是一样的。

区别只是：

```text
不再把所有结果都存下来
而是在中序遍历过程中直接计数
```

因为 BST 的中序遍历是升序，所以：

1. 访问到第 1 个节点，就是第 1 小
2. 访问到第 2 个节点，就是第 2 小
3. ...
4. 访问到第 k 个节点，就是第 k 小

### 代码

```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        answer = None

        def inorder(node: Optional[TreeNode]) -> None:
            nonlocal count, answer

            if not node or answer is not None:
                return

            inorder(node.left)

            if answer is not None:
                return

            count += 1
            if count == k:
                answer = node.val
                return

            inorder(node.right)

        inorder(root)
        return answer
```

### 这版为什么完全可行

因为中序遍历的访问顺序本来就是升序。

我们并不一定非要把升序序列完整存到数组里，完全可以：

```text
访问一个，数一个
数到第 k 个就结束
```

### 这版的关键难点

难点不在思路，而在代码细节：

1. 需要记录当前访问到第几个节点，所以要有 `count`
2. 找到答案后，要阻止后续无意义递归，所以要有 `answer`
3. 递归函数内部要修改外层变量，所以通常会用 `nonlocal`

### 复杂度

```text
时间复杂度：最坏 O(n)
空间复杂度：O(h)
```

### 这版适不适合面试

适合。

如果你平时递归写得顺，这版在面试里完全可以作为主答案。

只是它比迭代版更容易在细节上写乱一点，比如：

```text
找到答案后怎么提前停止
如何正确维护 count
```

所以如果你对递归非常熟，这版很好；如果你想让过程更稳定、更可控，迭代版通常更稳。

---

## 解法四：迭代中序 + 消耗 k 提前返回

对应文件：

```text
11_二叉搜索树/03_q230/solution_4_iterative_inorder.py
```

## 这是最适合面试的解法

它的关键想法是：

```text
既然中序遍历本身就是升序，
那我没必要把所有值都存下来，
只要在遍历过程中把 `k` 一步步减到 `0`，立刻返回即可。
```

---

## 为什么用“迭代中序”

中序遍历可以递归写，也可以用栈模拟。

面试里用迭代写法有两个优点：

1. 逻辑很清楚，能直接展示你对中序遍历过程的理解
2. 不需要依赖 `nonlocal` 或额外的 `count` 变量去记录第几个节点

当然递归也能做，这里主推迭代版本，是因为它更像“过程可视化”。

---

## 先理解中序遍历的访问顺序

中序遍历永远是：

```text
一路往左走
左边走到底后，弹栈访问当前节点
再转向右子树
```

对于 BST：

```text
最左边节点一定最小
然后一点一点变大
```

所以我们每访问一个节点，就相当于找到了当前第几个小的元素。

---

## 迭代流程怎么写

我们准备：

1. 一个栈 `stack`
2. 一个指针 `cur`
3. 每访问一个节点，就把 `k` 减 1

### 第一步：一直往左压栈

```python
while cur:
    stack.append(cur)
    cur = cur.left
```

这一步是为了先找到当前子树里最小的节点。

### 第二步：弹出栈顶节点

```python
cur = stack.pop()
```

此时这个节点就是“当前还没访问过的最小值”。

### 第三步：消耗一个名额

```python
k -= 1
if k == 0:
    return cur.val
```

因为中序序列是有序的，所以当我们访问到第 `k` 个节点时，它就是答案。

### 第四步：转向右子树

```python
cur = cur.right
```

然后继续重复“先往左压栈，再弹出访问”的过程。

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            k -= 1

            if k == 0:
                return cur.val

            cur = cur.right
```

---

## 用例子手动走一遍

还是看这棵树：

```text
    5
   / \
  3   6
 / \
2   4
/
1
```

如果 `k = 3`。

### 一开始

```text
cur = 5
stack = []
```

一路往左压栈：

```text
stack = [5, 3, 2, 1]
cur = None
```

### 第一次弹栈

弹出 `1`，这是第 `1` 小。

### 第二次弹栈

弹出 `2`，这是第 `2` 小。

### 第三次弹栈

弹出 `3`，这是第 `3` 小。

此时：

```python
k == 0
```

直接返回 `3`。

你会发现：

```text
我们根本不需要把 [1, 2, 3, 4, 5, 6] 全部存出来
```

只要数到第 `k` 个就可以结束。

---

## 复杂度

```text
时间复杂度：最坏 O(n)
空间复杂度：O(h)
```

更细一点说：

1. 最坏情况下我们可能还是会访问很多节点，所以最坏时间是 `O(n)`
2. 但如果 `k` 很小，通常会更早返回
3. 栈中最多同时存一条从根到叶子的路径，所以空间是 `O(h)`

其中 `h` 是树高。

对于平衡 BST，`h = O(log n)`。

---

## 三种解法怎么选

### 学习顺序

建议按这个顺序掌握：

1. 先写“遍历后排序”，确认题意
2. 再写“中序存数组”，真正用上 BST 性质
3. 再补上“递归中序 + count”，理解不存数组也能做
4. 最后掌握“迭代中序 + 提前返回”，作为主力写法

### 面试顺序

面试里建议这样表达：

1. 先说 BST 的中序遍历是升序
2. 所以第 `k` 小就是中序遍历第 `k` 个访问到的节点
3. 递归版和迭代版都可以边遍历边计数
4. 为了避免存整个数组，可以数到 `k` 直接返回

这样会显得你的思路既自然又高效。

---

## 面试表达模板

你可以直接这样说：

```text
这题的关键是 BST 的中序遍历结果是严格升序。
所以第 k 小的元素，本质上就是中序遍历时第 k 个被访问到的节点。

最直接的做法是先中序遍历存数组，再返回第 k - 1 个元素。
但这样空间是 O(n)。

更优的做法是边中序遍历边计数，
无论是递归还是迭代都可以；
如果用栈做迭代中序遍历，过程会更直观一些，
当计数到 k 时立刻返回当前节点值。

这样最坏时间复杂度 O(n)，空间复杂度 O(h)。
```

---

## 补充：题目的 follow-up

这题在 LeetCode 里常见一个追问：

```text
如果 BST 会频繁插入和删除，并且需要频繁查询第 k 小，该怎么办？
```

这个时候就不能每次都重新中序遍历了。

更好的方向是：

```text
给每个节点额外维护“子树节点数”
```

这样就能像二分一样判断第 `k` 小在左边、当前节点还是右边。

不过这是进阶内容，普通面试里先把中序计数法讲明白就已经很好了。

---

## 总结

这题本质并不复杂，关键就一句：

```text
BST 的中序遍历是升序，第 k 小就是中序的第 k 个
```

从学习角度：

1. 暴力排序法最容易起步
2. 中序存数组法最直观
3. 递归中序计数法是很自然的过渡版本
4. 迭代中序计数法最适合面试

把后两种“边中序边计数”的方法练熟之后，很多 BST 相关题你都会明显更顺手。
