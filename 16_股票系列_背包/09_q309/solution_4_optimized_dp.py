# 方法四：状态压缩 DP
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        # 与 122 对齐：0=rest（空仓/可买），1=hold（持股），2=sold（刚卖出）
        rest = 0
        hold = -prices[0]
        sold = float("-inf")

        for price in prices[1:]:
            prev_rest = rest
            prev_hold = hold
            prev_sold = sold

            rest = max(prev_rest, prev_sold)
            hold = max(prev_hold, prev_rest - price)
            sold = prev_hold + price

        return max(rest, sold)


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [1, 2, 3, 0, 2],
        [1],
        [2, 1, 2, 0, 1],
        [2, 1, 4],
        [6, 1, 3, 2, 4, 7],
    ]

    for prices in test_cases:
        print(f"prices={prices}, profit={solver.maxProfit(prices)}")
