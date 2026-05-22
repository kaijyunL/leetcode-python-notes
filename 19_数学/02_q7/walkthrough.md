# 逐步掌握：7. 整数反转 (Reverse Integer)

解决这个问题的关键不是单纯地反转数字，而是**在有限的 32 位环境下安全地处理潜在的溢出**。

---

### 第一步：最基础的反转逻辑（数学法）

如果不考虑溢出，反转一个数字的标准做法是利用**取模 (`%`)** 和 **整除 (`//`)**。

```python
res = 0
while x != 0:
    digit = x % 10  # 取出最后一位
    x //= 10        # 去掉最后一位
    res = res * 10 + digit  # 拼接到结果末尾
```

**原理图解：**
输入 `123`：
1. `digit = 3`, `x = 12`, `res = 0 * 10 + 3 = 3`
2. `digit = 2`, `x = 1`,  `res = 3 * 10 + 2 = 32`
3. `digit = 1`, `x = 0`,  `res = 32 * 10 + 1 = 321`

---

### 第二步：处理负数

Python 的 `%` 在处理负数时和 C++/Java 有所不同（例如 `-123 % 10` 在 Python 中是 `7` 而不是 `-3`）。
**最简单稳妥的办法**：先记录符号，把数字转为正数处理，最后再还原符号。

```python
is_negative = x < 0
x = abs(x)
# ... 进行上面第一步的逻辑 ...
return -res if is_negative else res
```

---

### 第三步：核心挑战 —— 处理 32 位溢出

题目有一个关键限制：**假设环境不允许存储 64 位整数**。
在 32 位环境下，由于我们无法直接得到 `res * 10 + digit` 后的结果再判断是否溢出（因为这时候已经溢出了），我们必须**在执行乘法之前**进行预判。

**32 位有符号整数范围：** `[-2,147,483,648, 2,147,483,647]`。

#### 溢出判断逻辑：
我们要判断 `res * 10 + digit <= INT_MAX` 是否成立。
这等价于判断：
`res > (INT_MAX - digit) // 10` 是否成立。如果成立，就说明下一步执行 `res * 10 + digit` **一定会溢出**。

---

### 第四步：最终优化代码

结合以上所有点，我们得到最佳解法：

```python
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        res = 0
        is_negative = x < 0
        num = abs(x)
        
        while num != 0:
            digit = num % 10
            num //= 10
            
            # 溢出预检查
            if is_negative:
                # 目标是最终结果 -(res * 10 + digit) >= INT_MIN
                # 等效于 res * 10 + digit <= 2147483648
                if res > (2**31 - digit) // 10:
                    return 0
            else:
                # 目标是 res * 10 + digit <= INT_MAX
                if res > (INT_MAX - digit) // 10:
                    return 0
            
            res = res * 10 + digit
            
        return -res if is_negative else res
```

### 进阶思考：为什么 Python 刷题时有时直接判断结果？
在 Python 中，整数是无限精度的，所以 `res * 10 + digit` 永远不会报错。很多面试官会接受你在最后一步判断 `res > INT_MAX`。但为了模拟真实底层环境（如 C++/Java），**预检查逻辑**才是展现水平的地方。
