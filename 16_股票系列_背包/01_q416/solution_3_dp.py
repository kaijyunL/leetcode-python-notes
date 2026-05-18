from typing import List


# 方法三：二维 DP
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            num = nums[i - 1]
            dp[i][0] = True
            for current in range(1, target + 1):
                dp[i][current] = dp[i - 1][current]
                if current >= num:
                    dp[i][current] = dp[i][current] or dp[i - 1][current - num]

        return dp[n][target]


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
