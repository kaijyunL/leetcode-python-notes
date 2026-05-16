from typing import List


# 方法一：暴力枚举
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_side = 0

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == "0":
                    continue

                side = 1
                while row + side <= m and col + side <= n:
                    valid = True

                    for i in range(row, row + side):
                        for j in range(col, col + side):
                            if matrix[i][j] == "0":
                                valid = False
                                break
                        if not valid:
                            break

                    if not valid:
                        break

                    max_side = max(max_side, side)
                    side += 1

        return max_side * max_side


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]],
        [["0", "1"], ["1", "0"]],
    ]

    for matrix in test_cases:
        print(f"matrix={matrix}, area={solver.maximalSquare(matrix)}")
