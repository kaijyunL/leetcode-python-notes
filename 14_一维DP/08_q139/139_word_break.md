# 139. 单词拆分

## 题目理解

给你一个字符串 `s`，再给你一个字符串列表 `wordDict` 作为字典。

你需要判断：

> 能不能把 `s` 拆分成若干个字典中的单词。

注意：

- 字典中的单词可以重复使用
- 只需要判断 **能不能拆分成功**，不是求方案数，也不是输出所有方案

例如：

```text
s = "leetcode", wordDict = ["leet", "code"]
答案是 true
```

因为可以拆成：

```text
"leet" + "code"
```

再比如：

```text
s = "applepenapple", wordDict = ["apple", "pen"]
答案是 true
```

```text
s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
答案是 false
```

这题是很经典的字符串 DP，也是一维 DP 里非常高频的一道题。

---

## 为什么这题适合这样学

这题很适合按下面这条线来理解：

```text
暴力递归 -> 记忆化递归 -> 动态规划
```

因为它最本质的问题是：

- 从某个位置开始，后面的字符串能不能被成功拆分

所以天然就适合先用递归建模，再逐步优化成 DP。

这题最重要的是要搞清楚：

- 状态到底表示什么
- 为什么“从某个位置开始能不能拆”可以转成 DP
- 为什么 `dp[i]` 通常定义成“前缀是否可拆分”

---

## 方法一：暴力递归

### 思路

先从最直观的角度想。

如果我们现在站在下标 `i`，那就要判断：

```text
s[i:]
```

能不能被拆分成功。

这时可以尝试枚举下一个单词的结束位置 `j`：

- 如果 `s[i:j]` 在字典里
- 那就继续递归判断 `s[j:]` 能不能拆开

所以可以定义：

```text
dfs(i) = 从下标 i 开始的后缀能否被成功拆分
```

转移逻辑：

- 枚举所有 `j > i`
- 如果 `s[i:j]` 是一个字典单词，并且 `dfs(j)` 为真
- 那么 `dfs(i)` 就为真

### 代码

```python
from typing import List


# 方法一：暴力递归
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)

        def dfs(i):
            if i == n:
                return True

            for j in range(i + 1, n + 1):
                if s[i:j] in word_set and dfs(j):
                    return True

            return False

        return dfs(0)
```

### 复杂度

- 时间复杂度：指数级
- 空间复杂度：`O(n)`，递归栈深度

### 评价

这个方法适合理解这题的“原始状态”是什么。

但它的问题很明显：

- 同一个位置 `i` 会被反复递归计算
- 重复子问题非常严重

---

## 方法二：记忆化递归

### 思路

既然暴力递归慢，是因为同一个 `dfs(i)` 会反复算，那就把算过的结果存下来。

定义仍然不变：

```text
dfs(i) = 从下标 i 开始的后缀能否被成功拆分
```

再加一个 `memo`：

```text
memo[i] = dfs(i) 的结果
```

每次递归时：

- 如果 `i` 已经算过，直接返回
- 没算过，再继续递归

### 代码

```python
from typing import List


# 方法二：记忆化递归
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        memo = {}

        def dfs(i):
            if i == n:
                return True
            if i in memo:
                return memo[i]

            for j in range(i + 1, n + 1):
                if s[i:j] in word_set and dfs(j):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dfs(0)
```

### 复杂度

- 时间复杂度：`O(n^3)`
- 空间复杂度：`O(n)`（不计切片产生的临时开销时）

### 为什么是 `O(n^3)`

有 `n` 个状态：

```text
i = 0, 1, 2, ..., n-1
```

每个状态要枚举 `j`，大约 `O(n)` 次。

而 `s[i:j]` 这个切片本身平均也要 `O(n)` 时间。

所以整体通常写成：

```text
O(n^3)
```

### 评价

这个方法已经可以通过，而且递归思路很自然。

优点：

- 很容易从暴力递归升级过来
- 状态含义非常直接

缺点：

- 还是递归写法
- 面试里一般更推荐写迭代 DP

---

## 方法三：动态规划（最适合面试）

### 为什么这个最适合面试

这是这题最标准、最稳的写法。

原因：

1. 状态定义清楚
2. 转移逻辑自然
3. 没有递归栈
4. 是字符串 DP 的经典模板之一

所以这题如果面试只准备一个版本，优先准备这个。

---

### 第一步：定义状态

定义：

```text
dp[i] = 前 i 个字符 s[:i] 能否被成功拆分
```

这个定义非常重要。

我们最终要求的是整个字符串能不能拆分，所以答案就是：

```text
dp[n]
```

其中 `n = len(s)`。

---

### 第二步：转移怎么来

如果我们要求 `dp[i]`，那就表示：

```text
前 i 个字符能不能拆分
```

那最后一段一定是某个：

```text
s[j:i]
```

其中 `0 <= j < i`。

如果满足两个条件：

1. `dp[j] == True`，说明前面的 `s[:j]` 已经能拆开
2. `s[j:i]` 在字典里，说明最后这一段本身是合法单词

那么：

```text
dp[i] = True
```

所以转移就是：

```text
如果存在某个 j，使得 dp[j] 为真 且 s[j:i] 在字典里，那么 dp[i] 为真
```

---

### 第三步：边界怎么定

最关键的边界是：

```text
dp[0] = True
```

为什么？

因为空字符串可以看成“已经被成功拆分”。

这个初始化非常关键。

它的作用是：

- 当 `s[:i]` 本身就是一个单词时
- 我们可以从 `dp[0]` 转移到 `dp[i]`

例如：

```text
s = "leet"
```

如果 `"leet"` 在字典里，那么：

```text
dp[4] = dp[0] and "leet" in wordDict
```

没有 `dp[0] = True`，这个转移就立不起来。

---

### 第四步：用例子走一遍

以：

```text
s = "leetcode"
wordDict = ["leet", "code"]
```

为例。

初始化：

```text
dp[0] = True
其余先是 False
```

接着往后推：

- 当 `i = 4` 时，`s[0:4] = "leet"` 在字典里，且 `dp[0] = True`
  - 所以 `dp[4] = True`
- 当 `i = 8` 时，`s[4:8] = "code"` 在字典里，且 `dp[4] = True`
  - 所以 `dp[8] = True`

最后：

```text
dp[8] = True
```

说明整个字符串可以拆分成功。

---

### 代码

```python
from typing import List


# 方法三：动态规划
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
```

### 复杂度

- 时间复杂度：`O(n^3)`
- 空间复杂度：`O(n)`

---

### 面试时推荐怎么讲

你可以这样讲：

#### 1. 先定义状态

```text
dp[i] 表示前 i 个字符能否被成功拆分
```

#### 2. 再看最后一段

如果最后一段 `s[j:i]` 是字典单词，并且前面 `s[:j]` 能拆分，
那么 `s[:i]` 就也能拆分。

#### 3. 写出转移

```text
如果存在 j < i，使得 dp[j] 为真 且 s[j:i] 在字典中，那么 dp[i] = True
```

#### 4. 说明边界

```text
dp[0] = True
```

#### 5. 最后返回

```text
dp[n]
```

这套讲法很完整，也很符合字符串 DP 的标准表达。

---

## 方法四：动态规划 + 剪枝优化

### 思路

方法三已经很好了，但还有一个常见优化思路：

我们没必要让 `j` 从 `0` 一直枚举到 `i-1`，因为字典里的单词长度是有限的。

先预处理出：

```text
max_len = 字典里最长单词的长度
```

那么在计算 `dp[i]` 时，只需要检查：

```text
j >= i - max_len
```

也就是说，只看那些长度不超过 `max_len` 的后缀。

这样能减少很多无效枚举。

### 代码

```python
from typing import List


# 方法四：动态规划 + 剪枝优化
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        max_len = max(len(word) for word in wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            start = max(0, i - max_len)
            for j in range(start, i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
```

### 复杂度

- 时间复杂度：通常写作 `O(n * max_len^2)`
- 空间复杂度：`O(n)`

### 评价

这个方法和标准 DP 是同一个核心思路，只是更高效一些。

如果面试官追问优化，你可以顺手补这个版本，会比较加分。

---

## 哪个方法最适合面试

### 结论

**最适合面试的是：方法三，动态规划。**

如果面试官继续追问性能优化，可以再补方法四。

### 为什么不是别的方法

#### 方法一：暴力递归

- 适合理解状态
- 但会超时
- 不能作为最终答案

#### 方法二：记忆化递归

- 能通过
- 也很自然
- 但一般没有迭代 DP 稳

#### 方法四：DP + 剪枝优化

- 确实更快
- 但本质还是在方法三基础上的优化
- 面试里先写方法三更标准

所以综合来看：

> **方法三最稳，最标准，也最适合面试。**

---

## 最适合面试的方法：详细讲解

### 1. 这题的本质是什么

这题问的不是：

- 有多少种拆法
- 拆法具体是什么

而只是：

```text
能不能拆成功
```

所以这是一个典型的：

```text
可行性判断型 DP
```

状态只需要是 `True / False`。

---

### 2. 为什么 `dp[i]` 定义成“前 i 个字符能否拆分”

因为这题本质上是在问前缀问题。

如果 `s[:i]` 能拆分，那么它一定可以看成：

```text
前面一段 + 最后一个单词
```

所以最自然的定义就是：

```text
dp[i] = s[:i] 能否拆分
```

这个定义一出来，最后一段 `s[j:i]` 的思路就自然有了。

---

### 3. 为什么转移一定正确

如果 `s[:i]` 能被成功拆分，那么它最后一定有一个单词结尾。

设这个最后单词是：

```text
s[j:i]
```

那就说明：

- `s[j:i]` 本身一定在字典里
- `s[:j]` 也一定已经能拆开

所以必然满足：

```text
dp[j] == True 且 s[j:i] in wordDict
```

反过来，如果存在这样的 `j`，那当然就说明 `s[:i]` 能拆开。

所以这个转移是充分必要的。

---

### 4. 为什么 `dp[0] = True` 不能忘

这是这题非常关键的初始化。

它表示：

```text
空前缀是可拆分的
```

这不是因为空串真的“拆出了某个单词”，而是因为它作为递推起点必须成立。

否则像：

```text
s = "leet"
wordDict = ["leet"]
```

这种最基础情况就无法从 `dp[0]` 转移到 `dp[4]`。

---

### 5. 为什么这题是字符串 DP 高频题

因为它的结构非常典型：

- `dp[i]` 表示前缀状态
- 枚举切分点 `j`
- 检查 `s[j:i]` 是否满足条件

这类思路在很多字符串 DP 题里都会出现。

所以这题不只是会做一道题，而是在练一个非常通用的模板。

---

### 6. 面试里怎么说最自然

你可以这样讲：

> 我定义 `dp[i]` 表示前 `i` 个字符能否被成功拆分。对于每个 `i`，我去枚举最后一个切分点 `j`。如果 `dp[j]` 为真，并且子串 `s[j:i]` 在字典中，那么说明前 `i` 个字符可以拆分，所以令 `dp[i] = True`。初始条件是 `dp[0] = True`，最后返回 `dp[n]`。

这套表述非常标准。

---

### 面试最推荐代码

```python
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
```

---

## 总结

### 递进关系

1. **暴力递归**
   - 最直观
   - 但重复子问题很多

2. **记忆化递归**
   - 消除重复计算
   - 保留原始递归思路

3. **动态规划**
   - 最标准
   - 最适合面试

4. **动态规划 + 剪枝优化**
   - 在标准 DP 基础上进一步提速

### 一句话记忆

> `dp[i]` 表示前 `i` 个字符能否拆分；只要存在一个切分点 `j`，使得前缀 `s[:j]` 可拆分且 `s[j:i]` 在字典里，那么 `dp[i]` 就为真。
