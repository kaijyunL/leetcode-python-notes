class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """
        基数排序：按十进制位从低到高排序，额外处理负数
        时间复杂度: O(d * n)
        空间复杂度: O(n)
        """
        positives = [num for num in nums if num >= 0]
        negatives = [-num for num in nums if num < 0]

        self._radix_sort_non_negative(positives)
        self._radix_sort_non_negative(negatives)

        nums[:] = [-num for num in reversed(negatives)] + positives
        return nums

    def _radix_sort_non_negative(self, nums: list[int]) -> None:
        if not nums:
            return

        max_num = max(nums)
        exp = 1

        while max_num // exp > 0:
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

    test_cases = [
        [5, 2, 3, 1],
        [5, 1, 1, 2, 0, 0],
        [],
        [1],
        [-1, 5, 3, 4, 0],
        [2, 2, 2],
    ]

    for nums in test_cases:
        print(f"nums = {nums}, result = {solution.sortArray(nums[:])}")
