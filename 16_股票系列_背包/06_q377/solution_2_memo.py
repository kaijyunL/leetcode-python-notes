from typing import List


# 方法二：记忆化递归
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(remain):
            if remain == 0:
                return 1
            if remain in memo:
                return memo[remain]

            ways = 0
            # 枚举最后一个位置放哪个数
            for num in nums:
                if num <= remain:
                    ways += dfs(remain - num)

            memo[remain] = ways
            return ways

        return dfs(target)


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
