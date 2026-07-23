# 方法2：二分查找（面试主推）


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // cols
            col = mid % cols
            num = matrix[row][col]

            if num == target:
                return True

            if num < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


if __name__ == "__main__":
    solution = Solution()

    assert solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) is True
    assert solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) is False
    assert solution.searchMatrix([[1]], 1) is True
    assert solution.searchMatrix([[1]], 2) is False
    assert solution.searchMatrix([], 1) is False
    assert solution.searchMatrix([[1, 3]], 3) is True
    assert solution.searchMatrix([[1], [3], [5]], 4) is False

    print("all tests passed")
