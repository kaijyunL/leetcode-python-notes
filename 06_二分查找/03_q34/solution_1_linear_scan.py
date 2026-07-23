# 方法1：线性扫描


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = -1
        end = -1

        for i, num in enumerate(nums):
            if num == target:
                if start == -1:
                    start = i
                end = i

        return [start, end]


if __name__ == "__main__":
    solution = Solution()

    assert solution.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert solution.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert solution.searchRange([], 0) == [-1, -1]
    assert solution.searchRange([1], 1) == [0, 0]
    assert solution.searchRange([2, 2], 2) == [0, 1]

    print("all tests passed")
