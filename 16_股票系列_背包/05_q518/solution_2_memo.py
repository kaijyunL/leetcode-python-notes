from typing import List


# 方法二：记忆化递归
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(index, remain):
            if remain == 0:
                return 1
            if remain < 0 or index == len(coins):
                return 0

            key = (index, remain)
            if key in memo:
                return memo[key]

            memo[key] = dfs(index + 1, remain) + dfs(index, remain - coins[index])
            return memo[key]

        return dfs(0, amount)


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
