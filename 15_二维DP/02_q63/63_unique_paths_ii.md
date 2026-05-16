# 63. 不同路径 II

## 题目理解

一个机器人位于一个 `m x n` 网格的左上角。

它每次只能：

- 向下走一格
- 向右走一格

目标是走到右下角。

但是这一次，网格里有障碍物。

- `0` 表示空位置，可以走
- `1` 表示障碍物，不能走

你需要返回：

> 一共有多少条不同路径。

例如：

```text
obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
答案是 2
```

因为中间那个格子被挡住了，只剩两条可行路径。

这题本质上就是第 62 题《不同路径》的带障碍版本，是二维网格 DP 的经典进阶题。

---

## 为什么这题适合这样学

这题非常适合按下面这条线来理解：

```text
暴力递归 -> 记忆化递归 -> 二维 DP -> 一维压缩 DP
```

它和第 62 题几乎是同一条主线，只不过多了一个关键变化：

```text
有些格子不能走
```

所以这题特别适合练：

1. 原有转移在加约束后怎么改
2. 边界初始化为什么更容易出错
3. 一维压缩时障碍物如何处理

---

## 方法一：暴力递归

### 思路

先从最直观的角度想。

如果当前站在位置：

```text
(row, col)
```

那下一步仍然只有两种可能：

- 向下走
- 向右走

但是前提是：

- 当前位置不能是障碍物
- 下一步不能越界

所以可以定义：

```text
dfs(row, col) = 从 (row, col) 走到右下角的路径数
```

### 转移

如果当前位置是障碍物：

```text
返回 0
```

如果已经走到右下角，且这个位置不是障碍物：

```text
返回 1
```

否则就继续尝试向下和向右。

### 代码

```python
from typing import List


# 方法一：暴力递归
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        def dfs(row, col):
            if row >= m or col >= n:
                return 0
            if obstacleGrid[row][col] == 1:
                return 0
            if row == m - 1 and col == n - 1:
                return 1

            return dfs(row + 1, col) + dfs(row, col + 1)

        return dfs(0, 0)
```

### 复杂度

- 时间复杂度：指数级
- 空间复杂度：`O(m + n)`

### 评价

这个方法适合理解障碍物是怎么影响原始递归的。

但重复子问题仍然很多，所以不能作为最终解法。

---

## 方法二：记忆化递归

### 思路

和第 62 题一样，问题在于：

```text
dfs(row, col)
```

会被重复计算很多次。

那就把结果存起来。

定义：

```text
memo[(row, col)] = 从这个位置走到终点的路径数
```

### 代码

```python
from typing import List


# 方法二：记忆化递归
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}

        def dfs(row, col):
            if row >= m or col >= n:
                return 0
            if obstacleGrid[row][col] == 1:
                return 0
            if row == m - 1 and col == n - 1:
                return 1
            if (row, col) in memo:
                return memo[(row, col)]

            memo[(row, col)] = dfs(row + 1, col) + dfs(row, col + 1)
            return memo[(row, col)]

        return dfs(0, 0)
```

### 复杂度

- 时间复杂度：`O(m * n)`
- 空间复杂度：`O(m * n)`

### 评价

这个方法已经能过，而且很容易从暴力递归升级过来。

缺点还是一样：

- 递归写法
- 面试里通常不如迭代 DP 稳

---

## 方法三：二维动态规划（最适合面试）

### 为什么这个最适合面试

这是这题最标准、最稳的写法。

原因：

1. 状态定义非常清楚
2. 障碍物处理能直接体现在状态转移里
3. 边界处理虽然更细，但逻辑完整
4. 是网格 DP 进阶题里非常标准的一道

所以这题如果面试只准备一个版本，优先准备这个。

---

### 第一步：定义状态

定义：

```text
dp[row][col] = 从左上角走到 (row, col) 的路径数
```

最终答案就是：

```text
dp[m - 1][n - 1]
```

---

### 第二步：障碍物怎么处理

如果某个格子是障碍物，那就说明：

```text
不能走到这里
```

所以它的路径数必须是：

```text
dp[row][col] = 0
```

这一步是和第 62 题最本质的区别。

---

### 第三步：转移怎么来

如果当前位置不是障碍物，那么它仍然只能从两个方向过来：

- 上边 `(row - 1, col)`
- 左边 `(row, col - 1)`

所以：

```text
dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
```

但这只在当前位置不是障碍物时成立。

---

### 第四步：边界怎么定

这题最容易出错的地方就在边界。

#### 1. 起点如果是障碍物

如果左上角就是障碍物：

```text
答案直接是 0
```

#### 2. 第一列初始化

第一列本来只能一直向下走。

但是一旦某个位置出现障碍物，后面就都到不了了。

所以：

- 遇到障碍物之前，如果上面可达，就填 1
- 一旦被障碍物挡住，后面都只能是 0

#### 3. 第一行初始化

第一行同理。

- 遇到障碍物之前，如果左边可达，就填 1
- 一旦被挡住，后面也都只能是 0

---

### 第五步：用例子走一遍

以：

```text
obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
```

为例。

先初始化起点：

```text
dp[0][0] = 1
```

第一行：

```text
1 1 1
```

第一列：

```text
1
1
1
```

中间 `(1,1)` 是障碍物，所以：

```text
dp[1][1] = 0
```

然后继续推：

- `dp[1][2] = dp[0][2] + dp[1][1] = 1 + 0 = 1`
- `dp[2][1] = dp[1][1] + dp[2][0] = 0 + 1 = 1`
- `dp[2][2] = dp[1][2] + dp[2][1] = 1 + 1 = 2`

所以答案是：

```text
2
```

---

### 代码

```python
from typing import List


# 方法三：二维动态规划
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for row in range(1, m):
            if obstacleGrid[row][0] == 0:
                dp[row][0] = dp[row - 1][0]

        for col in range(1, n):
            if obstacleGrid[0][col] == 0:
                dp[0][col] = dp[0][col - 1]

        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] == 0:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

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
dp[row][col] 表示走到当前格子的路径数
```

#### 2. 说明障碍物影响

如果当前格子是障碍物，那么它不可达，路径数就是 0。

#### 3. 写出转移

如果不是障碍物，就仍然来自上边和左边：

```text
dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
```

#### 4. 强调边界

- 起点如果是障碍物，直接返回 0
- 第一行和第一列要考虑障碍物会把后续整段截断

#### 5. 最后返回

```text
dp[m - 1][n - 1]
```

这套讲法会很完整，而且比直接背代码更像真正理解了题目。

---

## 方法四：一维压缩动态规划

### 思路

和第 62 题一样，这题也可以做空间优化。

我们用：

```text
dp[col]
```

表示当前处理到这一行时，每一列的路径数。

但是这里要多处理一个点：

如果当前位置是障碍物，那么：

```text
dp[col] = 0
```

因为这个位置不可达。

如果不是障碍物，那么：

```text
dp[col] += dp[col - 1]
```

其中：

- `dp[col]` 表示上方路径数
- `dp[col - 1]` 表示左边路径数

### 代码

```python
from typing import List


# 方法四：一维压缩动态规划
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0

        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0
                elif col > 0:
                    dp[col] += dp[col - 1]

        return dp[-1]
```

### 复杂度

- 时间复杂度：`O(m * n)`
- 空间复杂度：`O(n)`

### 评价

这个方法是标准 DP 的空间优化版。

如果面试官追问优化，可以继续写这个版本。

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
- 但障碍物处理会稍微绕一点
- 面试里先写二维 DP 更清晰

所以综合来看：

> **方法三最标准，最稳，也最适合作为面试主答案。**

---

## 最适合面试的方法：详细讲解

### 1. 这题比第 62 题多了什么

第 62 题是没有障碍物的纯计数。

这题只多了一个条件：

```text
有些格子不能走
```

所以本质上仍然是网格计数 DP，只是要把障碍物状态加进去。

---

### 2. 为什么状态定义不变

我们仍然定义：

```text
dp[row][col] = 走到当前格子的路径数
```

因为题目要的还是“到达终点有多少种走法”。

障碍物不会改变这个状态定义，只会改变某些格子的取值。

---

### 3. 为什么障碍物格子的值一定是 0

因为障碍物格子根本不能站上去。

既然不能站上去，那么走到这里的路径数当然就是：

```text
0
```

这一步想清楚之后，后面的转移就顺了很多。

---

### 4. 为什么正常格子还是“上边 + 左边”

只要当前格子不是障碍物，那么走到它的最后一步来源没有变。

机器人仍然只能：

- 从上边下来
- 从左边过来

所以转移仍然是：

```text
dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
```

也就是说：

> **障碍物改变的是某些格子的可达性，不改变普通格子的转移结构。**

---

### 5. 为什么第一行和第一列要单独处理

因为第一行只能从左边来，第一列只能从上边来。

一旦遇到障碍物：

- 第一行后面的格子都到不了了
- 第一列下面的格子也都到不了了

所以边界不能像第 62 题那样直接全填 1，而必须结合障碍物逐个初始化。

这正是这题最容易写错的地方。

---

### 6. 面试里怎么说最自然

你可以这样讲：

> 我定义 `dp[row][col]` 表示从左上角走到当前格子的路径数。如果当前位置是障碍物，那么它不可达，`dp[row][col] = 0`。如果不是障碍物，那么它只能从上边或者左边过来，所以转移方程还是 `dp[row][col] = dp[row - 1][col] + dp[row][col - 1]`。需要特别注意的是第一行和第一列的初始化，因为一旦遇到障碍物，后面的格子就都不可达了。最后返回 `dp[m - 1][n - 1]`。

这套表达会很完整，也能说明你真正理解了这题和第 62 题的关系。

---

### 面试最推荐代码

```python
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for row in range(1, m):
            if obstacleGrid[row][0] == 0:
                dp[row][0] = dp[row - 1][0]

        for col in range(1, n):
            if obstacleGrid[0][col] == 0:
                dp[0][col] = dp[0][col - 1]

        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] == 0:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

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

> 如果当前格子是障碍物，路径数就是 0；否则路径数等于上边格子的路径数加上左边格子的路径数。
