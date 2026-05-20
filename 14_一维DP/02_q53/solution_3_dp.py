class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        best = dp[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            best = max(best, dp[i])

        return best


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1],
        [5, 4, -1, 7, 8],
        [-1, -2, -3],
    ]

    for nums in test_cases:
        print(f"nums={nums}, max_sum={solver.maxSubArray(nums)}")
