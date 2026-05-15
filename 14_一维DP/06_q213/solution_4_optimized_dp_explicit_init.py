class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_line(left, right):
            if left == right:
                return nums[left]

            dp_i_2 = nums[left]
            dp_i_1 = max(nums[left], nums[left + 1])

            for i in range(left + 2, right + 1):
                curr = max(dp_i_1, dp_i_2 + nums[i])
                dp_i_2 = dp_i_1
                dp_i_1 = curr

            return dp_i_1

        return max(
            rob_line(0, n - 2),
            rob_line(1, n - 1),
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
