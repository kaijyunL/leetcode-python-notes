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


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
    ]

    for prices in test_cases:
        print(f"prices={prices}, profit={solver.maxProfit(prices)}")
