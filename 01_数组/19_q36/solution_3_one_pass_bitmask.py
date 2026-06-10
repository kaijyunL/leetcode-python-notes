# 方法3：一次遍历，用位运算记录出现状态

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == '.':
                    continue

                bit_index = int(value) - 1
                mask = 1 << bit_index
                box_index = (row // 3) * 3 + col // 3

                if (rows[row] & mask) or (cols[col] & mask) or (boxes[box_index] & mask):
                    return False

                rows[row] |= mask
                cols[col] |= mask
                boxes[box_index] |= mask

        return True


def run_case(board, expected):
    actual = Solution().isValidSudoku(board)
    assert actual == expected


if __name__ == "__main__":
    run_case(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
        True,
    )
    run_case(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
        False,
    )

    print("all tests passed")
