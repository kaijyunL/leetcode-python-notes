from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        方法二：使用行和列的标记数组 (空间复杂度 O(m+n))
        """
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        # 分别用来标记某一行、某一列是否存在 0
        row_has_zero = [False] * m
        col_has_zero = [False] * n
        
        # 1. 第一段：遍历矩阵，更新行和列的标记数组
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_has_zero[i] = True
                    col_has_zero[j] = True
                    
        # 2. 第二段：再次遍历矩阵，如果所在的行或列有 0，就把当前元素设为 0
        for i in range(m):
            for j in range(n):
                # 只要当前行或者当前列曾经出现过 0，这个位置就必须变 0
                if row_has_zero[i] or col_has_zero[j]:
                    matrix[i][j] = 0

# 测试代码
if __name__ == "__main__":
    solution = Solution()
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print("【方法二 (O(m+n) 空间)】")
    print("原矩阵:")
    for row in matrix: print(row)
    solution.setZeroes(matrix)
    print("置零后矩阵:")
    for row in matrix: print(row)
