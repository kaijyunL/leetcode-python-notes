class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
                continue

            right = stack.pop()
            left = stack.pop()
            stack.append(operations[token](left, right))

        return stack[-1]


def run_test() -> None:
    solver = Solution()
    test_cases = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["4", "-2", "/", "2", "-3", "-", "-"], -7),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ]

    for tokens, expected in test_cases:
        result = solver.evalRPN(tokens)
        assert result == expected, f"failed for {tokens}: expected {expected}, got {result}"


if __name__ == "__main__":
    run_test()
    print("all tests passed")
