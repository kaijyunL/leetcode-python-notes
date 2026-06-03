"""
LeetCode 48. 旋转图像
解法一：辅助矩阵（暴力法）

思路：创建一个新矩阵，按旋转规律 (i,j) → (j, n-1-i) 放置元素，再复制回去
时间复杂度：O(n²)
空间复杂度：O(n²) — 需要额外矩阵，不满足原地要求，但利于理解规律
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 创建一个同样大小的新矩阵
        new_matrix = [[0] * n for _ in range(n)]

        # 按照旋转规律填入新矩阵
        # 原位置 (i, j) 的元素，旋转后到 (j, n-1-i)
        for i in range(n):
            for j in range(n):
                new_matrix[j][n - 1 - i] = matrix[i][j]

        # 将新矩阵的值复制回原矩阵（模拟原地修改）
        for i in range(n):
            for j in range(n):
                matrix[i][j] = new_matrix[i][j]


# ============ 测试代码 ============
def print_matrix(matrix, label=""):
    """格式化打印矩阵"""
    if label:
        print(label)
    for row in matrix:
        print("  ", row)
    print()


if __name__ == "__main__":
    sol = Solution()

    # 测试用例 1：3×3 矩阵
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix(matrix1, "测试1 - 旋转前:")
    sol.rotate(matrix1)
    print_matrix(matrix1, "测试1 - 旋转后:")
    # 期望输出: [[7,4,1],[8,5,2],[9,6,3]]

    # 测试用例 2：4×4 矩阵
    matrix2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    print_matrix(matrix2, "测试2 - 旋转前:")
    sol.rotate(matrix2)
    print_matrix(matrix2, "测试2 - 旋转后:")
    # 期望输出: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    # 测试用例 3：1×1 矩阵（边界情况）
    matrix3 = [[1]]
    print_matrix(matrix3, "测试3 - 旋转前:")
    sol.rotate(matrix3)
    print_matrix(matrix3, "测试3 - 旋转后:")
    # 期望输出: [[1]]

    # 测试用例 4：2×2 矩阵
    matrix4 = [
        [1, 2],
        [3, 4]
    ]
    print_matrix(matrix4, "测试4 - 旋转前:")
    sol.rotate(matrix4)
    print_matrix(matrix4, "测试4 - 旋转后:")
    # 期望输出: [[3,1],[4,2]]
