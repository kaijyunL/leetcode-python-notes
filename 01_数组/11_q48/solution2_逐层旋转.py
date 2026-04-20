"""
LeetCode 48. 旋转图像
解法二：逐层旋转（四元素循环交换）

思路：把矩阵看成一层层的"框"，从最外层到最内层逐层处理
      每一层中，将四个对应位置的元素进行循环交换
时间复杂度：O(n²)
空间复杂度：O(1) — 真正的原地旋转
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 逐层处理，从最外层(layer=0)到最内层(layer=n//2-1)
        # n×n 矩阵共有 n//2 层
        for layer in range(n // 2):
            first = layer           # 当前层的起始索引
            last = n - 1 - layer    # 当前层的结束索引

            # 在当前层中，逐个位置进行四元素循环交换
            for i in range(first, last):
                offset = i - first  # 当前位置相对于层起始的偏移量

                # 保存【上边】的元素
                top = matrix[first][i]

                # 【左边】→【上边】
                # matrix[last-offset][first] 移动到 matrix[first][i]
                matrix[first][i] = matrix[last - offset][first]

                # 【下边】→【左边】
                # matrix[last][last-offset] 移动到 matrix[last-offset][first]
                matrix[last - offset][first] = matrix[last][last - offset]

                # 【右边】→【下边】
                # matrix[i][last] 移动到 matrix[last][last-offset]
                matrix[last][last - offset] = matrix[i][last]

                # 【上边（已保存）】→【右边】
                # top 移动到 matrix[i][last]
                matrix[i][last] = top


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
