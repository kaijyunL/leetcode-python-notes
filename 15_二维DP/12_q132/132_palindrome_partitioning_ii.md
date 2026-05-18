# 132. 分割回文串 II

## 题目理解

给你一个字符串 `s`，你需要返回：

> 把 `s` 分割成若干个子串后，每个子串都必须是回文串，最少要切几刀。

这里的关键词有两个：

1. **每一段都必须是回文串**
2. **要求的是最少切割次数，不是返回所有方案**

例如：

```text
s = "aab"
答案是 1
```

因为可以切成：

```text
"aa" | "b"
```

只需要切 1 刀。

再比如：

```text
s = "a"
答案是 0
```

因为整个字符串本身就是回文串，根本不用切。

---

## 和第 131 题的关系

这题和 [131. 分割回文串](../../09_回溯/11_q131/solution.md) 是一组配套题。

- 第 131 题：返回所有合法分割方案
- 第 132 题：只问最少切几刀

所以两题的共同点是：

```text
都要判断某一段 s[i:j+1] 是否是回文
```

但后半部分不一样：

- 第 131 题是回溯枚举所有切法
- 第 132 题是 DP 求最优值

这题的本质其实是：

> 先解决“哪些区间是回文”，再解决“最少切几刀”。

---

## 为什么这题适合这样学

这题很适合按下面这条线理解：

```text
暴力递归 -> 记忆化搜索 -> 动态规划
```

你最需要想清楚的是：

- 为什么“切割问题”可以定义成前缀 DP
- 为什么先预处理回文区间会让转移更清楚
- 为什么状态里记“最少切几刀”，而不是“最少分成几段”

这题看起来像回溯题，但真正高效的解法是 DP。

---

## 方法一：暴力递归

### 思路

定义：

```text
dfs(start) = 把 s[start:] 切成若干回文串所需的最少段数
```

为什么先求“最少段数”？

因为这样递归比较自然：

- 枚举第一段的结束位置 `end`
- 如果 `s[start:end+1]` 是回文
- 那就可以把这一段作为当前的一段，再递归处理后面部分

于是：

```text
dfs(start) = 1 + min(dfs(end + 1))
```

其中前提是：

```text
s[start:end+1] 是回文
```

当 `start == n` 时，说明后面已经没有字符了，不需要再分段，所以返回 `0`。

最后答案是：

```text
dfs(0) - 1
```

因为如果一共分成 `k` 段，只需要切 `k - 1` 刀。

### 代码

```python
# 方法一：暴力递归
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(start):
            if start == n:
                return 0

            best = float("inf")
            for end in range(start, n):
                if not is_palindrome(start, end):
                    continue
                best = min(best, 1 + dfs(end + 1))

            return best

        return dfs(0) - 1
```

### 复杂度

- 时间复杂度：很高，存在大量重复子问题
- 空间复杂度：递归栈最坏 `O(n)`

### 评价

这个方法适合理解“第一段切到哪里”的递归结构。

但它会反复计算相同后缀的答案，也会反复判断很多区间是不是回文，所以效率不行。

---

## 方法二：记忆化搜索

### 思路

方法一的问题主要有两个：

1. 同一个 `start` 会被反复计算
2. 同一个区间是否回文也会被反复判断

先做第一层优化：

```text
给 dfs(start) 加 memo
```

这样每个起点只会算一次。

回文判断这里仍然保留双指针版本，这样更容易看出它是从暴力递归平滑过渡来的。

### 代码

```python
# 方法二：记忆化搜索
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        memo = {}

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(start):
            if start == n:
                return 0
            if start in memo:
                return memo[start]

            best = float("inf")
            for end in range(start, n):
                if not is_palindrome(start, end):
                    continue
                best = min(best, 1 + dfs(end + 1))

            memo[start] = best
            return best

        return dfs(0) - 1
```

### 复杂度

- 时间复杂度：仍然偏高，因为回文判断有重复
- 空间复杂度：`O(n)` 到 `O(n^2)`，取决于递归和记忆化开销

### 评价

这个方法已经把“后缀最优值”的结构固定下来了。

但如果面试里直接停在这里，通常还不够，因为回文判断仍然是重复成本。

---

## 方法三：回文预处理 + 一维 DP（最适合面试）

### 为什么这个最适合面试

这题如果面试只准备一个版本，我最推荐这一种。

原因：

1. 思路完整，先预处理回文，再做最优切割
2. 状态定义清楚，转移很自然
3. 时间复杂度是标准最优级别 `O(n^2)`
4. 和第 131 题、第 5 题、第 647 题可以形成知识联动

所以这题最适合面试的方法，就是：

> **回文预处理 + 一维 DP**

---

### 第一步：先预处理所有回文区间

定义：

```text
is_pal[left][right] = s[left:right+1] 是否是回文串
```

判断条件和第 131、5、647 题一样：

```text
s[left] == s[right] 且
(
    right - left <= 2
    或者 is_pal[left + 1][right - 1]
)
```

这里 `right - left <= 2` 表示三种基础情况：

- 长度 1：`"a"`
- 长度 2：`"aa"`
- 长度 3：`"aba"`

这几种只要两端相等，就一定是回文。

为了保证 `is_pal[left + 1][right - 1]` 已经算好，要让 `left` 从右往左枚举：

```python
for left in range(n - 1, -1, -1):
    for right in range(left, n):
```

---

### 第二步：定义最少切割 DP

定义：

```text
dp[i] = s[0:i+1] 这个前缀最少要切几刀
```

也就是：

```text
dp[i] 负责前缀 s[:i+1]
```

我们要的答案就是：

```text
dp[n - 1]
```

---

### 第三步：状态转移

看前缀 `s[0:i+1]` 的最后一段从哪里开始。

如果：

```text
s[j:i+1] 是回文串
```

那最后一刀可以切在 `j - 1` 后面。

这时分两种情况：

#### 情况 1：整个前缀本身就是回文

如果：

```text
j == 0
```

说明：

```text
s[0:i+1]
```

整段都是回文，那根本不用切：

```text
dp[i] = 0
```

#### 情况 2：最后一段是回文，但前面还有内容

如果：

```text
j > 0
```

那前面这段：

```text
s[0:j]
```

最少切割次数是 `dp[j - 1]`。

然后再切一刀，把最后这段 `s[j:i+1]` 分出来。

所以候选值是：

```text
dp[j - 1] + 1
```

把所有合法 `j` 取最小值即可。

于是转移就是：

```text
if is_pal[0][i]:
    dp[i] = 0
else:
    dp[i] = min(dp[j - 1] + 1)
    其中 1 <= j <= i 且 is_pal[j][i] == True
```

---

### 代码

```python
# 方法三：回文预处理 + 一维动态规划
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]

        for left in range(n - 1, -1, -1):
            for right in range(left, n):
                if s[left] == s[right] and (
                    right - left <= 2 or is_pal[left + 1][right - 1]
                ):
                    is_pal[left][right] = True

        dp = [0] * n
        for i in range(n):
            if is_pal[0][i]:
                dp[i] = 0
                continue

            dp[i] = i
            for j in range(1, i + 1):
                if is_pal[j][i]:
                    dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[-1]
```

### 复杂度

- 时间复杂度：`O(n^2)`
- 空间复杂度：`O(n^2)`

### 面试怎么讲

面试里建议按这条线讲：

1. 这题本质是前缀最优划分问题
2. 先预处理 `is_pal[i][j]`，让回文判断变成 `O(1)`
3. `dp[i]` 表示前缀 `s[:i+1]` 最少切几刀
4. 枚举最后一段的起点 `j`
5. 如果 `s[j:i+1]` 是回文，那么候选答案是 `dp[j - 1] + 1`
6. 如果整个前缀本身就是回文，则 `dp[i] = 0`

这个版本最稳，也最容易讲清楚。

---

## 为什么不用“分段数”直接做二维 DP？

其实也可以。

但这题没必要把状态搞复杂。

因为我们只关心：

```text
每个前缀的最少切割次数
```

所以用一维 DP 就够了。

真正需要二维的是“回文判断表”，而不是“最少切割次数表”。

这也是这题很典型的一点：

> 一个问题里可能会同时出现两个 DP，但它们负责的事情不同。

- `is_pal[left][right]`：负责判断区间性质
- `dp[i]`：负责求前缀最优值

---

## 以 `s = "aab"` 为例

先预处理出这些回文区间：

```text
"a"   -> s[0:1]
"a"   -> s[1:2]
"b"   -> s[2:3]
"aa"  -> s[0:2]
```

然后看 `dp`：

### `i = 0`

前缀是：

```text
"a"
```

本身是回文，所以：

```text
dp[0] = 0
```

### `i = 1`

前缀是：

```text
"aa"
```

本身也是回文，所以：

```text
dp[1] = 0
```

### `i = 2`

前缀是：

```text
"aab"
```

本身不是回文。

枚举最后一段起点：

- `j = 1`，`"ab"` 不是回文，跳过
- `j = 2`，`"b"` 是回文

所以：

```text
dp[2] = dp[1] + 1 = 1
```

最终答案就是：

```text
1
```

---

## 最后总结

这题建议这样记：

- **核心拆分**：先判回文区间，再做最少切割 DP
- **关键状态**：`dp[i]` 表示前缀 `s[:i+1]` 最少切几刀
- **最适合面试**：回文预处理 + 一维 DP
- **知识联动**：和第 131、5、647 题共用同一套回文区间判断思路

如果你是为了面试准备，这题最值得熟练掌握的是：

> **回文预处理 + 一维 DP 版本**

因为它兼顾了：

- 思路完整
- 复杂度优秀
- 解释清楚
- 不容易写错
