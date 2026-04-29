class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        temp = [0] * len(nums)

        def merge_sort(left: int, right: int) -> None:
            if left >= right:
                return

            mid = left + (right - left) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)

            i, j, k = left, mid + 1, left

            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1
                k += 1

            while i <= mid:
                temp[k] = nums[i]
                i += 1
                k += 1

            while j <= right:
                temp[k] = nums[j]
                j += 1
                k += 1

            nums[left : right + 1] = temp[left : right + 1]

        merge_sort(0, len(nums) - 1)
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
