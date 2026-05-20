# 方法三：三维 DP
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        neg_inf = float("-inf")
        dp = [[[neg_inf, neg_inf] for _ in range(3)] for _ in range(n)]

        # 与 122 对齐：最后一维 0=空仓，1=持股
        # 第二维 t 表示已经完成了 t 次交易（卖出次数）
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
