# LeetCode 35. 搜索插入位置

## 题目理解

给你一个升序数组 `nums` 和一个目标值 `target`。

如果 `target` 在数组中，返回它的下标。

如果不在数组中，返回它应该插入的位置，使数组仍然保持升序。

例如：

```text
nums = [1, 3, 5, 6]
target = 5
```

`5` 在数组中，下标是 `2`，返回：

```text
2
```

再比如：

```text
nums = [1, 3, 5, 6]
target = 2
```

`2` 不在数组中，应该插入到 `1` 和 `3` 之间，返回：

```text
1
```

---

## 方法一：线性扫描

### 思路

从左到右遍历数组，找到第一个：

```text
nums[i] >= target
```

的位置。

这个位置就是答案。

如果遍历完整个数组都没找到，说明 `target` 比所有元素都大，应该插入到数组末尾，返回：

```text
len(nums)
```

### 复杂度

时间复杂度：

```text
O(n)
```

空间复杂度：

```text
O(1)
```

代码见：

```text
06_二分查找/01_q35/linear_scan.py
```

---

## 方法二：二分查找

这是最适合面试的方法。

### 核心思路

这题本质上是在找：

```text
第一个大于等于 target 的位置
```

也就是：

```text
first index where nums[index] >= target
```

如果这个位置存在，它就是 `target` 的位置或插入位置。

如果这个位置不存在，说明所有数都小于 `target`，答案就是 `len(nums)`。

### 二分边界

用左闭右闭区间：

```text
left = 0
right = len(nums) - 1
```

循环条件：

```python
while left <= right:
```

每次取中点：

```python
mid = (left + right) // 2
```

如果：

```text
nums[mid] >= target
```

说明答案可能是 `mid`，也可能在 `mid` 左边。

所以收缩右边界：

```python
right = mid - 1
```

如果：

```text
nums[mid] < target
```

说明 `mid` 以及左边都太小了，答案只能在右边。

所以：

```python
left = mid + 1
```

循环结束后，`left` 就是第一个大于等于 `target` 的位置。

### 为什么最后返回 left

循环结束时：

```text
right < left
```

`left` 会停在第一个满足：

```text
nums[left] >= target
```

的位置。

如果 `target` 比所有数都大，`left` 会移动到：

```text
len(nums)
```

这正好是插入到末尾的位置。

### 面试推荐讲法

面试时可以这样讲：

1. 线性扫描可以做，但复杂度是 `O(n)`。
2. 数组有序，所以可以使用二分查找。
3. 这题不是只找等于 `target`，而是找第一个大于等于 `target` 的位置。
4. 如果 `nums[mid] >= target`，说明当前位置可能是答案，继续向左找。
5. 如果 `nums[mid] < target`，说明答案只能在右边。
6. 最后返回 `left`。

### 复杂度

时间复杂度：

```text
O(log n)
```

空间复杂度：

```text
O(1)
```

代码见：

```text
06_二分查找/01_q35/optimal_solution.py
```

---

## 最终建议

面试最推荐：

```text
二分查找：找第一个大于等于 target 的位置
```

关键一句话：

```text
nums[mid] >= target 时往左收缩，nums[mid] < target 时往右查找，最后返回 left。
```
