# 方法2：逐层旋转

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer

            for i in range(first, last):
                offset = i - first
                top = matrix[first][i]

                matrix[first][i] = matrix[last - offset][first]
                matrix[last - offset][first] = matrix[last][last - offset]
                matrix[last][last - offset] = matrix[i][last]
                matrix[i][last] = top


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
