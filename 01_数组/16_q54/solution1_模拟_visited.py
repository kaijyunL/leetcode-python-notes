"""
LeetCode 54. 螺旋矩阵
方法一：模拟 + visited 数组（最直觉的暴力法）

思路：模拟一个人在矩阵中按螺旋路径行走
- 用方向数组控制行走方向（右→下→左→上循环）
- 用 visited 数组标记已访问的位置
- 碰到边界或已访问的格子就转向

时间复杂度：O(m × n)
空间复杂度：O(m × n)  ← 需要 visited 数组
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])  # m行n列
        total = m * n  # 总共需要访问的元素个数

        # visited 数组：标记每个位置是否已经访问过
        visited = [[False] * n for _ in range(m)]

        # 方向数组：右(0,1)、下(1,0)、左(0,-1)、上(-1,0)
        # 顺时针螺旋的顺序就是 右→下→左→上 不断循环
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0  # 当前方向索引，从"向右"开始

        result = []
        row, col = 0, 0  # 从左上角 (0, 0) 出发

        for _ in range(total):
            # 将当前位置的值加入结果
            result.append(matrix[row][col])
            # 标记当前位置为已访问
            visited[row][col] = True

            # 尝试按当前方向走一步
            next_row = row + directions[dir_idx][0]
            next_col = col + directions[dir_idx][1]

            # 如果下一步越界或已访问 → 顺时针转向
            if (next_row < 0 or next_row >= m or
                next_col < 0 or next_col >= n or
                visited[next_row][next_col]):
                # 转向：(dir_idx + 1) % 4 实现 右→下→左→上 的循环
                dir_idx = (dir_idx + 1) % 4
                next_row = row + directions[dir_idx][0]
                next_col = col + directions[dir_idx][1]

            # 移动到下一个位置
            row, col = next_row, next_col

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

    # 测试用例6：4×4 矩阵（多层嵌套）
    matrix6 = [
        [ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print("测试6:", sol.spiralOrder(matrix6))
    # 预期: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
