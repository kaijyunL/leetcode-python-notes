# 方法1：辅助矩阵

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        new_matrix = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                new_matrix[j][n - 1 - i] = matrix[i][j]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = new_matrix[i][j]


if __name__ == "__main__":
    solution = Solution()

    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution.rotate(matrix1)
    assert matrix1 == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    solution.rotate(matrix2)
    assert matrix2 == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

    matrix3 = [[1]]
    solution.rotate(matrix3)
    assert matrix3 == [[1]]

    matrix4 = [[1, 2], [3, 4]]
    solution.rotate(matrix4)
    assert matrix4 == [[3, 1], [4, 2]]

    print("all tests passed")
