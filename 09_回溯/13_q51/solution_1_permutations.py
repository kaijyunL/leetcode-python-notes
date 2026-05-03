from itertools import permutations


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        """
        解法1：暴力排列 + 最后校验
        时间复杂度: O(n! * n^2)
        空间复杂度: O(n)
        """
        ans = []

        def is_valid(cols: tuple[int, ...]) -> bool:
            for row1 in range(n):
                for row2 in range(row1 + 1, n):
                    if abs(row1 - row2) == abs(cols[row1] - cols[row2]):
                        return False
            return True

        def build_board(cols: tuple[int, ...]) -> list[str]:
            board = []
            for col in cols:
                row = ["."] * n
                row[col] = "Q"
                board.append("".join(row))
            return board

        for cols in permutations(range(n)):
            if is_valid(cols):
                ans.append(build_board(cols))

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [1, 4]

    for n in test_cases:
        print(f"输入: n={n}, 输出: {solution.solveNQueens(n)}")
