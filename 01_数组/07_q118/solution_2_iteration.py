# 方法2：按行迭代构造（面试主推）

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row in range(numRows):
            cur_row = [1] * (row + 1)
            for col in range(1, row):
                cur_row[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
            triangle.append(cur_row)

        return triangle


if __name__ == "__main__":
    solution = Solution()

    assert solution.generate(1) == [[1]]
    assert solution.generate(2) == [[1], [1, 1]]
    assert solution.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    print("all tests passed")
