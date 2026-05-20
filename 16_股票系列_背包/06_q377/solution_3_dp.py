from typing import List


# 方法三：一维 DP
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1  # 凑出 0：什么都不放，1 种方式

        # 外层枚举目标值，内层枚举最后一个数
        for total in range(1, target + 1):
            for num in nums:
                if num <= total:
                    dp[total] += dp[total - num]

        return dp[target]


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ([1, 2, 3], 4),
        ([9], 3),
        ([2, 3, 5], 8),
        ([4, 2, 1], 10),
    ]

    for nums, target in test_cases:
        print(f"nums={nums}, target={target}, ways={solver.combinationSum4(nums, target)}")
