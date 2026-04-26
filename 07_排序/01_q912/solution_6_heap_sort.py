class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """
        堆排序：建最大堆后不断把堆顶放到末尾
        时间复杂度: O(n log n)
        空间复杂度: O(1)
        """
        n = len(nums)

        def sift_down(root: int, heap_size: int) -> None:
            while True:
                child = root * 2 + 1

                if child >= heap_size:
                    break

                if child + 1 < heap_size and nums[child + 1] > nums[child]:
                    child += 1

                if nums[root] >= nums[child]:
                    break

                nums[root], nums[child] = nums[child], nums[root]
                root = child

        for root in range(n // 2 - 1, -1, -1):
            sift_down(root, n)

        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            sift_down(0, end)

        return nums


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
