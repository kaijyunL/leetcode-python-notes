# LeetCode 52 — N 皇后 II（N-Queens II）

## 题目

给定整数 `n`，返回 N 皇后不同解法的数量。

和 Q51 不同，这题不需要返回具体棋盘，只需要返回方案数。

### 示例

```
输入: n = 4
输出: 2
```

因为 4 皇后一共有 2 种不同摆法。

---

## 和 Q51 的区别

Q51 是：

```python
return 所有棋盘
```

所以需要构造：

```python
[".Q..", "...Q", "Q...", "..Q."]
```

Q52 是：

```python
return 方案数量
```

所以不需要维护完整棋盘，也不需要构造字符串。

只要每找到一个合法方案，就：

```python
count += 1
```

---

## 核心理解

N 皇后仍然按行递归。

```python
backtrack(row)
```

表示：

```
当前要给第 row 行放皇后
```

每一行尝试所有列：

```python
for col in range(n):
```

如果当前位置不冲突，就放皇后，递归下一行。

当：

```python
row == n
```

说明 `0` 到 `n-1` 行都放好了，找到一个完整方案。

---

## 解法一览

| 解法 | 思路 | 时间复杂度 | 空间复杂度 | 是否推荐面试 |
|---|---|---|---|---|
| 1. 回溯 + 扫描检查 | 逐行放皇后，每次扫描上方列和对角线 | O(n!) 级别 | O(n^2) | 标准回溯 |
| 2. 回溯 + 集合剪枝 | 用集合 O(1) 判断列和对角线冲突 | O(n!) 级别 | O(n) | **面试推荐 ✅** |

> 这题还有位运算写法，速度更快，但对普通面试不是必须。先掌握集合剪枝版更稳。

---

## 解法 1：回溯 + 扫描检查

### 思路

这是 Q51 的标准回溯写法，只是把“收集棋盘”改成“计数”。

仍然维护一个棋盘：

```python
board = [["."] * n for _ in range(n)]
```

判断当前位置能不能放时，扫描：

1. 当前列上方
2. 左上对角线
3. 右上对角线

如果都没有皇后，就可以放。

### 代码

```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
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
            nonlocal count

            if row == n:
                count += 1
                return

            for col in range(n):
                if not is_valid(row, col):
                    continue

                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

        backtrack(0)
        return count
```

### 为什么这叫标准回溯？

因为结构非常清楚：

```python
for col in range(n):
    if 不能放:
        continue

    放皇后
    backtrack(row + 1)
    撤销皇后
```

它完整表达了：

```
做选择 -> 递归 -> 撤销选择
```

---

## 解法 2：回溯 + 集合剪枝 ⭐ 面试推荐

### 思路

Q52 只要数量，不需要棋盘，所以可以不用 `board`。

用 3 个集合记录已经被占用的列和对角线：

| 集合 | 记录内容 | 冲突条件 |
|---|---|---|
| `cols` | 已经放过皇后的列 | `col in cols` |
| `diag1` | 主对角线 `row - col` | `row - col in diag1` |
| `diag2` | 副对角线 `row + col` | `row + col in diag2` |

每次判断冲突就是：

```python
if col in cols or row - col in diag1 or row + col in diag2:
    continue
```

如果不冲突，就加入集合，递归下一行。递归回来后从集合中删除。

### 代码

```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row: int) -> None:
            nonlocal count

            if row == n:
                count += 1
                return

            for col in range(n):
                if col in cols or row - col in diag1 or row + col in diag2:
                    continue

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return count
```

### 为什么 Q52 可以不维护 board？

因为题目只要数量。

Q51 需要返回棋盘，所以必须知道每一行皇后放在哪一列。

Q52 只关心有多少种放法。只要集合能判断冲突，就不需要保存具体棋盘。

当：

```python
row == n
```

时，说明已经成功放了 `n` 个皇后，直接：

```python
count += 1
```

就可以了。

### 对角线为什么还是 `row - col` 和 `row + col`？

和 Q51 一样：

```python
row - col
```

表示主对角线。

```python
row + col
```

表示副对角线。

只要这两个值已经在集合里，说明当前位置会和已有皇后处于同一条对角线。

### 为什么要 `nonlocal count`？

因为 `count` 定义在外层函数：

```python
count = 0
```

内部函数 `backtrack` 中要修改它：

```python
count += 1
```

Python 中如果内部函数要修改外层变量，需要声明：

```python
nonlocal count
```

否则 Python 会把 `count` 当成内部函数的局部变量，导致报错。

### 复杂度

搜索复杂度仍然是阶乘级。

相比扫描检查版，集合版把冲突判断降到了 O(1)。

如果不算递归调用栈，三个集合最多各存 `n` 个元素：

```
O(n)
```

递归深度最多也是：

```
O(n)
```

所以额外空间是：

```
O(n)
```

### 为什么它最适合面试？

因为它是 Q51 集合剪枝版的自然简化：

1. 按行递归
2. 用 `cols` 判断列冲突
3. 用 `row - col` 判断主对角线冲突
4. 用 `row + col` 判断副对角线冲突
5. 找到一组完整摆法时只计数，不构造棋盘

面试时可以这样讲：

> Q52 和 Q51 一样按行放皇后。区别是 Q52 只返回数量，所以不需要维护棋盘。用三个集合记录已经被占用的列、主对角线和副对角线。如果当前位置不冲突，就加入集合并递归下一行；递归回来后撤销。`row == n` 时说明放完了 n 个皇后，方案数加一。

---

## 最终推荐

面试最推荐写 **解法 2：回溯 + 集合剪枝**。

核心代码：

```python
if col in cols or row - col in diag1 or row + col in diag2:
    continue

cols.add(col)
diag1.add(row - col)
diag2.add(row + col)

backtrack(row + 1)

cols.remove(col)
diag1.remove(row - col)
diag2.remove(row + col)
```

重点记住：

```
Q51：返回棋盘，需要构造 board
Q52：返回数量，可以只维护冲突集合和 count
```
