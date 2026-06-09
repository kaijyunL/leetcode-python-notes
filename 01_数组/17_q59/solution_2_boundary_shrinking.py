# 方法2：边界收缩（面试主推）

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        num = 1
        target = n * n

        while num <= target:
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1

            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1

            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1

            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1

        return matrix


if __name__ == "__main__":
    solution = Solution()

    assert solution.generateMatrix(1) == [[1]]
    assert solution.generateMatrix(2) == [[1, 2], [4, 3]]
    assert solution.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    assert solution.generateMatrix(4) == [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]

    print("all tests passed")
