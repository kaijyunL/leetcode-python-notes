# 647. 回文子串

## 题目理解

给你一个字符串 `s`，你需要返回：

> `s` 里一共有多少个回文子串。

这里有两个关键点：

- **子串必须连续**
- **即使内容一样，只要起止位置不同，也算不同子串**

例如：

```text
s = "abc"
答案是 3
```

因为单个字符都是回文串：

```text
"a", "b", "c"
```

再看一个更典型的例子：

```text
s = "aaa"
答案是 6
```

分别是：

```text
"a", "a", "a", "aa", "aa", "aaa"
```

这题和 [5. 最长回文子串](../06_q5/5_longest_palindromic_substring.md) 是一组经典配套题。

- 第 5 题问：最长的是谁
- 第 647 题问：总共有多少个

所以这题的重点不只是“判断某段是不是回文”，还要学会**如何系统地把所有回文都数出来**。

---

## 为什么这题适合这样学

这题很适合按下面这条线来理解：

```text
暴力枚举 -> 递归定义 -> 区间 DP -> 中心扩展
```

因为它背后其实有两种经典视角：

1. **区间视角**：`s[left:right+1]` 是不是回文
2. **中心视角**：一个回文串一定可以从某个中心往两边扩出来

这题最重要的是搞清楚：

- 为什么“回文”天然适合区间 DP
- 为什么“计数”这个任务通常更适合中心扩展

---

## 方法一：暴力枚举

### 思路

最直观的做法就是：

- 枚举所有子串 `s[left:right+1]`
- 对每个子串判断它是不是回文
- 如果是，答案加一

判断回文的方法仍然是双指针：

- 一个指针从左往右
- 一个指针从右往左
- 只要遇到不同字符，就不是回文

### 代码

```python
# 方法一：暴力枚举
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for left in range(n):
            for right in range(left, n):
                if is_palindrome(left, right):
                    count += 1

        return count
```

### 复杂度

- 时间复杂度：`O(n^3)`
- 空间复杂度：`O(1)`

### 评价

这个方法适合理解题意，但效率比较差。

因为：

- 子串一共有 `O(n^2)` 个
- 每次判断回文最坏还要 `O(n)`

---

## 方法二：递归定义 + 记忆化

### 思路

如果换成“区间是不是回文”这个视角，可以定义：

```text
dfs(left, right) = s[left:right+1] 是否是回文串
```

递归关系很自然：

- 如果 `s[left] != s[right]`，那一定不是回文
- 如果 `s[left] == s[right]`，那还要看中间那段是不是回文

也就是：

```text
s[left:right+1] 是回文
等价于
s[left] == s[right] 且 s[left+1:right] 也是回文
```

然后枚举所有区间，凡是 `dfs(left, right)` 为真，就把它计入答案。

加上记忆化以后，每个区间状态只会算一次。

### 代码

```python
# 方法二：记忆化递归
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        memo = {}
        count = 0

        def dfs(left, right):
            if left >= right:
                return True
            if (left, right) in memo:
                return memo[(left, right)]
            if s[left] != s[right]:
                memo[(left, right)] = False
                return False

            memo[(left, right)] = dfs(left + 1, right - 1)
            return memo[(left, right)]

        for left in range(n):
            for right in range(left, n):
                if dfs(left, right):
                    count += 1

        return count
```

### 复杂度

- 时间复杂度：`O(n^2)`
- 空间复杂度：`O(n^2)`

### 评价

这个方法已经很不错了，而且能非常清楚地看出“回文区间”的递归结构。

但面试里一般更常写迭代 DP 或中心扩展，因为它们更直接。

---

## 方法三：动态规划

### 思路

这是和第 5 题同一套区间 DP 思路，只不过第 5 题是找最长，这题是统计总数。

定义：

```text
dp[left][right] = s[left:right+1] 是否是回文串
```

转移逻辑和第 5 题一致：

- 如果 `s[left] != s[right]`，那它一定不是回文
- 如果 `s[left] == s[right]`，再看内部区间是不是回文
- 当 `right - left <= 1` 时，内部已经空了或者只剩一个字符，直接成立

所以可以写成：

```text
if s[left] == s[right] and (right - left <= 1 or dp[left + 1][right - 1]):
    dp[left][right] = True
```

和第 5 题一样，这里也按 `right` 从左到右推进。

这样做的好处是：

- `dp[left + 1][right - 1]` 一定已经算过
- 写法和第 5 题统一，记忆负担更小

不同点只在于：

- 第 5 题找到更长回文时更新答案区间
- 第 647 题只要发现一个回文区间，就把计数加一

### 代码

```python
# 方法三：动态规划
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        for right in range(n):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 1 or dp[left + 1][right - 1]):
                    dp[left][right] = True
                    count += 1

        return count
```

### 复杂度

- 时间复杂度：`O(n^2)`
- 空间复杂度：`O(n^2)`

### 评价

这个方法很标准，特别适合练区间 DP。

如果你正在系统学习二维 DP，这个写法很值得掌握。

---

## 方法四：中心扩展（最适合面试）

### 为什么这个最适合面试

这题如果面试只准备一个版本，我最推荐**中心扩展**。

原因很简单：

1. 代码短，容易一次写对
2. 思路直观，不需要开 `dp` 表
3. 这题要求的是“统计个数”，中心扩展天然贴题
4. 奇数长度回文和偶数长度回文都能统一处理

相比之下：

- 暴力法太慢
- 记忆化和 DP 都没问题，但写起来更重
- 中心扩展在这题里通常是**最稳、最好讲、最像面试答案**的版本

所以这题最适合面试的方法，就是中心扩展。

---

### 第一步：抓住回文的结构

任意一个回文串，都一定能围绕某个“中心”向两边扩展。

比如：

```text
"aba"
```

中心是中间的 `b`。

而：

```text
"abba"
```

中心是中间两个字符之间的空隙。

所以回文中心分两类：

1. **单字符中心**，对应奇数长度回文
2. **双字符中心**，对应偶数长度回文

---

### 第二步：从每个中心往两边扩

对于每个中心，我们做一件事：

- 只要左右字符相同，就说明当前这段还是回文
- 每成功扩一次，就多找到一个回文子串
- 然后继续向外扩

例如：

```text
s = "aaa"
```

以中间这个 `a` 为奇数中心：

- `"a"` 是回文
- `"aaa"` 也是回文

以前两个 `a` 中间为偶数中心：

- `"aa"` 是回文

这样把所有中心都扫一遍，所有回文子串就都被数到了。

---

### 第三步：为什么不会漏、也不会重

这是面试里很值得主动讲出来的一点。

- **不会漏**：任何回文串都一定有一个中心
- **不会重**：每个回文串只会在它自己的那个中心被统计一次

所以“枚举中心 + 向外扩展”可以完整覆盖全部答案。

---

### 代码

```python
# 方法四：中心扩展
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand(left, right):
            total = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                total += 1
                left -= 1
                right += 1
            return total

        for i in range(len(s)):
            count += expand(i, i)
            count += expand(i, i + 1)

        return count
```

### 复杂度

- 时间复杂度：`O(n^2)`
- 空间复杂度：`O(1)`

### 面试怎么讲

如果面试官让你讲思路，可以按这条线说：

1. 题目要统计所有回文子串
2. 任意回文串都可以看成从某个中心向两边扩出来
3. 中心有两类：单点中心和双点中心
4. 对每个中心向外扩，每成功一次就找到一个回文子串
5. 所以总答案就是所有中心扩展次数之和

这样讲会很顺，而且逻辑非常完整。

---

## 最后总结

这题建议这样记：

- **理解题意**：不是找最长，而是统计总数
- **练区间思维**：可以用记忆化 / 区间 DP 判断某段是否回文
- **面试主解**：优先准备中心扩展

如果你是为了面试复习，这题最值得熟练掌握的是：

> **中心扩展法**

因为它既保留了回文结构的本质，又能用最短的代码稳定写出来。
