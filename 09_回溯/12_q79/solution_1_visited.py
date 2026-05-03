class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        解法1：DFS + visited 矩阵
        时间复杂度: O(mn * 4^L)
        空间复杂度: O(mn + L)
        """
        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(row: int, col: int, index: int) -> bool:
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

            if visited[row][col] or board[row][col] != word[index]:
                return False

            if index == len(word) - 1:
                return True

            visited[row][col] = True

            found = (
                dfs(row + 1, col, index + 1)
                or dfs(row - 1, col, index + 1)
                or dfs(row, col + 1, index + 1)
                or dfs(row, col - 1, index + 1)
            )

            visited[row][col] = False
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
