# 方法四：状态压缩 DP
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        # cash0 恒为 0，因此不单独存储
        hold0 = -prices[0]          # 完成0次交易后持股
        cash1 = float("-inf")      # 完成1次交易后空仓
        hold1 = float("-inf")      # 完成1次交易后持股
        cash2 = float("-inf")      # 完成2次交易后空仓

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


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [3, 3, 5, 0, 0, 3, 1, 4],
        [1, 2, 3, 4, 5],
        [7, 6, 4, 3, 1],
        [1],
        [2, 1, 2, 0, 1],
        [6, 1, 3, 2, 4, 7],
    ]

    for prices in test_cases:
        print(f"prices={prices}, profit={solver.maxProfit(prices)}")
