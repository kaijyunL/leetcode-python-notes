# LeetCode 4. 寻找两个正序数组的中位数

## 题目理解

给你两个已经升序排列的数组 `nums1` 和 `nums2`。

要求返回这两个数组合并后的中位数。

例如：

```text
nums1 = [1, 3]
nums2 = [2]
```

合并后是：

```text
[1, 2, 3]
```

中位数是：

```text
2
```

题目要求时间复杂度是：

```text
O(log(m + n))
```

所以不能只停留在合并数组。

---

## 方法一：合并两个有序数组

### 思路

像归并排序的 merge 步骤一样，用两个指针合并两个有序数组。

合并完成后，根据总长度取中位数。

如果总长度是奇数：

```python
return merged[n // 2]
```

如果总长度是偶数：

```python
return (merged[n // 2 - 1] + merged[n // 2]) / 2
```

### 复杂度

时间复杂度：

```text
O(m + n)
```

空间复杂度：

```text
O(m + n)
```

代码见：

```text
06_二分查找/10_q4/linear_scan.py
```

---

## 方法二：二分查找分割点

这是面试最推荐的解法。

### 核心思路

我们不真的合并数组，而是想象在两个数组中各切一刀。

例如：

```text
nums1 = [1, 3, 8]
nums2 = [7, 9, 10, 11]
```

某次切分可能是：

```text
nums1: [1, 3] | [8]
nums2: [7]    | [9, 10, 11]
```

左半部分是：

```text
[1, 3, 7]
```

右半部分是：

```text
[8, 9, 10, 11]
```

如果满足：

```text
左半部分所有数 <= 右半部分所有数
```

那中位数就只和边界上的几个数有关。

---

## 分割点如何定义

设：

```text
i = nums1 左边取多少个数
j = nums2 左边取多少个数
```

我们希望左半部分长度固定为：

```python
total_left = (m + n + 1) // 2
```

所以：

```python
j = total_left - i
```

也就是说，只要确定了 `i`，`j` 就跟着确定。

所以我们只需要在 `nums1` 上二分查找 `i`。

为了让二分范围更小，一开始要保证：

```python
len(nums1) <= len(nums2)
```

也就是始终在较短数组上二分。

---

## 正确分割的条件

切分之后，四个边界值是：

```text
nums1_left   = nums1[i - 1]
nums1_right  = nums1[i]
nums2_left   = nums2[j - 1]
nums2_right  = nums2[j]
```

要让左半部分全部小于等于右半部分，只需要满足：

```python
nums1_left <= nums2_right
nums2_left <= nums1_right
```

为什么只看这四个数？

因为两个数组本身已经有序：

```text
nums1 左边最大值是 nums1_left
nums1 右边最小值是 nums1_right
nums2 左边最大值是 nums2_left
nums2 右边最小值是 nums2_right
```

所以只要两个数组交叉边界也不冲突，整个左右分割就正确。

---

## 边界怎么处理

如果 `i == 0`，说明 `nums1` 左边没有元素。

这时：

```python
nums1_left = -inf
```

如果 `i == m`，说明 `nums1` 右边没有元素。

这时：

```python
nums1_right = inf
```

`nums2` 同理。

这样可以避免写很多额外的边界分支。

---

## 找到正确分割后如何返回

如果总长度是奇数：

```python
return max(nums1_left, nums2_left)
```

因为左半部分会比右半部分多一个元素，中位数就是左半部分最大值。

如果总长度是偶数：

```python
left_max = max(nums1_left, nums2_left)
right_min = min(nums1_right, nums2_right)
return (left_max + right_min) / 2
```

中位数是左半部分最大值和右半部分最小值的平均数。

---

## 如何移动二分边界

如果：

```python
nums1_left > nums2_right
```

说明 `nums1` 左边拿多了。

要让 `i` 变小：

```python
right = i - 1
```

否则说明 `nums1` 左边拿少了。

要让 `i` 变大：

```python
left = i + 1
```

---

## 最佳写法

```python
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        total_left = (m + n + 1) // 2

        left = 0
        right = m

        while left <= right:
            i = (left + right) // 2
            j = total_left - i

            nums1_left = float("-inf") if i == 0 else nums1[i - 1]
            nums1_right = float("inf") if i == m else nums1[i]
            nums2_left = float("-inf") if j == 0 else nums2[j - 1]
            nums2_right = float("inf") if j == n else nums2[j]

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (m + n) % 2 == 1:
                    return float(max(nums1_left, nums2_left))

                left_max = max(nums1_left, nums2_left)
                right_min = min(nums1_right, nums2_right)
                return (left_max + right_min) / 2

            if nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1
```

代码见：

```text
06_二分查找/10_q4/optimal_solution.py
```

---

## 例子

```text
nums1 = [1, 3, 8]
nums2 = [7, 9, 10, 11]
```

总长度是：

```text
7
```

左半部分应该有：

```text
(7 + 1) // 2 = 4
```

也就是：

```text
total_left = 4
```

开始在 `nums1` 上二分。

### 第 1 轮

```text
left = 0
right = 3
i = 1
j = 3
```

切分：

```text
nums1: [1] | [3, 8]
nums2: [7, 9, 10] | [11]
```

边界：

```text
nums1_left = 1
nums1_right = 3
nums2_left = 10
nums2_right = 11
```

此时：

```text
nums2_left > nums1_right
```

说明 `nums1` 左边拿少了，要让 `i` 变大：

```python
left = i + 1
```

### 第 2 轮

```text
left = 2
right = 3
i = 2
j = 2
```

切分：

```text
nums1: [1, 3] | [8]
nums2: [7, 9] | [10, 11]
```

边界：

```text
nums1_left = 3
nums1_right = 8
nums2_left = 9
nums2_right = 10
```

仍然：

```text
nums2_left > nums1_right
```

所以继续让 `i` 变大。

### 第 3 轮

```text
left = 3
right = 3
i = 3
j = 1
```

切分：

```text
nums1: [1, 3, 8] | []
nums2: [7] | [9, 10, 11]
```

边界：

```text
nums1_left = 8
nums1_right = inf
nums2_left = 7
nums2_right = 9
```

满足：

```text
nums1_left <= nums2_right
nums2_left <= nums1_right
```

因为总长度是奇数，中位数是左半部分最大值：

```python
max(8, 7) = 8
```

返回：

```text
8
```

---

## 面试推荐讲法

1. 先说可以合并两个数组，复杂度是 `O(m + n)`。
2. 题目要求对数复杂度，所以不能真正合并。
3. 把问题转化为：在两个数组中找到一个分割，使左半部分长度等于右半部分，且左边所有数小于等于右边所有数。
4. 只需要在较短数组上二分一个分割点 `i`，另一个分割点 `j` 由总长度决定。
5. 正确分割条件是 `nums1_left <= nums2_right and nums2_left <= nums1_right`。
6. 找到后根据总长度奇偶返回中位数。

### 复杂度

时间复杂度：

```text
O(log(min(m, n)))
```

空间复杂度：

```text
O(1)
```
