# LeetCode 81. 搜索旋转排序数组 II

## 题目理解

给你一个旋转后的升序数组 `nums`，判断 `target` 是否存在。

和第 33 题相比，这题允许重复元素。

例如：

```text
nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
```

返回：

```text
True
```

如果：

```text
target = 3
```

返回：

```text
False
```

---

## 方法一：线性扫描

### 思路

从左到右遍历数组。

如果遇到 `target`，返回 `True`。

如果遍历结束都没遇到，返回 `False`。

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
06_二分查找/08_q81/linear_scan.py
```

---

## 方法二：带重复元素的二分查找

第 81 题可以看成第 33 题的升级版。

第 33 题没有重复元素，所以每轮可以判断：

```python
nums[left] <= nums[mid]
```

如果成立，左半边有序。

否则右半边有序。

但第 81 题有重复元素，会出现无法判断哪一边有序的情况。

---

## 重复元素带来的问题

例如：

```text
nums = [1, 0, 1, 1, 1]
target = 0
```

初始：

```text
left = 0
right = 4
mid = 2
```

此时：

```text
nums[left] = 1
nums[mid] = 1
nums[right] = 1
```

如果直接套第 33 题的判断：

```python
nums[left] <= nums[mid]
```

会得到：

```text
1 <= 1
```

看起来左半边有序。

但实际上左半边是：

```text
[1, 0, 1]
```

它并不是普通升序区间。

这时不能确定哪边有序，只能先缩小边界：

```python
left += 1
right -= 1
```

因为前面已经判断过：

```python
nums[mid] == target
```

所以当：

```python
nums[left] == nums[mid] == nums[right]
```

且 `nums[mid]` 不是 `target` 时，`nums[left]` 和 `nums[right]` 也都不是 `target`，可以安全丢掉。

---

## 最佳写法

核心代码：

```python
while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        return True

    if nums[left] == nums[mid] == nums[right]:
        left += 1
        right -= 1
    elif nums[left] <= nums[mid]:
        if nums[left] <= target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if nums[mid] < target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1

return False
```

这段逻辑可以分成三种情况：

```text
1. nums[mid] == target
   直接找到，返回 True

2. nums[left] == nums[mid] == nums[right]
   无法判断哪边有序，收缩两端

3. 能判断哪边有序
   按第 33 题的方式继续二分
```

---

## 和第 33 题的关系

第 33 题的核心是：

```text
先判断哪边有序，再判断 target 在不在有序区间里
```

第 81 题还是这个思路，只是多了一步：

```text
如果 nums[left]、nums[mid]、nums[right] 都相等，就无法判断哪边有序
```

所以要先写：

```python
if nums[left] == nums[mid] == nums[right]:
    left += 1
    right -= 1
```

剩下的情况再照第 33 题处理。

---

## 为什么最坏是 O(n)

如果数组里有大量重复元素，例如：

```text
nums = [1, 1, 1, 1, 1, 1, 1]
target = 2
```

每一轮都会遇到：

```python
nums[left] == nums[mid] == nums[right]
```

这时只能：

```python
left += 1
right -= 1
```

每次只能缩小一点点区间，所以最坏时间复杂度是：

```text
O(n)
```

但如果重复元素不多，大多数时候仍然可以每次丢掉一半区间，平均表现接近：

```text
O(log n)
```

---

## 面试推荐讲法

1. 这题是第 33 题的重复元素版本。
2. 如果 `nums[mid] == target`，直接返回 `True`。
3. 如果 `nums[left] == nums[mid] == nums[right]`，无法判断哪半边有序，收缩两端。
4. 否则就能判断左半边或右半边有序。
5. 判断 `target` 是否落在有序半边里，决定继续搜哪边。
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
06_二分查找/08_q81/optimal_solution.py
```
