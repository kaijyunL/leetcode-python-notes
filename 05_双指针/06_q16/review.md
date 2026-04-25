# LeetCode 16 - 最接近的三数之和 · 复盘笔记

> **难度**：中等  
> **关键技巧**：排序 + 双指针  
> **关联题目**：第 15 题（3Sum）

---

## 一、题目理解

给定一个整数数组 `nums` 和一个目标值 `target`，从数组中选出三个数，使它们的和**最接近** `target`，返回这三个数的和。

- 输入：`nums = [-1, 2, 1, -4]`，`target = 1`
- 输出：`2`（因为 `-1 + 2 + 1 = 2`，是所有组合中最接近 1 的）

---

## 二、解法演进

### 解法一：暴力破解（Brute Force）

**思路**：三层循环枚举所有三元组，逐一比较差值，记录最接近的和。

```python
def threeSumClosest(nums, target):
    n = len(nums)
    res = sum(nums[:3])  # 初始值设为前三个数的和
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                current_sum = nums[i] + nums[j] + nums[k]
                if abs(current_sum - target) < abs(res - target):
                    res = current_sum
    return res
```

| 时间复杂度 | 空间复杂度 | 评价 |
|---|---|---|
| $O(n^3)$ | $O(1)$ | 逻辑清晰，但数组稍大即 TLE |

---

### 解法二：排序 + 双指针（最优解）

**思路**：先排序，固定第一个数 `nums[i]`，用左右指针向中间夹逼，根据当前和与 `target` 的大小关系动态移动指针。

```python
def threeSumClosest(nums, target):
    nums.sort()           # 核心：先排序，使数组有序
    n = len(nums)
    res = nums[0] + nums[1] + nums[2]

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:  # 跳过重复的第一个数
            continue

        left, right = i + 1, n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            # 【剪枝】完美匹配，差值为 0，不可能更好，直接返回
            if current_sum == target:
                return target

            # 更新最接近的结果
            if abs(current_sum - target) < abs(res - target):
                res = current_sum

            # 根据当前和与 target 的关系移动指针
            if current_sum < target:
                left += 1   # 和太小，左指针右移使和变大
            else:
                right -= 1  # 和太大，右指针左移使和变小

    return res
```

| 时间复杂度 | 空间复杂度 | 评价 |
|---|---|---|
| $O(n^2)$ | $O(\log n)$ | 面试标准解，高效且清晰 |

---

## 三、与第 15 题的异同

### 相同点
- 都用到**排序 + 双指针**的核心框架
- 外层固定一个数，内层用左右指针夹逼
- 指针移动逻辑完全相同：和小则 `left++`，和大则 `right--`

### 不同点

| | 第 15 题（3Sum） | 第 16 题（3Sum Closest） |
|---|---|---|
| 目标 | 三数之和**精确等于 0** | 三数之和**最接近 target** |
| 问题类型 | 精确匹配问题 | 最优化问题 |
| 判断方式 | `current_sum == 0 / < 0 / > 0` | `abs(current_sum - target)` 比大小 |
| 命中时 | 加入结果列表，继续找其他组合 | 直接 `return target`（差值为 0） |
| 需要去重 | ✅ 必须（可能有重复三元组） | ❌ 不需要（只返回一个最优值） |

### 写法对比
两道题的内层逻辑等价，可以用统一的 `current_sum` 写法来类比记忆：

```
第 15 题：if current_sum == 0   → 找到答案
第 16 题：if current_sum == target → 找到最优答案（直接返回）
```

---

## 四、关键知识点

### 💡 为什么第 15 题常写 `target = -nums[i]`？
这是一种"**降维**"思维：
- 三数之和等于 0，等价于另外两数之和等于 `-nums[i]`
- 把 3Sum 变成一个 **2Sum** 子问题，语义更清晰，理论上也更容易封装复用

但用 `current_sum = nums[i] + nums[left] + nums[right]` 直接判断完全等价，只是风格不同。

### 💡 `if current_sum == target: return target` 是纯粹的剪枝
- **删掉不影响正确性**：下面的逻辑会正常更新 `res = target`，最终也能返回正确答案
- **写上可以提前退出**：差值为 0 是理论最优，后续循环没有意义
- 这种技巧叫 **Early Termination（提前终止）**，在面试中写上是加分项

---

## 五、解题模板总结

解决 **nSum** 类问题（3Sum / 4Sum / 3Sum Closest）的通用框架：

```
1. 排序
2. 外层循环固定前 n-2 个数
3. 内层用双指针处理剩余两个数
4. 根据 current_sum 与目标的关系移动指针
5. 根据题目要求（精确匹配 or 最优化）更新结果
```

---

## 六、易错点

1. **忘记排序**：双指针依赖数组有序，不排序结果是错的
2. **循环边界**：外层循环到 `n - 2`，保证至少还有两个数给左右指针用
3. **初始值设置**：`res` 必须初始化为一个合法的三元组之和（如前三个数），不能用 `float('inf')`，否则最终加法溢出或类型错误
