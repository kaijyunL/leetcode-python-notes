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
最后一个小于 target 的位置
```

找到这个位置后，插入位置就是它的右边：

```text
right + 1
```

如果没有任何数小于 `target`，`right` 会停在 `-1`，答案就是 `0`。

如果所有数都小于 `target`，`right` 会停在 `len(nums) - 1`，答案就是 `len(nums)`。

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
nums[mid] < target
```

说明 `mid` 是一个满足条件的位置，但可能还有更靠右的位置也小于 `target`。

所以继续往右找：

```python
left = mid + 1
```

如果：

```text
nums[mid] >= target
```

说明 `mid` 太大，最后一个小于 `target` 的位置只能在左边。

所以：

```python
right = mid - 1
```

循环结束后，`right` 就是最后一个小于 `target` 的位置。

### 为什么最后返回 right + 1

循环结束时：

```text
right < left
```

`right` 会停在最后一个满足：

```text
nums[right] < target
```

的位置。

插入位置应该在它的右边，所以返回：

```text
right + 1
```

### 面试推荐讲法

面试时可以这样讲：

1. 线性扫描可以做，但复杂度是 `O(n)`。
2. 数组有序，所以可以使用二分查找。
3. 统一模板：找最后一个满足条件的位置。
4. 这题的条件是 `nums[mid] < target`。
5. 如果满足，就 `left = mid + 1` 继续向右找。
6. 如果不满足，就 `right = mid - 1` 向左收缩。
7. 最后返回 `right + 1`。

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
二分查找：找最后一个小于 target 的位置
```

关键一句话：

```text
nums[mid] < target 时 left = mid + 1，否则 right = mid - 1，最后返回 right + 1。
```
