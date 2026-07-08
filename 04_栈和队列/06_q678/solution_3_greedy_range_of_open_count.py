class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for ch in s:
            if ch == "(":
                low += 1
                high += 1
            elif ch == ")":
                low = max(low - 1, 0)
                high -= 1
            else:
                low = max(low - 1, 0)
                high += 1

            if high < 0:
                return False

        return low == 0


def run_test() -> None:
    solver = Solution()
    test_cases = [
        ("()", True),
        ("(*)", True),
        ("(*))", True),
        ("(", False),
        (")(", False),
        ("(((******))", True),
        ("*()(", False),
        ("((*)", True),
        ("(*()", True),
    ]

    for s, expected in test_cases:
        result = solver.checkValidString(s)
        assert result == expected, f"failed for {s!r}: expected {expected}, got {result}"


if __name__ == "__main__":
    run_test()
    print("all tests passed")
