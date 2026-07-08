class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        arr = tokens[:]
        operators = {"+", "-", "*", "/"}

        while len(arr) > 1:
            for i, token in enumerate(arr):
                if token not in operators:
                    continue

                left = int(arr[i - 2])
                right = int(arr[i - 1])

                if token == "+":
                    value = left + right
                elif token == "-":
                    value = left - right
                elif token == "*":
                    value = left * right
                else:
                    value = int(left / right)

                arr = arr[: i - 2] + [str(value)] + arr[i + 1 :]
                break

        return int(arr[0])


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
