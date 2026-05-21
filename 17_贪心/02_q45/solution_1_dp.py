# 方法1：动态规划
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [float("inf")] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [2, 3, 1, 1, 4],
        [2, 3, 0, 1, 4],
        [1],
        [1, 2],
        [1, 1, 1, 1],
    ]

    for nums in test_cases:
        print(f"nums={nums}, min_jumps={solver.jump(nums)}")
