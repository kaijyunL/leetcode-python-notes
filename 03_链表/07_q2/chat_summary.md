# Python 学习笔记：LeetCode 2. 两数相加

这份文档总结了我们在讨论 **LeetCode 2. 两数相加** 过程中的关键知识点，包括 Python 运算符和代码优化建议。

## 1. Python 基础运算符

在处理数字位运算（如链表加法中的进位和取值）时，常用的两个运算符：

*   **`//` (整除/Floor Division)**：
    *   执行除法并向下取整。
    *   示例：`7 // 3` 得到 `2`。
    *   用途：在加法中用于计算**进位 (carry)**。
*   **`%` (取模/Modulo)**：
    *   返回除法后的余数。
    *   示例：`7 % 3` 得到 `1`。
    *   用途：在加法中用于计算当前位的**值 (digit)**。

## 2. 代码实现方案对比

我们对比了两种 `addTwoNumbers` 的实现：

### 写法 A（分步处理）
```python
while l1 or l2:
    # ... 计算过程 ...
    cur.next = ListNode(total % 10)
    carry = total // 10

if carry:
    cur.next = ListNode(carry)
```
*   **优点**：逻辑直观，符合线性思维。
*   **缺点**：循环外需要额外处理最后的进位。

### 写法 B（推荐：逻辑闭环）
```python
while l1 or l2 or carry:
    # ... 统一处理节点和进位 ...
    carry = total // 10
    digit = total % 10
    curr.next = ListNode(digit)
```
*   **优点**：将 `carry` 纳入循环条件，使得所有进位逻辑（包括最后一位）统一处理，代码更简洁、优雅。

## 3. 进阶 Tip：`divmod()` 内置函数

Python 提供了一个内置函数 `divmod()`，可以在一行内同时获取商和余数。

*   **语法**：`quotient, remainder = divmod(n, d)`
*   **优势**：
    *   **效率**：底层只进行一次除法运算。
    *   **可读性**：代码更简洁。
*   **在加法中的应用**：
    ```python
    carry, val = divmod(v1 + v2 + carry, 10)
    ```

---
*保存时间：2026-02-23*
