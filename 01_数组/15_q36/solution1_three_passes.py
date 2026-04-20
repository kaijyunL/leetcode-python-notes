class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 1. 检查每一行
        for i in range(9):
            seen = set()
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    # 如果该数字在该行已经出现过，直接返回 False
                    if val in seen:
                        return False
                    seen.add(val)
        
        # 2. 检查每一列
        for j in range(9):
            seen = set()
            for i in range(9):
                val = board[i][j]
                if val != '.':
                    # 如果该数字在该列已经出现过，直接返回 False
                    if val in seen:
                        return False
                    seen.add(val)
        
        # 3. 检查每一个 3x3 宫
        # 共有 3x3 = 9 个宫，分别编号
        for box_i in range(3):
            for box_j in range(3):
                seen = set()
                # 遍历属于当前 3x3 宫内的所有格子
                for row in range(box_i * 3, box_i * 3 + 3):
                    for col in range(box_j * 3, box_j * 3 + 3):
                        val = board[row][col]
                        if val != '.':
                            # 如果该数字在当前宫已经出现过，直接返回 False
                            if val in seen:
                                return False
                            seen.add(val)
                            
        # 如果都没有违反规则，返回有效
        return True

if __name__ == "__main__":
    board = [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    solution = Solution()
    print("-----------------------------------------")
    print("解题方法一运行结果：")
    print(f"当前数独是否有效: {solution.isValidSudoku(board)}")
    print("-----------------------------------------")
