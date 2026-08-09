# 方法9：基数排序


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        positives = [num for num in nums if num >= 0]
        negatives = [-num for num in nums if num < 0]

        self._radix_sort_non_negative(positives)
        self._radix_sort_non_negative(negatives)

        nums[:] = [-num for num in reversed(negatives)] + positives
        return nums

    def _radix_sort_non_negative(self, nums: list[int]) -> None:
        if not nums:
            return

        max_value = max(nums)
        exp = 1

        while max_value // exp > 0:
            buckets = [[] for _ in range(10)]

            for num in nums:
                digit = (num // exp) % 10
                buckets[digit].append(num)

            index = 0
            for bucket in buckets:
                for num in bucket:
                    nums[index] = num
                    index += 1

            exp *= 10


if __name__ == "__main__":
    solution = Solution()

    assert solution.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]
    assert solution.sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
    assert solution.sortArray([]) == []
    assert solution.sortArray([-1, 5, 3, 4, 0]) == [-1, 0, 3, 4, 5]
    assert solution.sortArray([-170, 45, -75, 90, 802, 24, 2, 66]) == [-170, -75, 2, 24, 45, 66, 90, 802]

    print("all tests passed")
