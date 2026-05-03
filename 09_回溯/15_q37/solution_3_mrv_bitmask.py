class Solution:
    FULL_MASK = (1 << 9) - 1

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        解法3：位运算 + MRV（候选最少优先）
        时间复杂度：最坏仍是指数级，但实战里通常最快
        空间复杂度：O(E)
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    empties.append((row, col))
                    continue

                bit = 1 << (int(board[row][col]) - 1)
                box = (row // 3) * 3 + col // 3
                rows[row] |= bit
                cols[col] |= bit
                boxes[box] |= bit

        def available_mask(row: int, col: int) -> int:
            box = (row // 3) * 3 + col // 3
            used = rows[row] | cols[col] | boxes[box]
            return self.FULL_MASK & ~used

        def place(row: int, col: int, bit: int) -> None:
            box = (row // 3) * 3 + col // 3
            rows[row] |= bit
            cols[col] |= bit
            boxes[box] |= bit
            board[row][col] = str(bit.bit_length())

        def remove(row: int, col: int, bit: int) -> None:
            box = (row // 3) * 3 + col // 3
            rows[row] ^= bit
            cols[col] ^= bit
            boxes[box] ^= bit
            board[row][col] = "."

        def backtrack() -> bool:
            best_index = -1
            best_mask = 0
            best_count = 10

            for index, (row, col) in enumerate(empties):
                if board[row][col] != ".":
                    continue

                mask = available_mask(row, col)
                count = mask.bit_count()
                if count == 0:
                    return False

                if count < best_count:
                    best_count = count
                    best_mask = mask
                    best_index = index
                    if count == 1:
                        break

            if best_index == -1:
                return True

            row, col = empties[best_index]
            mask = best_mask

            while mask:
                bit = mask & -mask  # lowbit：取出当前最低位的候选数字
                place(row, col, bit)
                if backtrack():
                    return True
                remove(row, col, bit)
                mask ^= bit

            return False

        backtrack()


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
    print("解法3结果：")
    print_board(board)
