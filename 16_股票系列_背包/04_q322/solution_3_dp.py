from typing import List


# 方法三：动态规划
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount

        for total in range(1, amount + 1):
            for coin in coins:
                if coin <= total:
                    dp[total] = min(dp[total], dp[total - coin] + 1)

        return -1 if dp[amount] == amount + 1 else dp[amount]


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
