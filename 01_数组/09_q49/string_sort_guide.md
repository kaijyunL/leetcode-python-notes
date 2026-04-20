# Python 字符串排序解析

在 Python 中，字符串是**不可变的（Immutable）**，这意味着你不能直接修改原字符串。要对字符串进行排序，通常遵循以下三个步骤。

## 核心步骤

1.  **使用 `sorted()` 函数**：将字符串拆分为单个字符并排序，返回一个**列表**。
2.  **使用 `join()` 方法**：将排序后的列表拼接回**字符串**。

---

## 示例代码

```python
s = "leetcode"

# 1. 排序
# sorted(s) 会将 "leetcode" 变成 ['c', 'd', 'e', 'e', 'e', 'l', 'o', 't']
char_list = sorted(s)

# 2. 拼接
# "".join() 将列表中的每一个元素连在一起，中间不加任何东西
sorted_s = "".join(char_list)

print(sorted_s) # 输出: cdeeelor
```

## 常见技巧

### 1. 倒序排列
如果想从大到小排列，可以使用 `reverse=True` 参数：
```python
s = "abc"
res = "".join(sorted(s, reverse=True))
print(res) # 输出: cba
```

### 2. 忽略大小写排序
默认情况下，大写字母（如 'A'）的 ASCII 值小于小写字母（如 'a'），所以大写会排在前面。如果想忽略大小写：
```python
s = "aBc"
res = "".join(sorted(s, key=str.lower))
print(res) # 输出: aBc (或类似逻辑)
```

---

## 为什么 LeetCode 49 题要用这个？
在第 49 题中，字母异位词（如 `eat` 和 `tea`）虽然字母顺序不同，但它们包含的**字母是一模一样**的。
*   `sorted("eat")` -> `['a', 'e', 't']`
*   `sorted("tea")` -> `['a', 'e', 't']`

通过排序并转换回字符串 `"aet"`，我们就可以把它们作为哈希表的同一个 **Key** 来进行归类。
