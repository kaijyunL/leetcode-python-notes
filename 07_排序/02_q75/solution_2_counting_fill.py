# 方法2：计数后回填


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        方法2：计数后回填
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        counts = [0] * 3

        for color in nums:
            counts[color] += 1

        write = 0
        for color, count in enumerate(counts):
            for _ in range(count):
                nums[write] = color
                write += 1


if __name__ == "__main__":
    solution = Solution()

    nums = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]

    nums = [2, 0, 1]
    solution.sortColors(nums)
    assert nums == [0, 1, 2]

    nums = [2, 2, 1, 1, 0, 0]
    solution.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]

    print("all tests passed")
