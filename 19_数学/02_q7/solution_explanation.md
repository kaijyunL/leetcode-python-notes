# LeetCode 7. 整数反转（Reverse Integer）解析

## 题目描述

给你一个 32 位有符号整数 `x`，返回把它的数字部分反转后的结果。

如果反转后超出 32 位有符号整数范围，就返回 `0`。

范围是：

```text
INT_MIN = -2^31
INT_MAX =  2^31 - 1
```

也就是：

```text
[-2147483648, 2147483647]
```

例子：

```text
123 -> 321
-123 -> -321
120 -> 21
1534236469 -> 0
```

最后一个返回 `0`，因为反转后会超过 `2147483647`。

---

## 先理解题意

这题要做两件事：

1. 把整数的数字顺序反过来
2. 判断反转后的结果是否越过 32 位范围

比如：

```text
x = 123
```

反转过程是：

```text
取 3 -> res = 3
取 2 -> res = 32
取 1 -> res = 321
```

对于负数，可以先记录符号，再把绝对值拿出来处理：

```text
-123 -> 123 -> 321 -> -321
```

---

## 方法一：字符串反转

### 思路

最直接的方法是把数字转成字符串。

如果是负数，去掉负号，只反转数字部分，最后再加回负号。

### 代码

```python
class Solution:
    def reverse(self, x: int) -> int:
        int_min = -(1 << 31)
        int_max = (1 << 31) - 1

        sign = -1 if x < 0 else 1
        reversed_num = int(str(abs(x))[::-1]) * sign

        if reversed_num < int_min or reversed_num > int_max:
            return 0
        return reversed_num
```

### 复杂度

- 时间复杂度：`O(n)`，`n` 是数字位数
- 空间复杂度：`O(n)`

### 评价

这个方法最容易写。

但它用了字符串，不是这题最想考的数学反转。

---

## 方法二：数学反转，最后检查溢出

### 思路

不用字符串，直接用 `%` 和 `//` 一位一位取。

取最后一位：

```python
digit = num % 10
```

把这一位接到结果后面：

```python
res = res * 10 + digit
```

去掉最后一位：

```python
num //= 10
```

### 代码

```python
class Solution:
    def reverse(self, x: int) -> int:
        int_min = -(1 << 31)
        int_max = (1 << 31) - 1

        sign = -1 if x < 0 else 1
        num = abs(x)
        res = 0

        while num:
            res = res * 10 + num % 10
            num //= 10

        res *= sign

        if res < int_min or res > int_max:
            return 0
        return res
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

### 评价

这个方法已经是数学解法。

但它是在反转完成后才检查溢出。Python 可以这么写，因为 Python 整数不会溢出。

题目原意是假设环境不能存 64 位整数，所以面试里更推荐方法三：在拼接下一位之前先判断会不会溢出。

---

## 方法三：数学反转，提前检查溢出

### 核心思路

这题最关键的是这一句：

```python
res = res * 10 + digit
```

如果执行完这句才发现溢出，在 C++/Java 这种固定整数语言里已经晚了。

所以要在执行前判断：

```text
res * 10 + digit 是否会超过上限
```

等价改写：

```text
res > (limit - digit) // 10
```

如果这个条件成立，说明下一步拼接一定溢出，直接返回 `0`。

### 面试代码

```python
class Solution:
    def reverse(self, x: int) -> int:
        int_max = (1 << 31) - 1
        negative_limit = 1 << 31

        sign = -1 if x < 0 else 1
        limit = negative_limit if x < 0 else int_max

        num = abs(x)
        res = 0

        while num:
            digit = num % 10
            num //= 10

            if res > (limit - digit) // 10:
                return 0

            res = res * 10 + digit

        return sign * res
```

### 变量说明

```python
int_max = (1 << 31) - 1
```

正数最大值：

```text
2147483647
```

```python
negative_limit = 1 << 31
```

负数绝对值最大可以到：

```text
2147483648
```

因为：

```text
INT_MIN = -2147483648
```

所以：

```python
limit = negative_limit if x < 0 else int_max
```

意思是：

- 原数是正数，反转结果最多是 `2147483647`
- 原数是负数，反转结果的绝对值最多是 `2147483648`

### 用 `123` 走一遍

初始：

```text
num = 123
res = 0
```

第 1 轮：

```text
digit = 3
num = 12
res = 0 * 10 + 3 = 3
```

第 2 轮：

```text
digit = 2
num = 1
res = 3 * 10 + 2 = 32
```

第 3 轮：

```text
digit = 1
num = 0
res = 32 * 10 + 1 = 321
```

返回：

```text
321
```

### 溢出判断怎么看

假设正数场景：

```text
limit = 2147483647
```

下一步要执行：

```python
res = res * 10 + digit
```

为了不溢出，必须满足：

```text
res * 10 + digit <= limit
```

移项得到：

```text
res <= (limit - digit) / 10
```

用整数判断就是：

```python
res > (limit - digit) // 10
```

如果大于，说明拼接下一位会越界。

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

---

## 哪个方法最适合面试

最适合面试的是 **方法三：数学反转，提前检查溢出**。

原因：

- 不用字符串
- 不依赖 Python 大整数特性
- 符合题目“32 位整数范围”的考点
- 代码仍然不长，现场能写出来

面试里可以这样说：

```text
我先记录符号，把 x 转成正数处理。
每次用 num % 10 取最后一位，用 num //= 10 去掉最后一位。
拼接到 res 前，先判断 res * 10 + digit 是否会超过 32 位边界。
如果会溢出，直接返回 0。
最后根据原符号返回结果。
```

---

## 总结

- 方法一：字符串反转
  - 最简单
  - 但不是这题主要考点

- 方法二：数学反转，最后检查溢出
  - Python 可用
  - 但不符合题目对固定整数环境的考察

- 方法三：数学反转，提前检查溢出
  - 面试主推
  - 时间 `O(n)`，空间 `O(1)`
