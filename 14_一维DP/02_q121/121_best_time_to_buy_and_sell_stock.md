# 121. Best Time to Buy and Sell Stock

## 题目理解

给你一个数组 `prices`，`prices[i]` 表示第 `i` 天股票的价格。

你只能 **买入一次**、**卖出一次**，并且：

- 买入必须发生在卖出之前
- 如果赚不到钱，返回 `0`

例如：

- `prices = [7,1,5,3,6,4]`，答案是 `5`
  - 第 2 天买入 `1`
  - 第 5 天卖出 `6`
  - 利润 = `6 - 1 = 5`
- `prices = [7,6,4,3,1]`，答案是 `0`
  - 因为一直跌，没有任何正利润

这道题的核心不是“模拟交易”，而是：

> 对于每一天作为卖出日，如何快速知道它前面最低的买入价格？

---

## 方法一：暴力枚举

### 思路

最直接的想法就是：

- 枚举每一个买入日 `i`
- 再枚举每一个卖出日 `j`
- 要求 `j > i`
- 计算利润 `prices[j] - prices[i]`
- 取最大值

也就是把所有可能的买卖组合全试一遍。

### 代码

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        best = 0

        for i in range(n):
            for j in range(i + 1, n):
                best = max(best, prices[j] - prices[i])

        return best
```

### 复杂度

- 时间复杂度：`O(n^2)`
- 空间复杂度：`O(1)`

### 评价

这个方法很容易想到，也能帮助你确认题意。

但它的问题很明显：

- 每个买入日都要往后看所有卖出日
- 重复比较太多
- 数据一大就会慢

所以它适合作为**起点思路**，不适合作为最终答案。

---

## 方法二：前缀最小值数组

### 思路

我们换个角度看。

如果第 `i` 天要卖出，那么最好的买入价一定是：

```text
第 0 天到第 i 天之间的最低价格
```

所以我们可以先维护一个数组：

```text
min_price[i] = 第 0 天到第 i 天为止的最低价格
```

那么第 `i` 天卖出的利润就是：

```text
prices[i] - min_price[i]
```

再把所有卖出日的利润取最大值即可。

### 代码

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        min_price = [0] * n
        min_price[0] = prices[0]

        for i in range(1, n):
            min_price[i] = min(min_price[i - 1], prices[i])

        best = 0
        for i in range(n):
            best = max(best, prices[i] - min_price[i])

        return best
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

### 评价

这个方法已经把时间降到了线性。

优点：

- 思路清楚
- 容易理解“卖出日 + 前面最低买入价”这个结构

缺点：

- 额外用了一个数组
- 其实我们并不需要把所有历史最低价都存下来

因此还可以继续优化。

---

## 方法三：动态规划

### 思路

这题也可以用 DP 来理解。

定义：

- `dp[i]` 表示：**第 `i` 天卖出时，能得到的最大利润**

那么：

```text
dp[i] = prices[i] - min(prices[0..i])
```

但为了递推，我们再同时维护：

```text
low[i] = 第 0 天到第 i 天为止的最低价格
```

状态转移：

```text
low[i] = min(low[i - 1], prices[i])
dp[i] = prices[i] - low[i]
```

最后答案是：

```text
max(dp[0], dp[1], ..., dp[n - 1])
```

### 代码

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        low = [0] * n
        dp = [0] * n

        low[0] = prices[0]
        dp[0] = 0

        for i in range(1, n):
            low[i] = min(low[i - 1], prices[i])
            dp[i] = prices[i] - low[i]

        return max(dp)
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`

### 为什么这也算 DP

因为它有明显的“当前位置依赖前一个状态”的结构：

- `low[i]` 依赖 `low[i - 1]`
- `dp[i]` 依赖当前价格和历史最低价

虽然这题很多时候不一定会先想到“标准 DP 表”，但从递推视角看，它是完全可以写成 DP 的。

### 评价

这个方法比“前缀最小值数组”更像一份正式的 DP 写法。

如果你正在系统刷一维 DP，这个版本很值得写一遍。

不过它仍然保存了整张表，而实际上：

- `low[i]` 只依赖前一个 `low[i - 1]`
- 当前利润也只需要即时更新最大值

所以还可以继续压缩。

---

## 方法四：一次遍历 + 状态压缩（最优解）

### 思路

观察方法三会发现：

我们并不需要整个 `low` 数组，也不需要整个 `dp` 数组。

因为遍历到第 `i` 天时，我们真正关心的只有两件事：

1. **前面出现过的最低价格是多少**
2. **到目前为止的最大利润是多少**

所以只需要两个变量：

- `min_price`：遍历到当前为止见过的最低价格
- `max_profit`：遍历到当前为止能获得的最大利润

遍历每一天价格 `price` 时：

- 先更新最低买入价
- 再计算如果今天卖出，利润是多少
- 再更新最大利润

状态更新写成：

```text
min_price = min(min_price, price)
max_profit = max(max_profit, price - min_price)
```

### 代码

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

### 评价

这是这道题最常见、最实用的最优写法。

优点：

- 只遍历一次
- 不用额外数组
- 代码短
- 边界清楚
- 很适合面试现场手写

---

## 哪个方法最适合面试

### 结论

**最适合面试的是：方法四，一次遍历 + 状态压缩。**

---

### 为什么它最适合面试

面试里，面试官通常不只想看你“能写出答案”，还想看你是否理解这个优化过程。

这道题最好的表达路径是：

1. 先说暴力法
   - 枚举买入日和卖出日
   - 时间复杂度 `O(n^2)`
2. 再指出优化关键
   - 对于每个卖出日，只关心它前面最低的价格
3. 然后给出一次遍历写法
   - 一边维护历史最低价
   - 一边维护最大利润
4. 最后总结复杂度
   - 时间 `O(n)`
   - 空间 `O(1)`

这条思路非常自然，面试官一听就知道你不是死记硬背，而是真的理解了题目的突破口。

---

### 面试时推荐怎么讲

你可以这样讲：

#### 1. 先明确题目本质

题目要求只做一次买卖，而且买入必须在卖出前面。

所以当我枚举某一天作为卖出日时，我只需要知道：

> 在它之前出现过的最低价格是多少。

因为：

```text
利润 = 当前卖出价 - 之前最低买入价
```

#### 2. 再定义两个变量

- `min_price`：到当前为止出现过的最低股价
- `max_profit`：到当前为止能获得的最大利润

#### 3. 说明遍历时怎么更新

假设当前价格是 `price`：

- 先拿它更新最低价：`min_price = min(min_price, price)`
- 再看今天卖出最多赚多少：`price - min_price`
- 用这个利润更新全局答案：`max_profit = max(max_profit, price - min_price)`

#### 4. 为什么这样不会漏答案

因为每一天都被当作“卖出日”检查过一次。

而每次检查时，`min_price` 都表示它前面所有天里的最低价格。

所以：

- 对当前卖出日来说，我们已经找到了最好的买入点
- 对所有卖出日都检查完后，自然就得到了全局最优解

这就是这道题最关键的正确性来源。

---

### 面试最推荐代码

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
```

---

### 这个方法和 DP 的关系

虽然很多人会把它叫做“贪心”或“维护最小值”，但它也可以理解成 DP 的空间优化版。

因为你可以把它看成：

- `low[i]`：前 `i` 天最低价格
- `profit[i]`：第 `i` 天卖出的利润

只是我们发现：

- `low[i]` 只依赖 `low[i-1]`
- 全局答案只需要一个最大值

所以整张表都可以压缩掉。

如果你在刷一维 DP，把它理解成“DP 的状态压缩”会很顺。

---

## 总结

### 递进关系

1. **暴力枚举**
   - 枚举所有买卖组合
   - 简单但慢

2. **前缀最小值数组**
   - 把“前面最低买入价”预处理出来
   - 时间降到 `O(n)`

3. **动态规划**
   - 用递推方式表达“历史最低价”和“当天卖出利润”
   - 适合训练状态定义能力

4. **一次遍历 + 状态压缩**
   - 保留核心状态
   - 去掉整张表
   - 是最优写法，也是面试最推荐写法

### 一句话记忆

> 遍历每一天，把它当作卖出日，并持续维护它前面出现过的最低买入价。
