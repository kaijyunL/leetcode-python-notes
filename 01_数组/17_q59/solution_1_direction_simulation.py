# 方法1：方向模拟

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        row = 0
        col = 0

        for num in range(1, n * n + 1):
            matrix[row][col] = num

            next_row = row + directions[dir_idx][0]
            next_col = col + directions[dir_idx][1]

            if not (0 <= next_row < n and 0 <= next_col < n and matrix[next_row][next_col] == 0):
                dir_idx = (dir_idx + 1) % 4
                next_row = row + directions[dir_idx][0]
                next_col = col + directions[dir_idx][1]

            row, col = next_row, next_col

        return matrix


if __name__ == "__main__":
    solution = Solution()

    assert solution.generateMatrix(1) == [[1]]
    assert solution.generateMatrix(2) == [[1, 2], [4, 3]]
    assert solution.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    assert solution.generateMatrix(4) == [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]

    print("all tests passed")
