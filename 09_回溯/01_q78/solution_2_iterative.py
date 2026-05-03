class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        解法2：迭代扩展
        时间复杂度: O(n * 2^n)
        空间复杂度: O(n * 2^n)
        """
        ans = [[]]

        for num in nums:
            new_subsets = []
            for subset in ans:
                new_subsets.append(subset + [num])
            ans.extend(new_subsets)

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [1, 2, 3],
        [0],
        [],
    ]

    for nums in test_cases:
        print(f"输入: nums={nums}, 输出: {solution.subsets(nums)}")
