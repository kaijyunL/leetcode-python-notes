class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        解法1：递归复制剩余列表
        时间复杂度: O(n * n!)
        空间复杂度: O(n * n!)
        """
        ans = []

        def dfs(path: list[int], remaining: list[int]) -> None:
            if not remaining:
                ans.append(path[:])
                return

            for i, num in enumerate(remaining):
                dfs(path + [num], remaining[:i] + remaining[i + 1:])

        dfs([], nums)
        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [1, 2, 3],
        [0, 1],
        [1],
    ]

    for nums in test_cases:
        print(f"输入: nums={nums}, 输出: {solution.permute(nums)}")
