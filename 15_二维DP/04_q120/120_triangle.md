# 120. 三角形最小路径和

## 题目理解

给你一个三角形数组 `triangle`。

从顶部出发，每次只能移动到下一行中相邻的两个位置之一。

也就是说，如果你当前在第 `row` 行第 `col` 列，那么下一步只能走到：

- `(row + 1, col)`
- `(row + 1, col + 1)`

你需要返回：

> 从顶到底的最小路径和。

例如：

```text
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
答案是 11
```

因为最优路径是：

```text
2 -> 3 -> 5 -> 1
```

路径和为：

```text
11
```

这题本质上仍然是二维 DP，只不过网格不再是矩形，而是三角形。

---

## 为什么这题适合这样学

这题非常适合按下面这条线来理解：

```text
暴力递归 -> 记忆化递归 -> 二维 DP -> 一维压缩 DP
```

因为它和第 64 题《最小路径和》很像，都是最值型 DP。

但它又有自己的特点：

- 状态空间是三角形，不是矩形
- 每个点只能往下一层的两个相邻位置走
- 很适合练“自顶向下”和“自底向上”的理解

---

## 方法一：暴力递归

### 思路

先从最直观的角度想。

如果当前站在位置：

```text
(row, col)
```

那下一步只有两种可能：

- 走到下一行同列 `(row + 1, col)`
- 走到下一行右侧相邻列 `(row + 1, col + 1)`

所以可以定义：

```text
dfs(row, col) = 从当前位置走到底部的最小路径和
```

那么转移就是：

```text
triangle[row][col] + min(dfs(row + 1, col), dfs(row + 1, col + 1))
```

### 边界

如果已经来到最后一行，那就不能再往下走了。

所以：

```text
直接返回当前值
```

### 代码

```python
from typing import List


# 方法一：暴力递归
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        def dfs(row, col):
            if row == n - 1:
                return triangle[row][col]

            return triangle[row][col] + min(dfs(row + 1, col), dfs(row + 1, col + 1))

        return dfs(0, 0)
```

### 复杂度

- 时间复杂度：指数级
- 空间复杂度：`O(n)`，递归栈深度

### 评价

这个方法适合理解状态来源，但重复子问题很多，效率很差。

---

## 方法二：记忆化递归

### 思路

和前面的题一样，问题在于：

```text
dfs(row, col)
```

会被重复计算。

那就把每个位置到底部的最优值存起来。

定义：

```text
memo[(row, col)] = 从这个位置走到底部的最小路径和
```

### 代码

```python
from typing import List


# 方法二：记忆化递归
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = {}

        def dfs(row, col):
            if row == n - 1:
                return triangle[row][col]
            if (row, col) in memo:
                return memo[(row, col)]

            memo[(row, col)] = triangle[row][col] + min(dfs(row + 1, col), dfs(row + 1, col + 1))
            return memo[(row, col)]

        return dfs(0, 0)
```

### 复杂度

- 时间复杂度：`O(n^2)`
- 空间复杂度：`O(n^2)`

### 评价

这个方法已经能过，而且和暴力递归衔接得很自然。

但面试里通常还是更推荐写迭代 DP。

---

## 方法三：二维动态规划（最适合面试）

### 为什么这个最适合面试

这是这题最标准、最稳的写法。

原因：

1. 状态定义非常清楚
2. 转移结构天然对应三角形
3. 边界处理逻辑完整
4. 很适合讲清楚“自顶向下”是怎么推的

所以这题如果面试只准备一个版本，优先准备这个。

---

### 第一步：定义状态

定义：

```text
dp[row][col] = 从顶部走到 triangle[row][col] 的最小路径和
```

最终答案不是某一个固定列，而是最后一行里的最小值：

```text
min(dp[n - 1])
```

因为你到底部之后，可能落在最后一行的任意位置。

---

### 第二步：转移怎么来

走到 `(row, col)`，它的来源取决于位置：

#### 1. 如果是这一行最左边

它只能从上一行最左边下来：

```text
dp[row][0] = dp[row - 1][0] + triangle[row][0]
```

#### 2. 如果是这一行最右边

它只能从上一行最右边过来：

```text
dp[row][row] = dp[row - 1][row - 1] + triangle[row][row]
```

#### 3. 如果是中间位置

它可能从上一行两个位置过来：

- `(row - 1, col - 1)`
- `(row - 1, col)`

所以：

```text
dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col]) + triangle[row][col]
```

这就是整道题最核心的转移结构。

---

### 第三步：边界怎么定

最顶部只有一个点：

```text
dp[0][0] = triangle[0][0]
```

之后一层层往下推即可。

这题和矩形网格不同的地方就在于：

- 每一行长度不同
- 左边界和右边界都要单独处理

---

### 第四步：用例子走一遍

以：

```text
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```

为例。

初始化：

```text
dp[0][0] = 2
```

第二行：

- `dp[1][0] = 2 + 3 = 5`
- `dp[1][1] = 2 + 4 = 6`

第三行：

- `dp[2][0] = 5 + 6 = 11`
- `dp[2][1] = min(5, 6) + 5 = 10`
- `dp[2][2] = 6 + 7 = 13`

第四行：

- `dp[3][0] = 11 + 4 = 15`
- `dp[3][1] = min(11, 10) + 1 = 11`
- `dp[3][2] = min(10, 13) + 8 = 18`
- `dp[3][3] = 13 + 3 = 16`

最后一行最小值是：

```text
11
```

所以答案就是 `11`。

---

### 代码

```python
from typing import List


# 方法三：二维动态规划
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * len(row) for row in triangle]
        dp[0][0] = triangle[0][0]

        for row in range(1, n):
            dp[row][0] = dp[row - 1][0] + triangle[row][0]
            dp[row][row] = dp[row - 1][row - 1] + triangle[row][row]

            for col in range(1, row):
                dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col]) + triangle[row][col]

        return min(dp[-1])
```

### 复杂度

- 时间复杂度：`O(n^2)`
- 空间复杂度：`O(n^2)`

---

### 面试时推荐怎么讲

你可以这样讲：

#### 1. 先定义状态

```text
dp[row][col] 表示从顶部走到当前点的最小路径和
```

#### 2. 再分类讨论来源

- 最左边只能从左上来
- 最右边只能从右上来
- 中间位置可以从左上或右上来

#### 3. 写出转移

```text
dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col]) + triangle[row][col]
```

当然这个式子只适用于中间位置，边界要单独处理。

#### 4. 起点初始化

```text
dp[0][0] = triangle[0][0]
```

#### 5. 最后返回

```text
min(dp[n - 1])
```

因为最后可能落在底边任意位置。

这套讲法很完整，也很符合三角形 DP 的标准表达。

---

## 方法四：一维压缩动态规划

### 思路

这题也可以做空间优化。

我们用一维数组：

```text
dp[col]
```

表示当前处理到这一行时，到达每个位置的最小路径和。

关键点在于：

> 必须从右往左更新。

为什么？

因为 `dp[col]` 新值会依赖上一行的：

- `dp[col]`
- `dp[col - 1]`

如果从左往右更新，会把上一行的值提前覆盖掉。

所以必须倒着更新，才能保证取到的还是上一行状态。

### 代码

```python
from typing import List


# 方法四：一维压缩动态规划
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[0][:]

        for row in range(1, len(triangle)):
            dp.append(dp[-1] + triangle[row][row])

            for col in range(row - 1, 0, -1):
                dp[col] = min(dp[col - 1], dp[col]) + triangle[row][col]

            dp[0] += triangle[row][0]

        return min(dp)
```

### 复杂度

- 时间复杂度：`O(n^2)`
- 空间复杂度：`O(n)`

### 评价

这个方法是标准二维 DP 的空间优化版。

如果面试官追问空间优化，这个版本会很加分。

---

## 方法五：自底向上动态规划

### 思路

这题还有一个非常经典的写法：

从最后一行往上推。

定义：

```text
dp[row][col] = 从当前位置走到底部的最小路径和
```

如果从下往上看，那么当前位置下面只有两个可选位置：

- `(row + 1, col)`
- `(row + 1, col + 1)`

所以：

```text
dp[row][col] = triangle[row][col] + min(dp[row + 1][col], dp[row + 1][col + 1])
```

这和递归定义完全一致，只是换成了迭代。

### 代码

```python
from typing import List


# 方法五：自底向上动态规划
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]

        for row in range(len(triangle) - 2, -1, -1):
            for col in range(row + 1):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])

        return dp[0]
```

### 复杂度

- 时间复杂度：`O(n^2)`
- 空间复杂度：`O(n)`

### 评价

这是这题非常经典的高质量写法。

优点：

- 代码短
- 状态非常自然
- 空间也优化到了 `O(n)`

缺点：

- 如果你前面一直在练“从起点到终点”的 DP，这个方向会稍微跳一下

---

## 哪个方法最适合面试

### 结论

**最适合面试的是：方法三，二维动态规划。**

如果面试官追问空间优化，优先补方法五或方法四都可以。

### 为什么不是别的方法

#### 方法一：暴力递归

- 适合理解状态
- 但会超时
- 不能作为最终答案

#### 方法二：记忆化递归

- 能通过
- 也很自然
- 但一般没有迭代 DP 稳

#### 方法四 / 方法五

- 代码更优
- 但本质上是方法三的优化版本
- 面试里先写二维 DP 更清楚

所以综合来看：

> **方法三最标准，最稳，也最适合作为面试主答案。**

---

## 最适合面试的方法：详细讲解

### 1. 这题和 64 的共同点是什么

共同点是：

- 都是在一个结构里从上往下走
- 都要求最小路径和
- 都属于最值型 DP

所以本质上，二者的思路非常接近。

---

### 2. 这题和 64 的区别是什么

区别在于状态结构不一样：

- 64 是矩形网格
- 120 是三角形结构

这会带来两个变化：

1. 每一行长度不同
2. 边界转移方式不同

尤其是最左边和最右边，来源只有一个，中间位置才有两个来源。

---

### 3. 为什么状态定义成“走到当前点的最小路径和”

因为题目要的是：

```text
从顶部走到底部的最小总代价
```

所以最自然的定义就是：

```text
dp[row][col] = 从顶部走到当前点的最小路径和
```

这样就能很自然地从上一层推到下一层。

---

### 4. 为什么中间位置的转移一定是 `min(左上, 右上) + 当前值`

对于三角形中间位置 `(row, col)` 来说，它只能从上一层两个位置过来：

- `(row - 1, col - 1)`
- `(row - 1, col)`

既然要求最小路径和，那就应该在这两个来源里选更小的那个，再加上当前值。

所以：

```text
dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col]) + triangle[row][col]
```

这就是这题最核心的转移来源。

---

### 5. 为什么最左和最右要单独处理

因为最左边没有“左上”，最右边没有“右上”。

它们各自只有唯一来源：

- 最左边只能从上一行最左边来
- 最右边只能从上一行最右边来

如果不单独处理，数组下标就会越界，而且逻辑也不完整。

这是这题和矩形 DP 最不一样的地方。

---

### 6. 为什么最后答案是 `min(dp[-1])`

因为题目只要求：

```text
走到底边任意位置时的最小路径和
```

并没有说必须落在最后一行某个固定列。

所以我们要在最后一整行里取最小值。

---

### 7. 面试里怎么说最自然

你可以这样讲：

> 我定义 `dp[row][col]` 表示从顶部走到当前点的最小路径和。对于中间位置，它可以从上一层的左上或右上两个位置转移过来，所以状态转移是 `dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col]) + triangle[row][col]`。最左边和最右边因为只有一个来源，所以要单独处理。初始条件是 `dp[0][0] = triangle[0][0]`，最后返回最后一行中的最小值。

这套表达非常完整，也很像三角形 DP 的标准面试答案。

---

### 面试最推荐代码

```python
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * len(row) for row in triangle]
        dp[0][0] = triangle[0][0]

        for row in range(1, n):
            dp[row][0] = dp[row - 1][0] + triangle[row][0]
            dp[row][row] = dp[row - 1][row - 1] + triangle[row][row]

            for col in range(1, row):
                dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col]) + triangle[row][col]

        return min(dp[-1])
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

5. **自底向上动态规划**
   - 方向不同，但也非常经典

### 一句话记忆

> 三角形里每个中间位置的最小路径和，等于左上和右上两条路径里较小的那个，再加上当前值。
