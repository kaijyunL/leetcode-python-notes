# 方法1：线性扫描


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i

        return len(nums)


if __name__ == "__main__":
    solution = Solution()

    assert solution.searchInsert([1, 3, 5, 6], 5) == 2
    assert solution.searchInsert([1, 3, 5, 6], 2) == 1
    assert solution.searchInsert([1, 3, 5, 6], 7) == 4
    assert solution.searchInsert([1, 3, 5, 6], 0) == 0
    assert solution.searchInsert([], 3) == 0

    print("all tests passed")
