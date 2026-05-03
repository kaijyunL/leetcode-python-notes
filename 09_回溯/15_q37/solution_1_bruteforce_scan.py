class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        解法1：暴力回溯 + 每次扫描行、列、宫
        时间复杂度：最坏约 O(9^E)
        空间复杂度：O(E)
        """
        empties = []
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    empties.append((row, col))

        def is_valid(row: int, col: int, ch: str) -> bool:
            for i in range(9):
                if board[row][i] == ch:
                    return False
                if board[i][col] == ch:
                    return False

            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    if board[r][c] == ch:
                        return False

            return True

        def backtrack(index: int) -> bool:
            if index == len(empties):
                return True

            row, col = empties[index]
            for num in range(1, 10):
                ch = str(num)
                if not is_valid(row, col, ch):
                    continue

                board[row][col] = ch
                if backtrack(index + 1):
                    return True
                board[row][col] = "."

            return False

        backtrack(0)


def build_demo_board() -> list[list[str]]:
    return [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]


def print_board(board: list[list[str]]) -> None:
    for row in board:
        print(" ".join(row))


if __name__ == "__main__":
    board = build_demo_board()
    Solution().solveSudoku(board)
    print("解法1结果：")
    print_board(board)
