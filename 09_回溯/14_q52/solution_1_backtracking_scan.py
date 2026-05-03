class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        解法1：回溯 + 扫描检查
        时间复杂度: O(n!) 级别
        空间复杂度: O(n^2)
        """
        count = 0
        board = [["."] * n for _ in range(n)]

        def is_valid(row: int, col: int) -> bool:
            for r in range(row):
                if board[r][col] == "Q":
                    return False

            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1

            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1

            return True

        def backtrack(row: int) -> None:
            nonlocal count

            if row == n:
                count += 1
                return

            for col in range(n):
                if not is_valid(row, col):
                    continue

                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

        backtrack(0)
        return count


if __name__ == "__main__":
    solution = Solution()

    test_cases = [1, 4, 5]

    for n in test_cases:
        print(f"输入: n={n}, 输出: {solution.totalNQueens(n)}")
