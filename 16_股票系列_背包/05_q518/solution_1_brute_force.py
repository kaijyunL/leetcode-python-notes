from typing import List


# 方法一：暴力递归
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dfs(index, remain):
            if remain == 0:
                return 1
            if remain < 0 or index == len(coins):
                return 0

            return dfs(index + 1, remain) + dfs(index, remain - coins[index])

        return dfs(0, amount)


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        (5, [1, 2, 5]),
        (3, [2]),
        (10, [10]),
        (0, [1, 2, 5]),
    ]

    for amount, coins in test_cases:
        print(f"amount={amount}, coins={coins}, ways={solver.change(amount, coins)}")
