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
两个方向上的任何一条对角线都不能有两个皇后
```

先把这道题看成“每一层给一行选一个位置”：

```text
F0：给第 0 行选列
F1：给第 1 行选列
F2：给第 2 行选列
...
Fn：所有行都放好了，得到一个答案
```

`row` 表示当前正在处理第几行，`col` 表示这一行准备尝试第几列。每一层的循环都会从左到右尝试所有列：

```python
for col in range(n):
```

如果当前位置和前面已经放好的皇后冲突，就跳过；如果不冲突，就暂时放下皇后，进入下一行。下一行搜索结束后，再把这个皇后拿走，回到当前行继续尝试下一个 `col`。

所以回溯的固定结构是：

```text
选择当前行的一列
进入下一行继续放
下一行结束后撤销选择
回到当前行尝试下一列
```

例如 `n = 4` 时，第一层可能这样展开：

```text
F0：row = 0
├── col = 0，放在 (0, 0)，进入 F1
├── col = 1，放在 (0, 1)，进入 F1
├── col = 2，放在 (0, 2)，进入 F1
└── col = 3，放在 (0, 3)，进入 F1
```

并不是每个分支都能走到最后。有的分支在某一行找不到合法列，就返回上一层，撤销上一行的皇后，再换一个列继续搜索。

---

## 对角线怎么判断？

不要把“主对角线”和“副对角线”理解成棋盘上各自只有一条线。这里真正需要区分的是两种方向：

```text
方向 1：左上 -> 右下
方向 2：右上 -> 左下
```

每个方向都有很多条平行的线。对于格子 `(row, col)`，用一个编号标记它属于哪一条线：

```text
左上 -> 右下方向：编号 row - col
右上 -> 左下方向：编号 row + col
```

编号相同，就在同一条对角线上。

例如：

```text
(0, 0) 和 (1, 1)
```

两者的：

```python
row - col: 0, 0
```

所以它们在同一条左上到右下的对角线上。

再看你刚才指出的冲突：

```text
(0, 1) 和 (1, 0)
```

两者的：

```python
row + col: 1, 1
```

所以它们在同一条右上到左下的对角线上。

因此，代码中的：

```python
diag1
diag2
```

分别记录两种方向上已经被占用的对角线编号。判断 `(row, col)` 能不能放皇后，只需要检查：

```python
col in cols
row - col in diag1
row + col in diag2
```

只要其中一个成立，就说明当前格子和已有皇后同列或同一条对角线，不能放。

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
| `diag1` | 左上到右下方向的所有对角线编号 `row - col` | `row - col in diag1` |
| `diag2` | 右上到左下方向的所有对角线编号 `row + col` | `row + col in diag2` |

这样每次判断是否能放皇后就是 O(1)：

```python
if col in cols or row - col in diag1 or row + col in diag2:
    continue
```

这里的三个集合可以先只理解成“当前路径上的禁用标记”：

```text
cols：这一列已经有皇后，不能再放
diag1：这条左上到右下方向的对角线已经有皇后，不能再放
diag2：这条右上到左下方向的对角线已经有皇后，不能再放
```

假设当前准备把皇后放到 `(row, col)`，就同时检查三个编号：

```python
col
row - col
row + col
```

只要其中一个编号已经在对应集合中，就说明当前格子会和已有皇后同列或同对角线，不能放。

放置一个皇后时，四个状态一起变化：

```python
board[row][col] = "Q"
cols.add(col)
diag1.add(row - col)
diag2.add(row + col)
```

递归返回时，必须把这四个变化全部撤销：

```python
board[row][col] = "."
cols.remove(col)
diag1.remove(row - col)
diag2.remove(row + col)
```

这样上一层才能把当前皇后拿走，并尝试同一行的下一个列。

### 用 `n = 4` 走一条失败分支

下面只关注程序执行位置，不展开所有分支：

```text
F0：row = 0，col = 0
放置 (0, 0)
board = ["Q...", "....", "....", "...."]
cols = {0}
diag1 = {0}
diag2 = {0}

进入 F1：row = 1
```

在 `F1` 中：

```text
col = 0：和 (0, 0) 同列，跳过
col = 1：和 (0, 0) 在同一条右上到左下方向的对角线上，跳过
col = 2：可以放置 (1, 2)
```

放置 `(1, 2)` 后：

```text
board = ["Q...", "..Q.", "....", "...."]
cols = {0, 2}
diag1 = {0, -1}
diag2 = {0, 3}
```

进入 `F2` 后：

```text
col = 0：同列冲突
col = 1：和 (1, 2) 在同一条右上到左下方向的对角线上，冲突
col = 2：同列冲突
col = 3：和 (1, 2) 在同一条左上到右下方向的对角线上，冲突
```

因此 `F2` 的循环结束，返回 `F1`。注意，返回后程序会继续执行 `F1` 中递归调用后面的撤销代码：

```python
board[1][2] = "."
cols.remove(2)
diag1.remove(-1)
diag2.remove(3)
```

状态恢复为：

```text
board = ["Q...", "....", "....", "...."]
cols = {0}
diag1 = {0}
diag2 = {0}
```

然后 `F1` 的循环继续，尝试下一个 `col = 3`。这就是“回到上一层”的具体含义：

```text
F2 结束
回到 F1
撤销 F1 刚才选择的第 2 列
F1 的 col 继续变成 3
```

如果 `F1` 的所有列都尝试完仍然失败，`F1` 自己也会返回 `F0`，然后 `F0` 撤销 `(0, 0)`，继续尝试第 0 行的 `col = 1`。

### 找到一个答案时发生什么？

当递归进入：

```python
backtrack(row)
```

并且：

```python
row == n
```

说明第 `0` 行到第 `n - 1` 行都已经放好了皇后。此时把当前棋盘复制到答案：

```python
ans.append(["".join(line) for line in board])
```

之后仍然会返回上一层并继续回溯，因为题目要求找到所有摆法，而不是找到一个就结束。

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

### 为什么 `row - col` 能标记左上到右下方向？

同一条左上到右下方向的对角线上的格子，`row` 和 `col` 同时增加或同时减少，所以差值不变。

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

### 为什么 `row + col` 能标记右上到左下方向？

同一条右上到左下方向的对角线上的格子，一个方向 `row` 增加，`col` 减少，所以和不变。

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
3. 用 `row - col` 记录左上到右下方向的对角线冲突
4. 用 `row + col` 记录右上到左下方向的对角线冲突
5. 放置后递归，回来后撤销

面试时可以这样讲：

> 我按行放皇后。因为每行只放一个，所以行冲突天然避免。为了 O(1) 判断当前位置能不能放，我用三个集合分别记录已经被占用的列，以及两个方向上的对角线。左上到右下方向用 `row - col` 表示，右上到左下方向用 `row + col` 表示。如果当前位置不冲突，就放皇后并递归下一行，递归结束后撤销。

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
左上到右下方向冲突：row - col
右上到左下方向冲突：row + col
```
