# 方法三：三状态 DP
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[0, 0, 0] for _ in range(n)]

        # 与 122 对齐：0=空仓/可买，1=持股，2=刚卖出
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = float("-inf")

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = dp[i - 1][1] + prices[i]

        return max(dp[n - 1][0], dp[n - 1][2])


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
