from typing import List


# 方法二：记忆化递归
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remain: int) -> int:
            if remain == 0:
                return 0
            if remain < 0:
                return float("inf")
            if remain in memo:
                return memo[remain]

            best = float("inf")
            for coin in coins:
                best = min(best, dfs(remain - coin) + 1)

            memo[remain] = best
            return best

        answer = dfs(amount)
        return -1 if answer == float("inf") else answer


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ([1, 2, 5], 11),
        ([2], 3),
        ([1], 0),
        ([2, 5, 10, 1], 27),
    ]

    for coins, amount in test_cases:
        print(f"coins={coins}, amount={amount}, answer={solver.coinChange(coins, amount)}")
