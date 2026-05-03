# LeetCode 17 — 电话号码的字母组合（Letter Combinations of a Phone Number）

## 题目

给定一个仅包含数字 `2-9` 的字符串 `digits`，返回它能表示的所有字母组合。

数字到字母的映射和手机九宫格一样：

```
2 -> abc
3 -> def
4 -> ghi
5 -> jkl
6 -> mno
7 -> pqrs
8 -> tuv
9 -> wxyz
```

如果 `digits` 是空字符串，返回空列表。

### 示例

```
输入: digits = "23"
输出: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```

解释：

```
2 可以选 a / b / c
3 可以选 d / e / f
```

所以组合是：

```
a + d/e/f
b + d/e/f
c + d/e/f
```

---

## 和前面回溯题的关系

Q77、Q39、Q40 是从一组数字里选若干个数。

Q17 不一样，它是：

```
每个数字位置都必须选一个字母
```

比如：

```
digits = "23"
```

第一层处理数字 `2`，可以选：

```
a, b, c
```

第二层处理数字 `3`，可以选：

```
d, e, f
```

每条路径长度必须等于 `len(digits)`。

这题本质是：

```
多选一组合
```

每一层对应一个数字，每一层从这个数字对应的字母里选一个。

---

## 解法一览

| 解法 | 思路 | 时间复杂度 | 空间复杂度 | 是否推荐面试 |
|---|---|---|---|---|
| 1. 迭代扩展 | 从空字符串开始，每处理一个数字就扩展一轮 | O(n * 4^n) | O(n * 4^n) | 简单好懂 |
| 2. BFS 队列 | 用队列按层生成组合 | O(n * 4^n) | O(n * 4^n) | 可以掌握 |
| 3. 回溯 DFS | 每层处理一个数字，递归枚举所有路径 | O(n * 4^n) | O(n * 4^n) | **面试推荐 ✅** |

> `n = len(digits)`。每个数字最多对应 4 个字母，所以组合数量最多是 `4^n`。每个结果字符串长度是 `n`，因此结果空间是 `O(n * 4^n)`。

---

## 解法 1：迭代扩展

### 思路

从一个空字符串开始：

```python
ans = [""]
```

每处理一个数字，就把当前已有字符串全部扩展一轮。

以：

```python
digits = "23"
```

为例。

初始：

```
[""]
```

处理 `2 -> abc`：

```
"" + a -> "a"
"" + b -> "b"
"" + c -> "c"
```

得到：

```
["a", "b", "c"]
```

处理 `3 -> def`：

```
"a" + d/e/f -> "ad", "ae", "af"
"b" + d/e/f -> "bd", "be", "bf"
"c" + d/e/f -> "cd", "ce", "cf"
```

得到最终答案：

```
["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```

### 代码

```python
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        ans = [""]

        for digit in digits:
            next_ans = []
            for prefix in ans:
                for ch in phone[digit]:
                    next_ans.append(prefix + ch)
            ans = next_ans

        return ans
```

### 评价

这个方法很好理解，也很短。

但它更像“逐层构造结果”，不是回溯模板。后续如果题目加入约束、剪枝、路径判断，回溯写法更容易扩展。

---

## 解法 2：BFS 队列

### 思路

这个方法和迭代扩展本质一样，只是用队列来表达“按层处理”。

初始队列：

```
[""]
```

处理每个数字时，把当前队列里的所有旧字符串弹出来，然后拼上当前数字对应的每个字母，再放回队列。

比如处理 `2 -> abc`：

```
弹出 ""
加入 "a", "b", "c"
```

处理 `3 -> def`：

```
弹出 "a"，加入 "ad", "ae", "af"
弹出 "b"，加入 "bd", "be", "bf"
弹出 "c"，加入 "cd", "ce", "cf"
```

最后队列里的内容就是答案。

### 代码

```python
from collections import deque


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        queue = deque([""])

        for digit in digits:
            for _ in range(len(queue)):
                prefix = queue.popleft()
                for ch in phone[digit]:
                    queue.append(prefix + ch)

        return list(queue)
```

### 评价

BFS 队列能帮助理解“每一层处理一个数字”。

但面试里通常没有必要专门写队列版。因为这题天然就是 DFS 回溯结构，回溯版更通用。

---

## 解法 3：回溯 DFS ⭐ 面试推荐

### 思路

用回溯枚举所有组合。

变量含义：

| 变量 | 含义 |
|---|---|
| `ans` | 存放所有完整组合 |
| `path` | 当前正在构造的字母组合 |
| `index` | 当前正在处理 `digits` 的哪个位置 |

当：

```python
index == len(digits)
```

说明每个数字都已经选了一个字母，当前 `path` 是完整答案。

把它加入 `ans`：

```python
ans.append("".join(path))
```

然后返回。

### 为什么要用 `index`？

因为每一层递归对应 `digits` 的一个位置。

例如：

```python
digits = "23"
```

递归第 0 层：

```
index = 0，处理 digits[0] = "2"
```

可以选：

```
a, b, c
```

递归第 1 层：

```
index = 1，处理 digits[1] = "3"
```

可以选：

```
d, e, f
```

递归第 2 层：

```
index = 2 == len(digits)
```

说明组合完成。

### 为什么递归时是 `index + 1`？

因为每个数字位置必须处理一次。

当前层处理完 `digits[index]` 后，下一层就处理下一个数字：

```python
backtrack(index + 1)
```

这和 Q39/Q40 的 `start` 不同。

Q17 不是从数组里自由选择若干个数，而是每个数字位置都必须选一个字母，所以用 `index` 更自然。

### 代码

```python
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        ans = []
        path = []

        def backtrack(index: int) -> None:
            if index == len(digits):
                ans.append("".join(path))
                return

            digit = digits[index]
            for ch in phone[digit]:
                path.append(ch)
                backtrack(index + 1)
                path.pop()

        backtrack(0)
        return ans
```

### 以 `"23"` 为例

递归树：

```
[]
├── a
│   ├── ad
│   ├── ae
│   └── af
├── b
│   ├── bd
│   ├── be
│   └── bf
└── c
    ├── cd
    ├── ce
    └── cf
```

最终结果：

```
["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```

### 复杂度

假设 `digits` 长度为 `n`。

每个数字最多对应 4 个字母，所以最多有：

```
4^n
```

个组合。

每个组合长度为 `n`，加入答案时：

```python
"".join(path)
```

需要 `O(n)`。

时间复杂度：

```
O(n * 4^n)
```

空间复杂度包含返回结果：

```
O(n * 4^n)
```

如果不算返回结果，递归栈和 `path` 是：

```
O(n)
```

### 为什么它最适合面试？

因为它清楚地表达了这题的搜索结构：

1. 每一层处理一个数字
2. 当前数字有几个字母，就分出几个分支
3. `path` 长度等于 `digits` 长度时得到一个答案
4. 递归后撤销选择

面试时可以这样讲：

> 我用回溯。`index` 表示当前处理到第几个数字，`path` 表示当前组合。对于 `digits[index]`，枚举它对应的所有字母，加入路径后递归处理下一个数字。 当 `index == len(digits)` 时，说明每个数字都选了一个字母，把 `path` 拼成字符串加入答案。

---

## 最终推荐

面试最推荐写 **解法 3：回溯 DFS**。

核心代码：

```python
digit = digits[index]
for ch in phone[digit]:
    path.append(ch)
    backtrack(index + 1)
    path.pop()
```

重点记住：

```
Q17：每一层对应 digits 的一个位置，用 index
Q46：每一层选一个未使用数字，用 used
Q77/Q39/Q40：组合问题，用 start 控制选择范围
```
