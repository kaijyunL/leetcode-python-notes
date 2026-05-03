class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        解法2：回溯 + 行列宫状态表
        时间复杂度：最坏约 O(9^E)
        空间复杂度：O(E)
        """
        rows = [[False] * 10 for _ in range(9)]
        cols = [[False] * 10 for _ in range(9)]
        boxes = [[False] * 10 for _ in range(9)]
        empties = []

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    empties.append((row, col))
                    continue

                num = int(board[row][col])
                box = (row // 3) * 3 + col // 3
                rows[row][num] = True
                cols[col][num] = True
                boxes[box][num] = True

        def backtrack(index: int) -> bool:
            if index == len(empties):
                return True

            row, col = empties[index]
            box = (row // 3) * 3 + col // 3

            for num in range(1, 10):
                if rows[row][num] or cols[col][num] or boxes[box][num]:
                    continue

                board[row][col] = str(num)
                rows[row][num] = True
                cols[col][num] = True
                boxes[box][num] = True

                if backtrack(index + 1):
                    return True

                board[row][col] = "."
                rows[row][num] = False
                cols[col][num] = False
                boxes[box][num] = False

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
    print("解法2结果：")
    print_board(board)
