# 方法一：暴力递归
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        def dfs(day: int, holding: bool) -> int:
            if day == n:
                return 0 if not holding else float("-inf")

            best = dfs(day + 1, holding)
            if holding:
                best = max(best, prices[day] + dfs(day + 1, False))
            else:
                best = max(best, -prices[day] + dfs(day + 1, True))

            return best

        return dfs(0, False)


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [1, 2, 3, 4, 5],
        [7, 6, 4, 3, 1],
        [1],
    ]

    for prices in test_cases:
        print(f"prices={prices}, profit={solver.maxProfit(prices)}")
