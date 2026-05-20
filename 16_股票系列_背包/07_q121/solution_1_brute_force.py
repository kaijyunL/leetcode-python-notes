class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        best = 0

        for i in range(n):
            for j in range(i + 1, n):
                best = max(best, prices[j] - prices[i])

        return best


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
    ]

    for prices in test_cases:
        print(f"prices={prices}, profit={solver.maxProfit(prices)}")
