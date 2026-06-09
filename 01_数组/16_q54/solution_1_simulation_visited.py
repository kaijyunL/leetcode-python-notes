# 方法1：模拟行走 + visited

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        total = m * n
        visited = [[False] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        row = 0
        col = 0
        ans = []

        for _ in range(total):
            ans.append(matrix[row][col])
            visited[row][col] = True

            next_row = row + directions[dir_idx][0]
            next_col = col + directions[dir_idx][1]

            if (
                next_row < 0
                or next_row >= m
                or next_col < 0
                or next_col >= n
                or visited[next_row][next_col]
            ):
                dir_idx = (dir_idx + 1) % 4
                next_row = row + directions[dir_idx][0]
                next_col = col + directions[dir_idx][1]

            row, col = next_row, next_col

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert solution.spiralOrder([[1, 2, 3, 4]]) == [1, 2, 3, 4]
    assert solution.spiralOrder([[1], [2], [3]]) == [1, 2, 3]
    assert solution.spiralOrder([[1]]) == [1]
    assert solution.spiralOrder([[1, 2], [3, 4]]) == [1, 2, 4, 3]

    print("all tests passed")
