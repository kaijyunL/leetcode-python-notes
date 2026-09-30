# LeetCode 22 — 括号生成（Generate Parentheses）

## 题目

给定一个整数 `n`，表示有 `n` 对括号。请生成所有合法的括号组合。

### 示例

```
输入: n = 3
输出: ["((()))", "(()())", "(())()", "()(())", "()()()"]
```

---

## 什么是合法括号？

一个括号字符串合法，需要满足两个条件：

1. 左括号和右括号数量都等于 `n`
2. 从左到右扫描时，任意位置的右括号数量不能超过左括号数量

比如：

```
合法:   (()())
不合法: ())(
```

`())(` 不合法，因为扫描到第三个字符时：

```
左括号数量 = 1
右括号数量 = 2
```

右括号已经超过左括号。

---

## 核心难点

这题不是简单地生成所有长度为 `2n` 的字符串。

每个位置确实可以放：

```
(
)
```

但很多字符串明显不合法。

比如 `n = 3` 时：

```
)))(((
())(()
```

都不合法。

所以最好的思路是：

```
在生成过程中就保证当前路径合法
```

这就是回溯剪枝。

---

## 解法一览

| 解法 | 思路 | 时间复杂度 | 空间复杂度 | 是否推荐面试 |
|---|---|---|---|---|
| 1. 暴力生成 + 校验 | 生成所有长度为 `2n` 的括号串，再筛选合法串 | O(n * 2^(2n)) | O(n * 2^(2n)) | 只适合理解 |
| 2. 回溯 + 字符串拼接 | 生成时限制左右括号数量 | O(n * Cn) | O(n * Cn) | 可以写 |
| 3. 回溯 + path 列表 | 用列表维护路径，减少字符串频繁拷贝 | O(n * Cn) | O(n * Cn) | **面试推荐 ✅** |

> `Cn` 是第 `n` 个卡特兰数，表示合法括号组合的数量。面试里可以简单说：答案数量本身就是卡特兰数级别，算法复杂度和答案规模相关。

---

## 解法 1：暴力生成 + 校验

### 思路

长度为 `2n` 的字符串，每个位置都有两种选择：

```
(
)
```

所以一共有：

```
2^(2n)
```

种字符串。

我们可以先全部生成出来，然后判断是否合法。

### 如何判断合法？

从左到右扫描，用 `balance` 表示当前还没被匹配的左括号数量。

遇到 `(`：

```python
balance += 1
```

遇到 `)`：

```python
balance -= 1
```

如果过程中 `balance < 0`，说明右括号太多，直接不合法。

最后如果 `balance == 0`，说明左右括号刚好匹配。

### 代码

```python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def is_valid(s: str) -> bool:
            balance = 0
            for ch in s:
                if ch == "(":
                    balance += 1
                else:
                    balance -= 1

                if balance < 0:
                    return False

            return balance == 0

        def dfs(path: str) -> None:
            if len(path) == 2 * n:
                if is_valid(path):
                    ans.append(path)
                return

            dfs(path + "(")
            dfs(path + ")")

        dfs("")
        return ans
```

### 评价

这个方法最容易想到，但不推荐面试。

原因是它生成了大量明显不合法的字符串，然后再筛掉。

比如第一个字符是 `)` 的字符串，一开始就已经不可能合法，但暴力法仍然会继续生成完整长度。

---

## 解法 2：回溯 + 字符串拼接

### 思路

既然暴力法的问题是生成了不合法路径，那我们可以在生成时加限制。

维护两个变量：

| 变量 | 含义 |
|---|---|
| `left` | 当前已经使用的左括号数量 |
| `right` | 当前已经使用的右括号数量 |

什么时候可以放左括号？

```python
left < n
```

因为左括号最多只能用 `n` 个。

什么时候可以放右括号？

```python
right < left
```

因为右括号不能超过左括号。只有当前左括号更多时，才能放一个右括号去匹配。

### 代码

```python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def backtrack(path: str, left: int, right: int) -> None:
            if len(path) == 2 * n:
                ans.append(path)
                return

            if left < n:
                backtrack(path + "(", left + 1, right)

            if right < left:
                backtrack(path + ")", left, right + 1)

        backtrack("", 0, 0)
        return ans
```

### 为什么 `right < left`？

因为在任意前缀中：

```
右括号数量 <= 左括号数量
```

如果现在：

```
right == left
```

再放一个 `)`，就会变成：

```
right > left
```

这一定不合法。

所以只有：

```python
right < left
```

时，才允许放右括号。

---

## 解法 3：回溯 + path 列表 ⭐ 面试推荐

### 思路

解法 2 已经是正确的回溯写法。

解法 3 只是把字符串拼接换成 `path` 列表：

```python
path.append("(")
backtrack(...)
path.pop()
```

这样更符合前面回溯题的统一模板：

```
做选择 -> 递归 -> 撤销选择
```

### 代码

```python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        path = []

        def backtrack(left: int, right: int) -> None:
            if len(path) == 2 * n:
                ans.append("".join(path))
                return

            if left < n:
                path.append("(")
                backtrack(left + 1, right)
                path.pop()

            if right < left:
                path.append(")")
                backtrack(left, right + 1)
                path.pop()

        backtrack(0, 0)
        return ans
```

### 以 `n = 3` 为例

一开始：

```
path = []
left = 0
right = 0
```

只能放左括号：

```
(
```

因为 `right < left` 不成立，不能一开始就放 `)`。

当：

```
path = ["("]
left = 1
right = 0
```

可以放：

```
继续放 "("
或者放 ")"
```

只要遵守：

```
left < n      才能放 "("
right < left  才能放 ")"
```

最终会生成：

```
((()))
(()())
(())()
()(())
()()()
```

### 复杂度

合法括号组合数量是第 `n` 个卡特兰数，记作 `Cn`。

每个结果长度为 `2n`，加入答案时需要拼接：

```python
"".join(path)
```

时间复杂度：

```
O(n * Cn)
```

空间复杂度包含返回结果：

```
O(n * Cn)
```

如果不算返回结果，递归栈和 `path` 都是：

```
O(n)
```

### 为什么它最适合面试？

因为它清楚表达了合法括号生成的两个约束：

```python
if left < n:
```

左括号还没用完，可以放左括号。

```python
if right < left:
```

右括号数量少于左括号数量，可以放右括号。

面试时可以这样讲：

> 我用回溯生成括号。`left` 表示已经放了多少个左括号，`right` 表示已经放了多少个右括号。只要左括号数量还没到 `n`，就可以继续放左括号。只有右括号数量小于左括号数量时，才能放右括号，保证任何前缀都合法。当路径长度等于 `2n` 时，得到一个完整答案。

---

## 最终推荐

面试最推荐写 **解法 3：回溯 + path 列表**。

核心代码：

```python
if left < n:
    path.append("(")
    backtrack(left + 1, right)
    path.pop()

if right < left:
    path.append(")")
    backtrack(left, right + 1)
    path.pop()
```

重点记住：

```
left < n：还能放左括号
right < left：还能放右括号
```
