# LeetCode 93 — 复原 IP 地址（Restore IP Addresses）

## 题目

给定一个只包含数字的字符串 `s`，返回所有可能的有效 IP 地址。

有效 IP 地址由 4 个整数段组成，每段范围是 `0` 到 `255`，段之间用点号 `.` 分隔。

每段不能有前导零，除非这个段本身就是 `"0"`。

### 示例

```
输入: s = "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
```

```
输入: s = "0000"
输出: ["0.0.0.0"]
```

---

## 合法 IP 段的规则

一个字符串 `part` 是合法 IP 段，需要满足：

1. 长度在 `1` 到 `3` 之间
2. 数值在 `0` 到 `255` 之间
3. 如果长度大于 1，不能以 `"0"` 开头

比如：

```
"0"    合法
"9"    合法
"10"   合法
"255"  合法
"256"  不合法，超过 255
"01"   不合法，有前导 0
"001"  不合法，有前导 0
```

---

## 核心理解

这题本质是：

```
把字符串切成 4 段
每段长度只能是 1、2、3
每段都必须是合法 IP 段
```

比如：

```
s = "25525511135"
```

可以切成：

```
255 | 255 | 11 | 135
255 | 255 | 111 | 35
```

对应：

```
255.255.11.135
255.255.111.35
```

---

## 解法一览

| 解法 | 思路 | 时间复杂度 | 空间复杂度 | 是否推荐面试 |
|---|---|---|---|---|
| 1. 三重循环枚举切点 | 枚举 3 个点的位置，检查 4 段是否合法 | O(1) | O(1) | 简单可写 |
| 2. 基础回溯 + 总长度剪枝 | 每次切 1 到 3 位，递归构造 4 段 | O(1) | O(1) | **面试推荐 ✅** |
| 3. 回溯 + 递归内剪枝 | 根据剩余字符数量提前停止无效分支 | O(1) | O(1) | 进阶补充 |

> 这题字符串长度最多是 12，因为 IP 地址 4 段，每段最多 3 位。所以从大 O 角度可以认为是常数级。但按回溯结构理解，搜索分支最多是 `3^4`，非常小。

---

## 解法 1：三重循环枚举切点

### 思路

IP 地址需要切成 4 段，也就是要放 3 个点。

可以枚举前三段的长度：

```python
len1 in 1..3
len2 in 1..3
len3 in 1..3
```

第四段由剩余字符串决定。

比如：

```
s = "25525511135"
```

如果前三段长度是：

```
3, 3, 2
```

则：

```
255 | 255 | 11 | 135
```

检查 4 段都合法，就加入答案。

### 代码

```python
class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        ans = []

        def is_valid(part: str) -> bool:
            if not part or len(part) > 3:
                return False
            if len(part) > 1 and part[0] == "0":
                return False
            return int(part) <= 255

        n = len(s)

        for len1 in range(1, 4):
            for len2 in range(1, 4):
                for len3 in range(1, 4):
                    len4 = n - len1 - len2 - len3
                    if len4 < 1 or len4 > 3:
                        continue

                    p1 = s[:len1]
                    p2 = s[len1:len1 + len2]
                    p3 = s[len1 + len2:len1 + len2 + len3]
                    p4 = s[len1 + len2 + len3:]

                    if all(is_valid(part) for part in [p1, p2, p3, p4]):
                        ans.append(".".join([p1, p2, p3, p4]))

        return ans
```

### 评价

这个方法很直接，因为 IP 地址固定就是 4 段。

它不是典型回溯模板，但面试中也可以接受。缺点是写法不如回溯通用，后续遇到“不固定段数”的切割问题时不容易迁移。

---

## 解法 2：基础回溯 + 总长度剪枝 ⭐ 面试推荐

### 思路

用回溯逐段切字符串。

先做一个总长度判断：

```python
if len(s) < 4 or len(s) > 12:
    return []
```

因为 IP 地址固定 4 段，每段长度 1 到 3，所以字符串总长度必须在：

```
4 到 12
```

之间。

这个剪枝简单、清楚、收益稳定，面试建议加。

变量含义：

| 变量 | 含义 |
|---|---|
| `ans` | 存放所有 IP 地址 |
| `path` | 当前已经切出来的 IP 段 |
| `start` | 当前还没处理的字符串起点 |

每次从 `start` 开始，尝试切长度为 1、2、3 的段：

```python
for length in range(1, 4):
```

如果这一段合法，就加入 `path`，继续递归切下一段。

当：

```python
len(path) == 4
```

时，说明已经切了 4 段。

如果这时刚好用完整个字符串：

```python
start == len(s)
```

就得到一个合法 IP。

### 代码

```python
class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        if len(s) < 4 or len(s) > 12:
            return []

        ans = []
        path = []

        def is_valid(part: str) -> bool:
            if len(part) > 1 and part[0] == "0":
                return False
            return int(part) <= 255

        def backtrack(start: int) -> None:
            if len(path) == 4:
                if start == len(s):
                    ans.append(".".join(path))
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start + length]
                if not is_valid(part):
                    continue

                path.append(part)
                backtrack(start + length)
                path.pop()

        backtrack(0)
        return ans
```

### 为什么 `path` 长度等于 4 时要判断 `start == len(s)`？

因为 IP 地址必须刚好用完整个字符串。

比如：

```
s = "12345"
```

如果切出：

```
1.2.3.4
```

这时已经 4 段了，但还剩下 `"5"` 没用，所以不能加入答案。

只有：

```python
len(path) == 4 and start == len(s)
```

才是完整合法 IP。

---

## 解法 3：回溯 + 递归内剪枝（进阶补充）

### 思路

基础回溯已经正确。如果面试官追问还能不能继续剪枝，可以补充递归内剪枝。

假设当前已经切了：

```python
len(path)
```

段。

还需要切：

```python
remaining_parts = 4 - len(path)
```

段。

当前还剩：

```python
remaining_chars = len(s) - start
```

个字符。

每段至少 1 个字符，最多 3 个字符。

所以剩余字符数量必须满足：

```python
remaining_parts <= remaining_chars <= remaining_parts * 3
```

如果不满足，就不用继续递归。

### 代码

```python
class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        ans = []
        path = []

        def is_valid(part: str) -> bool:
            if len(part) > 1 and part[0] == "0":
                return False
            return int(part) <= 255

        def backtrack(start: int) -> None:
            remaining_parts = 4 - len(path)
            remaining_chars = len(s) - start

            if remaining_chars < remaining_parts or remaining_chars > remaining_parts * 3:
                return

            if len(path) == 4:
                ans.append(".".join(path))
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start + length]
                if not is_valid(part):
                    continue

                path.append(part)
                backtrack(start + length)
                path.pop()

        backtrack(0)
        return ans
```

### 为什么这个剪枝是对的？

剩余每段至少要 1 位。

如果：

```python
remaining_chars < remaining_parts
```

说明字符太少，不够分。

例如还需要 3 段，但只剩 2 个字符，不可能。

剩余每段最多 3 位。

如果：

```python
remaining_chars > remaining_parts * 3
```

说明字符太多，放不下。

例如还需要 2 段，但剩 7 个字符，不可能，因为两段最多只能放 6 位。

### 为什么 `len(path) == 4` 时可以直接加入答案？

因为前面已经做过剪枝：

```python
remaining_chars < remaining_parts or remaining_chars > remaining_parts * 3
```

当：

```python
len(path) == 4
```

时：

```python
remaining_parts = 0
```

只有：

```python
remaining_chars = 0
```

才能通过剪枝。

所以这时可以直接：

```python
ans.append(".".join(path))
```

不用再额外判断 `start == len(s)`。

如果你觉得这样不直观，也可以保留显式判断：

```python
if len(path) == 4:
    if start == len(s):
        ans.append(".".join(path))
    return
```

两种都可以。学习阶段写显式判断更直观；面试时加剪枝后直接加入也可以。

### 前导零怎么处理？

合法：

```
"0"
```

不合法：

```
"00"
"01"
"001"
```

所以：

```python
if len(part) > 1 and part[0] == "0":
    return False
```

### 超过 255 怎么处理？

```python
return int(part) <= 255
```

因为 `part` 长度最多是 3，所以转整数很安全。

### 复杂度

最多切 4 段，每段最多尝试 3 种长度。

搜索分支最多是：

```
3^4
```

所以这题可以认为是常数级复杂度。

如果按字符串长度 `n` 表达，因为 `n <= 12`，也可以说复杂度非常小，主要由固定的切段数量决定。

### 什么时候需要这个剪枝？

这个剪枝是正确的，也能减少一些递归分支。

但 Q93 的搜索空间本来很小：

```
每段最多 3 种长度，一共 4 段，最多约 3^4 个分支
```

所以递归内剪枝不一定会让实际运行更快。每层都计算：

```python
remaining_parts
remaining_chars
```

也有额外开销。

面试时更推荐把这段作为口头补充，而不是强行写进主答案。

如果要讲，可以这样说：

> 还可以进一步剪枝：剩余字符数量必须能被剩余段数容纳。每段至少 1 位，最多 3 位，所以 `remaining_chars` 必须在 `[remaining_parts, remaining_parts * 3]` 范围内。

这样既能展示剪枝意识，又不会让主代码变复杂。

---

## 最终推荐

面试最推荐写 **解法 2：基础回溯 + 总长度剪枝**。

核心代码：

```python
if len(s) < 4 or len(s) > 12:
    return []
```

以及：

```python
for length in range(1, 4):
    part = s[start:start + length]
    if not is_valid(part):
        continue

    path.append(part)
    backtrack(start + length)
    path.pop()
```

重点记住：

```
IP 一共 4 段
每段长度 1 到 3
每段数值 0 到 255
长度大于 1 时不能以 0 开头
```

递归内的 `remaining_parts / remaining_chars` 剪枝可以作为进阶补充，不是面试主代码必须写的部分。
