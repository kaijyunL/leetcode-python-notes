# 5. 最长回文子串

## 题目理解

给你一个字符串 `s`，请你返回：

> `s` 中最长的回文子串。

注意这里是：

- **子串**，必须连续
- **回文**，正着读和倒着读都一样

例如：

```text
s = "babad"
答案可以是 "bab"
也可以是 "aba"
```

```text
s = "cbbd"
答案是 "bb"
```

这题是字符串 DP 的经典门面题，同时也是中心扩展法的高频代表题。

---

## 为什么这题适合这样学

这题非常适合按下面这条线来理解：

```text
暴力枚举 -> 递归定义 -> 动态规划 -> 中心扩展
```

因为它有两条非常经典的思路：

1. 用区间 DP 判断某段是不是回文
2. 从中心往两边扩展寻找最长回文

这题最重要的是搞清楚：

- 回文的状态为什么天然适合区间 DP
- 为什么中心扩展反而更适合面试手写

---

## 方法一：暴力枚举

### 思路

最直观的做法就是：

- 枚举所有子串 `s[left:right+1]`
- 判断它是不是回文
- 如果是，就更新最长答案

判断回文的方法也很直接：

- 用双指针从两端往中间走
- 只要遇到不同字符，就不是回文

### 代码

```python
# 方法一：暴力枚举
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        best = s[0]

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for left in range(n):
            for right in range(left, n):
                if right - left + 1 > len(best) and is_palindrome(left, right):
                    best = s[left:right + 1]

        return best
```

### 复杂度

- 时间复杂度：`O(n^3)`
- 空间复杂度：`O(1)`

### 评价

这个方法适合理解题意，但效率较差。

因为：

- 子串有 `O(n^2)` 个
- 每次检查回文最坏又要 `O(n)`

---

## 方法二：递归定义 + 记忆化

### 思路

如果从“区间是不是回文”来想，可以定义：

```text
dfs(left, right) = s[left:right+1] 是否是回文串
```

那么：

- 如果 `s[left] != s[right]`，那一定不是回文
- 如果 `s[left] == s[right]`，那还要看内部那一段：

```text
s[left+1:right]
```

是不是回文

所以递归定义是：

```text
s[left:right+1] 是回文
等价于
s[left] == s[right] 且内部子串也是回文
```

再加上记忆化，避免重复计算。

### 代码

```python
# 方法二：记忆化递归
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        memo = {}
        best_left = 0
        best_len = 1

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
                if right - left + 1 > best_len and dfs(left, right):
                    best_left = left
                    best_len = right - left + 1

        return s[best_left:best_left + best_len]
```

### 复杂度

- 时间复杂度：`O(n^2)`
- 空间复杂度：`O(n^2)`

### 评价

这个方法已经把暴力优化下来了，而且能很清楚地看出“区间回文”的递归结构。

但面试里一般更推荐写迭代 DP 或中心扩展。

---

## 方法三：动态规划

### 思路

这是这题最经典的区间 DP 写法。

定义：

```text
dp[left][right] = s[left:right+1] 是否是回文串
```

如果 `s[left] != s[right]`，那它一定不是回文。

如果 `s[left] == s[right]`，那分两种情况：

#### 情况 1：区间长度 <= 2

比如：

- 单个字符
- 两个相同字符
- 三个字符且两端相同

这种时候内部不用再看，直接就是回文。

#### 情况 2：区间长度 > 2

那就要看内部子串：

```text
dp[left + 1][right - 1]
```

所以转移就是：

```text
如果 s[left] == s[right]：
    当 right - left <= 2 时，dp[left][right] = True
    否则 dp[left][right] = dp[left + 1][right - 1]
```

### 代码

```python
# 方法三：动态规划
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, end = 0, 0

        for right in range(n):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True
                    if right - left > end - start:
                        start, end = left, right

        return s[start:end + 1]
```

### 复杂度

- 时间复杂度：`O(n^2)`
- 空间复杂度：`O(n^2)`

### 评价

这是字符串区间 DP 的标准模板写法。

优点：

- 状态定义非常经典
- 很适合练“区间 DP”思维
- 逻辑完整

缺点：

- 代码量比中心扩展略大
- 空间复杂度是 `O(n^2)`

---

## 方法四：中心扩展（最适合面试）

### 为什么这个最适合面试

这是这题最常见、最顺手、也最容易现场讲清楚的写法。

原因：

1. 不需要二维表
2. 状态更直观
3. 代码短
4. 面试里很容易手写正确

所以这题如果面试只准备一个版本，优先准备这个。

---

### 核心思路

回文串的特点是：

> 它一定是从中间向两边对称的。

所以我们可以把每个位置都当成回文中心，然后往两边扩展。

但要注意，回文有两种类型：

1. **奇数长度回文**，比如：`aba`
   - 中心是一个字符
2. **偶数长度回文**，比如：`abba`
   - 中心是两个字符中间那条缝

所以对每个位置，都要扩两次：

- 一次以 `(i, i)` 为中心
- 一次以 `(i, i + 1)` 为中心

### 代码

```python
# 方法四：中心扩展
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]
```

### 复杂度

- 时间复杂度：`O(n^2)`
- 空间复杂度：`O(1)`

### 评价

这是这题最推荐的面试写法。

优点：

- 思路自然
- 代码短
- 不需要额外二维数组
- 很适合现场讲解

---

## 哪个方法最适合面试

### 结论

**最适合面试的是：方法四，中心扩展。**

### 为什么不是别的方法

#### 方法一：暴力枚举

- 太慢
- 只能帮助理解题意
- 不能作为最终答案

#### 方法二：记忆化递归

- 能体现区间回文定义
- 但不如后两种写法常见

#### 方法三：动态规划

- 很标准
- 也完全可以作为答案
- 但代码更重，空间也更大

所以综合来看：

> **方法四最稳、最好写，也最适合作为面试主答案。**

---

## 最适合面试的方法：详细讲解

### 1. 为什么回文适合从中心扩展

因为回文的本质就是“左右对称”。

如果一段字符串是回文，那么从中间往两边看，一定总能一一对应相等。

所以与其枚举整个区间，不如直接从中心出发往两边扩。

这就是这题中心扩展法最核心的直觉。

---

### 2. 为什么要分奇数中心和偶数中心

因为回文串不一定只有一个中心字符。

比如：

- `aba` 的中心是 `b`
- `abba` 的中心是中间两个 `b` 之间

如果你只枚举单字符中心，就会漏掉偶数长度回文。

所以必须同时处理：

- `(i, i)`
- `(i, i + 1)`

---

### 3. 为什么扩展停止时要返回 `left + 1, right - 1`

因为 while 循环退出时，说明：

- 要么越界了
- 要么左右字符已经不相等了

也就是说，当前的 `left, right` 已经不是合法回文边界。

真正最后一个合法回文区间，是上一次成功匹配的位置：

```text
left + 1 到 right - 1
```

这点非常容易写错。

---

### 4. 为什么这题中心扩展比 DP 更适合面试

因为面试里通常更看重：

- 思路是不是自然
- 代码是不是容易写对
- 边界是不是容易控制

中心扩展法：

- 不需要二维表
- 不需要考虑区间遍历顺序
- 逻辑短很多

所以通常比 DP 更适合现场手写。

---

### 5. 用例子走一遍

以：

```text
s = "babad"
```

为例。

当中心在 `a`（下标 1）时：

- 先看 `a`
- 两边扩成 `bab`
- 再往外就不相等了

所以得到回文串：

```text
"bab"
```

当中心在下标 2 的 `b` 时：

- 先看 `b`
- 两边扩成 `aba`

所以又得到：

```text
"aba"
```

这也是为什么这题答案可能不唯一。

---

### 6. 面试里怎么说最自然

你可以这样讲：

> 我利用回文串左右对称的性质，把每个位置都当成回文中心，然后向两边扩展。由于回文既可能是奇数长度，也可能是偶数长度，所以每个位置我要扩两次：一次以 `(i, i)` 为中心，一次以 `(i, i + 1)` 为中心。每次扩展时只要左右字符相同就继续，维护最长回文子串即可。

这套表达非常像这题的标准面试回答。

---

### 面试最推荐代码

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_left = 0
        best_len = 1

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            left1, right1 = expand(i, i)
            if right1 - left1 + 1 > best_len:
                best_left = left1
                best_len = right1 - left1 + 1

            left2, right2 = expand(i, i + 1)
            if right2 - left2 + 1 > best_len:
                best_left = left2
                best_len = right2 - left2 + 1

        return s[best_left:best_left + best_len]
```

---

## 总结

### 递进关系

1. **暴力枚举**
   - 最直观
   - 但复杂度高

2. **记忆化递归**
   - 体现区间回文定义
   - 已经能过

3. **动态规划**
   - 区间 DP 的标准模板
   - 很适合练字符串 DP

4. **中心扩展**
   - 最常见
   - 最适合面试
   - 空间更优

### 一句话记忆

> 回文串一定围绕某个中心左右对称，所以枚举中心并向两边扩展，就能找到最长回文子串。
