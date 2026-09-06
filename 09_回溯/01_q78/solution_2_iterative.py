class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        方法2：迭代扩展（简洁构造）
        时间复杂度：O(n * 2^n)
        空间复杂度：O(n * 2^n)
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
        ([1, 2, 3], {(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)}),
        ([0], {(), (0,)}),
        ([], {()}),
    ]

    for nums, expected in test_cases:
        actual = {tuple(subset) for subset in solution.subsets(nums)}
        assert actual == expected

    print("all tests passed")
