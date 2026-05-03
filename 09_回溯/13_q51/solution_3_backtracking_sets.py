class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        """
        解法3：回溯 + 集合剪枝 — 面试推荐
        时间复杂度: O(n!) 级别
        空间复杂度: O(n^2)
        """
        ans = []
        board = [["."] * n for _ in range(n)]
        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row: int) -> None:
            if row == n:
                ans.append(["".join(line) for line in board])
                return

            for col in range(n):
                if col in cols or row - col in diag1 or row + col in diag2:
                    continue

                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [1, 4]

    for n in test_cases:
        print(f"输入: n={n}, 输出: {solution.solveNQueens(n)}")
