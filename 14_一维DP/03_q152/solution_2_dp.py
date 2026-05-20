# 方法二：动态规划
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        max_dp = [0] * n
        min_dp = [0] * n

        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        best = nums[0]

        for i in range(1, n):
            num = nums[i]
            max_dp[i] = max(num, max_dp[i - 1] * num, min_dp[i - 1] * num)
            min_dp[i] = min(num, max_dp[i - 1] * num, min_dp[i - 1] * num)
            best = max(best, max_dp[i])

        return best


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [2, 3, -2, 4],
        [-2, 0, -1],
        [-2, 3, -4],
        [-2],
    ]

    for nums in test_cases:
        print(f"nums={nums}, max_product={solver.maxProduct(nums)}")
