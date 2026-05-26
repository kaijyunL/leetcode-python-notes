# LeetCode 187. 重复的 DNA 序列（Repeated DNA Sequences）解析

## 题目描述

给你一个 DNA 字符串 `s`，只包含：

```text
A, C, G, T
```

请找出所有出现超过一次的、长度为 `10` 的子串。

例子：

```text
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC", "CCCCCAAAAA"]
```

---

## 先理解题意

题目只看长度为 `10` 的连续片段。

比如：

```text
s = "AAAAACCCCCAAAAA"
```

长度为 `10` 的窗口会依次是：

```text
s[0:10]
s[1:11]
s[2:12]
...
```

只要某个长度为 `10` 的片段第二次出现，就把它加入答案。

---

## 方法一：哈希集合 + 字符串切片

### 思路

用两个集合：

- `seen`：已经见过一次的长度为 `10` 的子串
- `repeated`：已经确认重复的子串

遍历所有长度为 `10` 的窗口：

```python
seq = s[i:i + 10]
```

如果 `seq` 已经在 `seen` 中，说明它重复了，放进 `repeated`。

如果没见过，就放进 `seen`。

### 面试代码

```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen = set()
        repeated = set()

        for i in range(len(s) - 9):
            seq = s[i:i + 10]
            if seq in seen:
                repeated.add(seq)
            else:
                seen.add(seq)

        return list(repeated)
```

### 代码里的关键点

```python
range(len(s) - 9)
```

表示所有长度为 `10` 的窗口起点。

如果 `len(s) = 10`，只有一个窗口，起点是 `0`。

```python
s[i:i + 10]
```

表示从 `i` 开始取 10 个字符。

```python
repeated.add(seq)
```

用集合保存答案，避免同一个重复序列被加入多次。

### 复杂度

因为窗口长度固定为 `10`，切片成本可以看成常数。

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

---

## 方法二：2-bit 滚动编码

### 思路

这个方法做的事情和方法一一样：仍然是检查每个长度为 `10` 的窗口。

区别是：

- 方法一把窗口字符串本身放进集合，比如 `"AAAAACCCCC"`
- 方法二把窗口压成一个整数，再把整数放进集合

DNA 只有 4 种字符，所以可以用 2 个 bit 表示一个字符：

```text
A -> 00
C -> 01
G -> 10
T -> 11
```

长度为 `10` 的 DNA 子串就可以压成 `20` 个 bit，因为：

```text
10 个字符 * 每个字符 2 bit = 20 bit
```

`code` 表示当前窗口的编码。

当已经读到下标 `i`，并且 `i >= 9` 时，当前窗口就是：

```python
s[i - 9:i + 1]
```

也就是以 `s[i]` 结尾、长度为 `10` 的子串。

### 窗口怎么从旧窗口变成新窗口

假设当前窗口是：

```text
ACGTACGTAA
```

它的 2-bit 编码是：

```text
A  C  G  T  A  C  G  T  A  A
00 01 10 11 00 01 10 11 00 00
```

现在右边新进来一个字符 `C`，新窗口应该变成：

```text
CGTACGTAAC
```

也就是：

```text
丢掉最左边的 A
保留后面的 CGTACGTAA
末尾加入新的 C
```

代码用这一句完成：

```python
code = ((code << 2) | value[ch]) & mask
```

假设 `ch = "C"`，分三步看。

第一步：

```python
code << 2
```

把旧编码整体左移 2 位，末尾空出 2 位：

```text
旧窗口：
00 01 10 11 00 01 10 11 00 00

左移 2 位后：
00 01 10 11 00 01 10 11 00 00 00
```

第二步：

```python
| value["C"]
```

`C` 的编码是 `01`，把它放到最低 2 位：

```text
00 01 10 11 00 01 10 11 00 00 01
```

这时它其实表示 11 个字符：

```text
ACGTACGTAAC
```

第三步：

```python
& mask
```

`mask = (1 << 20) - 1`，表示只保留低 20 位，也就是最后 10 个字符。

所以最左边旧的 `A` 被丢掉，剩下：

```text
C  G  T  A  C  G  T  A  A  C
01 10 11 00 01 10 11 00 00 01
```

这正好是新窗口：

```text
CGTACGTAAC
```

注意：这里“保留下来的低 20 位”只是 **当前长度为 10 的窗口编码**，不是说它已经重复了。

重复要靠集合判断：

```python
if code in seen:
```

如果当前 `code` 之前已经出现在 `seen` 里，才说明当前这个长度为 10 的窗口重复出现了。

也就是说：

```text
& mask         负责得到当前窗口
code in seen  负责判断当前窗口是不是重复
```

### 为什么 `mask` 是 `(1 << 20) - 1`

长度为 `10` 的窗口需要 20 位。

```text
1 << 20
= 1 后面跟 20 个 0

(1 << 20) - 1
= 低 20 位全是 1
```

所以：

```text
code & mask
```

意思就是：只保留最近 10 个 DNA 字符的编码。

### 面试代码

```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s) < 10:
            return []

        value = {"A": 0, "C": 1, "G": 2, "T": 3}
        seen = set()
        repeated = set()
        ans = []

        code = 0
        mask = (1 << 20) - 1

        for i, ch in enumerate(s):
            code = ((code << 2) | value[ch]) & mask

            if i < 9:
                continue

            if code in seen and code not in repeated:
                ans.append(s[i - 9:i + 1])
                repeated.add(code)
            else:
                seen.add(code)

        return ans
```

### 代码对应解释

```python
if len(s) < 10:
    return []
```

长度不足 10，不可能有长度为 10 的重复子串。

```python
value = {"A": 0, "C": 1, "G": 2, "T": 3}
```

把 DNA 字符映射成 2-bit 数值：

```text
A -> 0 -> 00
C -> 1 -> 01
G -> 2 -> 10
T -> 3 -> 11
```

```python
seen = set()
repeated = set()
ans = []
```

- `seen`：见过一次的窗口编码
- `repeated`：已经加入过答案的重复窗口编码
- `ans`：答案字符串列表

```python
code = 0
mask = (1 << 20) - 1
```

- `code`：当前窗口的 20 位编码
- `mask`：保留低 20 位

```python
for i, ch in enumerate(s):
```

从左到右读每个字符。

```python
code = ((code << 2) | value[ch]) & mask
```

把当前字符加入窗口编码，并且只保留最近 10 个字符。

```python
if i < 9:
    continue
```

当 `i < 9` 时，还没有形成长度为 10 的窗口。

比如：

```text
i = 0 只有 1 个字符
i = 8 只有 9 个字符
i = 9 才有第一个长度为 10 的窗口 s[0:10]
```

所以 `i < 9` 时跳过检查。

```python
s[i - 9:i + 1]
```

这是当前长度为 10 的窗口。

比如 `i = 9`：

```text
s[0:10]
```

比如 `i = 10`：

```text
s[1:11]
```

### 用前 11 个字符走一遍

假设字符串开头是：

```text
AAAAACCCCCC
```

第一个完整窗口在 `i = 9` 时出现：

```text
s[0:10] = "AAAAACCCCC"
```

这时 `code` 表示的就是 `"AAAAACCCCC"` 的 20 位编码。

如果这个 `code` 没见过，就加入 `seen`。

下一个字符在 `i = 10`，当前窗口变成：

```text
s[1:11] = "AAAACCCCCC"
```

代码：

```python
code = ((code << 2) | value[s[10]]) & mask
```

做了三件事：

```text
1. code << 2：把旧窗口整体左移，给 s[10] 腾出最低 2 位
2. | value[s[10]]：把新字符 s[10] 放进最低 2 位
3. & mask：只保留最近 10 个字符，丢掉最左边那个旧字符
```

所以 `code` 从表示：

```text
"AAAAACCCCC"
```

变成表示：

```text
"AAAACCCCCC"
```

这就是滚动窗口。

### 重复怎么判断

```python
if code in seen and code not in repeated:
    ans.append(s[i - 9:i + 1])
    repeated.add(code)
else:
    seen.add(code)
```

含义是：

- 如果 `code` 已经在 `seen`，说明这个长度为 10 的窗口之前出现过
- 如果它还不在 `repeated`，说明还没加入过答案，就加入一次
- 如果第一次见，就放进 `seen`

这里 `ans` 里放的是字符串：

```python
ans.append(s[i - 9:i + 1])
```

因为题目要求返回重复的 DNA 字符串，不是返回编码整数。

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

位压缩减少的是 key 的大小：集合里存整数编码，而不是长度为 10 的字符串。

---

## 哪个方法最适合面试

如果面试没有强制位运算，最推荐 **方法一：哈希集合 + 字符串切片**。

原因：

- 代码最短
- 逻辑最直观
- Python 里长度 10 是固定常数，复杂度仍然是 `O(n)`
- 现场不容易写错

如果面试官明确要求“优化字符串存储”或“用位运算”，再写 **方法二：2-bit 滚动编码**。

面试里可以这样说方法一：

```text
我遍历所有长度为 10 的子串。
seen 记录见过一次的子串。
如果当前子串已经在 seen 里，说明它重复了，加入 repeated。
repeated 用集合是为了避免同一个答案重复加入。
因为窗口长度固定是 10，所以整体时间复杂度是 O(n)。
```

---

## 总结

- 方法一：哈希集合 + 字符串切片
  - Python 面试最稳
  - 推荐优先写

- 方法二：2-bit 滚动编码
  - 更符合位运算专题
  - 适合面试官追问空间压缩时补充
