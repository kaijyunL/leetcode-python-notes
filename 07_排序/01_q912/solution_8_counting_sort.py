# 方法8：计数排序


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        min_num = min(nums)
        max_num = max(nums)
        counts = [0] * (max_num - min_num + 1)

        for num in nums:
            counts[num - min_num] += 1

        index = 0
        for offset, count in enumerate(counts):
            num = offset + min_num
            for _ in range(count):
                nums[index] = num
                index += 1

        return nums


if __name__ == "__main__":
    solution = Solution()

    assert solution.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]
    assert solution.sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
    assert solution.sortArray([]) == []
    assert solution.sortArray([-1, 5, 3, 4, 0]) == [-1, 0, 3, 4, 5]
    assert solution.sortArray([-2, 3, -2, 1]) == [-2, -2, 1, 3]

    print("all tests passed")
