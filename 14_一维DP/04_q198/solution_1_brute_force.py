# 方法一：暴力递归
class Solution:
    def rob(self, nums: list[int]) -> int:
        def dfs(i: int) -> int:
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            return max(dfs(i - 1), dfs(i - 2) + nums[i])

        n = len(nums)
        if n == 1:
            return nums[0]
        return dfs(n - 1)


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [1, 2, 3, 1],
        [2, 7, 9, 3, 1],
        [2, 1, 1, 2],
        [5],
    ]

    for nums in test_cases:
        print(f"nums={nums}, max_money={solver.rob(nums)}")
