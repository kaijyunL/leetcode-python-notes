# 方法1：记录所有初始 0 的坐标

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        zero_positions = []

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zero_positions.append((row, col))

        for zero_row, zero_col in zero_positions:
            for col in range(n):
                matrix[zero_row][col] = 0
            for row in range(m):
                matrix[row][zero_col] = 0


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

    print("all tests passed")
