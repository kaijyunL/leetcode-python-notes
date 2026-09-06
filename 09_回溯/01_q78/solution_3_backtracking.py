class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        方法3：回溯（面试主推）
        时间复杂度：O(n * 2^n)
        空间复杂度：O(n * 2^n)
        """
        ans = []
        path = []

        def backtrack(start: int) -> None:
            ans.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
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
