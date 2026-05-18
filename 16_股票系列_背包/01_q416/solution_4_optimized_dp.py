from typing import List


# 方法四：一维优化 DP
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for current in range(target, num - 1, -1):
                dp[current] = dp[current] or dp[current - num]

        return dp[target]


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [1, 5, 11, 5],
        [1, 2, 3, 5],
        [2, 2, 1, 1],
        [1, 2, 5],
    ]

    for nums in test_cases:
        print(f"nums={nums}, can_partition={solver.canPartition(nums)}")
