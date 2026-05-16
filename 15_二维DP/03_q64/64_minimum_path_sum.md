# 64. 最小路径和

## 题目理解

给你一个 `m x n` 的非负整数网格 `grid`。

你从左上角出发，每次只能：

- 向下走一格
- 向右走一格

最终要走到右下角。

你需要返回：

> 从左上到右下路径上的数字总和最小是多少。

例如：

```text
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
答案是 7
```

因为最优路径可以是：

```text
1 -> 3 -> 1 -> 1 -> 1
```

路径和为：

```text
7
```

这题和第 62、63 题的结构非常接近，只不过它不再是“计数”，而是“最值”。

---

## 为什么这题适合这样学

这题非常适合按下面这条线来理解：

```text
暴力递归 -> 记忆化递归 -> 二维 DP -> 一维压缩 DP
```

因为它和前两道网格题很像，但多了一个关键变化：

```text
不是求路径数，而是求最小代价
```

所以这题很适合练：

1. 二维网格里的“最值型 DP”
2. 为什么转移是 `min(...)`
3. 边界初始化为什么不能直接全设成 1

---

## 方法一：暴力递归

### 思路

先从最直观的角度想。

如果当前站在位置：

```text
(row, col)
```

那下一步只有两种可能：

- 向下走
- 向右走

所以可以定义：

```text
dfs(row, col) = 从 (row, col) 走到右下角的最小路径和
```

那么：

- 如果往下走，总代价是 `grid[row][col] + dfs(row + 1, col)`
- 如果往右走，总代价是 `grid[row][col] + dfs(row, col + 1)`

取两者较小值即可。

### 边界

- 如果已经走到右下角，返回当前格子的值
- 如果越界，返回正无穷，表示这条路不可选

### 代码

```python
from typing import List


# 方法一：暴力递归
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(row, col):
            if row >= m or col >= n:
                return float("inf")
            if row == m - 1 and col == n - 1:
                return grid[row][col]

            return grid[row][col] + min(dfs(row + 1, col), dfs(row, col + 1))

        return dfs(0, 0)
```

### 复杂度

- 时间复杂度：指数级
- 空间复杂度：`O(m + n)`

### 评价

这个方法适合理解状态来源和为什么要取 `min`。

但它会反复计算同一个位置，所以效率很差。

---

## 方法二：记忆化递归

### 思路

和前两道网格题一样，问题在于：

```text
dfs(row, col)
```

会被重复计算很多次。

那就把每个位置的答案存起来。

定义：

```text
memo[(row, col)] = 从这个位置到终点的最小路径和
```

### 代码

```python
from typing import List


# 方法二：记忆化递归
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}

        def dfs(row, col):
            if row >= m or col >= n:
                return float("inf")
            if row == m - 1 and col == n - 1:
                return grid[row][col]
            if (row, col) in memo:
                return memo[(row, col)]

            memo[(row, col)] = grid[row][col] + min(dfs(row + 1, col), dfs(row, col + 1))
            return memo[(row, col)]

        return dfs(0, 0)
```

### 复杂度

- 时间复杂度：`O(m * n)`
- 空间复杂度：`O(m * n)`

### 评价

这个方法已经很好了，而且从暴力递归升级过来非常自然。

但面试里通常还是更推荐写迭代 DP。

---

## 方法三：二维动态规划（最适合面试）

### 为什么这个最适合面试

这是这题最标准、最稳的写法。

原因：

1. 状态定义自然
2. 转移方程清楚
3. 边界处理逻辑完整
4. 是网格最值 DP 的经典模板

所以这题如果面试只准备一个版本，优先准备这个。

---

### 第一步：定义状态

定义：

```text
dp[row][col] = 从左上角走到 (row, col) 的最小路径和
```

最终答案就是：

```text
dp[m - 1][n - 1]
```

---

### 第二步：转移怎么来

要走到某个格子 `(row, col)`，最后一步仍然只可能来自：

- 上边 `(row - 1, col)`
- 左边 `(row, col - 1)`

但是这题要求的是最小路径和，所以要选代价更小的那条路：

```text
dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]
```

这就是这道题最核心的转移方程。

---

### 第三步：边界怎么定

#### 1. 起点

起点只能从自己开始，所以：

```text
dp[0][0] = grid[0][0]
```

#### 2. 第一列

第一列只能从上边一路走下来，所以：

```text
dp[row][0] = dp[row - 1][0] + grid[row][0]
```

#### 3. 第一行

第一行只能从左边一路走过来，所以：

```text
dp[0][col] = dp[0][col - 1] + grid[0][col]
```

这些边界和 62/63 不同，因为这里不是“路径数”，而是“累计代价”。

---

### 第四步：用例子走一遍

以：

```text
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
```

为例。

先初始化：

```text
dp[0][0] = 1
```

第一行：

```text
1 4 5
```

因为：

- `1`
- `1 + 3 = 4`
- `4 + 1 = 5`

第一列：

```text
1
2
6
```

因为：

- `1`
- `1 + 1 = 2`
- `2 + 4 = 6`

然后继续推：

- `dp[1][1] = min(4, 2) + 5 = 7`
- `dp[1][2] = min(5, 7) + 1 = 6`
- `dp[2][1] = min(7, 6) + 2 = 8`
- `dp[2][2] = min(6, 8) + 1 = 7`

最后答案就是：

```text
7
```

---

### 代码

```python
from typing import List


# 方法三：二维动态规划
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for row in range(1, m):
            dp[row][0] = dp[row - 1][0] + grid[row][0]

        for col in range(1, n):
            dp[0][col] = dp[0][col - 1] + grid[0][col]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]

        return dp[m - 1][n - 1]
```

### 复杂度

- 时间复杂度：`O(m * n)`
- 空间复杂度：`O(m * n)`

---

### 面试时推荐怎么讲

你可以这样讲：

#### 1. 先定义状态

```text
dp[row][col] 表示走到当前格子的最小路径和
```

#### 2. 再解释最后一步来源

走到当前格子，只可能从上面或左边过来。

#### 3. 写出转移

```text
dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]
```

#### 4. 说明边界

- 起点是 `grid[0][0]`
- 第一行只能从左边累加
- 第一列只能从上边累加

#### 5. 最后返回

```text
dp[m - 1][n - 1]
```

这套讲法会非常完整，也很像网格最值 DP 的标准面试答案。

---

## 方法四：一维压缩动态规划

### 思路

观察方法三会发现：

```text
dp[row][col]
```

只依赖：

- 上一行同列的值
- 当前行左边的值

所以可以用一维数组：

```text
dp[col]
```

来压缩空间。

更新时：

```text
dp[col] = min(dp[col], dp[col - 1]) + grid[row][col]
```

其中：

- `dp[col]` 更新前表示上边路径和
- `dp[col - 1]` 表示左边路径和

### 代码

```python
from typing import List


# 方法四：一维压缩动态规划
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]

        for col in range(1, n):
            dp[col] = dp[col - 1] + grid[0][col]

        for row in range(1, m):
            dp[0] += grid[row][0]
            for col in range(1, n):
                dp[col] = min(dp[col], dp[col - 1]) + grid[row][col]

        return dp[-1]
```

### 复杂度

- 时间复杂度：`O(m * n)`
- 空间复杂度：`O(n)`

### 评价

这个方法是标准二维 DP 的空间优化版。

如果面试官追问能不能优化空间，可以继续写这个版本。

---

## 哪个方法最适合面试

### 结论

**最适合面试的是：方法三，二维动态规划。**

### 为什么不是别的方法

#### 方法一：暴力递归

- 适合理解状态
- 但会超时
- 不能作为最终答案

#### 方法二：记忆化递归

- 能通过
- 也很自然
- 但一般没有迭代 DP 稳

#### 方法四：一维压缩 DP

- 更省空间
- 但转移解释不如二维表直观
- 面试里通常先写二维 DP 更清晰

所以综合来看：

> **方法三最标准，最稳，也最适合作为面试主答案。**

---

## 最适合面试的方法：详细讲解

### 1. 这题和 62 / 63 的共同点是什么

共同点是：

- 都是在网格上移动
- 都只能向下或向右
- 所以当前状态都只会从上面或左边转移过来

这说明它们本质上都是同一类网格 DP。

---

### 2. 这题和 62 / 63 的区别是什么

区别在于：

- 62 求的是路径数
- 63 求的是带障碍的路径数
- 64 求的是最小路径和

所以这题不再是：

```text
上边 + 左边
```

而是：

```text
min(上边, 左边) + 当前格子代价
```

这就是“计数型 DP”切换到“最值型 DP”的关键变化。

---

### 3. 为什么状态定义成“走到当前格子的最小路径和”

因为题目要的是：

```text
从起点走到终点的最小总代价
```

所以最自然的定义就是：

```text
dp[row][col] = 走到当前格子的最小路径和
```

最终答案自然就是右下角的值。

这个状态定义非常顺，也最容易写出转移方程。

---

### 4. 为什么转移一定是 `min(上边, 左边) + 当前值`

因为走到当前格子 `(row, col)`，最后一步只有两个来源：

- 从 `(row - 1, col)` 向下走
- 从 `(row, col - 1)` 向右走

既然题目要最小路径和，那就应该选择：

```text
到达这两个来源位置时，路径和更小的那一个
```

再加上当前格子的代价。

所以：

```text
dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]
```

这是这题最核心的正确性来源。

---

### 5. 为什么第一行和第一列要单独初始化

因为第一行只能从左边一路走过来。

所以它只能做前缀和累加。

第一列只能从上边一路走下来。

所以它也只能做前缀和累加。

这和 62/63 的边界完全不同：

- 62/63 的边界是路径数
- 64 的边界是累计代价

这点特别容易混。

---

### 6. 面试里怎么说最自然

你可以这样讲：

> 我定义 `dp[row][col]` 表示从左上角走到当前格子的最小路径和。由于每次只能向右或者向下，所以走到当前格子只可能从上边或者左边过来，因此转移方程是 `dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]`。边界上，第一行只能从左边累加，第一列只能从上边累加，起点初始化为 `grid[0][0]`。最后返回 `dp[m - 1][n - 1]`。

这套表述很完整，也很像网格最值型 DP 的标准面试回答。

---

### 面试最推荐代码

```python
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for row in range(1, m):
            dp[row][0] = dp[row - 1][0] + grid[row][0]

        for col in range(1, n):
            dp[0][col] = dp[0][col - 1] + grid[0][col]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]

        return dp[m - 1][n - 1]
```

---

## 总结

### 递进关系

1. **暴力递归**
   - 最直观
   - 但重复子问题很多

2. **记忆化递归**
   - 消除重复计算
   - 保留递归思路

3. **二维动态规划**
   - 最标准
   - 最适合面试

4. **一维压缩动态规划**
   - 在标准 DP 基础上优化空间

### 一句话记忆

> 走到每个格子的最小路径和，等于走到它上边或左边的较小路径和，再加上当前格子的值。
