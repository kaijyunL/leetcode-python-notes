# 方法三：二维 DP
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[0, 0] for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[n - 1][0]


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
