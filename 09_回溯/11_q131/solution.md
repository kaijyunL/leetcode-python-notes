# LeetCode 131 — 分割回文串（Palindrome Partitioning）

## 题目

给定一个字符串 `s`，请把 `s` 分割成一些子串，使每个子串都是回文串。

返回所有可能的分割方案。

### 示例

```
输入: s = "aab"
输出: [["a", "a", "b"], ["aa", "b"]]
```

解释：

```
"a" | "a" | "b"
"aa" | "b"
```

每一段都是回文串。

---

## 和 Q93 的关系

Q93 复原 IP 地址是：

```
把字符串切成固定 4 段
每段必须是合法 IP 段
```

Q131 分割回文串是：

```
把字符串切成任意段
每段必须是回文串
```

所以它们都是字符串切割回溯。

区别是：

```text
Q93：段数固定，段长度 1 到 3
Q131：段数不固定，段长度可以从 1 到剩余全部
```

---

## 什么是回文串？

回文串就是正着读和反着读一样的字符串。

比如：

```
"a"      是回文
"aa"     是回文
"aba"    是回文
"abba"   是回文
"ab"     不是回文
"aab"    不是回文
```

---

## 核心理解

这题本质是：

```
从当前位置 start 开始，枚举一个切割终点 end
如果 s[start:end+1] 是回文，就切这一段
然后从 end + 1 继续切
```

当：

```python
start == len(s)
```

说明整个字符串已经切完，当前 `path` 就是一个合法方案。

---

## 解法一览

| 解法 | 思路 | 时间复杂度 | 空间复杂度 | 是否推荐面试 |
|---|---|---|---|---|
| 1. 暴力切割 + 最后校验 | 枚举所有切法，最后检查每段是否回文 | O(n * 2^n) | O(n * 2^n) | 只适合理解 |
| 2. 回溯 + 实时判断回文 | 边切边判断当前段是否回文 | O(n * 2^n) | O(n * 2^n) | 可以写 |
| 3. 回溯 + 回文预处理 | 先 DP 预处理所有子串是否回文，再回溯 | O(n * 2^n) | O(n * 2^n) | **面试推荐 ✅** |

> 长度为 `n` 的字符串一共有 `n - 1` 个切割位置，每个位置可以切或不切，所以切法数量最多是 `2^(n-1)`。返回结果本身就是指数级。

---

## 解法 1：暴力切割 + 最后校验

### 思路

字符串长度为 `n`，字符之间有 `n - 1` 个间隔。

每个间隔有两种选择：

```
切
不切
```

比如：

```
s = "aab"
```

两个间隔：

```
a | a | b
```

可以有这些切法：

```
"aab"
"a" | "ab"
"aa" | "b"
"a" | "a" | "b"
```

然后检查每种切法中的每一段是否都是回文。

### 代码

```python
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        n = len(s)

        def is_palindrome(part: str) -> bool:
            return part == part[::-1]

        for mask in range(1 << (n - 1)):
            path = []
            start = 0

            for i in range(n - 1):
                if mask & (1 << i):
                    path.append(s[start:i + 1])
                    start = i + 1

            path.append(s[start:])

            if all(is_palindrome(part) for part in path):
                ans.append(path)

        return ans
```

### 评价

这个方法能帮助理解“切割位置”的概念。

但它先生成所有切法，再整体检查，不能在发现某一段不是回文时提前停止，所以不推荐面试。

---

## 解法 2：回溯 + 实时判断回文

### 思路

回溯过程中，每次从 `start` 开始尝试切一段：

```python
for end in range(start, len(s)):
```

当前段是：

```python
part = s[start:end + 1]
```

如果当前段不是回文，跳过：

```python
if not is_palindrome(part):
    continue
```

如果是回文，就加入路径，继续从 `end + 1` 开始切。

### 代码

```python
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        path = []

        def is_palindrome(part: str) -> bool:
            return part == part[::-1]

        def backtrack(start: int) -> None:
            if start == len(s):
                ans.append(path[:])
                return

            for end in range(start, len(s)):
                part = s[start:end + 1]
                if not is_palindrome(part):
                    continue

                path.append(part)
                backtrack(end + 1)
                path.pop()

        backtrack(0)
        return ans
```

### 为什么终止条件是 `start == len(s)`？

因为 `start` 表示下一段要从哪里开始切。

当：

```python
start == len(s)
```

说明字符串已经全部切完。

比如：

```
s = "aab"
```

切法：

```
"aa" | "b"
```

过程：

```
切 "aa" 后，start = 2
切 "b" 后，start = 3
```

而：

```python
len(s) == 3
```

所以 `start == len(s)` 表示刚好用完整个字符串。

---

## 解法 3：回溯 + 回文预处理 ⭐ 面试推荐

### 思路

解法 2 每次都用：

```python
part == part[::-1]
```

判断回文。

这会反复检查相同子串。

可以先用 DP 预处理：

```python
is_pal[i][j]
```

表示：

```python
s[i:j+1] 是否是回文
```

之后回溯时就可以 O(1) 判断：

```python
if not is_pal[start][end]:
    continue
```

### 回文 DP 怎么写？

一个子串：

```python
s[left:right + 1]
```

是回文，需要满足：

1. 两端字符相同
2. 中间部分也是回文

也就是：

```python
s[left] == s[right] and is_pal[left + 1][right - 1]
```

但长度为 1 或 2 的子串，中间部分可以直接认为成立。

所以判断是：

```python
if s[left] == s[right] and (right - left <= 2 or is_pal[left + 1][right - 1]):
    is_pal[left][right] = True
```

为什么是 `right - left <= 2`？

看三种情况：

```text
长度 1：left == right，比如 "a"
长度 2：right - left == 1，比如 "aa"
长度 3：right - left == 2，比如 "aba"
```

这三种只要两端相等，就一定是回文，或者中间只有一个字符。

为了让 `is_pal[left + 1][right - 1]` 已经计算好，需要让 `left` 从右往左遍历：

```python
for left in range(n - 1, -1, -1):
    for right in range(left, n):
```

这样计算较长子串时，中间较短子串已经有结果。

### 代码

```python
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]

        for left in range(n - 1, -1, -1):
            for right in range(left, n):
                if s[left] == s[right] and (
                    right - left <= 2 or is_pal[left + 1][right - 1]
                ):
                    is_pal[left][right] = True

        ans = []
        path = []

        def backtrack(start: int) -> None:
            if start == n:
                ans.append(path[:])
                return

            for end in range(start, n):
                if not is_pal[start][end]:
                    continue

                path.append(s[start:end + 1])
                backtrack(end + 1)
                path.pop()

        backtrack(0)
        return ans
```

### 以 `"aab"` 为例

回文子串有：

```
"a"   s[0:1]
"a"   s[1:2]
"b"   s[2:3]
"aa"  s[0:2]
```

回溯时：

```
start = 0
可以切 "a"
也可以切 "aa"
不能切 "aab"
```

切 `"a"` 后：

```
start = 1
可以切 "a"
不能切 "ab"
```

得到：

```
["a", "a", "b"]
```

切 `"aa"` 后：

```
start = 2
可以切 "b"
```

得到：

```
["aa", "b"]
```

### 复杂度

回文预处理需要：

```
O(n^2)
```

回溯返回所有切法，最坏情况下有指数级数量。每次复制路径也有成本。

整体时间复杂度通常写：

```
O(n * 2^n)
```

空间复杂度包含返回结果：

```
O(n * 2^n)
```

额外的 DP 表是：

```
O(n^2)
```

如果不算返回结果，递归栈和 `path` 是 `O(n)`。

### 为什么它最适合面试？

因为它体现了字符串切割回溯的完整思路，也避免了重复判断回文：

1. `start` 表示当前切割位置
2. `path` 保存当前切割方案
3. 枚举 `end`，尝试切 `s[start:end+1]`
4. 只有这段是回文才递归
5. 用 DP 预处理让回文判断变成 O(1)

面试时可以这样讲：

> 我先预处理 `is_pal[i][j]`，表示 `s[i:j+1]` 是否是回文。然后用回溯切字符串，`start` 表示当前切割位置。每次枚举 `end`，如果 `s[start:end+1]` 是回文，就加入路径并递归切剩余部分。当 `start == len(s)` 时，说明整个字符串切完，把当前路径加入答案。

---

## 最终推荐

面试最推荐写 **解法 3：回溯 + 回文预处理**。

核心回溯代码：

```python
for end in range(start, n):
    if not is_pal[start][end]:
        continue

    path.append(s[start:end + 1])
    backtrack(end + 1)
    path.pop()
```

核心 DP 代码：

```python
for left in range(n - 1, -1, -1):
    for right in range(left, n):
        if s[left] == s[right] and (
            right - left <= 2 or is_pal[left + 1][right - 1]
        ):
            is_pal[left][right] = True
```

重点记住：

```
Q93：切固定 4 段，每段是合法 IP 段
Q131：切任意段，每段是回文串
```
