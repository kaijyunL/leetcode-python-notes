# LeetCode 79 — 单词搜索（Word Search）

## 题目

给定一个 `m x n` 的字符网格 `board` 和一个字符串 `word`。

如果 `word` 存在于网格中，返回 `True`；否则返回 `False`。

单词必须按照字母顺序，通过相邻单元格内的字母构成。相邻单元格是指水平或垂直方向相邻。

同一个单元格在同一条路径中不能重复使用。

### 示例

```
board =
[
  ["A","B","C","E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
]

word = "ABCCED"
输出: True
```

路径可以是：

```
A -> B -> C -> C -> E -> D
```

---

## 核心理解

这题是网格 DFS 回溯。

我们要做的是：

```
从每个格子出发，尝试匹配 word[0]
如果匹配，就继续从上下左右匹配 word[1], word[2], ...
同一条路径里，一个格子不能重复使用
```

所以每次 DFS 需要知道：

| 变量 | 含义 |
|---|---|
| `row`, `col` | 当前所在格子 |
| `index` | 当前要匹配 `word[index]` |
| `visited` 或原地标记 | 当前路径已经用过哪些格子 |

---

## 解法一览

| 解法 | 思路 | 时间复杂度 | 空间复杂度 | 是否推荐面试 |
|---|---|---|---|---|
| 1. DFS + visited 矩阵 | 用额外矩阵记录访问状态 | O(mn * 4^L) | O(mn + L) | 好理解 |
| 2. 原地标记 + 预检查 | 临时修改 board 标记访问状态，先做长度/频率检查 | O(mn * 4^L) | O(L) | **面试推荐 ✅** |

> `L = len(word)`。严格一点，第一步之后每个位置最多有 3 个方向可走，因为不能回到刚来的格子，所以也常写成 `O(mn * 3^L)`。面试里说 `O(mn * 4^L)` 更直观。

---

## 解法 1：DFS + visited 矩阵

### 思路

用一个和 `board` 同样大小的布尔矩阵：

```python
visited = [[False] * cols for _ in range(rows)]
```

记录当前路径中哪些格子已经用过。

DFS 过程：

1. 越界，返回 `False`
2. 当前格子已访问，返回 `False`
3. 当前字符不等于 `word[index]`，返回 `False`
4. 如果 `index` 已经是最后一个字符，返回 `True`
5. 标记当前格子已访问
6. 向上下左右继续搜索
7. 搜索结束后撤销访问标记

### 代码

```python
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(row: int, col: int, index: int) -> bool:
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

            if visited[row][col] or board[row][col] != word[index]:
                return False

            if index == len(word) - 1:
                return True

            visited[row][col] = True

            found = (
                dfs(row + 1, col, index + 1)
                or dfs(row - 1, col, index + 1)
                or dfs(row, col + 1, index + 1)
                or dfs(row, col - 1, index + 1)
            )

            visited[row][col] = False
            return found

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False
```

### 为什么要撤销 `visited[row][col]`？

因为 `visited` 表示的是：

```
当前这条路径里用过哪些格子
```

不是整个搜索过程中永久不能再用。

比如某条路径从 `(0,0)` 出发失败了，之后从另一个起点搜索时，`(0,0)` 仍然可以被使用。

所以 DFS 返回前必须撤销：

```python
visited[row][col] = False
```

这就是回溯。

---

## 解法 2：原地标记 + 预检查 ⭐ 面试推荐

### 思路

可以不用额外的 `visited` 矩阵，而是用 `board` 自己记录当前路径的访问状态。

当一个格子已经被当前路径使用时，临时把它改成一个不可能匹配的字符：

```python
temp = board[row][col]
board[row][col] = "#"
```

递归结束后再恢复：

```python
board[row][col] = temp
```

这样就能用 `board` 自己记录访问状态。

另外，面试版可以加两个简单预检查。

### 1. 长度检查

如果单词长度大于格子总数，不可能匹配：

```python
if len(word) > rows * cols:
    return False
```

### 2. 字符频率检查

如果 `word` 中某个字符需要的次数超过 `board` 中这个字符的数量，也不可能匹配。

比如：

```python
board = [["A"]]
word = "AA"
```

明显不可能。

可以用 `Counter` 检查：

```python
board_count = Counter(ch for row in board for ch in row)
word_count = Counter(word)

for ch, count in word_count.items():
    if board_count[ch] < count:
        return False
```

这两个预检查简单、稳定，面试里建议加。它们不是为了改变复杂度，而是快速过滤明显不可能的输入。

### 代码

```python
from collections import Counter


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        if len(word) > rows * cols:
            return False

        board_count = Counter(ch for row in board for ch in row)
        word_count = Counter(word)

        for ch, count in word_count.items():
            if board_count[ch] < count:
                return False

        def dfs(row: int, col: int, index: int) -> bool:
            if index == len(word):
                return True

            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

            if board[row][col] != word[index]:
                return False

            temp = board[row][col]
            board[row][col] = "#"

            found = (
                dfs(row + 1, col, index + 1)
                or dfs(row - 1, col, index + 1)
                or dfs(row, col + 1, index + 1)
                or dfs(row, col - 1, index + 1)
            )

            board[row][col] = temp
            return found

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False
```

### 为什么原地标记后必须恢复？

因为同一个格子不能在同一条路径里重复使用，但可以在不同路径里使用。

如果不恢复：

```python
board[row][col] = temp
```

那么一次失败搜索会污染后续搜索，导致本来可以找到的路径找不到。

这和前面回溯题里的：

```python
path.append(...)
backtrack(...)
path.pop()
```

是同一个思想。

### 两种终止写法

解法 1 用的是：

```python
if index == len(word) - 1:
    return True
```

意思是当前格子已经匹配最后一个字符。

解法 2 用的是：

```python
if index == len(word):
    return True
```

意思是前面已经成功匹配完所有字符。

两种都正确。解法 2 的写法更统一，因为每次 DFS 开始先看是否已经全部匹配。

### 复杂度

设：

```
m = 行数
n = 列数
L = word 长度
```

最坏情况下，每个格子都可能作为起点，每次 DFS 最多向 4 个方向扩展。

时间复杂度：

```
O(mn * 4^L)
```

如果写得更精细，因为不能回到刚来的格子，也可以说：

```
O(mn * 3^L)
```

空间复杂度不算输入和返回：

```
O(L)
```

因为递归深度最多是单词长度。

### 为什么它最适合面试？

因为它包含网格回溯的核心模板：

1. 从每个格子作为起点
2. DFS 中检查越界、字符是否匹配
3. 原地标记当前格子，避免同一路径重复使用
4. 搜索上下左右
5. 恢复当前格子

面试时可以这样讲：

> 我从每个格子出发做 DFS。`index` 表示当前要匹配 `word[index]`。如果当前格子越界或字符不匹配，就返回 False。匹配后临时把当前格子标记为 `#`，然后向四个方向搜索下一个字符。递归结束后恢复原字符，保证其他路径还能使用这个格子。开始前可以先做长度和字符频率检查，过滤明显不可能的情况。

---

## 最终推荐

面试最推荐写 **解法 2：原地标记 + 预检查**。

核心 DFS 代码：

```python
def dfs(row: int, col: int, index: int) -> bool:
    if index == len(word):
        return True

    if row < 0 or row >= rows or col < 0 or col >= cols:
        return False

    if board[row][col] != word[index]:
        return False

    temp = board[row][col]
    board[row][col] = "#"

    found = (
        dfs(row + 1, col, index + 1)
        or dfs(row - 1, col, index + 1)
        or dfs(row, col + 1, index + 1)
        or dfs(row, col - 1, index + 1)
    )

    board[row][col] = temp
    return found
```

重点记住：

```
原地标记是为了防止同一路径重复使用格子
恢复原字符是为了不影响其他路径
```
