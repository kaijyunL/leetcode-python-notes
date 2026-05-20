class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp_i_2 = 0
        dp_i_1 = 0

        for i in range(n):
            curr = max(dp_i_1, dp_i_2 + nums[i])
            dp_i_2 = dp_i_1
            dp_i_1 = curr

        return dp_i_1


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
