# 1143. 最长公共子序列

## 题目理解

给你两个字符串 `text1` 和 `text2`，你需要返回：

> 它们的最长公共子序列长度。

这里要特别注意：

- **子序列不要求连续**
- 但字符的相对顺序不能变

例如：

```text
text1 = "abcde"
text2 = "ace"
答案是 3
```

因为公共子序列可以是：

```text
"ace"
```

再看一个例子：

```text
text1 = "abc"
text2 = "abc"
答案是 3
```

再看：

```text
text1 = "abc"
text2 = "def"
答案是 0
```

这题是双序列 DP 的门面题之一。

你后面学编辑距离、不同子序列、交错字符串，这题的状态定义都会反复出现。

---

## 为什么这题适合这样学

这题非常适合按下面这条线理解：

```text
暴力递归 -> 记忆化搜索 -> 二维 DP -> 一维压缩 DP
```

因为它的关键不是技巧多，而是状态定义非常经典。

你真正要想明白的是：

- 为什么状态要定义成“前 i 个字符”和“前 j 个字符”
- 当两个字符相等时，为什么答案来自左上角加一
- 当两个字符不相等时，为什么只需要比较“上边”和“左边”

这题一旦吃透，很多双序列 DP 都会顺很多。

---

## 方法一：暴力递归

### 思路

先从最自然的递归定义开始。

设：

```text
dfs(i, j) = text1[i:] 和 text2[j:] 的最长公共子序列长度
```

如果某一边已经走到结尾，那就没有公共子序列了，直接返回 `0`。

如果当前字符相等：

```text
text1[i] == text2[j]
```

那这个字符一定可以加入公共子序列，所以：

```text
1 + dfs(i + 1, j + 1)
```

如果当前字符不相等，就有两种选择：

1. 跳过 `text1[i]`
2. 跳过 `text2[j]`

取两者最大值。

### 代码

```python
# 方法一：暴力递归
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        def dfs(i, j):
            if i == m or j == n:
                return 0
            if text1[i] == text2[j]:
                return 1 + dfs(i + 1, j + 1)
            return max(dfs(i + 1, j), dfs(i, j + 1))

        return dfs(0, 0)
```

### 复杂度

- 时间复杂度：较高，存在大量重复子问题
- 空间复杂度：递归栈最坏 `O(m + n)`

### 评价

这个方法最适合理解状态定义。

但重复计算非常多，实际效率不行。

---

## 方法二：记忆化搜索

### 思路

方法一的递归定义完全没问题，问题只在于同一个状态会被反复计算。

所以只要加一个 `memo`，把：

```text
dfs(i, j)
```

算过的结果存起来，就能把复杂度降到 `O(m * n)`。

### 代码

```python
# 方法二：记忆化搜索
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo = {}

        def dfs(i, j):
            if i == m or j == n:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i + 1, j + 1)
                return memo[(i, j)]

            memo[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            return memo[(i, j)]

        return dfs(0, 0)
```

### 复杂度

- 时间复杂度：`O(m * n)`
- 空间复杂度：`O(m * n)`

### 评价

这个方法已经很好了，而且能非常自然地从递归过渡到 DP。

但面试里通常更推荐直接写迭代 DP，因为更标准。

---

## 方法三：二维动态规划（最适合面试）

### 为什么这个最适合面试

这题如果面试只准备一个版本，我最推荐二维 DP。

原因：

1. 这是 LCS 的标准写法
2. 状态定义非常典型
3. 转移逻辑清晰，容易讲
4. 很多后续双序列 DP 都能从它迁移出去

所以这题最适合面试的方法，就是二维 DP。

---

### 第一步：定义状态

定义：

```text
dp[i][j] = text1 前 i 个字符 和 text2 前 j 个字符 的最长公共子序列长度
```

也就是：

```text
text1[:i] 和 text2[:j]
```

这个定义特别重要，因为它让“最后一个字符要不要参与答案”变得很清楚。

---

### 第二步：边界初始化

只要有一边是空串，最长公共子序列长度一定是 `0`。

所以：

```text
dp[0][j] = 0
dp[i][0] = 0
```

这也是为什么我们会开 `(m + 1) * (n + 1)` 的表。

---

### 第三步：状态转移

如果当前两个字符相等：

```text
text1[i - 1] == text2[j - 1]
```

那它们可以一起作为公共子序列的最后一个字符，所以：

```text
dp[i][j] = dp[i - 1][j - 1] + 1
```

如果当前两个字符不相等，那最后一个字符至少有一个不能同时选。

于是只需要比较两种情况：

1. 不用 `text1[i - 1]`
2. 不用 `text2[j - 1]`

所以：

```text
dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
```

---

### 代码

```python
# 方法三：二维动态规划
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
```

### 复杂度

- 时间复杂度：`O(m * n)`
- 空间复杂度：`O(m * n)`

### 面试怎么讲

面试里建议你按这条线来讲：

1. `dp[i][j]` 表示两个前缀的最长公共子序列长度
2. 一边为空时答案是 `0`
3. 如果当前字符相等，答案来自左上角加一
4. 如果不相等，答案来自上边和左边的最大值

这套逻辑非常标准，也很容易让面试官跟上。

---

## 方法四：一维压缩 DP

### 思路

观察二维 DP 的转移：

```text
dp[i][j]
```

只依赖：

- 上一行当前列
- 当前行左边
- 上一行左上角

所以可以把二维表压成一维数组。

但和编辑距离一样，这样会更绕一些，因为你需要额外维护“左上角旧值”。

### 代码

```python
# 方法四：一维压缩动态规划
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            prev_diagonal = 0
            for j in range(1, n + 1):
                current = dp[j]
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = prev_diagonal + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
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
- 更直观
- 更容易把状态和转移讲清楚

---

## 最后总结

这题建议这样记：

- **递归定义**：从两个后缀出发，字符相等就一起拿，不等就跳过一边
- **核心状态**：两个前缀的最长公共子序列长度
- **最适合面试**：二维 DP
- **进阶优化**：一维压缩 DP

如果你是为了面试准备，这题最值得熟练掌握的是：

> **二维 DP 版本**

因为它是双序列 DP 的核心门面题之一，后面很多题都能从它迁移出去。
