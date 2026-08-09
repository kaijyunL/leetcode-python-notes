# 方法4：归并排序（面试主推）


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        temp = [0] * len(nums)

        def merge_sort(left, right):
            if left >= right:
                return

            mid = left + (right - left) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)

            i = left
            j = mid + 1
            k = left

            # 两个子区间已经有序，用双指针把它们合并到 temp。
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

    assert solution.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]
    assert solution.sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
    assert solution.sortArray([]) == []
    assert solution.sortArray([-1, 5, 3, 4, 0]) == [-1, 0, 3, 4, 5]
    assert solution.sortArray([2, 2, 2]) == [2, 2, 2]

    print("all tests passed")
