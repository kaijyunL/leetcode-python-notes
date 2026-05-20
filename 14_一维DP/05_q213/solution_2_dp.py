class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_line(arr):
            if not arr:
                return 0
            if len(arr) == 1:
                return arr[0]

            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

            return dp[-1]

        return max(
            rob_line(nums[:-1]),
            rob_line(nums[1:]),
        )


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [2, 3, 2],
        [1, 2, 3, 1],
        [1, 2, 3],
        [1],
    ]

    for nums in test_cases:
        print(f"nums={nums}, max_money={solver.rob(nums)}")
