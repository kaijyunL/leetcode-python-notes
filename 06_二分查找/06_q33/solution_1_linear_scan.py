# 方法1：线性扫描


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for index, num in enumerate(nums):
            if num == target:
                return index

        return -1


if __name__ == "__main__":
    solution = Solution()

    assert solution.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert solution.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert solution.search([1], 0) == -1
    assert solution.search([1], 1) == 0
    assert solution.search([3, 1], 1) == 1
    assert solution.search([5, 1, 3], 5) == 0

    print("all tests passed")
