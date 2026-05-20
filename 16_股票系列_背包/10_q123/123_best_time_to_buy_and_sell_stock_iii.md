# 123. Best Time to Buy and Sell Stock III

## 题目理解

给你一个数组 `prices`，`prices[i]` 表示第 `i` 天股票的价格。

你最多可以完成 **两笔交易**，并且：

- 同一时间只能持有 **一股** 股票
- 必须先卖出，才能再次买入
- 如果赚不到钱，可以不交易，答案返回 `0`

例如：

- `prices = [3,3,5,0,0,3,1,4]`，答案是 `6`
  - 第一次：`0 -> 3`，赚 `3`
  - 第二次：`1 -> 4`，赚 `3`
  - 总利润 `6`
- `prices = [1,2,3,4,5]`，答案是 `4`
  - 其实做一笔交易就够了：`1 -> 5`
- `prices = [7,6,4,3,1]`，答案是 `0`
  - 一直下跌，不做交易最好

这题和前面股票题的关系很值得连起来看：

- 第 `121` 题：**只能做 1 次交易**
- 第 `122` 题：**交易次数无限**
- 第 `309` 题：**交易次数无限，但有冷冻期**
- 第 `123` 题：**最多只能做 2 次交易**

所以第 `123` 题最关键的新限制不是：

```text
能不能买 / 卖
```

而是：

```text
还能不能继续完成下一笔交易
```

这题最适合按下面的路线理解：

```text
暴力递归 -> 记忆化递归 -> 三维 DP -> 状态压缩 DP
```

---

## 为什么这题不能只沿用第 122 题的二维状态

第 `122` 题里，我们只需要区分：

- 空仓 / 可买
- 持股

因为交易次数无限，所以只要今天手里没股票，明天就总还能继续买。

但第 `123` 题不行。

比如你今天已经完成了 2 次卖出，那么即使现在手里没股票：

- 你也不能再买
- 因为题目只允许最多两笔交易

这说明：

> **光知道“今天是空仓还是持股”还不够，还要知道“已经完成了几次交易”。**

所以这题和第 `309` 题的区别是：

- 第 `309` 题：因为冷冻期，**空仓状态被拆开**
- 第 `123` 题：因为交易次数有限，**状态要多一维“交易次数”**

也就是说：

- `309` 的难点是：状态种类变多
- `123` 的难点是：状态维度变多

---

## 方法一：暴力递归

### 思路

先完全不写 DP，直接把每天的选择递归出来。

定义：

```text
dfs(day, remain, holding) = 从第 day 天开始，在还可以完成 remain 笔交易、holding 表示当前是否持股 的情况下，后面最多能赚多少钱
```

这里：

- `day`：当前走到第几天
- `remain`：还剩几次完整交易可以做
- `holding`：当前是否持有股票

为了和第 `122` 题保持一致，也可以把 `holding` 理解成：

```text
0 = 空仓 / 可买
1 = 持股
```

### 情况一：当前没有持股

这时有两种选择：

1. 今天什么都不做，去下一天
2. 今天买入，利润减去 `prices[day]`

所以：

```text
dfs(day, remain, 0) = max(
    dfs(day + 1, remain, 0),
    -prices[day] + dfs(day + 1, remain, 1)
)
```

注意：

- 买入本身不算完成一笔交易
- 真正消耗交易次数的是“卖出”

### 情况二：当前持有股票

这时也有两种选择：

1. 今天继续持有
2. 今天卖出，利润加上 `prices[day]`

卖出之后，一笔完整交易才真正完成，所以：

```text
dfs(day, remain, 1) = max(
    dfs(day + 1, remain, 1),
    prices[day] + dfs(day + 1, remain - 1, 0)
)
```

### 边界

#### 1. 走到最后一天之后

```text
day == n
```

说明已经没有天数可用了：

- 如果此时没持股，返回 `0`
- 如果此时还持股，说明最后没卖掉，这条路径不合法

所以：

```text
dfs(n, remain, 0) = 0
dfs(n, remain, 1) = -∞
```

#### 2. 已经没有交易次数了

```text
remain == 0
```

此时：

- 如果没持股，后面什么都不能做，返回 `0`
- 如果还持股，也没法再卖了，这条路径不合法

所以：

```text
dfs(day, 0, 0) = 0
dfs(day, 0, 1) = -∞
```

### 代码

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        def dfs(day: int, remain: int, holding: bool) -> int:
            if day == n:
                return 0 if not holding else float("-inf")
            if remain == 0:
                return 0 if not holding else float("-inf")

            best = dfs(day + 1, remain, holding)
            if holding:
                best = max(best, prices[day] + dfs(day + 1, remain - 1, False))
            else:
                best = max(best, -prices[day] + dfs(day + 1, remain, True))

            return best

        return dfs(0, 2, False)
```

### 复杂度

- 时间复杂度：指数级
- 空间复杂度：`O(n)`，主要来自递归深度

### 评价

这个方法的价值在于：

- 把“买入不消耗交易次数，卖出才消耗”想清楚
- 把后面 DP 的三维状态先定义出来

但它重复状态太多，不能作为最终答案。

---

## 方法二：记忆化递归

### 思路

暴力递归慢，是因为同一个状态会被反复计算。

比如：

```text
dfs(day, remain, holding)
```

只要：

- `day` 一样
- `remain` 一样
- `holding` 一样

那么后面的最优利润就一定一样。

所以可以把已经算过的状态缓存起来。

状态定义和转移都完全不变：

```text
dfs(day, remain, 0) = max(dfs(day + 1, remain, 0), -prices[day] + dfs(day + 1, remain, 1))
dfs(day, remain, 1) = max(dfs(day + 1, remain, 1), prices[day] + dfs(day + 1, remain - 1, 0))
```

### 代码

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        memo = {}

        def dfs(day: int, remain: int, holding: bool) -> int:
            if day == n:
                return 0 if not holding else float("-inf")
            if remain == 0:
                return 0 if not holding else float("-inf")

            key = (day, remain, holding)
            if key in memo:
                return memo[key]

            best = dfs(day + 1, remain, holding)
            if holding:
                best = max(best, prices[day] + dfs(day + 1, remain - 1, False))
            else:
                best = max(best, -prices[day] + dfs(day + 1, remain, True))

            memo[key] = best
            return best

        return dfs(0, 2, False)
```

### 复杂度

- 时间复杂度：`O(n)`，这里 `remain` 只有 `0/1/2`
- 空间复杂度：`O(n)`

### 评价

这个方法已经能通过，而且很适合作为“递归 -> DP”的自然过渡。

优点：

- 状态定义最直观
- 很适合先把题目限制讲清楚

缺点：

- 还是递归写法
- 面试里一般不如迭代 DP 稳定

---

## 方法三：三维 DP（最适合面试）

### 为什么这里要三维

在第 `122` 题里，状态只有：

- 第几天 `i`
- 是否持股 `0 / 1`

但现在还不够，因为还要知道：

- 已经完成了几次交易

所以最自然的定义是：

```text
dp[i][t][0] = 到第 i 天结束时，已经完成 t 次交易，手里没股票的最大利润
dp[i][t][1] = 到第 i 天结束时，已经完成 t 次交易，手里持有股票的最大利润
```

这里：

- `i`：第几天
- `t`：已经完成几次交易，取值 `0 / 1 / 2`
- 最后一维继续沿用股票系列的老习惯：
  - `0 = 空仓 / 可买`
  - `1 = 持股`

这样记非常顺：

```text
122：只有 0/1 两种持股状态
123：在 122 的基础上，再补一维 t = 已完成交易数
```

### 第 0 天怎么初始化

第 `0` 天结束时：

#### 1. 完成 0 次交易，空仓

什么都不做：

```text
dp[0][0][0] = 0
```

#### 2. 完成 0 次交易，持股

说明今天买了：

```text
dp[0][0][1] = -prices[0]
```

#### 3. 其他状态

比如：

- 第 0 天结束就已经完成 1 次或 2 次交易
- 第 0 天结束时完成 2 次交易还持股

这些都不可能，所以记为：

```text
-∞
```

### 转移怎么推

#### 1. 空仓状态 `dp[i][t][0]`

今天结束时空仓，有两种来源：

1. 昨天就空仓，今天继续不动
2. 昨天持股，今天卖出，于是完成次数从 `t - 1` 变成 `t`

所以：

```text
dp[i][t][0] = max(
    dp[i - 1][t][0],
    dp[i - 1][t - 1][1] + prices[i]
)          (t >= 1)
```

如果 `t = 0`，那就不可能通过卖出转过来，所以：

```text
dp[i][0][0] = dp[i - 1][0][0]
```

#### 2. 持股状态 `dp[i][t][1]`

今天结束时持股，也有两种来源：

1. 昨天就持股，今天继续拿着
2. 昨天空仓，今天买入

注意：

- 买入不会增加已完成交易数
- 所以买入前后 `t` 不变

因此：

```text
dp[i][t][1] = max(
    dp[i - 1][t][1],
    dp[i - 1][t][0] - prices[i]
)
```

不过这里要注意一个语义细节：

- 当 `t = 2` 时，说明你已经完成了 2 次交易
- 这时再买入已经没有意义，也不应该被允许

所以真正需要计算持股状态的只有 `t = 0 / 1`。

### 为什么答案要取空仓状态的最大值

最后一天结束时，如果还持股，那说明股票还没卖掉，利润没有真正落袋。

所以答案只能在：

```text
dp[n - 1][0][0]
dp[n - 1][1][0]
dp[n - 1][2][0]
```

里面取最大值。

也就是：

```text
max(dp[n - 1][t][0] for t in range(3))
```

### 代码

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        neg_inf = float("-inf")
        dp = [[[neg_inf, neg_inf] for _ in range(3)] for _ in range(n)]

        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0]

        for i in range(1, n):
            for t in range(3):
                dp[i][t][0] = dp[i - 1][t][0]
                if t >= 1:
                    dp[i][t][0] = max(dp[i][t][0], dp[i - 1][t - 1][1] + prices[i])

                dp[i][t][1] = dp[i - 1][t][1]
                if t < 2:
                    dp[i][t][1] = max(dp[i][t][1], dp[i - 1][t][0] - prices[i])

        return max(dp[n - 1][t][0] for t in range(3))
```

### 复杂度

- 时间复杂度：`O(n)`，因为 `t` 只有 `0/1/2`
- 空间复杂度：`O(n)`

### 评价

这是我最推荐的面试写法。

优点：

- 第 `122` 题的两态模板可以直接复用
- “交易次数上限”是怎么进入状态定义的，讲得最清楚
- 很适合继续推广到第 `188` 题

缺点：

- 不是空间最优

但对面试来说，通常逻辑清晰比省这点空间更重要。

---

## 方法四：状态压缩 DP（最优解）

### 思路

观察方法三会发现：

- 第 `i` 天只依赖第 `i - 1` 天
- 而且 `t` 只有 `0 / 1 / 2`

所以没必要整张三维表都存下来。

如果把合法状态展开，其实真正有用的只有 4 个：

- `hold0`：完成 `0` 次交易后，当前持股
- `cash1`：完成 `1` 次交易后，当前空仓
- `hold1`：完成 `1` 次交易后，当前持股
- `cash2`：完成 `2` 次交易后，当前空仓

另外还有一个隐含状态：

- `cash0 = 0`：什么都没做，空仓

之所以不用单独存它，是因为它永远都是 `0`。

### 这 4 个状态分别代表什么

你可以把它们理解成：

```text
hold0 = 第一次买入后
cash1 = 第一次卖出后
hold1 = 第二次买入后
cash2 = 第二次卖出后
```

于是每天更新时，只需要考虑这 4 个状态如何转移。

### 转移怎么来

#### 1. `hold0`

要么之前就已经是第一次买入后的持股状态，
要么今天第一次买入：

```text
hold0 = max(hold0, -price)
```

#### 2. `cash1`

要么之前已经完成过第一次卖出，
要么今天把第一次买入的股票卖掉：

```text
cash1 = max(cash1, hold0 + price)
```

#### 3. `hold1`

要么之前已经完成第一次卖出后又买入了第二次，
要么今天在 `cash1` 基础上买入第二股：

```text
hold1 = max(hold1, cash1 - price)
```

#### 4. `cash2`

要么之前已经完成两次交易，
要么今天卖掉第二次买入的股票：

```text
cash2 = max(cash2, hold1 + price)
```

### 更新时为什么要先保存旧值

因为这 4 个状态都必须基于：

```text
前一天的状态
```

来更新。

如果你边算边覆盖，就有可能把“今天刚更新出的状态”错误拿来继续转移，语义就乱了。

所以要先保存旧值，再统一算新值。

### 代码

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        hold0 = -prices[0]
        cash1 = float("-inf")
        hold1 = float("-inf")
        cash2 = float("-inf")

        for price in prices[1:]:
            prev_hold0 = hold0
            prev_cash1 = cash1
            prev_hold1 = hold1
            prev_cash2 = cash2

            hold0 = max(prev_hold0, -price)
            cash1 = max(prev_cash1, prev_hold0 + price)
            hold1 = max(prev_hold1, prev_cash1 - price)
            cash2 = max(prev_cash2, prev_hold1 + price)

        return max(0, cash1, cash2)
```

### 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

### 评价

这是这道题的最优写法。

优点：

- 时间最优
- 空间最优
- 对固定 `2` 次交易来说，代码非常精炼

缺点：

- 如果前面的三维状态没理解清楚，这一版容易写对了但说不透

所以它更适合作为：

```text
在方法三讲清楚之后，再给出的优化版
```

---

## 哪个方法最适合面试

### 结论

**最适合面试的是：方法三，三维 DP。**

### 原因

#### 方法一：暴力递归

- 适合起步
- 能把“卖出才消耗交易次数”想清楚
- 但会超时

#### 方法二：记忆化递归

- 能通过
- 是递归到 DP 的自然过渡
- 但现场书写一般不如迭代稳

#### 方法三：三维 DP

- 状态定义最清楚
- 第 `122` 题的持股模板可以直接迁移过来
- 很容易继续推广到第 `188` 题
- 最适合面试口述

#### 方法四：状态压缩 DP

- 是最终最优写法
- 但建立在你已经理解三维状态的基础上

所以综合来看：

> **方法三最稳，方法四最优。**

---

## 最适合面试的方法：详细讲解

### 1. 先说清楚这题比 122 难在哪

第 `122` 题里，只要你今天空仓，明天就总还能继续买。

但第 `123` 题不行。

因为如果你已经完成了 2 次交易，哪怕今天空仓：

- 你也不能再买
- 因为次数已经用完了

所以这题真正新增的信息不是：

```text
今天持股还是空仓
```

而是：

```text
已经完成了几次交易
```

### 2. 为什么这里用“已完成交易数”最顺

因为一次完整交易一定是：

```text
买入 -> 卖出
```

所以：

- 买入时，不增加交易数
- 卖出时，交易数 `+1`

这样状态转移非常自然。

### 3. 为什么空仓状态可以来自 `t - 1` 的持股状态

如果今天卖出后完成了第 `t` 次交易，
说明昨天一定是：

- 已完成 `t - 1` 次交易
- 而且手里还持有股票

所以：

```text
dp[i][t][0] = max(dp[i - 1][t][0], dp[i - 1][t - 1][1] + prices[i])
```

### 4. 为什么持股状态的交易次数不变

因为买入不算一笔完整交易。

所以今天买入前后，`t` 不会变化：

```text
dp[i][t][1] = max(dp[i - 1][t][1], dp[i - 1][t][0] - prices[i])
```

### 5. 为什么最后答案只看空仓

因为如果最后一天结束后还持股，
说明你还有一股股票没卖掉，利润没有真正兑现。

所以答案一定只能取：

```text
max(dp[n - 1][t][0] for t in range(3))
```

### 6. 面试时推荐怎么讲

你可以这样说：

> 这题和第 122 题的区别，不在于“持股 / 空仓”的转移规则变了，而在于多了“最多两次交易”的限制。所以我继续保留股票题最核心的两种持股状态：`0 = 空仓`、`1 = 持股`，再额外加一维 `t` 表示已经完成了几次交易。买入不会增加 `t`，卖出才会让 `t + 1`。这样就能很自然地把题意完整编码到状态转移里。

这套讲法很稳，而且很容易顺着推广到第 `188` 题。

### 面试最推荐代码

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        neg_inf = float("-inf")
        dp = [[[neg_inf, neg_inf] for _ in range(3)] for _ in range(n)]

        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0]

        for i in range(1, n):
            for t in range(3):
                dp[i][t][0] = dp[i - 1][t][0]
                if t >= 1:
                    dp[i][t][0] = max(dp[i][t][0], dp[i - 1][t - 1][1] + prices[i])

                dp[i][t][1] = dp[i - 1][t][1]
                if t < 2:
                    dp[i][t][1] = max(dp[i][t][1], dp[i - 1][t][0] - prices[i])

        return max(dp[n - 1][t][0] for t in range(3))
```

---

## 总结

### 递进关系

1. **暴力递归**
   - 先把“卖出才消耗交易次数”想清楚
   - 是最原始的决策树

2. **记忆化递归**
   - 去掉重复状态
   - 从搜索平滑过渡到 DP

3. **三维 DP**
   - 保留第 `122` 题的持股状态主轴
   - 额外补一维“已完成交易数”
   - 最适合面试讲解

4. **状态压缩 DP**
   - 把有限个关键状态压成常数空间
   - 是最终最优写法

### 一句话记忆

> **第 123 题的记法，可以继续沿用第 122 题：`0 = 空仓`、`1 = 持股`；真正新增的是另一维——`t = 已完成几次交易`。**
