from collections import Counter


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        解法2：原地标记 + 预检查 — 面试推荐
        时间复杂度: O(mn * 4^L)
        空间复杂度: O(L)
        """
        rows, cols = len(board), len(board[0])

        if len(word) > rows * cols:
            return False

        board_count = Counter(ch for row in board for ch in row)
        word_count = Counter(word)

        for ch, count in word_count.items():
            if board_count[ch] < count:
                return False

        def dfs(row: int, col: int, index: int) -> bool:
            if index == len(word):
                return True

            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

            if board[row][col] != word[index]:
                return False

            temp = board[row][col]
            board[row][col] = "#"

            found = (
                dfs(row + 1, col, index + 1)
                or dfs(row - 1, col, index + 1)
                or dfs(row, col + 1, index + 1)
                or dfs(row, col - 1, index + 1)
            )

            board[row][col] = temp
            return found

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED",
        ),
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "SEE",
        ),
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCB",
        ),
    ]

    for board, word in test_cases:
        print(f"输入: word={word!r}, 输出: {solution.exist([row[:] for row in board], word)}")
