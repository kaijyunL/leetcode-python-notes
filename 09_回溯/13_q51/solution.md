# LeetCode 51 — N 皇后（N-Queens）

## 题目

按照国际象棋规则，皇后可以攻击同一行、同一列、同一条对角线上的棋子。

给定整数 `n`，返回所有不同的 N 皇后摆法。

每个解包含一个 `n x n` 的棋盘：

- `"Q"` 表示皇后
- `"."` 表示空位

### 示例

```
输入: n = 4
输出:
[
  [".Q..", "...Q", "Q...", "..Q."],
  ["..Q.", "Q...", "...Q", ".Q.."]
]
```

---

## 核心理解

N 皇后要求：

```
n 个皇后放在 n x n 棋盘上
任意两个皇后不能互相攻击
```

因为同一行不能有两个皇后，所以可以天然按“行”来放：

```
第 0 行放一个皇后
第 1 行放一个皇后
第 2 行放一个皇后
...
第 n-1 行放一个皇后
```

这样行冲突天然避免。

剩下只需要检查：

```
同列不能冲突
两条对角线不能冲突
```

---

## 对角线怎么判断？

对一个格子：

```python
row, col
```

主对角线方向是左上到右下：

```text
row - col 相同
```

比如：

```
(0,0), (1,1), (2,2)
```

它们的：

```python
row - col = 0
```

副对角线方向是右上到左下：

```text
row + col 相同
```

比如：

```
(0,3), (1,2), (2,1), (3,0)
```

它们的：

```python
row + col = 3
```

所以判断冲突只需要看：

```python
col
row - col
row + col
```

是否已经被占用。

---

## 解法一览

| 解法 | 思路 | 时间复杂度 | 空间复杂度 | 是否推荐面试 |
|---|---|---|---|---|
| 1. 暴力排列 + 最后校验 | 每行选一列，生成所有列排列，再检查对角线 | O(n! * n^2) | O(n) | 只适合理解 |
| 2. 回溯 + 扫描检查 | 逐行放皇后，每次扫描上方列和对角线 | O(n!) 级别 | O(n^2) | 可以写 |
| 3. 回溯 + 集合剪枝 | 用集合 O(1) 判断列和对角线冲突 | O(n!) 级别 | O(n^2) | **面试推荐 ✅** |

> N 皇后本质是搜索问题，复杂度是阶乘级。优化重点不是把它变成多项式，而是尽量减少无效搜索和降低冲突判断成本。

---

## 解法 1：暴力排列 + 最后校验

### 思路

因为每一行必须放一个皇后，并且每一列也不能重复，所以可以先生成列的全排列。

比如：

```python
cols = [1, 3, 0, 2]
```

表示：

```
第 0 行皇后放第 1 列
第 1 行皇后放第 3 列
第 2 行皇后放第 0 列
第 3 行皇后放第 2 列
```

这样行和列都不会冲突。

然后只需要检查对角线是否冲突。

### 如何检查对角线？

对每一对皇后：

```python
(row1, col1)
(row2, col2)
```

如果：

```python
abs(row1 - row2) == abs(col1 - col2)
```

说明它们在同一条对角线上，冲突。

### 代码

```python
from itertools import permutations


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []

        def is_valid(cols: tuple[int, ...]) -> bool:
            for row1 in range(n):
                for row2 in range(row1 + 1, n):
                    if abs(row1 - row2) == abs(cols[row1] - cols[row2]):
                        return False
            return True

        def build_board(cols: tuple[int, ...]) -> list[str]:
            board = []
            for col in cols:
                row = ["."] * n
                row[col] = "Q"
                board.append("".join(row))
            return board

        for cols in permutations(range(n)):
            if is_valid(cols):
                ans.append(build_board(cols))

        return ans
```

### 评价

这个方法很好理解：

```
先保证行列不冲突，再检查对角线
```

但它先生成所有排列，再过滤，剪枝太晚。面试不推荐作为最终写法。

---

## 解法 2：回溯 + 扫描检查

### 思路

逐行放皇后。

当要在：

```python
row, col
```

放皇后时，只需要检查前面已经放过的行。

因为我们是一行一行往下放的，下面的行还没有皇后。

要检查三件事：

1. 当前列上方有没有皇后
2. 左上对角线有没有皇后
3. 右上对角线有没有皇后

如果都没有，就可以放。

### 代码

```python
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]

        def is_valid(row: int, col: int) -> bool:
            for r in range(row):
                if board[r][col] == "Q":
                    return False

            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1

            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1

            return True

        def backtrack(row: int) -> None:
            if row == n:
                ans.append(["".join(line) for line in board])
                return

            for col in range(n):
                if not is_valid(row, col):
                    continue

                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

        backtrack(0)
        return ans
```

### 为什么只检查上方？

因为回溯是按行从上到下放皇后：

```python
backtrack(row)
```

当前正在放第 `row` 行，只有：

```
0 到 row - 1 行
```

已经放过皇后。

下面的行还没有放，所以不需要检查。

---

## 解法 3：回溯 + 集合剪枝 ⭐ 面试推荐

### 思路

解法 2 每次判断是否合法都要扫描棋盘。

可以用 3 个集合记录已经被占用的列和对角线：

```python
cols
diag1
diag2
```

含义：

| 集合 | 记录内容 | 冲突条件 |
|---|---|---|
| `cols` | 已经放过皇后的列 | `col in cols` |
| `diag1` | 主对角线 `row - col` | `row - col in diag1` |
| `diag2` | 副对角线 `row + col` | `row + col in diag2` |

这样每次判断是否能放皇后就是 O(1)：

```python
if col in cols or row - col in diag1 or row + col in diag2:
    continue
```

### 代码

```python
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]
        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row: int) -> None:
            if row == n:
                ans.append(["".join(line) for line in board])
                return

            for col in range(n):
                if col in cols or row - col in diag1 or row + col in diag2:
                    continue

                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return ans
```

### 为什么 `row - col` 表示主对角线？

主对角线方向是左上到右下。

同一条主对角线上的格子，`row` 和 `col` 同时增加或同时减少，所以差值不变。

比如：

```
(0, 0), (1, 1), (2, 2)
```

都有：

```python
row - col = 0
```

再比如：

```
(0, 1), (1, 2), (2, 3)
```

都有：

```python
row - col = -1
```

### 为什么 `row + col` 表示副对角线？

副对角线方向是右上到左下。

同一条副对角线上的格子，一个方向 `row` 增加，`col` 减少，所以和不变。

比如：

```
(0, 3), (1, 2), (2, 1), (3, 0)
```

都有：

```python
row + col = 3
```

### 为什么要 remove？

因为集合表示的是当前路径中已经放过的皇后攻击范围。

当回溯从下一层返回时，说明当前这个位置的尝试结束了，需要撤销：

```python
cols.remove(col)
diag1.remove(row - col)
diag2.remove(row + col)
```

这和：

```python
board[row][col] = "."
```

是同一个回溯动作。

### 复杂度

搜索树仍然是阶乘级。

用集合后，每次冲突判断是 O(1)，比扫描棋盘更高效。

空间复杂度包含返回结果。

如果不算返回结果：

```text
board 是 O(n^2)
递归深度是 O(n)
三个集合都是 O(n)
```

所以额外空间是：

```
O(n^2)
```

如果只用 `queens[row] = col` 存皇后位置，不维护完整棋盘，可以把工作空间降到 `O(n)`，但构造答案时仍然需要生成棋盘字符串。

### 为什么它最适合面试？

因为它体现了 N 皇后的关键建模：

1. 一行只放一个皇后，所以按行递归
2. 用 `cols` 记录列冲突
3. 用 `row - col` 记录主对角线冲突
4. 用 `row + col` 记录副对角线冲突
5. 放置后递归，回来后撤销

面试时可以这样讲：

> 我按行放皇后。因为每行只放一个，所以行冲突天然避免。为了 O(1) 判断当前位置能不能放，我用三个集合分别记录已经被占用的列、主对角线和副对角线。主对角线用 `row - col` 表示，副对角线用 `row + col` 表示。如果当前位置不冲突，就放皇后并递归下一行，递归结束后撤销。

---

## 最终推荐

面试最推荐写 **解法 3：回溯 + 集合剪枝**。

核心代码：

```python
if col in cols or row - col in diag1 or row + col in diag2:
    continue

board[row][col] = "Q"
cols.add(col)
diag1.add(row - col)
diag2.add(row + col)

backtrack(row + 1)

board[row][col] = "."
cols.remove(col)
diag1.remove(row - col)
diag2.remove(row + col)
```

重点记住：

```
一行一个皇后：按 row 递归
列冲突：col
主对角线冲突：row - col
副对角线冲突：row + col
```
