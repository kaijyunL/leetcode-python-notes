# 方法二：记忆化递归
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        memo = {}

        def dfs(day: int, holding: bool) -> int:
            if day == n:
                return 0 if not holding else float("-inf")

            key = (day, holding)
            if key in memo:
                return memo[key]

            best = dfs(day + 1, holding)
            if holding:
                best = max(best, prices[day] + dfs(day + 1, False))
            else:
                best = max(best, -prices[day] + dfs(day + 1, True))

            memo[key] = best
            return best

        return dfs(0, False)


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
