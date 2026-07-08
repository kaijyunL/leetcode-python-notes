class Solution:
    def checkValidString(self, s: str) -> bool:
        return self._dfs(s, 0, 0)

    def _dfs(self, s: str, index: int, balance: int) -> bool:
        if balance < 0:
            return False

        if index == len(s):
            return balance == 0

        ch = s[index]

        if ch == "(":
            return self._dfs(s, index + 1, balance + 1)

        if ch == ")":
            return self._dfs(s, index + 1, balance - 1)

        return (
            self._dfs(s, index + 1, balance + 1)
            or self._dfs(s, index + 1, balance - 1)
            or self._dfs(s, index + 1, balance)
        )


def run_test() -> None:
    solver = Solution()
    test_cases = [
        ("()", True),
        ("(*)", True),
        ("(*))", True),
        ("(", False),
        (")(", False),
        ("(((******))", True),
        ("(*()", True),
    ]

    for s, expected in test_cases:
        result = solver.checkValidString(s)
        assert result == expected, f"failed for {s!r}: expected {expected}, got {result}"


if __name__ == "__main__":
    run_test()
    print("all tests passed")
