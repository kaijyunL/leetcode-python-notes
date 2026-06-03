from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        方法一：记录所有0的坐标 (空间复杂度 O(mn))
        """
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        # 存放所有值为 0 的元素的横纵坐标
        zero_positions = []
        
        # 1. 遍历矩阵，记录所有 0 的坐标
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_positions.append((i, j))
                    
        # 2. 遍历保存的坐标列表，把对应的行和列都置为 0
        for r, c in zero_positions:
            # 将第 r 行全设为 0
            for j in range(n):
                matrix[r][j] = 0
            # 将第 c 列全设为 0
            for i in range(m):
                matrix[i][c] = 0

# 测试代码
if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print("【方法一 (O(mn) 空间)】")
    print("原矩阵:")
    for row in matrix: print(row)
    solution.setZeroes(matrix)
    print("置零后矩阵:")
    for row in matrix: print(row)
