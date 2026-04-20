"""
LeetCode 54. 螺旋矩阵
方法三：边界收缩法（最优解 ✨ 面试首选）

思路：定义上下左右四个边界，每遍历完一条边就收缩对应边界
- 遍历上边 → top 下移 (top++)
- 遍历右边 → right 左移 (right--)
- 遍历下边 → bottom 上移 (bottom--)
- 遍历左边 → left 右移 (left++)
- 每次收缩后立刻检查边界是否交叉，交叉则终止

关键优势：边界收缩自然地处理了单行/单列的特殊情况！

时间复杂度：O(m × n)
空间复杂度：O(1)  ← 除结果数组外无额外空间
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        result = []

        # 初始化四个边界
        top, bottom = 0, len(matrix) - 1      # 上下边界
        left, right = 0, len(matrix[0]) - 1   # 左右边界

        # 当边界没有交叉时，持续遍历
        while top <= bottom and left <= right:

            # ① 遍历上边：从左到右 →
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1  # 上边界下移（上边已经遍历完了）

            # ② 遍历右边：从上到下 ↓
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1  # 右边界左移（右边已经遍历完了）

            # ③ 遍历下边：从右到左 ←
            # 注意：需要检查 top <= bottom，防止单行时重复遍历
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1  # 下边界上移

            # ④ 遍历左边：从下到上 ↑
            # 注意：需要检查 left <= right，防止单列时重复遍历
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1  # 左边界右移

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
