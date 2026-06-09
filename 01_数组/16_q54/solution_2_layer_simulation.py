# 方法2：逐层模拟

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        layers = (min(m, n) + 1) // 2
        ans = []

        for layer in range(layers):
            top = layer
            bottom = m - 1 - layer
            left = layer
            right = n - 1 - layer

            for col in range(left, right + 1):
                ans.append(matrix[top][col])

            for row in range(top + 1, bottom + 1):
                ans.append(matrix[row][right])

            if top < bottom:
                for col in range(right - 1, left - 1, -1):
                    ans.append(matrix[bottom][col])

            if left < right:
                for row in range(bottom - 1, top, -1):
                    ans.append(matrix[row][left])

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
