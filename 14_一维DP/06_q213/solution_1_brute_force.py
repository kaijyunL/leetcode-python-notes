class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_range(left: int, right: int, index: int) -> int:
            if index > right:
                return 0

            not_take = rob_range(left, right, index + 1)
            take = nums[index] + rob_range(left, right, index + 2)
            return max(not_take, take)

        # 环拆成两种线性情况：不偷最后一间，或不偷第一间
        return max(
            rob_range(0, n - 2, 0),
            rob_range(1, n - 1, 1),
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
