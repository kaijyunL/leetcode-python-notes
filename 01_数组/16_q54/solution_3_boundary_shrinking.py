# 方法3：边界收缩（面试主推）

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        ans = []

        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                ans.append(matrix[top][col])
            top += 1

            for row in range(top, bottom + 1):
                ans.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    ans.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    ans.append(matrix[row][left])
                left += 1

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
