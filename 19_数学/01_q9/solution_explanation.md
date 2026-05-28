# LeetCode 9. 回文数（Palindrome Number）解析

## 题目描述

给你一个整数 `x`，判断它是不是回文数。

回文数指的是：

```text
正着读和反着读都一样
```

例子：

```text
121 -> True
-121 -> False
10 -> False
0 -> True
```

注意：

```text
-121
```

反过来不是 `-121`，而是类似 `121-`，所以负数不是回文数。

---

## 先理解题意

这题最直接的判断方式是：

```text
把数字反过来，看是否等于原数字
```

比如：

```text
1221 反过来还是 1221，所以是回文
123  反过来是 321，所以不是回文
```

问题在于：面试里有时会追问“不转字符串怎么做”。

所以这题可以从字符串法开始，再推进到数学反转。

---

## 方法一：转字符串

### 思路

把整数转成字符串，然后判断字符串是否等于它的反转。

### 代码

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
```

### 复杂度

- 时间复杂度：`O(n)`，`n` 是数字位数
- 空间复杂度：`O(n)`

### 评价

这是最简单的方法。

如果面试官没有限制，能快速写出来。

但如果面试官要求“不转字符串”，就要用后面的数学方法。

---

## 方法二：反转整个整数

### 思路

用数学方式把整个整数反转。

取最后一位：

```python
digit = x % 10
```

把最后一位接到反转结果后面：

```python
reversed_num = reversed_num * 10 + digit
```

去掉原数字最后一位：

```python
x //= 10
```

最后比较：

```python
original == reversed_num
```

### 代码

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        reversed_num = 0

        while x:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return original == reversed_num
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

### 评价

这个方法不需要字符串。

但它会反转整个数字。在 Python 里不会溢出；在 C++、Java 这类固定整数范围语言里，完整反转可能有溢出风险。

所以面试里更推荐方法三：只反转一半。

---

## 方法三：只反转后一半数字

### 核心思路

完整反转没有必要。

判断一个数是不是回文，只需要比较前半部分和后半部分。

比如：

```text
1221
```

可以拆成：

```text
前半部分：12
后半部分反转：12
```

相等，所以是回文。

再比如：

```text
12321
```

中间的 `3` 不影响回文判断。

可以比较：

```text
前半部分：12
后半部分反转后去掉中间位：12
```

### 面试代码

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10
```

### 代码关键点

```python
if x < 0:
```

负数不是回文数。

```python
x % 10 == 0 and x != 0
```

非零数字如果以 `0` 结尾，也不可能是回文。

比如：

```text
10, 100, 120
```

如果它们是回文，开头也必须是 `0`，但整数不会以 `0` 开头。

`0` 本身是回文，所以要排除：

```python
x != 0
```

```python
while x > reversed_half:
```

只反转后一半。

循环过程中：

- `x` 是还没处理的前半部分
- `reversed_half` 是已经反转出来的后半部分

当 `reversed_half >= x` 时，说明已经处理到中间位置了。

### 用 `1221` 走一遍

初始：

```text
x = 1221
reversed_half = 0
```

第 1 轮：

```text
取 x 的最后一位 1
reversed_half = 1
x = 122
```

第 2 轮：

```text
取 x 的最后一位 2
reversed_half = 12
x = 12
```

此时：

```text
x == reversed_half
12 == 12
```

所以是回文。

### 用 `12321` 走一遍

初始：

```text
x = 12321
reversed_half = 0
```

第 1 轮：

```text
reversed_half = 1
x = 1232
```

第 2 轮：

```text
reversed_half = 12
x = 123
```

第 3 轮：

```text
reversed_half = 123
x = 12
```

此时 `reversed_half` 多了一位中间数 `3`。

去掉它：

```text
reversed_half // 10 = 12
```

比较：

```text
x == reversed_half // 10
12 == 12
```

所以是回文。

### 复杂度

- 时间复杂度：`O(n)`，实际只处理一半位数
- 空间复杂度：`O(1)`

---

## 哪个方法最适合面试

最适合面试的是 **方法三：只反转后一半数字**。

原因：

- 不用字符串
- 不反转整个整数，避免固定整数语言里的溢出风险
- 代码短，现场容易写
- 边界清楚：负数、非零且以 0 结尾的数直接返回 `False`

面试里可以这样说：

```text
我不反转整个数字，只反转后半部分。
reversed_half 保存已经反转出来的后半部分，x 保留前半部分。
当 reversed_half >= x 时，说明已经到达中间。
偶数位时比较 x == reversed_half。
奇数位时 reversed_half 会多一个中间位，所以比较 x == reversed_half // 10。
```

---

## 总结

- 方法一：转字符串
  - 最简单
  - 但用了额外字符串空间

- 方法二：反转整个整数
  - 不用字符串
  - 但可能有完整反转溢出问题

- 方法三：只反转后一半数字
  - 面试主推
  - 时间 `O(n)`，空间 `O(1)`
