class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 初始化 9 个空集合，分别用于记录 9行、9列、9个3x3宫的数字使用情况
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # 一次性遍历整个 9x9 的棋盘
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                
                # 如果是未填数字的空格，则跳过不管
                if val == '.':
                    continue
                
                # 计算当前格子属于哪一个 3x3 宫 (编号 0-8)
                # i // 3 决定是哪一大行宫，j // 3 决定是哪一大列宫
                box_index = (i // 3) * 3 + j // 3
                
                # 检查是否违反了重复规则
                if val in rows[i] or val in cols[j] or val in boxes[box_index]:
                    return False
                
                # 将该数字分别记录到对应的 行、列、宫 的哈希集合中
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_index].add(val)
                
        # 遍历完毕，所有填入的数字均无冲突，判定为有效的数独
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
    print("解题方法二运行结果：")
    print(f"当前数独是否有效: {solution.isValidSudoku(board)}")
    print("-----------------------------------------")
