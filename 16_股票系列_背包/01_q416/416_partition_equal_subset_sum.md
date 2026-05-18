# 416. 分割等和子集

## 题目理解

给定一个只包含正整数的数组 `nums`，判断你能不能把它分成两个子集，使得两个子集的元素和相等。

例如：

```text
nums = [1, 5, 11, 5]
可以分成 [11] 和 [1, 5, 5]
答案是 True
```

```text
nums = [1, 2, 3, 5]
总和是 11，奇数，不可能平分
答案是 False
```

这题最关键的不是代码，而是先把题目翻译一下：

如果数组总和是 `total`，想分成两个和相等的子集，那么每个子集的目标和就必须是：

```text
target = total // 2
```

所以原题其实等价于：

> 能不能从 `nums` 里选出若干个数，使它们的和恰好等于 `target`。

而且这里每个数只能用一次，因为数组里的每个元素只能选或不选。

这就变成了一个非常标准的：

> **0-1 背包 / 子集和判定问题**

如果按刷题训练路线来走，这题最适合按下面顺序理解：

```text
暴力递归 -> 记忆化递归 -> 二维 DP -> 一维优化 DP
```

---

## 为什么这题适合这样学

这题特别适合完整走一遍推导链，因为它有两个很典型的卡点：

1. 怎么把“平分两个集合”转成“找一个子集和”
2. 为什么这是 0-1 背包，而不是完全背包

如果一上来就背模板，很容易只记住“写个布尔 DP 就完了”，但不清楚：

- 状态为什么这么定义
- 转移为什么成立
- 为什么一维优化时必须倒序

所以这题最适合从最直观的选或不选开始，一步一步推到 DP。

---

## 方法一：暴力递归

### 思路

先想最朴素的做法。

我们要判断：

```text
从 nums 里能不能选一些数，凑出 target
```

对于每个位置 `index`，都只有两种选择：

- 选当前数 `nums[index]`
- 不选当前数 `nums[index]`

于是可以定义：

```text
dfs(index, remain) = 从下标 index 开始选，能不能凑出 remain
```

那么递归转移就是：

```text
选当前数：dfs(index + 1, remain - nums[index])
不选当前数：dfs(index + 1, remain)
```

只要两条路里有一条能成功，就返回 `True`。

### 边界

有两个最重要的边界：

```text
remain == 0         -> 已经凑出来了，返回 True
index == len(nums)  -> 数字用完了还没凑出来，返回 False
remain < 0          -> 已经超过目标，返回 False
```

### 代码

```python
from typing import List


# 方法一：暴力递归
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2

        def dfs(index, remain):
            if remain == 0:
                return True
            if index == len(nums) or remain < 0:
                return False

            return dfs(index + 1, remain - nums[index]) or dfs(index + 1, remain)

        return dfs(0, target)
```

### 复杂度

- 时间复杂度：`O(2^n)`
- 空间复杂度：`O(n)`，主要是递归栈深度

### 评价

这个方法的价值主要是帮助你看清楚：

- 状态是什么
- 每一步的选择是什么
- 为什么这题天然是“选 / 不选”的结构

但它不能作为最终解法，因为很多状态会被反复计算。

---

## 方法二：记忆化递归

### 思路

暴力递归为什么慢？

因为同一个状态会被重复计算很多次。

比如 `dfs(index, remain)`，不同路径可能会反复走到同一个位置和同一个剩余目标。

所以可以很自然地加一个 `memo`，把已经算过的结果存起来。

仍然定义：

```text
dfs(index, remain) = 从 nums[index:] 中选，能不能凑出 remain
```

只是这次：

- 如果 `(index, remain)` 已经算过，直接返回
- 没算过，再继续递归

### 代码

```python
from typing import List


# 方法二：记忆化递归
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        memo = {}

        def dfs(index, remain):
            if remain == 0:
                return True
            if index == len(nums) or remain < 0:
                return False

            key = (index, remain)
            if key in memo:
                return memo[key]

            memo[key] = dfs(index + 1, remain - nums[index]) or dfs(index + 1, remain)
            return memo[key]

        return dfs(0, target)
```

### 复杂度

- 时间复杂度：`O(n * target)`
- 空间复杂度：`O(n * target)`

### 评价

这个方法已经能通过，而且从暴力递归升级过来很自然。

优点：

- 思路直观
- 很适合理解状态复用
- 容易从暴力写法平滑升级

缺点：

- 还是递归
- 面试里通常不如迭代 DP 稳定

---

## 方法三：二维 DP（最适合面试）

### 为什么这个最适合面试

这是我最推荐的面试写法。

原因是：

1. 它把 0-1 背包的状态表达得最清楚
2. 转移方程非常直观，不容易写错
3. 边界条件清晰，解释起来顺
4. 虽然不是空间最优，但最稳、最好讲

所以如果面试官先问标准解法，我会优先写这个。

---

### 第一步：先做等价转化

如果数组总和是奇数，那就不可能平分，直接返回 `False`。

只有总和是偶数时，问题才有意义。

设：

```text
total = sum(nums)
target = total // 2
```

原题就变成：

```text
能不能从前 i 个数里选一些，使它们的和等于 target
```

---

### 第二步：定义状态

定义：

```text
dp[i][j] = 使用前 i 个数，能不能凑出和 j
```

这里的“前 `i` 个数”指的是：

```text
nums[0], nums[1], ..., nums[i - 1]
```

我们的目标就是：

```text
dp[n][target]
```

其中 `n = len(nums)`。

---

### 第三步：想清楚转移为什么成立

现在来看 `dp[i][j]`。

第 `i` 个数其实对应的是：

```text
num = nums[i - 1]
```

对于这个数，只有两种选择：

#### 1. 不选它

那就看前 `i - 1` 个数能不能凑出 `j`：

```text
dp[i - 1][j]
```

#### 2. 选它

如果要选它，那么前提是：

```text
j >= num
```

而且前 `i - 1` 个数必须先凑出：

```text
j - num
```

所以这一种情况对应：

```text
dp[i - 1][j - num]
```

综合起来：

```text
dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]
```

当然第二项只有在 `j >= num` 时才存在。

---

### 第四步：边界怎么定

最核心的边界是：

```text
dp[0][0] = True
```

意思是：

```text
一个数都不选，凑出 0，是可以做到的
```

另外：

```text
dp[i][0] = True
```

因为不管看多少个数，只要什么都不选，就都能凑出 0。

而：

```text
dp[0][j] = False   (j > 0)
```

因为一个数都没有，不可能凑出正数和。

---

### 第五步：用例子走一遍

以：

```text
nums = [1, 5, 11, 5]
```

为例。

总和：

```text
22
```

所以目标和：

```text
target = 11
```

然后我们去问：

```text
能不能从这些数里选一些，凑出 11
```

显然可以，因为：

```text
11 = 11
```

或者：

```text
11 = 1 + 5 + 5
```

所以最后 `dp[n][11] = True`，答案就是 `True`。

---

### 第六步：为什么这是 0-1 背包

这题本质上就是 0-1 背包里的可达性判定：

- 物品：数组里的每个数
- 体积：数值本身
- 每个物品：只能选 0 次或 1 次
- 背包容量：`target`
- 问题目标：能不能恰好装满到 `target`

所以这是一个很标准的：

> **0-1 背包中“是否能恰好凑出目标和”问题。**

这句话在面试里说出来，会很加分。

---

### 代码

```python
from typing import List


# 方法三：二维 DP
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            num = nums[i - 1]
            dp[i][0] = True
            for current in range(1, target + 1):
                dp[i][current] = dp[i - 1][current]
                if current >= num:
                    dp[i][current] = dp[i][current] or dp[i - 1][current - num]

        return dp[n][target]
```

### 复杂度

- 时间复杂度：`O(n * target)`
- 空间复杂度：`O(n * target)`

---

### 面试时推荐怎么讲

你可以这样讲：

#### 1. 先做题意转化

如果总和是奇数，直接不可能平分。

如果总和是偶数，就等价于判断：

```text
能不能选出一些数，使它们的和等于 total // 2
```

#### 2. 再定义状态

```text
dp[i][j] 表示前 i 个数能不能凑出和 j
```

#### 3. 再解释转移

对于第 `i` 个数：

- 不选：看 `dp[i - 1][j]`
- 选：看 `dp[i - 1][j - num]`

所以：

```text
dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]
```

#### 4. 最后说边界

```text
dp[0][0] = True
```

表示一个数都不选，可以凑出 0。

#### 5. 再补一句模型归类

这是标准的 0-1 背包可达性问题。

这套表达会很完整，而且逻辑特别顺。

---

## 方法四：一维优化 DP（最优解法）

### 思路

二维 DP 已经很好了，但它其实只依赖上一行。

所以可以把：

```text
dp[i][j]
```

压缩成一维：

```text
dp[j] = 当前处理到某个前缀时，能不能凑出和 j
```

初始时：

```text
dp[0] = True
```

因为不选任何数，就能凑出 0。

每处理一个 `num`，就更新一次 `dp`。

如果当前 `dp[j - num]` 是 `True`，那说明把 `num` 加进去之后，就可以让 `dp[j]` 也变成 `True`。

所以转移就是：

```text
dp[j] = dp[j] or dp[j - num]
```

---

### 为什么这里必须倒序遍历

这是这题最容易写错的地方。

因为每个数只能用一次，所以当前这个 `num` 在这一轮更新里，不能被重复使用。

因此 `j` 必须从大到小枚举：

```text
for j in range(target, num - 1, -1)
```

如果你正序更新，就会让同一个数在一轮里被重复利用，那就变成完全背包了。

这也是为什么这题虽然最优空间能做到一维，但面试时我通常先讲二维版本，再顺手优化。

---

### 代码

```python
from typing import List


# 方法四：一维优化 DP
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for current in range(target, num - 1, -1):
                dp[current] = dp[current] or dp[current - num]

        return dp[target]
```

### 复杂度

- 时间复杂度：`O(n * target)`
- 空间复杂度：`O(target)`

### 评价

这个方法是空间最优写法。

优点：

- 时间复杂度和二维 DP 一样
- 空间从 `O(n * target)` 降到 `O(target)`
- 是这题更常见的最终最优代码

缺点：

- 倒序遍历这个细节容易写错
- 如果一上来就写一维版，解释成本比二维版更高

---

## 哪个方法最适合面试

### 结论

**最适合面试的是：方法三，二维 DP。**

### 为什么不是别的方法

#### 方法一：暴力递归

- 只能帮助推导状态
- 复杂度太高
- 不能作为最终答案

#### 方法二：记忆化递归

- 可以通过
- 也比较自然
- 但递归写法通常不如迭代 DP 稳定

#### 方法四：一维优化 DP

- 这是空间最优解法
- 但要额外解释为什么必须倒序
- 如果面试官先看你基础是否扎实，二维 DP 更稳、更清楚

所以综合来看：

> **方法三最适合面试；方法四最适合作为进一步优化。**

---

## 最适合面试的方法：详细讲解

### 第一步：先把题目翻译对

题目表面上是在问：

```text
能不能分成两个和相等的子集
```

但真正更容易处理的版本是：

```text
能不能选出一些数，使它们的和等于总和的一半
```

如果总和是奇数，连继续做都不用，直接返回 `False`。

这一步转化是整题最关键的入口。

---

### 第二步：为什么状态定义成 `dp[i][j]`

因为这题每个数只能用一次，所以我们必须知道：

- 现在考虑到了第几个数
- 现在目标和是多少

所以定义成：

```text
dp[i][j] = 前 i 个数能不能凑出和 j
```

这个状态定义同时把“物品数量”和“背包容量”都表达清楚了。

---

### 第三步：为什么转移只看选或不选

因为每个数只有一次机会。

对 `nums[i - 1]` 来说，只有两种情况：

- 不用它
- 用它一次

这正是 0-1 背包的核心特征。

所以：

```text
dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]
```

前者表示不选，后者表示选。

---

### 第四步：为什么边界是 `dp[0][0] = True`

因为一个数都不拿的时候：

- 凑出 0 是可能的
- 凑出正数是不可能的

所以：

```text
dp[0][0] = True
dp[0][j] = False (j > 0)
```

这个边界一旦立住，后面所有状态都能顺着推出来。

---

### 第五步：为什么二维版更适合先讲

虽然一维版更省空间，但二维版有个明显优势：

```text
状态来源看得见
```

你在面试板书时，面试官很容易跟着你的表格理解：

- 行表示用了多少个数
- 列表示目标和是多少
- 每个格子只从上一行转移

这比一上来就讲一维滚动数组更稳。

---

### 第六步：如果面试官追问优化怎么办

这时你再补一句：

> 因为 `dp[i][j]` 只依赖上一行，所以可以压成一维数组。由于每个数只能使用一次，所以内层必须倒序遍历，避免同一个数在一轮里被重复使用。

这样回答会很完整，也能体现你既懂标准解，也懂优化。

---

## 总结

### 递进关系

1. **暴力递归**
   - 先理解选或不选
   - 但复杂度太高

2. **记忆化递归**
   - 消除重复状态
   - 可以顺着暴力解自然升级

3. **二维 DP**
   - 标准 0-1 背包写法
   - 最适合面试

4. **一维优化 DP**
   - 空间更优
   - 但倒序细节更容易写错

### 最终建议

- **刷题主线**：优先掌握方法三
- **如果你想把这题吃透**：再补方法四的一维优化
- **如果你在准备面试**：把“题意转化 + 0-1 背包本质 + 二维到一维优化”这一整套讲顺
