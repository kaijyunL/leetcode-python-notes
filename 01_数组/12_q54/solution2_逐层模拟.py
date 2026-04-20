"""
LeetCode 54. 螺旋矩阵
方法二：逐层模拟（按层剥离 / 剥洋葱法）

思路：把矩阵看成一层层嵌套的"圈"
- 从外到内，一层一层地遍历
- 每一层按 右→下→左→上 的顺序收集元素
- 特别注意：单行或单列时，下边和左边不能重复遍历

时间复杂度：O(m × n)
空间复杂度：O(1)  ← 除结果数组外无额外空间
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        result = []

        # 总共有多少层？取行列最小值除以2，向上取整
        # 例如 3×4 矩阵有 2 层：外圈 + 内圈
        layers = (min(m, n) + 1) // 2

        for layer in range(layers):
            # 当前层的四个边界
            top = layer
            bottom = m - 1 - layer
            left = layer
            right = n - 1 - layer

            # ① 遍历上边：从左到右
            # 这一步总是需要的（至少有一个元素）
            for col in range(left, right + 1):
                result.append(matrix[top][col])

            # ② 遍历右边：从上到下（注意跳过右上角，因为上边已经遍历过了）
            for row in range(top + 1, bottom + 1):
                result.append(matrix[row][right])

            # ③ 遍历下边：从右到左
            # 注意：只有当 top != bottom 时才遍历（避免单行时重复遍历）
            if top < bottom:
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[bottom][col])

            # ④ 遍历左边：从下到上
            # 注意：只有当 left != right 时才遍历（避免单列时重复遍历）
            if left < right:
                for row in range(bottom - 1, top, -1):
                    result.append(matrix[row][left])

        return result


# ==================== 测试代码 ====================
if __name__ == "__main__":
    sol = Solution()

    # 测试用例1：3×3 矩阵
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("测试1:", sol.spiralOrder(matrix1))
    # 预期: [1, 2, 3, 6, 9, 8, 7, 4, 5]

    # 测试用例2：3×4 矩阵
    matrix2 = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9, 10, 11, 12]
    ]
    print("测试2:", sol.spiralOrder(matrix2))
    # 预期: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    # 测试用例3：单行
    matrix3 = [[1, 2, 3, 4]]
    print("测试3:", sol.spiralOrder(matrix3))
    # 预期: [1, 2, 3, 4]

    # 测试用例4：单列
    matrix4 = [[1], [2], [3]]
    print("测试4:", sol.spiralOrder(matrix4))
    # 预期: [1, 2, 3]

    # 测试用例5：1×1 矩阵
    matrix5 = [[1]]
    print("测试5:", sol.spiralOrder(matrix5))
    # 预期: [1]

    # 测试用例6：4×4 矩阵
    matrix6 = [
        [ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print("测试6:", sol.spiralOrder(matrix6))
    # 预期: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
