from typing import List


# 方法一：暴力递归
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(i, prev_index):
            if i == n:
                return 0

            best = dfs(i + 1, prev_index)

            if prev_index == -1 or nums[i] > nums[prev_index]:
                best = max(best, 1 + dfs(i + 1, i))

            return best

        return dfs(0, -1)


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [10, 9, 2, 5, 3, 7, 101, 18],
        [0, 1, 0, 3, 2, 3],
        [7, 7, 7, 7, 7, 7, 7],
    ]

    for nums in test_cases:
        print(f"nums={nums}, lis={solver.lengthOfLIS(nums)}")
