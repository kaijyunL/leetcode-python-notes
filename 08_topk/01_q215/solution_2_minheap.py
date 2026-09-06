import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        方法2：大小为 k 的最小堆（Top K 通用解）
        时间复杂度：O(n log k)
        空间复杂度：O(k)
        """
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)

        return heap[0]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([7, 9, 2, 8, 1], 3, 7),
        ([5, 5, 5], 2, 5),
    ]

    for nums, k, expected in test_cases:
        assert solution.findKthLargest(nums, k) == expected

    print("all tests passed")
