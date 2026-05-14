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


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
    ]

    for prices in test_cases:
        print(f"prices={prices}, profit={solver.maxProfit(prices)}")
