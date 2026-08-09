# 方法1：内置排序（题外对照，不可提交）


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        方法1：内置排序（题外对照，不可提交）
        时间复杂度：通常为 O(n log n)
        空间复杂度：取决于语言库实现
        """
        nums.sort()


if __name__ == "__main__":
    solution = Solution()

    nums = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]

    nums = [2, 0, 1]
    solution.sortColors(nums)
    assert nums == [0, 1, 2]

    nums = [0, 0, 0]
    solution.sortColors(nums)
    assert nums == [0, 0, 0]

    print("all tests passed")
