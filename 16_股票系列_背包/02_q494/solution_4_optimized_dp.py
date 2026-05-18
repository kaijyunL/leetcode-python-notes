from typing import List


# 方法四：一维优化 DP
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total or (total + target) % 2 == 1:
            return 0

        positive = (total + target) // 2
        dp = [0] * (positive + 1)
        dp[0] = 1

        for num in nums:
            for current in range(positive, num - 1, -1):
                dp[current] += dp[current - num]

        return dp[positive]


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
