# LeetCode 13: 罗马数字转整数 (Roman to Integer) 复盘总结

## 1. 题目核心
罗马数字由 7 个不同的符号表示：`I`, `V`, `X`, `L`, `C`, `D` 和 `M`。
通常情况下，较大的数字在左边，较小的数字在右边。但存在**减法规则**：
- `I` 在 `V` 或 `X` 左边：4, 9
- `X` 在 `L` 或 `C` 左边：40, 90
- `C` 在 `D` 或 `M` 左边：400, 900

---

## 2. 解题核心规律
无论正序还是倒序遍历，判断加减的关键在于**当前位与相邻位的数值关系**。

### 规律：
- **正序遍历**：如果当前字符对应的数值 **小于** 右边字符的数值，则**减去**当前值；否则**加上**当前值。
- **倒序遍历**：如果当前字符对应的数值 **小于** 右边已处理的最大数值（或上一个数值），则**减去**当前值；否则**加上**当前值。

---

## 3. 代码实现 (Python)

### 方法一：正序遍历 (你采用的最优解)
这种方法最直观，但需要注意数组越界处理。

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        sym_to_val = {
            "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1
        }
        res = 0
        n = len(s)
        for i in range(n):
            # 核心逻辑：偷看右边一位
            if i + 1 < n and sym_to_val[s[i]] < sym_to_val[s[i+1]]:
                res -= sym_to_val[s[i]]
            else:
                res += sym_to_val[s[i]]
        return res
```

### 方法二：倒序遍历 (进阶写法)
不需要处理 `i+1 < n` 的越界判断，逻辑更纯粹。

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        sym_to_val = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        res = 0
        last_val = 0
        for char in reversed(s):
            curr_val = sym_to_val[char]
            if curr_val < last_val:
                res -= curr_val
            else:
                res += curr_val
                last_val = curr_val # 更新“阻挡位”
        return res
```

---

## 4. 复杂度分析
- **时间复杂度**: $O(n)$ - 只需要扫描一遍字符串。
- **空间复杂度**: $O(1)$ - 哈希表大小固定（7个字符），仅需常数级额外空间。

---

## 5. 易错点/经验总结
1. **边界检查**：正序遍历时，一定要用 `i + 1 < len(s)` 确保不会报 `IndexError`。
2. **理解特殊规则**：不要试图在哈希表里硬编码 `IV`, `IX` 等组合（虽然也可以，但不够优雅），理解“左小右大即为减”才是这道题的算法精髓。
3. **扩展性**：如果题目增加了新的符号，只要维护 `sym_to_val` 字典即可。

---
*恭喜完成 LeetCode 第 13 题！*
