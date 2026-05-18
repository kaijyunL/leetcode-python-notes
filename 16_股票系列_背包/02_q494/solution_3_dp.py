from typing import List


# 方法三：二维 DP
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total or (total + target) % 2 == 1:
            return 0

        positive = (total + target) // 2
        n = len(nums)
        dp = [[0] * (positive + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            num = nums[i - 1]
            for current in range(positive + 1):
                dp[i][current] = dp[i - 1][current]
                if current >= num:
                    dp[i][current] += dp[i - 1][current - num]

        return dp[n][positive]


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ([1, 1, 1, 1, 1], 3),
        ([1], 1),
        ([1], 2),
        ([2, 1], 1),
    ]

    for nums, target in test_cases:
        print(f"nums={nums}, target={target}, ways={solver.findTargetSumWays(nums, target)}")
