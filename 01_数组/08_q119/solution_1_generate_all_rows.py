# 方法1：先生成前面所有行

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []

        for row in range(rowIndex + 1):
            current_row = [1] * (row + 1)
            for col in range(1, row):
                current_row[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
            triangle.append(current_row)

        return triangle[rowIndex]


if __name__ == "__main__":
    solution = Solution()

    assert solution.getRow(0) == [1]
    assert solution.getRow(1) == [1, 1]
    assert solution.getRow(3) == [1, 3, 3, 1]
    assert solution.getRow(4) == [1, 4, 6, 4, 1]

    print("all tests passed")
