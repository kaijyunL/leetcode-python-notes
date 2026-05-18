from typing import List


# 方法二：记忆化递归
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(index, current_sum):
            if index == len(nums):
                return 1 if current_sum == target else 0

            key = (index, current_sum)
            if key in memo:
                return memo[key]

            memo[key] = dfs(index + 1, current_sum + nums[index]) + dfs(index + 1, current_sum - nums[index])
            return memo[key]

        return dfs(0, 0)


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
