# 方法3：用第一行和第一列做原地标记（面试主推）

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False

        for col in range(n):
            if matrix[0][col] == 0:
                first_row_has_zero = True
                break

        for row in range(m):
            if matrix[row][0] == 0:
                first_col_has_zero = True
                break

        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if first_row_has_zero:
            for col in range(n):
                matrix[0][col] = 0

        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0


def run_case(matrix, expected):
    actual = [row[:] for row in matrix]
    Solution().setZeroes(actual)
    assert actual == expected


if __name__ == "__main__":
    run_case(
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
    )
    run_case(
        [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
        [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
    )
    run_case([[1, 0, 3]], [[0, 0, 0]])
    run_case([[1], [0], [3]], [[0], [0], [0]])
    run_case([[0]], [[0]])

    print("all tests passed")
