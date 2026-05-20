from typing import List


# 方法三：二维 DP
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            coin = coins[i - 1]
            for total in range(1, amount + 1):
                dp[i][total] = dp[i - 1][total]
                if total >= coin:
                    dp[i][total] += dp[i][total - coin]

        return dp[n][amount]


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
