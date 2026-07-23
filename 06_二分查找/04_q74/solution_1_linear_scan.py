# 方法1：线性扫描


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        for row in matrix:
            for num in row:
                if num == target:
                    return True

        return False


if __name__ == "__main__":
    solution = Solution()

    assert solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) is True
    assert solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) is False
    assert solution.searchMatrix([[1]], 1) is True
    assert solution.searchMatrix([[1]], 2) is False
    assert solution.searchMatrix([], 1) is False

    print("all tests passed")
