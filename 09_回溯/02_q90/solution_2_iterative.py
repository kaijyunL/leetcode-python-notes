class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        """
        解法2：迭代扩展 + 去重范围
        时间复杂度: O(n * 2^n)
        空间复杂度: O(n * 2^n)
        """
        nums.sort()
        ans = [[]]
        start = 0

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                extend_from = start
            else:
                extend_from = 0

            start = len(ans)

            for j in range(extend_from, start):
                ans.append(ans[j] + [num])

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [1, 2, 2],
        [0],
        [1, 1, 1],
        [],
    ]

    for nums in test_cases:
        print(f"输入: nums={nums}, 输出: {solution.subsetsWithDup(nums)}")
