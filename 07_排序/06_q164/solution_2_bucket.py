class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        """
        方法2：桶 + 鸽笼原理（面试主推）
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if len(nums) < 2:
            return 0

        min_value = min(nums)
        max_value = max(nums)

        if min_value == max_value:
            return 0

        n = len(nums)
        value_range = max_value - min_value
        bucket_size = (value_range + n - 2) // (n - 1)
        bucket_count = value_range // bucket_size + 1

        bucket_min = [None] * bucket_count
        bucket_max = [None] * bucket_count

        for num in nums:
            bucket_index = (num - min_value) // bucket_size

            if bucket_min[bucket_index] is None:
                bucket_min[bucket_index] = num
                bucket_max[bucket_index] = num
            else:
                bucket_min[bucket_index] = min(bucket_min[bucket_index], num)
                bucket_max[bucket_index] = max(bucket_max[bucket_index], num)

        max_gap = 0
        previous_max = None

        for i in range(bucket_count):
            if bucket_min[i] is None:
                continue

            if previous_max is not None:
                max_gap = max(max_gap, bucket_min[i] - previous_max)

            previous_max = bucket_max[i]

        return max_gap


if __name__ == "__main__":
    solution = Solution()

    assert solution.maximumGap([3, 6, 9, 1]) == 3
    assert solution.maximumGap([10]) == 0
    assert solution.maximumGap([1, 1, 1, 1]) == 0
    assert solution.maximumGap([1, 10_000_000]) == 9_999_999
    assert solution.maximumGap([]) == 0
    assert solution.maximumGap([1, 3, 100]) == 97
    assert solution.maximumGap([1, 2, 3, 4, 100]) == 96

    print("all tests passed")
