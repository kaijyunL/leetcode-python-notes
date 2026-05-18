from typing import List


# 方法二：记忆化递归
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        memo = {}

        def dfs(index, remain):
            if remain == 0:
                return True
            if index == len(nums) or remain < 0:
                return False

            key = (index, remain)
            if key in memo:
                return memo[key]

            memo[key] = dfs(index + 1, remain - nums[index]) or dfs(index + 1, remain)
            return memo[key]

        return dfs(0, target)


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
