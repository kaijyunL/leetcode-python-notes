# 两数之和 (Two Sum) 调试记录

## 用户提问
**代码内容：**
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _d = {}
        for i, num in enumerate(nums):
            _d[num] = i
        for i, num in enumerate(nums):
            if target - num in _d:
                return [i, _d[target - num]]
            #_d[num] = i
        return [0, 0]
```
**问题：** 问题出在哪？

---

## 诊断结果
主要问题在于**没有检查查找到的元素是否为当前元素本身**。题目要求不能重复使用同一个下标的数值。

### 错误详情
如果 `target` 正好是某个数（如 `x`）的两倍，且数组中只存在一个 `x`：
1. 第一遍循环会将 `x` 的下标存入字典。
2. 第二遍循环到 `x` 时，计算 `target - x` 得到 `x`。
3. 程序检查字典，发现 `x` 存在，于是返回了 `[当前下标, 当前下标]`。

---

## 修复建议

### 方案一：在两遍循环中增加下标判定
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _d = {}
        for i, num in enumerate(nums):
            _d[num] = i
        
        for i, num in enumerate(nums):
            complement = target - num
            # 关键：检查 _d[complement] 是否就是当前 i
            if complement in _d and _d[complement] != i:
                return [i, _d[complement]]
        return []
```

### 方案二：一遍循环（最优解）
在将数字存入字典**之前**先寻找匹配值，自然避免了重复使用同一个元素。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _d = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in _d:
                return [_d[complement], i]
            _d[num] = i
        return []
```

---
*记录时间：2026-02-23*
