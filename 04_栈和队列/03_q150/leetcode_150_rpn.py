#!/usr/bin/env python3
import sys


class Solution:
    def evalRPN_bruteforce(self, tokens):
        arr = tokens[:]

        while len(arr) > 1:
            for i, token in enumerate(arr):
                if token not in {"+", "-", "*", "/"}:
                    continue

                a = int(arr[i - 2])
                b = int(arr[i - 1])

                if token == "+":
                    value = a + b
                elif token == "-":
                    value = a - b
                elif token == "*":
                    value = a * b
                else:
                    value = int(a / b)

                arr = arr[: i - 2] + [str(value)] + arr[i + 1 :]
                break

        return int(arr[0])

    def evalRPN_stack(self, tokens):
        stack = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
                continue

            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))

        return stack[-1]

    def evalRPN_optimized(self, tokens):
        stack = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
                continue

            b = stack.pop()
            a = stack.pop()
            stack.append(ops[token](a, b))

        return stack[-1]

    def evalRPN(self, tokens):
        return self.evalRPN_stack(tokens)


def run_case(tokens):
    solver = Solution()
    brute = solver.evalRPN_bruteforce(tokens)
    stack = solver.evalRPN_stack(tokens)
    optimized = solver.evalRPN_optimized(tokens)

    print(f"tokens = {tokens}")
    print(f"暴力模拟: {brute}")
    print(f"栈（面试版）: {stack}")
    print(f"栈 + 运算封装: {optimized}")
    print("-" * 40)


def parse_tokens(arg):
    cleaned = arg.strip()
    if cleaned.startswith("[") and cleaned.endswith("]"):
        cleaned = cleaned[1:-1]

    if not cleaned:
        return []

    return [part.strip().strip("\"'") for part in cleaned.split(",")]


def main():
    if len(sys.argv) > 1:
        tokens = parse_tokens(sys.argv[1])
        result = Solution().evalRPN(tokens)
        print(result)
        return

    demo_cases = [
        ["2", "1", "+", "3", "*"],
        ["4", "13", "5", "/", "+"],
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
    ]

    for tokens in demo_cases:
        run_case(tokens)


if __name__ == "__main__":
    main()
