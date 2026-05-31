# LeetCode 166. 分数到小数（Fraction to Recurring Decimal）解析

## 题目描述

给定两个整数 `numerator` 和 `denominator`，表示一个分数：

```text
numerator / denominator
```

把它转换成字符串形式的小数。

如果小数部分出现循环节，就用括号括起来。

例子：

```text
1 / 2   -> "0.5"
2 / 1   -> "2"
4 / 333 -> "0.(012)"
1 / 6   -> "0.1(6)"
```

---

## 先理解题意

这题其实就是手写小学长除法。

比如：

```text
1 / 6
```

整数部分：

```text
1 // 6 = 0
1 % 6  = 1
```

所以开头是：

```text
0.
```

接下来处理小数部分。每一轮都做三件事：

```text
余数 * 10
拿它去除以 denominator，得到下一位小数
再更新余数
```

`1 / 6` 的过程：

```text
余数 1
1 * 10 = 10
10 // 6 = 1    小数第 1 位是 1
10 % 6 = 4     新余数是 4

余数 4
4 * 10 = 40
40 // 6 = 6    小数第 2 位是 6
40 % 6 = 4     新余数还是 4
```

余数 `4` 再次出现，说明从这里开始会无限重复：

```text
0.16666...
```

所以答案是：

```text
0.1(6)
```

---

## 为什么看余数，而不是看小数位

长除法里，**余数决定后面所有的小数位**。

如果某一轮的余数和之前某一轮相同，那么从这一轮开始，后面的计算过程就会完全重复。

比如 `1 / 6`：

```text
第一次出现余数 4 时，算出小数位 6，下一轮余数还是 4
第二次出现余数 4 时，接下来还会算出 6，再得到余数 4
```

所以：

```text
余数重复 => 小数循环
```

这题最关键的一句话就是：

```text
用余数定位循环节开始的位置。
```

---

## 方法一：长除法 + 列表线性查找重复余数

### 思路

先按长除法生成小数位。

同时用一个列表保存每次出现过的余数：

```python
remainders = []
```

每次进入新一轮之前，先看当前余数是否出现过：

```text
如果没出现过：继续算下一位
如果出现过：说明循环节开始了
```

循环节开始的位置，就是这个余数第一次出现的位置。

### 用 `1 / 6` 走一遍

```text
整数部分：0
初始余数：1
```

| 当前余数 | 是否见过 | 小数位 | 新余数 | 小数结果 |
| --- | --- | --- | --- | --- |
| 1 | 没见过 | 1 | 4 | 1 |
| 4 | 没见过 | 6 | 4 | 16 |
| 4 | 见过 | - | - | 1(6) |

最终：

```text
0.1(6)
```

### 代码

```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        negative = (numerator < 0) != (denominator < 0)
        numerator = abs(numerator)
        denominator = abs(denominator)

        sign = "-" if negative else ""
        integer = numerator // denominator
        remainder = numerator % denominator

        if remainder == 0:
            return sign + str(integer)

        digits = []
        remainders = []

        while remainder != 0:
            if remainder in remainders:
                start = remainders.index(remainder)
                digits.insert(start, "(")
                digits.append(")")
                break

            remainders.append(remainder)
            remainder *= 10
            digits.append(str(remainder // denominator))
            remainder %= denominator

        return sign + str(integer) + "." + "".join(digits)
```

### 评价

这个方法很接近直觉：

```text
把见过的余数按顺序存起来；
如果余数重复，就找到它第一次出现的位置。
```

缺点是：

```python
remainder in remainders
remainders.index(remainder)
```

都是线性查找。

如果循环节很长，每一轮都在线性列表里找一次，整体会变慢。

复杂度：

- 时间复杂度：`O(k^2)`，`k` 是小数部分生成的位数
- 空间复杂度：`O(k)`

下一步优化很自然：

```text
既然要快速查一个余数第一次出现在哪里，那就用哈希表。
```

---

## 方法二：长除法 + 哈希表记录余数位置（面试主推）

### 核心思路

把方法一的列表换成哈希表：

```python
seen = {}
```

它记录：

```text
余数 -> 这个余数第一次出现时，对应结果字符串的位置
```

为什么要记录“结果字符串的位置”？

因为一旦余数重复，就要在这个位置插入左括号：

```text
0.1 6
   ↑
如果 6 从这里开始循环，就要插入 "("
```

代码里用列表 `res` 拼字符串：

```python
res = [sign + str(integer), "."]
```

每次在生成下一位小数之前，记录：

```python
seen[remainder] = len(res)
```

意思是：

```text
如果这个余数以后再次出现，循环节就从当前 res 的位置开始。
```

### 用 `1 / 6` 走一遍

初始：

```text
res = ["0", "."]
remainder = 1
seen = {}
```

第一轮，余数 `1` 没见过：

```text
seen[1] = len(res) = 2
```

然后算下一位：

```text
1 * 10 = 10
10 // 6 = 1
10 % 6 = 4
```

得到：

```text
res = ["0", ".", "1"]
remainder = 4
```

第二轮，余数 `4` 没见过：

```text
seen[4] = len(res) = 3
```

然后算下一位：

```text
4 * 10 = 40
40 // 6 = 6
40 % 6 = 4
```

得到：

```text
res = ["0", ".", "1", "6"]
remainder = 4
```

第三轮，余数 `4` 见过了：

```text
seen[4] = 3
```

说明循环节从 `res[3]` 开始，也就是数字 `6` 开始。

所以插入括号：

```text
res = ["0", ".", "1", "(", "6", ")"]
```

最终：

```text
0.1(6)
```

### 面试代码

```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        negative = (numerator < 0) != (denominator < 0)
        numerator = abs(numerator)
        denominator = abs(denominator)

        sign = "-" if negative else ""
        integer = numerator // denominator
        remainder = numerator % denominator

        if remainder == 0:
            return sign + str(integer)

        res = [sign + str(integer), "."]
        seen = {}

        while remainder != 0:
            if remainder in seen:
                start = seen[remainder]
                res.insert(start, "(")
                res.append(")")
                break

            seen[remainder] = len(res)

            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(res)
```

### 关键点

#### 1. 为什么 `numerator == 0` 要先返回

如果分子是 0，不管分母是正是负，答案都是：

```text
0
```

不应该返回：

```text
-0
```

所以一开始直接处理：

```python
if numerator == 0:
    return "0"
```

#### 2. 为什么先处理符号

符号只影响最终结果，不影响长除法本身。

所以先判断结果是否为负：

```python
negative = (numerator < 0) != (denominator < 0)
```

然后统一用正数做除法：

```python
numerator = abs(numerator)
denominator = abs(denominator)
```

这样主体逻辑会干净很多。

#### 3. 为什么余数为 0 就结束

如果：

```python
remainder == 0
```

说明除尽了，是有限小数或整数。

比如：

```text
1 / 2 = 0.5
```

算到余数为 0，就可以直接结束，不需要括号。

#### 4. 为什么哈希表存的是 `len(res)`

假设当前余数是 `r`。

从这个余数开始，下一步会生成一个新的小数位。

所以如果 `r` 未来再次出现，循环节应该从“当前将要生成的小数位”开始。

而这个位置正好是：

```python
len(res)
```

因此：

```python
seen[remainder] = len(res)
```

#### 5. 为什么余数重复就插括号

因为长除法下一步完全由余数决定。

如果余数重复，后面产生的小数位也会重复。

所以：

```python
start = seen[remainder]
res.insert(start, "(")
res.append(")")
```

### 复杂度

- 时间复杂度：`O(k)`，`k` 是小数部分生成的位数
- 空间复杂度：`O(k)`

### 面试里怎么讲

可以这样说：

```text
我先处理符号和整数部分。

如果余数为 0，说明能整除，直接返回。

否则进入小数部分的长除法：
每次把余数乘 10，得到下一位小数，再更新余数。

循环小数的判断关键是余数。
因为余数决定后续所有计算，如果同一个余数第二次出现，后面的数字就会从第一次出现的位置开始循环。

所以我用哈希表记录每个余数第一次出现时在结果数组中的位置。
一旦余数重复，就在对应位置插入左括号，最后追加右括号。
```

---

## 总结

| 方法 | 思路 | 时间复杂度 | 空间复杂度 | 评价 |
| --- | --- | --- | --- | --- |
| 方法一 | 长除法 + 列表找重复余数 | `O(k^2)` | `O(k)` | 直观，但查找慢 |
| 方法二 | 长除法 + 哈希表记录余数位置 | `O(k)` | `O(k)` | 面试主推 |

最适合面试的是 **方法二：长除法 + 哈希表记录余数位置**。

真正要记住的是：

```text
不是数字重复就括号；
是余数重复，说明后续长除法过程重复。
```
