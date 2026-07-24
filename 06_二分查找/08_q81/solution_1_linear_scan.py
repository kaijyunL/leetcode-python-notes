# 方法1：线性扫描


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        for num in nums:
            if num == target:
                return True

        return False


if __name__ == "__main__":
    solution = Solution()

    assert solution.search([2, 5, 6, 0, 0, 1, 2], 0) is True
    assert solution.search([2, 5, 6, 0, 0, 1, 2], 3) is False
    assert solution.search([1, 0, 1, 1, 1], 0) is True
    assert solution.search([1, 1, 1, 1, 1], 2) is False
    assert solution.search([1], 1) is True
    assert solution.search([1, 3, 1, 1, 1], 3) is True

    print("all tests passed")
