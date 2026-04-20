"""
LeetCode 48. 旋转图像
解法三：转置 + 翻转（最优雅解法）⭐ 推荐

思路：将旋转操作分解为两步简单操作——
      1. 转置矩阵：沿主对角线翻转，swap(matrix[i][j], matrix[j][i])
      2. 水平翻转每行：将每行左右颠倒

数学推导：
      转置: (i,j) → (j,i)
      翻转: (j,i) → (j, n-1-i)
      合起来: (i,j) → (j, n-1-i)  正好是顺时针旋转90°！

时间复杂度：O(n²)
空间复杂度：O(1) — 原地操作
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 第一步：转置矩阵（沿主对角线翻转）
        # 只需遍历上三角区域（j 从 i+1 开始），避免交换两次导致还原
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 第二步：翻转每一行（左右颠倒）
        for row in matrix:
            row.reverse()


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
