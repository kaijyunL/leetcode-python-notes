# LeetCode 28. 找出字符串中第一个匹配项的下标 (Find the Index of the First Occurrence in a String)

这道题是经典的字符串匹配问题。我们需要在主串 `haystack` 中寻找子串 `needle` 第一次出现的位置。

---

## 循序渐进解法

### 1. 暴力匹配法 (Brute Force)
这是最直观的方法。我们从主串的第一个字符开始，逐个检查以该字符开头的子串是否与目标串 `needle` 相等。

- **逻辑**：
    1. 遍历 `haystack`，索引范围为 `0` 到 `len(haystack) - len(needle)`。
    2. 对于每个位置 `i`，截取长度为 `len(needle)` 的子串进行比较。
    3. 如果匹配成功，直接返回当前索引 `i`。
    4. 如果遍历结束仍未找到，返回 `-1`。
- **复杂度**：
    - 时间复杂度：$O(n \times m)$，其中 $n$ 是 `haystack` 的长度，$m$ 是 `needle` 的长度。
    - 空间复杂度：$O(1)$。
- **适用场景**：数据规模较小时，简单且有效。

### 2. Python 内置函数 (Built-in)
在实际工程中，除非面试考察算法原理，否则推荐直接使用语言提供的内置高效实现。

- **`haystack.find(needle)`**：
    - 返回第一个匹配项的下标，找不到则返回 `-1`。
- **`haystack.rfind(needle)`**：
    - 返回**最后一个**（Right-side）匹配项的下标，找不到则返回 `-1`。
- **指定位置查找**：
    - `haystack.find(needle, start_index)`：从 `start_index` 以后开始查找。
- **原理**：Python 的 `find` 系列方法在底层使用高效的 C 实现，采用了类似 Boyer-Moore 和 Horspool 的混合优化算法，性能极佳。

### 3. 如何查找“所有”匹配项？
Python 字符串没有直接的 `find_all` 方法，通常有两种实现方式：

1.  **正则法 (推荐)**：使用 `re.finditer`。
    ```python
    import re
    indices = [m.start() for m in re.finditer("needle", "haystack_needle_needle")]
    ```
2.  **循环偏移法**：利用 `find` 的第二个参数不断更新起始位置。
    ```python
    idx = s.find(needle)
    while idx != -1:
        # 处理 idx
        idx = s.find(needle, idx + 1)
    ```

### 4. KMP 算法 (Knuth-Morris-Pratt) —— 最优解
KMP 的核心思想是：**当出现不匹配时，利用已经匹配过的部分信息，避免回溯主串指针，尽可能多地向后滑动模式串。**

- **关键概念：前缀表 (LPS Array)**：
    - `lps[i]` 表示 `needle[0...i]` 中，最长的相等的前缀和后缀的长度。
    - 例如，`needle = "aabaa"`：
        - `a` -> 0
        - `aa` -> 1
        - `aab` -> 0
        - `aaba` -> 1
        - `aabaa` -> 2
- **逻辑**：
    1. **预处理**：计算 `needle` 的前缀表 `next`。
    2. **匹配过程**：在主串中匹配，当 `haystack[i] != needle[j]` 时，根据 `next[j-1]` 跳转 `j` 指针，而 `i` 指针不回溯。
- **复杂度**：
    - 时间复杂度：$O(n + m)$，预处理模式串 $O(m)$，遍历主串 $O(n)$。
    - 空间复杂度：$O(m)$，用于存储前缀表。

---

## 文件列表
- [solution1_brute_force.py](file:///Users/work/Downloads/for_myself/codes/%E5%AD%97%E7%AC%A6%E4%B8%B2/05_q28/solution1_brute_force.py): 暴力匹配解法
- [solution2_builtin.py](file:///Users/work/Downloads/for_myself/codes/%E5%AD%97%E7%AC%A6%E4%B8%B2/05_q28/solution2_builtin.py): 使用 Python 内置函数
- [solution3_kmp.py](file:///Users/work/Downloads/for_myself/codes/%E5%AD%97%E7%AC%A6%E4%B8%B2/05_q28/solution3_kmp.py): KMP 算法最优解

---

## 常见面试 Q&A

**Q: 这道题是 Easy，为什么要学 KMP 这么难的算法？**  
A: 因为它的暴力解法确实是 Easy，但 KMP 是为了考察你对字符串匹配底层原理、前缀表（LPS）以及如何利用已知信息跳过重复计算的理解。

**Q: 面试中直接写 `find()` 可以吗？**  
A: 除非面试官允许或题目没限制空间/时间复杂度。通常建议先写出暴力解，然后口头提出 KMP 优化方案。
