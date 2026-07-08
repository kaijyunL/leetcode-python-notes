class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev

            stack.append(i)

        return ans


def run_test() -> None:
    solver = Solution()
    test_cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([90, 80, 70], [0, 0, 0]),
        ([70], [0]),
        ([70, 70, 71], [2, 1, 0]),
        ([75, 71, 69, 72], [0, 2, 1, 0]),
    ]

    for temperatures, expected in test_cases:
        result = solver.dailyTemperatures(temperatures)
        assert result == expected, f"failed for {temperatures!r}: expected {expected}, got {result}"


if __name__ == "__main__":
    run_test()
    print("all tests passed")
