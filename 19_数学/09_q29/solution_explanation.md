# LeetCode 29. 两数相除（Divide Two Integers）解析

## 题目描述

给定两个整数 `dividend` 和 `divisor`，返回它们相除后的商。

要求：

- 不能使用乘法 `*`
- 不能使用除法 `/`
- 不能使用取模 `%`
- 结果只保留整数部分，向 0 截断
- 如果结果溢出 32 位有符号整数范围，返回 `2^31 - 1`

32 位范围是：

```text
INT_MIN = -2^31     = -2147483648
INT_MAX =  2^31 - 1 =  2147483647
```

例子：

```text
10 / 3  -> 3
7 / -3  -> -2
0 / 1   -> 0
1 / 1   -> 1
```

注意 `7 / -3` 的结果是 `-2`，不是 `-3`。

因为这题要求**向 0 截断**：

```text
7 / -3 = -2.333...
向 0 截断后是 -2
```

---

## 先理解题意

除法本质上是在问：

```text
dividend 里面能装下多少个 divisor？
```

比如：

```text
10 / 3
```

可以理解成：

```text
10 里能减掉几个 3？

10 - 3 = 7   第 1 个
7  - 3 = 4   第 2 个
4  - 3 = 1   第 3 个
1 不够再减 3

所以商是 3
```

这就是暴力减法的直觉。

但如果是：

```text
2147483647 / 1
```

一个一个减就要减 20 多亿次，肯定不行。

所以这题的核心优化是：

```text
不要一次只减 1 个 divisor，要一次减掉 2 个、4 个、8 个、16 个 divisor。
```

这和上一题 Q50 快速幂很像：

- Q50 是把指数拆成 `1, 2, 4, 8, ...`
- Q29 是把商也拆成 `1, 2, 4, 8, ...`

---

## 先处理符号和溢出

正式做减法之前，先把符号问题拿掉。

比如：

```text
10 / 3    -> 正数
10 / -3   -> 负数
-10 / 3   -> 负数
-10 / -3  -> 正数
```

也就是说：

```python
negative = (dividend < 0) != (divisor < 0)
```

两个数一正一负，结果就是负数。

然后统一用绝对值做计算：

```python
dividend_abs = abs(dividend)
divisor_abs = abs(divisor)
```

算出正商以后，再根据 `negative` 决定要不要取负。

还要提前处理唯一的溢出情况：

```text
-2147483648 / -1 = 2147483648
```

这个结果超过了 `INT_MAX = 2147483647`，所以要返回 `2147483647`。

---

## 方法一：暴力减法

### 思路

最直接的方法：

```text
只要 dividend_abs >= divisor_abs：
    dividend_abs -= divisor_abs
    quotient += 1
```

比如 `10 / 3`：

```text
剩余 10，减 3，商 +1，剩 7
剩余 7， 减 3，商 +1，剩 4
剩余 4， 减 3，商 +1，剩 1
剩余 1，不够减 3，结束

商 = 3
```

### 代码

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        int_min = -(1 << 31)
        int_max = (1 << 31) - 1

        if dividend == int_min and divisor == -1:
            return int_max

        negative = (dividend < 0) != (divisor < 0)
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)

        quotient = 0
        while dividend_abs >= divisor_abs:
            dividend_abs -= divisor_abs
            quotient += 1

        if negative:
            quotient = -quotient

        return quotient
```

### 评价

这个方法非常好理解。

但它会超时：

```text
2147483647 / 1
```

要循环 2147483647 次。

复杂度：

- 时间复杂度：`O(|quotient|)`
- 空间复杂度：`O(1)`

下一步优化的关键是：

```text
能不能每轮不只减一个 divisor？
```

---

## 方法二：倍增减法

### 核心思路

如果暴力减法每次只减：

```text
1 个 divisor
```

那太慢。

可以每轮尽量减掉：

```text
1 个 divisor
2 个 divisor
4 个 divisor
8 个 divisor
...
```

也就是不断把当前可减的数翻倍：

```text
divisor
divisor * 2
divisor * 4
divisor * 8
...
```

题目不让用乘法，所以用左移：

```python
current <<= 1
multiple <<= 1
```

这里：

```text
current  表示当前准备减掉的总值
multiple 表示 current 里面包含多少个 divisor
```

比如 `43 / 8`：

```text
8 * 1 = 8
8 * 2 = 16
8 * 4 = 32
8 * 8 = 64  太大，不能减
```

所以第一轮最多减掉 32，也就是 4 个 8。

```text
43 - 32 = 11
商 += 4
```

剩下 `11`，还能再减一个 `8`：

```text
11 - 8 = 3
商 += 1
```

最后商是：

```text
4 + 1 = 5
```

也就是：

```text
43 / 8 = 5
```

### 代码

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        int_min = -(1 << 31)
        int_max = (1 << 31) - 1

        if dividend == int_min and divisor == -1:
            return int_max

        negative = (dividend < 0) != (divisor < 0)
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)

        quotient = 0

        while dividend_abs >= divisor_abs:
            current = divisor_abs
            multiple = 1

            while dividend_abs >= (current << 1):
                current <<= 1
                multiple <<= 1

            dividend_abs -= current
            quotient += multiple

        if negative:
            quotient = -quotient

        return quotient
```

### 为什么比暴力快

暴力减法是：

```text
每次只拿走 1 个 divisor
```

倍增减法是：

```text
每次尽量拿走一大块 divisor
```

比如 `100 / 3`：

暴力大概要减 33 次。

倍增减法会先尝试：

```text
3, 6, 12, 24, 48, 96
```

第一轮直接减掉 `96`，商加 `32`，剩下 `4`。

再减一次 `3`，商加 `1`。

总共就几轮。

复杂度：

- 时间复杂度：`O(log^2 N)`，`N = abs(dividend)`
- 空间复杂度：`O(1)`

这个方法已经能通过。

但它每一轮都要从 `divisor` 开始重新倍增一次，还能再写得更直接：从最高位往低位试。

---

## 方法三：从高位到低位扫描（面试主推）

### 核心思路

方法二是在每一轮里从小到大找：

```text
divisor * 1
divisor * 2
divisor * 4
divisor * 8
...
```

方法三反过来：

```text
我直接从最大的 2 的幂开始试。
```

因为 32 位整数最多就 32 个二进制位，所以可以从 `31` 位一路试到 `0` 位：

```text
divisor << 31
divisor << 30
...
divisor << 2
divisor << 1
divisor << 0
```

如果某一档可以减，就说明商里包含这一档：

```text
dividend_abs >= divisor_abs << shift
```

那就：

```text
把这一档从 dividend_abs 里减掉
把 1 << shift 加到 quotient 里
```

### 用 `43 / 8` 走一遍

先看能不能减这些值：

```text
8 << 3 = 64  太大
8 << 2 = 32  可以
8 << 1 = 16
8 << 0 = 8
```

过程：

```text
dividend_abs = 43
divisor_abs = 8
quotient = 0
```

先试 `shift = 2`：

```text
8 << 2 = 32
43 >= 32，可以减

dividend_abs = 43 - 32 = 11
quotient += 1 << 2 = 4
```

再试 `shift = 1`：

```text
8 << 1 = 16
11 < 16，不能减
```

再试 `shift = 0`：

```text
8 << 0 = 8
11 >= 8，可以减

dividend_abs = 11 - 8 = 3
quotient += 1 << 0 = 1
```

最后：

```text
quotient = 4 + 1 = 5
```

答案就是 `5`。

### 代码

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        int_min = -(1 << 31)
        int_max = (1 << 31) - 1

        if dividend == int_min and divisor == -1:
            return int_max

        negative = (dividend < 0) != (divisor < 0)
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)

        quotient = 0

        for shift in range(31, -1, -1):
            if dividend_abs >= (divisor_abs << shift):
                dividend_abs -= divisor_abs << shift
                quotient += 1 << shift

        if negative:
            quotient = -quotient

        if quotient < int_min:
            return int_min
        if quotient > int_max:
            return int_max

        return quotient
```

### 关键变量

```python
divisor_abs << shift
```

表示：

```text
divisor_abs * 2^shift
```

题目不让用乘法，所以用左移。

```python
1 << shift
```

表示：

```text
2^shift
```

如果 `divisor_abs << shift` 可以从当前剩余的 `dividend_abs` 中减掉，就说明商里包含 `2^shift` 这一份。

比如：

```text
43 / 8
```

当发现：

```text
8 << 2 = 32 <= 43
```

就说明：

```text
商至少包含 4 个 8
```

所以：

```python
quotient += 1 << 2
```

也就是商加 `4`。

### 为什么从 31 到 0

题目限制是 32 位整数。

最大绝对值可能是：

```text
abs(-2147483648) = 2147483648 = 2^31
```

所以从第 `31` 位开始试，足够覆盖所有可能的商。

### 容易出错的地方

1. **截断方向是向 0，不是向下取整**

   ```text
   7 / -3 = -2
   ```

   Python 的 `//` 对负数是向下取整：

   ```text
   7 // -3 = -3
   ```

   所以这题不能直接参考 `//` 的行为。

2. **唯一溢出情况要提前处理**

   ```text
   -2147483648 / -1 = 2147483648
   ```

   超过 `INT_MAX`，返回 `2147483647`。

3. **符号最后再加回去**

   主体计算时统一用正数，可以减少很多分支。

4. **不要用 `*`、`/`、`%`**

   倍增用左移：

   ```python
   divisor_abs << shift
   ```

   商加对应的倍数：

   ```python
   quotient += 1 << shift
   ```

### 复杂度

- 时间复杂度：`O(32)`，也可以看作 `O(1)`；如果推广到任意整数，就是 `O(log N)`
- 空间复杂度：`O(1)`

### 面试里怎么讲

可以这样说：

```text
最朴素的做法是不断减 divisor，但当 divisor 很小时会超时。

优化思路是每次减去 divisor 的 2 的幂倍：
divisor, divisor*2, divisor*4, divisor*8...

由于不能用乘法，我用左移表示乘以 2 的幂。

我从高位到低位尝试，如果 dividend 剩余值能减掉 divisor << shift，
说明商里包含 1 << shift，就把这部分减掉，并累加到 quotient。

最后根据 dividend 和 divisor 的符号决定结果正负，并处理 INT_MIN / -1 的溢出。
```

---

## 总结

| 方法 | 思路 | 时间复杂度 | 空间复杂度 | 评价 |
| --- | --- | --- | --- | --- |
| 方法一 | 暴力减法 | `O(|quotient|)` | `O(1)` | 最直观，但会超时 |
| 方法二 | 倍增减法 | `O(log^2 N)` | `O(1)` | 能通过，容易从暴力想到 |
| 方法三 | 高位到低位 bit 扫描 | `O(32)` | `O(1)` | 面试主推 |

最适合面试的是 **方法三：从高位到低位扫描**。

它的核心是：

```text
除法是在找商；
商可以拆成若干个 2 的幂；
用 divisor << shift 判断这一档能不能放进 dividend；
能放就减掉，并把 1 << shift 加进商。
```
