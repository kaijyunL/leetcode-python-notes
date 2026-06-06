# 方法1：递归定义 + 记忆化

from functools import lru_cache
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        @lru_cache(None)
        def value(row, col):
            if col == 0 or col == row:
                return 1
            return value(row - 1, col - 1) + value(row - 1, col)

        triangle = []

        for row in range(numRows):
            current_row = []
            for col in range(row + 1):
                current_row.append(value(row, col))
            triangle.append(current_row)

        return triangle


if __name__ == "__main__":
    solution = Solution()

    assert solution.generate(1) == [[1]]
    assert solution.generate(2) == [[1], [1, 1]]
    assert solution.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    print("all tests passed")
