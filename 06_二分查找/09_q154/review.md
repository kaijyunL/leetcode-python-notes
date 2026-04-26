# LeetCode 154. 寻找旋转排序数组中的最小值 II

## 题目理解

给你一个旋转后的升序数组，返回数组中的最小值。

和第 153 题相比，这题允许重复元素。

例如：

```text
nums = [2, 2, 2, 0, 1]
```

返回：

```text
0
```

---

## 方法一：线性扫描

### 思路

从左到右遍历数组，维护当前见过的最小值。

遍历结束后返回最小值。

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
06_二分查找/09_q154/linear_scan.py
```

---

## 方法二：带重复元素的二分查找

第 154 题可以看成第 153 题的重复元素版本。

第 153 题里，我们比较：

```python
nums[mid]
nums[right]
```

如果：

```python
nums[mid] > nums[right]
```

说明最小值一定在 `mid` 右边。

如果：

```python
nums[mid] < nums[right]
```

说明最小值在左边，或者 `mid` 本身就是最小值。

第 154 题多了重复元素，所以还会出现：

```python
nums[mid] == nums[right]
```

这时不能判断最小值在哪边。

---

## 重复元素带来的问题

例如：

```text
nums = [10, 1, 10, 10, 10]
```

初始：

```text
left = 0
right = 4
mid = 2
```

此时：

```text
nums[mid] = 10
nums[right] = 10
```

因为二者相等，所以没法判断：

```text
最小值在 mid 左边？
还是在 mid 右边？
```

这时只能收缩右边界：

```python
right -= 1
```

为什么可以丢掉 `right`？

因为：

```python
nums[mid] == nums[right]
```

即使 `nums[right]` 是一个最小值，`nums[mid]` 也和它一样小，所以丢掉 `right` 不会丢掉最小值这个答案。

---

## 最佳写法

核心代码：

```python
while left < right:
    mid = (left + right) // 2

    if nums[mid] > nums[right]:
        left = mid + 1
    elif nums[mid] < nums[right]:
        right = mid
    else:
        right -= 1

return nums[left]
```

这段逻辑可以分成三种情况：

```text
1. nums[mid] > nums[right]
   最小值一定在 mid 右边
   left = mid + 1

2. nums[mid] < nums[right]
   最小值在左边，或者 mid 本身就是最小值
   right = mid

3. nums[mid] == nums[right]
   无法判断最小值在哪边，但可以安全丢掉 right
   right -= 1
```

---

## 为什么不能用第 153 题的 nums[-1] 边界模板

第 153 题没有重复元素时，可以写成：

```python
if nums[mid] > nums[-1]:
    left = mid + 1
else:
    right = mid - 1

return nums[right + 1]
```

但第 154 题有重复元素，这个写法会出错。

例如：

```text
nums = [2, 2, 2, 0, 1, 2]
```

这里：

```text
nums[-1] = 2
```

判断：

```python
nums[i] > nums[-1]
```

结果是：

```text
nums:   2      2      2      0      1      2
check: False  False  False  False  False  False
```

它不再是：

```text
True True True False False
```

所以 `right + 1` 会返回下标 `0`，得到 `2`，但真正的最小值是 `0`。

因此第 154 题不要强套固定 `nums[-1]` 的边界模板，最佳写法还是比较当前区间里的：

```python
nums[mid]
nums[right]
```

---

## 和第 153 题的关系

第 153 题：

```python
if nums[mid] > nums[right]:
    left = mid + 1
else:
    right = mid
```

第 154 题：

```python
if nums[mid] > nums[right]:
    left = mid + 1
elif nums[mid] < nums[right]:
    right = mid
else:
    right -= 1
```

所以第 154 题可以理解成：

```text
第 153 题 + nums[mid] == nums[right] 时收缩右边界
```

---

## 为什么最坏是 O(n)

如果数组里有大量重复元素，例如：

```text
nums = [1, 1, 1, 1, 1, 1]
```

每一轮都可能遇到：

```python
nums[mid] == nums[right]
```

这时只能：

```python
right -= 1
```

每次只缩小一格，所以最坏时间复杂度是：

```text
O(n)
```

但如果重复元素不多，大多数时候仍然可以每次丢掉一半区间，平均表现接近：

```text
O(log n)
```

---

## 面试推荐讲法

1. 这题是第 153 题的重复元素版本。
2. 仍然比较 `nums[mid]` 和 `nums[right]`。
3. 如果 `nums[mid] > nums[right]`，最小值一定在右边。
4. 如果 `nums[mid] < nums[right]`，最小值在左边，或者 `mid` 本身就是最小值。
5. 如果二者相等，无法判断方向，但可以丢掉一个重复的右边界。
6. 因为重复元素可能导致每次只缩小一格，所以最坏复杂度是 `O(n)`。

### 复杂度

平均时间复杂度：

```text
O(log n)
```

最坏时间复杂度：

```text
O(n)
```

空间复杂度：

```text
O(1)
```

代码见：

```text
06_二分查找/09_q154/optimal_solution.py
```
