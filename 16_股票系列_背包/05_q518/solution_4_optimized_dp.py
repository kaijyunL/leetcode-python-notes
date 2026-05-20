from typing import List


# 方法四：一维优化 DP
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for total in range(coin, amount + 1):
                dp[total] += dp[total - coin]

        return dp[amount]


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        (5, [1, 2, 5]),
        (3, [2]),
        (10, [10]),
        (0, [1, 2, 5]),
        (100, [1, 5, 10, 25]),
    ]

    for amount, coins in test_cases:
        print(f"amount={amount}, coins={coins}, ways={solver.change(amount, coins)}")
