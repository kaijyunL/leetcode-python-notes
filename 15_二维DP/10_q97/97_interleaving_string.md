# 97. 交错字符串

## 题目理解

给你三个字符串 `s1`、`s2`、`s3`，你需要判断：

> `s3` 能不能由 `s1` 和 `s2` 交错组成。

这里“交错”有两个关键要求：

1. `s1` 和 `s2` 里的字符顺序都不能被打乱
2. `s3` 必须刚好把 `s1` 和 `s2` 的所有字符都用完

例如：

```text
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
答案是 True
```

但：

```text
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
答案是 False
```

这题本质上是在问：

- `s3` 的当前位置
- 到底该接 `s1` 的下一个字符
- 还是接 `s2` 的下一个字符

所以它是非常典型的二维 DP 题。

---

## 为什么这题适合这样学

这题非常适合按下面这条线来理解：

```text
暴力递归 -> 记忆化搜索 -> 二维 DP -> 一维压缩 DP
```

你最需要想明白的是：

- 为什么只要知道“`s1` 用了多少个字符”和“`s2` 用了多少个字符”就够了
- 为什么 `s3` 的位置可以自动推出
- 为什么当前状态只会从“上面”或“左边”转移过来

这题吃透以后，你对“二维状态如何描述两个来源共同构造一个目标串”会清楚很多。

---

## 方法一：暴力递归

### 思路

先用最自然的递归方式来想。

设：

```text
dfs(i, j) = s1[i:] 和 s2[j:] 能不能交错组成 s3[i + j:]
```

这里 `i + j` 很关键。

因为：

- `s1` 已经用了 `i` 个字符
- `s2` 已经用了 `j` 个字符
- 那么 `s3` 一定已经匹配了 `i + j` 个字符

所以 `s3` 当前该看的位置，不需要单独存，直接就是：

```text
k = i + j
```

接下来分两种尝试：

1. 如果 `s1[i] == s3[k]`，那可以尝试从 `s1` 取当前字符
2. 如果 `s2[j] == s3[k]`，那可以尝试从 `s2` 取当前字符

只要有一种方式能走通，答案就是 `True`。

### 代码

```python
# 方法一：暴力递归
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)

        def dfs(i, j):
            if i == m and j == n:
                return True

            k = i + j
            if i < m and s1[i] == s3[k] and dfs(i + 1, j):
                return True
            if j < n and s2[j] == s3[k] and dfs(i, j + 1):
                return True
            return False

        return dfs(0, 0)
```

### 复杂度

- 时间复杂度：较高，存在大量重复子问题
- 空间复杂度：递归栈最坏 `O(m + n)`

### 评价

这个方法最适合理解题意和状态定义。

但如果某一步既能从 `s1` 取，又能从 `s2` 取，就会产生很多重复搜索。

---

## 方法二：记忆化搜索

### 思路

方法一的问题，不是状态定义不对，而是同一个状态：

```text
dfs(i, j)
```

会被反复计算。

所以只要把它记下来，就能把复杂度降下来。

递归逻辑和方法一完全一样，只是多了一个 `memo`。

### 代码

```python
# 方法二：记忆化搜索
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)
        memo = {}

        def dfs(i, j):
            if i == m and j == n:
                return True
            if (i, j) in memo:
                return memo[(i, j)]

            k = i + j
            if i < m and s1[i] == s3[k] and dfs(i + 1, j):
                memo[(i, j)] = True
                return True
            if j < n and s2[j] == s3[k] and dfs(i, j + 1):
                memo[(i, j)] = True
                return True

            memo[(i, j)] = False
            return False

        return dfs(0, 0)
```

### 复杂度

- 时间复杂度：`O(m * n)`
- 空间复杂度：`O(m * n)`

### 评价

这个方法已经很好了，而且特别适合帮助你看懂二维 DP 的状态来源。

但面试里更推荐直接写迭代 DP，因为更稳、更标准。

---

## 方法三：二维动态规划（最适合面试）

### 为什么这个最适合面试

这题如果面试只准备一个版本，我最推荐二维 DP。

原因：

1. 状态定义非常自然
2. 转移方向很清楚，只看上边和左边
3. `k = i + j` 这个细节很适合展示你是否真正理解状态
4. 代码不长，但很有代表性

所以这题最适合面试的方法，就是二维 DP。

---

### 第一步：定义状态

定义：

```text
dp[i][j] = s1 前 i 个字符 和 s2 前 j 个字符 能不能交错组成 s3 前 i + j 个字符
```

这里最重要的点是：

```text
s3 的前缀长度不是单独定义的，而是自动等于 i + j
```

这就是这题的核心。

---

### 第二步：边界初始化

先看：

```text
dp[0][0] = True
```

因为空串和空串当然能组成空串。

然后：

- `dp[i][0]` 表示只用 `s1[:i]` 去匹配 `s3[:i]`
- `dp[0][j]` 表示只用 `s2[:j]` 去匹配 `s3[:j]`

所以边界需要逐步判断前缀是否一致。

---

### 第三步：状态转移

当前位置对应 `s3` 的下标是：

```text
k = i + j - 1
```

为什么是 `-1`？

因为当前 `dp[i][j]` 对应的是“前 `i + j` 个字符”，最后一个字符下标自然是 `i + j - 1`。

接下来只看两种来源：

#### 1）从上面来

如果：

- `dp[i - 1][j]` 是 `True`
- 并且 `s1[i - 1] == s3[k]`

那说明可以从 `s1` 拿当前字符，得到 `dp[i][j] = True`。

#### 2）从左边来

如果：

- `dp[i][j - 1]` 是 `True`
- 并且 `s2[j - 1] == s3[k]`

那说明可以从 `s2` 拿当前字符，得到 `dp[i][j] = True`。

只要有一种方式可行，当前格就是 `True`。

---

### 代码

```python
# 方法三：二维动态规划
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                k = i + j - 1
                dp[i][j] = (
                    dp[i - 1][j] and s1[i - 1] == s3[k]
                ) or (
                    dp[i][j - 1] and s2[j - 1] == s3[k]
                )

        return dp[m][n]
```

### 复杂度

- 时间复杂度：`O(m * n)`
- 空间复杂度：`O(m * n)`

### 面试怎么讲

面试里建议你按这条线讲：

1. 先做长度剪枝
2. 定义 `dp[i][j]` 表示两个前缀能否组成 `s3` 的对应前缀
3. `s3` 的位置由 `i + j` 自动决定
4. 当前状态只可能从上边或左边转移过来
5. 只要有一条路可行，就是 `True`

这条线会非常顺。

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

所以这题比编辑距离和 LCS 更容易压缩成一维。

因为它不依赖左上角，只依赖“上”和“左”。

### 代码

```python
# 方法四：一维压缩动态规划
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)
        dp = [False] * (n + 1)
        dp[0] = True

        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                k = i + j - 1
                dp[j] = (
                    dp[j] and s1[i - 1] == s3[k]
                ) or (
                    dp[j - 1] and s2[j - 1] == s3[k]
                )

        return dp[n]
```

### 复杂度

- 时间复杂度：`O(m * n)`
- 空间复杂度：`O(n)`

### 评价

这个方法更省空间，而且写法也不算太绕。

但如果是面试现场，我还是更推荐先写二维 DP。

因为二维 DP：

- 更稳
- 更容易讲
- 更不容易在边界上出错

---

## 最后总结

这题建议这样记：

- **核心状态**：`s1` 前缀和 `s2` 前缀，能不能组成 `s3` 对应前缀
- **关键细节**：`s3` 的位置由 `i + j` 自动推出
- **最适合面试**：二维 DP
- **进阶优化**：一维压缩 DP

如果你是为了面试准备，这题最值得熟练掌握的是：

> **二维 DP 版本**

因为这题会很直接地考察你对二维布尔状态 DP 的理解是否扎实。
