# LeetCode 153. 寻找旋转排序数组中的最小值

## 题目理解

给你一个原本升序排列的数组，它在某个未知位置被旋转过。

例如原数组：

```text
[0, 1, 2, 4, 5, 6, 7]
```

旋转后可能变成：

```text
[4, 5, 6, 7, 0, 1, 2]
```

现在要求返回数组中的最小值。

题目保证：

```text
nums 中的元素互不相同
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
06_二分查找/07_q153/linear_scan.py
```

---

## 方法二：二分查找

这是最适合面试的方法。

### 核心思路

每次比较：

```python
nums[mid]
nums[right]
```

因为右边界 `right` 一定位于当前搜索区间内，所以拿 `nums[right]` 做参照，比固定拿 `nums[-1]` 更自然。

---

## 如何判断最小值在哪边

### 情况一：`nums[mid] > nums[right]`

例如：

```text
nums = [4, 5, 6, 7, 0, 1, 2]
```

如果：

```text
mid = 3
nums[mid] = 7
nums[right] = 2
```

此时：

```python
nums[mid] > nums[right]
```

说明 `mid` 落在旋转点左边那段较大的区间里。

最小值一定在 `mid` 右边，所以：

```python
left = mid + 1
```

注意这里可以排除 `mid`，因为 `nums[mid] > nums[right]`，`nums[mid]` 不可能是最小值。

---

### 情况二：`nums[mid] <= nums[right]`

例如：

```text
nums = [4, 5, 6, 7, 0, 1, 2]
```

如果当前区间变成：

```text
[0, 1, 2]
```

这时：

```text
nums[mid] <= nums[right]
```

说明 `mid` 到 `right` 这一段是有序的。

最小值可能就是 `mid`，也可能在 `mid` 左边。

所以：

```python
right = mid
```

注意这里不能写成：

```python
right = mid - 1
```

因为 `mid` 有可能就是最小值，不能排除。

---

## 最佳写法

代码：

```python
while left < right:
    mid = (left + right) // 2

    if nums[mid] > nums[right]:
        left = mid + 1
    else:
        right = mid

return nums[left]
```

为什么循环条件是：

```python
while left < right
```

因为我们始终保留答案所在的区间。

当：

```text
left == right
```

时，区间里只剩一个元素，它就是最小值。

所以：

```python
return nums[left]
```

---

## 为什么没有旋转也成立

例如：

```text
nums = [11, 13, 15, 17]
```

第一次：

```text
left = 0
right = 3
mid = 1
nums[mid] = 13
nums[right] = 17
```

因为：

```python
nums[mid] <= nums[right]
```

说明 `[mid, right]` 这一段有序，最小值在左边，或者就是 `mid`。

所以：

```python
right = mid
```

继续缩小后，最终会停在下标 `0`，返回：

```text
11
```

---

## 和第 35 题模板的关系

第 153 题也可以写成边界模板：

```python
if nums[mid] > nums[-1]:
    left = mid + 1
else:
    right = mid - 1

return nums[right + 1]
```

这个写法能过。

它的含义是把数组按下面这个判断分成两段：

```python
nums[i] > nums[-1]
```

例如：

```text
nums = [4, 5, 6, 7, 0, 1, 2]
```

判断结果是：

```text
nums:   4     5     6     7     0      1      2
check: True  True  True  True  False  False  False
```

所以：

```text
right
```

最后停在最后一个 `True` 的位置。

```text
right + 1
```

就是第一个 `False` 的位置，也就是最小值的位置。

完整代码见：

```text
06_二分查找/07_q153/optimal_solution.py
```

里面的：

```python
SolutionBoundaryTemplate
```

就是这个写法。

不过它不是本题最推荐的写法，因为它把题目转成了：

```text
找第一个 nums[i] <= nums[-1] 的位置
```

这个思路稍微绕了一层。

第 153 题更自然的写法是：

```python
if nums[mid] > nums[right]:
    left = mid + 1
else:
    right = mid
```

也就是直接判断最小值在 `mid` 左边还是右边。

---

## 和第 33 题的区别

第 33 题是找 `target`，旋转数组整体不是单调的，所以直接比较：

```python
nums[mid] < target
```

不一定能判断答案在左边还是右边。

第 153 题是找旋转点，也就是找最小值。

它不需要判断 `target` 在哪边，只需要判断最小值在哪个区间里，所以代码比第 33 题更短。

---

## 面试推荐讲法

1. 每次比较 `nums[mid]` 和 `nums[right]`。
2. 如果 `nums[mid] > nums[right]`，说明最小值一定在 `mid` 右边。
3. 否则说明最小值在左边，或者 `mid` 本身就是最小值。
4. 因为 `mid` 可能是答案，所以右边收缩时写 `right = mid`。
5. 当 `left == right` 时，当前下标就是最小值的位置。

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
06_二分查找/07_q153/optimal_solution.py
```
