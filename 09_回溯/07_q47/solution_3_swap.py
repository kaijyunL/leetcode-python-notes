class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        """
        解法3：原地交换 + 每层 set 去重
        时间复杂度: O(n * n!)
        空间复杂度: O(n * n!)
        """
        ans = []

        def backtrack(first: int) -> None:
            if first == len(nums):
                ans.append(nums[:])
                return

            seen = set()
            for i in range(first, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])

                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack(0)
        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [1, 1, 2],
        [1, 2, 3],
        [1],
    ]

    for nums in test_cases:
        print(f"输入: nums={nums}, 输出: {solution.permuteUnique(nums)}")
