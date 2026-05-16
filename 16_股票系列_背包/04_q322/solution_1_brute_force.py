from typing import List


# 方法一：暴力递归
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(remain: int) -> int:
            if remain == 0:
                return 0
            if remain < 0:
                return float("inf")

            best = float("inf")
            for coin in coins:
                best = min(best, dfs(remain - coin) + 1)

            return best

        answer = dfs(amount)
        return -1 if answer == float("inf") else answer


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ([1, 2, 5], 11),
        ([2], 3),
        ([1], 0),
    ]

    for coins, amount in test_cases:
        print(f"coins={coins}, amount={amount}, answer={solver.coinChange(coins, amount)}")
