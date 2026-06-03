from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        默认调用：记录第一列的版本
        """
        self.setZeroes_track_col0(matrix)

    def setZeroes_track_col0(self, matrix: List[List[int]]) -> None:
        """
        写法一：找外援 `flag_col0` 保护第一列（原矩阵的 `matrix[0][0]` 给第一行用）
        """
        if not matrix or not matrix[0]: return
        m, n = len(matrix), len(matrix[0])
        flag_col0 = False
        
        # 阶段一：全图扫描打标记
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # 第一列出事了，让外援兜底
                    if j == 0:
                        flag_col0 = True
                    else:
                        # 正常打标记投射到行头和列头
                        matrix[i][0] = 0
                        matrix[0][j] = 0
                        
        # 阶段二：反向置零内部（防止拔除自己的灯塔）
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, 0, -1):  # j 只遍历到 1，第一列交给外援处理
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            
            # 这一行走完后，最后单独判断这一行的第一列是否要置 0
            if flag_col0:
                matrix[i][0] = 0


    def setZeroes_track_row0(self, matrix: List[List[int]]) -> None:
        """
        写法二：找外援 `flag_row0` 保护第一行（原矩阵的 `matrix[0][0]` 给第一列用）
        """
        if not matrix or not matrix[0]: return
        m, n = len(matrix), len(matrix[0])
        flag_row0 = False 
        
        # 阶段一：全图扫描打标记
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # 第一行出事了，让外援兜底
                    if i == 0:
                        flag_row0 = True
                    else:
                        # 正常打标记投射到行头和列头
                        matrix[i][0] = 0
                        matrix[0][j] = 0
                        
        # 阶段二：反向置零内部（防止拔除自己的灯塔）
        for i in range(m - 1, 0, -1):      # i 只遍历到 1，第一行交给外援处理
            for j in range(n - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # 全部走完后，单独把第一行横向扫平
        if flag_row0:
            for j in range(n):
                matrix[0][j] = 0

# 测试代码
if __name__ == "__main__":
    import copy
    
    matrix1 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    matrix2 = copy.deepcopy(matrix1)
    
    print("原矩阵:")
    for row in matrix1: print(row)
    print("=" * 30)
    
    solution = Solution()
    
    solution.setZeroes_track_col0(matrix1)
    print("【写法一 (track_col0)】结果:")
    for row in matrix1: print(row)
    print("-" * 30)
    
    solution.setZeroes_track_row0(matrix2)
    print("【写法二 (track_row0)】结果:")
    for row in matrix2: print(row)
