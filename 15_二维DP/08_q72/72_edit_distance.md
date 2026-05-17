# 72. 编辑距离

## 题目理解

给你两个字符串 `word1` 和 `word2`，你需要返回：

> 把 `word1` 转换成 `word2` 所需的最少操作数。

允许的操作只有三种：

1. 插入一个字符
2. 删除一个字符
3. 替换一个字符

例如：

```text
word1 = "horse"
word2 = "ros"
答案是 3
```

一种可行转换过程是：

```text
horse -> rorse   （把 h 替换成 r）
rorse -> rose    （删除一个 r）
rose  -> ros     （删除一个 e）
```

再看一个经典例子：

```text
word1 = "intention"
word2 = "execution"
答案是 5
```

这题是二维 DP 里的门面题之一。

它最重要的地方不是代码长不长，而是：

- 怎么定义“前缀到前缀”的状态
- 为什么插入、删除、替换这三种操作正好对应三种转移

---

## 为什么这题适合这样学

这题很适合按下面这条线来理解：

```text
暴力递归 -> 记忆化搜索 -> 二维 DP -> 一维压缩 DP
```

因为它本质上是在比较两个字符串的前缀关系。

你需要真正想明白的是：

- 当两个字符相等时，为什么可以直接跳过
- 当两个字符不相等时，为什么只需要比较三种操作
- 为什么状态要定义成“前 i 个字符”和“前 j 个字符”

这题一旦把状态定义吃透，后面很多双序列 DP 都会顺很多，比如 LCS、交错字符串、不同子序列。

---

## 方法一：暴力递归

### 思路

先从最直观的定义开始。

设：

```text
dfs(i, j) = 把 word1[i:] 变成 word2[j:] 的最少操作数
```

如果当前两个字符相等：

- 不需要操作
- 直接去看后面：`dfs(i + 1, j + 1)`

如果当前两个字符不相等，就有三种选择：

1. **插入**：给 `word1` 当前位补一个 `word2[j]`，然后继续匹配 `dfs(i, j + 1)`
2. **删除**：删掉 `word1[i]`，然后看 `dfs(i + 1, j)`
3. **替换**：把 `word1[i]` 变成 `word2[j]`，然后看 `dfs(i + 1, j + 1)`

取三种情况的最小值，再加上当前这一步操作。

### 代码

```python
# 方法一：暴力递归
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)

            insert_cost = dfs(i, j + 1)
            delete_cost = dfs(i + 1, j)
            replace_cost = dfs(i + 1, j + 1)

            return min(insert_cost, delete_cost, replace_cost) + 1

        return dfs(0, 0)
```

### 复杂度

- 时间复杂度：较高，存在大量重复子问题
- 空间复杂度：递归栈最坏 `O(m + n)`

### 评价

这个方法最适合帮助你建立问题模型。

但它会重复计算很多状态，所以实际效率比较差。

---

## 方法二：记忆化搜索

### 思路

方法一的问题不是定义错了，而是重复计算太多。

比如：

```text
dfs(i, j)
```

这个状态，可能从很多不同路径反复走到。

所以只要把已经算过的结果记下来，就能把暴力递归优化成二维 DP 级别的复杂度。

递归定义和方法一完全一样，只是多加一个 `memo`。

### 代码

```python
# 方法二：记忆化搜索
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        memo = {}

        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if (i, j) in memo:
                return memo[(i, j)]
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]

            insert_cost = dfs(i, j + 1)
            delete_cost = dfs(i + 1, j)
            replace_cost = dfs(i + 1, j + 1)

            memo[(i, j)] = min(insert_cost, delete_cost, replace_cost) + 1
            return memo[(i, j)]

        return dfs(0, 0)
```

### 复杂度

- 时间复杂度：`O(m * n)`
- 空间复杂度：`O(m * n)`

### 评价

这个方法已经很好了。

它特别适合你从递归定义过渡到 DP 状态定义。

但面试里通常更推荐直接写迭代 DP，因为更标准、更稳。

---

## 方法三：二维动态规划（最适合面试）

### 为什么这个最适合面试

这题如果面试只准备一个版本，我最推荐二维 DP。

原因：

1. 这是编辑距离的标准写法
2. 状态定义非常经典，面试官一眼就知道你会不会这题
3. 三种操作对应三种转移，逻辑特别完整
4. 边界初始化也很有代表性，适合展示你的 DP 基础是否扎实

所以这题最适合面试的方法，就是二维 DP。

---

### 第一步：定义状态

定义：

```text
dp[i][j] = 把 word1 前 i 个字符 变成 word2 前 j 个字符 的最少操作数
```

注意这里的“前 i 个字符”是：

```text
word1[:i]
```

“前 j 个字符”是：

```text
word2[:j]
```

这个定义是这题最关键的地方。

因为它让“最后一步是什么操作”变得非常清楚。

---

### 第二步：初始化边界

如果 `word1` 是空串，要变成 `word2[:j]`，只能一直插入。

所以：

```text
dp[0][j] = j
```

如果 `word2` 是空串，要把 `word1[:i]` 变成空串，只能一直删除。

所以：

```text
dp[i][0] = i
```

---

### 第三步：状态转移

如果当前两个字符相等：

```text
word1[i - 1] == word2[j - 1]
```

那最后一个字符不需要额外操作，直接继承：

```text
dp[i][j] = dp[i - 1][j - 1]
```

如果不相等，就看三种操作：

#### 1）插入

如果最后一步是插入一个字符来匹配 `word2[j - 1]`，那之前相当于：

```text
word1[:i] -> word2[:j - 1]
```

所以代价是：

```text
dp[i][j - 1] + 1
```

#### 2）删除

如果最后一步是删除 `word1[i - 1]`，那之前相当于：

```text
word1[:i - 1] -> word2[:j]
```

所以代价是：

```text
dp[i - 1][j] + 1
```

#### 3）替换

如果最后一步是把 `word1[i - 1]` 替换成 `word2[j - 1]`，那之前相当于：

```text
word1[:i - 1] -> word2[:j - 1]
```

所以代价是：

```text
dp[i - 1][j - 1] + 1
```

最后取最小值：

```text
dp[i][j] = min(
    dp[i][j - 1],
    dp[i - 1][j],
    dp[i - 1][j - 1]
) + 1
```

---

### 代码

```python
# 方法三：二维动态规划
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i][j - 1],
                        dp[i - 1][j],
                        dp[i - 1][j - 1],
                    ) + 1

        return dp[m][n]
```

### 复杂度

- 时间复杂度：`O(m * n)`
- 空间复杂度：`O(m * n)`

### 面试怎么讲

面试里建议你按这条线来讲：

1. 定义 `dp[i][j]` 表示前缀到前缀的最小编辑距离
2. 边界是空串和非空串之间的转换
3. 字符相等时，直接继承左上角
4. 字符不等时，考虑插入、删除、替换三种操作
5. 取三者最小值加一

这一套说出来会非常完整，也非常像标准答案。

---

## 方法四：一维压缩 DP

### 思路

观察二维 DP 的转移：

```text
dp[i][j]
```

只依赖：

- 当前行左边 `dp[i][j - 1]`
- 上一行当前列 `dp[i - 1][j]`
- 上一行左上角 `dp[i - 1][j - 1]`

所以没必要保留整张二维表，可以压成一维数组。

不过这里会比二维版本更绕一点，因为你需要额外保存“左上角旧值”。

### 代码

```python
# 方法四：一维压缩动态规划
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = list(range(n + 1))

        for i in range(1, m + 1):
            prev_diagonal = dp[0]
            dp[0] = i

            for j in range(1, n + 1):
                current = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev_diagonal
                else:
                    dp[j] = min(
                        dp[j],
                        dp[j - 1],
                        prev_diagonal,
                    ) + 1
                prev_diagonal = current

        return dp[n]
```

### 复杂度

- 时间复杂度：`O(m * n)`
- 空间复杂度：`O(n)`

### 评价

这个方法更省空间，也很经典。

但如果是面试现场，我还是更推荐先写二维 DP。

因为二维 DP：

- 更稳
- 更不容易写错
- 更容易把状态和转移解释清楚

---

## 最后总结

这题建议这样记：

- **递归定义**：当前字符相等就跳过，不相等就试三种操作
- **核心状态**：前缀到前缀的最小编辑距离
- **最适合面试**：二维 DP
- **进阶优化**：一维压缩 DP

如果你是为了面试准备，这题最应该熟练到可以默写的是：

> **二维 DP 版本**

因为它是双序列 DP 的经典代表题，面试中出现频率非常高。
