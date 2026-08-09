# 方法6：堆排序


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        def sift_down(root: int, heap_size: int) -> None:
            while True:
                child = root * 2 + 1

                if child >= heap_size:
                    break

                # 选择两个孩子中较大的一个，与根比较。
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

    assert solution.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]
    assert solution.sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
    assert solution.sortArray([]) == []
    assert solution.sortArray([-1, 5, 3, 4, 0]) == [-1, 0, 3, 4, 5]
    assert solution.sortArray([2, 2, 2]) == [2, 2, 2]

    print("all tests passed")
