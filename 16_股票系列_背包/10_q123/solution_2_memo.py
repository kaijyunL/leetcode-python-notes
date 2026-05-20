# 方法二：记忆化递归
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        memo = {}

        def dfs(day: int, remain: int, holding: bool) -> int:
            if day == n:
                return 0 if not holding else float("-inf")
            if remain == 0:
                return 0 if not holding else float("-inf")

            key = (day, remain, holding)
            if key in memo:
                return memo[key]

            best = dfs(day + 1, remain, holding)
            if holding:
                best = max(best, prices[day] + dfs(day + 1, remain - 1, False))
            else:
                best = max(best, -prices[day] + dfs(day + 1, remain, True))

            memo[key] = best
            return best

        return dfs(0, 2, False)


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
