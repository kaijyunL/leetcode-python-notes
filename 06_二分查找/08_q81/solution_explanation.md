# LeetCode 81. 搜索旋转排序数组 II 解析

## 题目描述

给定一个经过旋转的升序数组 `nums`，再给定一个目标值 `target`，判断 `target` 是否存在于数组中。

如果存在，返回：

```text
True
```

否则返回：

```text
False
```

和 `q33` 最大的区别是：

```text
这题允许重复元素
```

例如：

```text
nums = [2, 5, 6, 0, 0, 1, 2], target = 0
```

答案是：

```text
True
```

如果：

```text
target = 3
```

答案是：

```text
False
```

---

## 先理解题意

这题本质上就是 `q33` 的升级版。

`q33` 里没有重复元素，所以每次都能比较干净地判断：

```text
左半边有序，还是右半边有序
```

但这题有重复元素之后，会出现一种麻烦情况：

```text
nums[left]、nums[mid]、nums[right] 都一样
```

这时你没法像 `q33` 那样，仅靠这三个值就断定哪一边有序。

所以这题的核心不是重新发明一种新二分，而是：

```text
在 q33 的基础上，额外处理“重复元素让有序性判断失效”的情况
```

---

## 方法一：线性扫描

### 思路

最直接的方法就是从左到右遍历数组。

只要遇到 `target`，立刻返回 `True`。

如果整个数组扫完都没找到，就返回 `False`。

---

### 为什么可行

因为线性扫描会检查每个元素，所以不会漏掉目标值。

---

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

---

### 这个方法差在哪里

它当然正确，但没有利用旋转数组的结构特征。

这题虽然最坏情况下二分也会退化到 `O(n)`，但正常情况下仍然可以利用旋转数组的局部有序性，把搜索做得更快。

---

## 方法二：二分查找（面试主推）

这是最适合面试的方法。

---

### 核心想法

主框架和 `q33` 一样：

1. 先看 `nums[mid]` 是不是目标值
2. 再判断哪一半有序
3. 判断 `target` 是否落在有序区间里

但这里多了一个前置判断：

```text
如果 nums[left] == nums[mid] == nums[right]，
那就无法判断哪一边有序
```

这种情况下，只能先缩小边界。

---

### 为什么重复元素会让判断失效

在 `q33` 里，我们常用：

```python
nums[left] <= nums[mid]
```

来判断左半边是否有序。

但在这题里，这个判断可能失真。

例如：

```text
nums = [1, 0, 1, 1, 1]
target = 0
```

初始时：

```text
left = 0
right = 4
mid = 2
nums[left] = 1
nums[mid] = 1
nums[right] = 1
```

如果你直接看：

```python
nums[left] <= nums[mid]
```

会得到：

```text
1 <= 1
```

看起来好像左半边有序。

但左半边其实是：

```text
[1, 0, 1]
```

这并不是普通升序区间。

所以这里不能像 `q33` 那样直接下结论。

---

### 为什么 `nums[left] == nums[mid] == nums[right]` 时可以收缩两端

注意代码里一定先判断：

```python
if nums[mid] == target:
    return True
```

也就是说，当我们进入：

```python
if nums[left] == nums[mid] == nums[right]:
```

这一支时，已经知道：

```text
nums[mid] != target
```

又因为三者相等，所以：

```text
nums[left] != target
nums[right] != target
```

因此把两端各缩掉一个是安全的：

```python
left += 1
right -= 1
```

这一步的目的不是“确定方向”，而只是：

```text
先去掉这些无法提供信息、同时又确定不是答案的重复值
```

---

### 如果不属于三值相等，就回到 `q33` 的判断

一旦不再出现：

```text
nums[left] == nums[mid] == nums[right]
```

我们就又能像 `q33` 那样判断哪边有序。

如果：

```python
nums[left] <= nums[mid]
```

说明左半边有序。

这时判断：

```python
nums[left] <= target < nums[mid]
```

如果成立，说明 `target` 在左半边，所以：

```python
right = mid - 1
```

否则去右边：

```python
left = mid + 1
```

---

如果左半边不是有序的，那右半边一定有序。

这时判断：

```python
nums[mid] < target <= nums[right]
```

如果成立，去右边：

```python
left = mid + 1
```

否则去左边：

```python
right = mid - 1
```

---

### 用例推演

以：

```text
nums = [1, 0, 1, 1, 1], target = 0
```

为例。

开始时：

```text
left = 0
right = 4
mid = 2
nums[left] = 1
nums[mid] = 1
nums[right] = 1
```

并且 `nums[mid] != target`。

此时三者相等，没法判断哪边有序，所以先收缩：

```python
left += 1
right -= 1
```

变成：

```text
left = 1
right = 3
```

这时：

```text
mid = 2
nums[left] = 0
nums[mid] = 1
nums[right] = 1
```

现在左半边可判断为有序，因为：

```text
0 <= 1
```

再看目标值 `0` 是否在左半边范围内：

```text
0 <= 0 < 1
```

成立，所以：

```python
right = mid - 1
```

区间变成：

```text
left = 1
right = 1
```

最后就能找到 `target`。

---

### 为什么最坏时间复杂度会退化成 `O(n)`

如果数组里有大量重复元素，比如：

```text
nums = [1, 1, 1, 1, 1, 1, 1]
target = 2
```

每一轮都可能遇到：

```python
nums[left] == nums[mid] == nums[right]
```

这时只能：

```python
left += 1
right -= 1
```

每次只能缩小一点点范围，不能稳定地丢掉一半区间。

所以最坏情况下复杂度会退化成：

```text
O(n)
```

但如果重复元素不多，大部分轮次仍然能像普通二分那样砍掉一半区间，因此通常表现还是接近：

```text
O(log n)
```

---

### 和 `q33` 的关系

这题可以直接理解成：

```text
q33 + 处理三值相等时的特殊分支
```

也就是说：

- 没有重复元素时，用 `q33` 的思路即可
- 有重复元素时，先判断会不会因为重复值而看不清哪边有序

这是这题最值得记住的主线。

---

### 复杂度

- 平均时间复杂度：`O(log n)`
- 最坏时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

---

## 为什么这是最适合面试的写法

因为它很自然地承接了 `q33`：

1. 先说这题本质上还是旋转数组二分
2. 再指出重复元素会让“判断哪边有序”失效
3. 加上一个“三值相等就收缩边界”的分支
4. 剩下的逻辑全部回到 `q33`

面试里可以直接这样解释：

```text
这题和第 33 题的主框架一样，区别只是重复元素会让有序区间判断失效。
如果 nums[left]、nums[mid]、nums[right] 都相等，我就先收缩两端；
否则仍然判断哪一半有序，再决定下一步搜哪边。
```

---

## 最终建议

这题最值得记住的不是整段代码，而是这三个步骤：

```text
1. mid 是不是目标
2. 三值相等时先去重缩边界
3. 剩下按 q33 判断哪边有序
```

核心代码骨架就是：

```python
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
```

把这条主线记住，这题就会很稳。
