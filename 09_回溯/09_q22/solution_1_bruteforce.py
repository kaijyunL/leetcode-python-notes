class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        解法1：暴力生成 + 校验
        时间复杂度: O(n * 2^(2n))
        空间复杂度: O(n * 2^(2n))
        """
        ans = []

        def is_valid(s: str) -> bool:
            balance = 0
            for ch in s:
                if ch == "(":
                    balance += 1
                else:
                    balance -= 1

                if balance < 0:
                    return False

            return balance == 0

        def dfs(path: str) -> None:
            if len(path) == 2 * n:
                if is_valid(path):
                    ans.append(path)
                return

            dfs(path + "(")
            dfs(path + ")")

        dfs("")
        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [1, 2, 3]

    for n in test_cases:
        print(f"输入: n={n}, 输出: {solution.generateParenthesis(n)}")
