# LeetCode 33. 搜索旋转排序数组

## 题目理解

给你一个原本升序排列的数组 `nums`，它在某个未知位置被旋转过。

例如原数组：

```text
[0, 1, 2, 4, 5, 6, 7]
```

旋转后可能变成：

```text
[4, 5, 6, 7, 0, 1, 2]
```

现在给一个 `target`，要求返回它在数组中的下标。如果不存在，返回 `-1`。

题目还保证：

```text
nums 中的元素互不相同
```

---

## 方法一：线性扫描

### 思路

从左到右遍历数组。

如果当前元素等于 `target`，直接返回当前位置。

如果遍历完都没找到，返回 `-1`。

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
06_二分查找/06_q33/linear_scan.py
```

---

## 方法二：二分查找

这是最适合面试的方法。

### 核心思路

旋转数组整体不是完全有序的，但每次取 `mid` 后，左右两边一定至少有一边是有序的。

所以每轮二分做两件事：

```text
1. 判断哪一半是有序的
2. 判断 target 是否在有序的那一半里
```

如果 `target` 在有序的一半里，就去那边找。

否则去另一边找。

---

## 如何判断左半边有序

如果：

```python
nums[left] <= nums[mid]
```

说明：

```text
[left, mid] 这一段是有序的
```

这时再判断 `target` 是否落在左半边：

```python
nums[left] <= target < nums[mid]
```

如果在，就缩小到左边：

```python
right = mid - 1
```

否则去右边：

```python
left = mid + 1
```

---

## 如何判断右半边有序

如果左半边不是有序的，那右半边一定有序。

也就是：

```text
[mid, right] 这一段是有序的
```

这时判断 `target` 是否落在右半边：

```python
nums[mid] < target <= nums[right]
```

如果在，就缩小到右边：

```python
left = mid + 1
```

否则去左边：

```python
right = mid - 1
```

---

## 例子

```text
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
```

开始：

```text
left = 0
right = 6
mid = 3
nums[mid] = 7
```

此时：

```text
nums[left] = 4
nums[mid] = 7
```

因为：

```text
4 <= 7
```

所以左半边 `[4, 5, 6, 7]` 有序。

但是 `target = 0` 不在 `[4, 7)` 里面，所以去右边：

```python
left = mid + 1
```

接着：

```text
left = 4
right = 6
mid = 5
nums[mid] = 1
```

左半边 `[0, 1]` 有序，`target = 0` 在 `[0, 1)` 里面，所以去左边：

```python
right = mid - 1
```

最后找到：

```text
nums[4] = 0
```

返回：

```text
4
```

---

## 和普通二分的关系

普通升序数组可以直接判断：

```python
if nums[mid] == target:
    return mid
elif nums[mid] < target:
    left = mid + 1
else:
    right = mid - 1
```

但旋转数组不能只看 `nums[mid] < target`。

例如：

```text
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
mid = 3
nums[mid] = 7
```

虽然：

```text
nums[mid] > target
```

但答案不在左边，而是在右边。

所以第 33 题的关键不是单纯比较 `nums[mid]` 和 `target`，而是：

```text
先判断哪一半有序，再判断 target 是否落在有序区间里。
```

---

## 面试推荐讲法

1. 旋转数组虽然整体无序，但以 `mid` 切开后，至少有一半是有序的。
2. 如果 `nums[left] <= nums[mid]`，说明左半边有序。
3. 判断 `target` 是否在左半边的范围内。
4. 如果在，就去左边；否则去右边。
5. 如果左半边无序，则右半边有序，用同样方式判断。

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
06_二分查找/06_q33/optimal_solution.py
```
