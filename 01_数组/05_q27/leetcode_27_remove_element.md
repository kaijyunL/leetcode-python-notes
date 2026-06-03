# LeetCode 第 27 题：移除元素 (Remove Element)

## 1. 题目描述

给你一个数组 `nums` 和一个值 `val`，你需要 **原地** 移除所有数值等于 `val` 的元素，并返回移除后数组的新长度。

**不要使用额外的数组空间**，你必须仅使用 `O(1)` 额外空间并 **原地** 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

---

## 2. 暴力解法 (Brute Force)

### 思路
暴力解法的核心思想是：当我们遍历数组时，如果发现当前元素等于 `val`，我们就将该元素之后的所有元素都向前移动一位，覆盖掉当前的 `val`。

### 算法步骤
1. 使用一个循环遍历数组。
2. 如果 `nums[i] == val`：
   - 将 `i+1` 到末尾的所有元素向前移动一位。
   - 数组长度减 1。
   - `i` 也需要减 1（因为当前位置被新元素覆盖了，需要再次检查当前位置）。

### 代码实现 (`brute_force.py`)
```python
def removeElement(nums, val):
    size = len(nums)
    i = 0
    while i < size:
        if nums[i] == val:
            # 发现目标值，将后面的元素全部向前挪一位
            for j in range(i + 1, size):
                nums[j - 1] = nums[j]
            size -= 1 # 数组长度减一
            i -= 1    # 下标减一，因为刚才挪过来的元素还没检查
        i += 1
    return size
```

### 复杂度分析
- **时间复杂度**: $O(n^2)$。其中 $n$ 是数组长度。最坏情况下，每个元素都要挪动。
- **空间复杂度**: $O(1)$。

---

## 3. 最优解法：双指针 (Two Pointers)

### 思路
我们可以使用“快慢指针”来解决。
- **快指针 (`fast`)**: 负责寻找新数组所需要的元素（即不等于 `val` 的元素）。
- **慢指针 (`slow`)**: 指向新数组下一个放置元素的位置。

### 算法步骤
1. 初始化 `slow = 0`。
2. 遍历数组，`fast` 从 0 到 `len(nums) - 1`：
   - 如果 `nums[fast] != val`：
     - 将 `nums[fast]` 赋值给 `nums[slow]`。
     - `slow` 递增。
3. 最后 `slow` 就是新数组的长度。

### 代码实现 (`two_pointers.py`)
```python
def removeElement(nums, val):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

### 复杂度分析
- **时间复杂度**: $O(n)$。只需遍历数组一次。
- **空间复杂度**: $O(1)$。

---

## 4. 进阶优化：双指针 (从两端遍历)

### 思路
如果数组中要移除的元素很少，比如数组长度为1000，但只有一个元素需要移除。上面的“快慢指针”仍然会复制几乎所有的元素。
我们可以使用左右指针。当左指针发现 `val` 时，直接将右指针指向的元素移动到左边。

### 代码实现 (`two_pointers_optimized.py`)
```python
def removeElement(nums, val):
    left = 0
    right = len(nums)
    while left < right:
        if nums[left] == val:
            # 如果左边是 val，就把右边的换过来，右边缩小范围
            nums[left] = nums[right - 1]
            right -= 1
            # 注意这里左指针不移动，因为换过来的值还没检查
        else:
            left += 1
    return left
```

### 复杂度分析
- **时间复杂度**: $O(n)$。每个元素最多被查看一次。
- **空间复杂度**: $O(1)$。
- **优点**: 赋值操作次数最少。
