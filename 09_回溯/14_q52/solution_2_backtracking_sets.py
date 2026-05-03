class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        解法2：回溯 + 集合剪枝 — 面试推荐
        时间复杂度: O(n!) 级别
        空间复杂度: O(n)
        """
        count = 0
        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row: int) -> None:
            nonlocal count

            if row == n:
                count += 1
                return

            for col in range(n):
                if col in cols or row - col in diag1 or row + col in diag2:
                    continue

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return count


if __name__ == "__main__":
    solution = Solution()

    test_cases = [1, 4, 5]

    for n in test_cases:
        print(f"输入: n={n}, 输出: {solution.totalNQueens(n)}")
