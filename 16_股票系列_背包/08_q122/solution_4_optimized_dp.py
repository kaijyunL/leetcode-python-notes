# 方法四：状态压缩 DP
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        cash = 0
        hold = -prices[0]

        for price in prices[1:]:
            prev_cash = cash
            prev_hold = hold
            cash = max(prev_cash, prev_hold + price)
            hold = max(prev_hold, prev_cash - price)

        return cash


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [1, 2, 3, 4, 5],
        [7, 6, 4, 3, 1],
        [1],
        [2, 1, 2, 0, 1],
    ]

    for prices in test_cases:
        print(f"prices={prices}, profit={solver.maxProfit(prices)}")
