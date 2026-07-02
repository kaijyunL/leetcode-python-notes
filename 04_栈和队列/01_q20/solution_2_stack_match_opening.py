class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ("", True),
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("((", False),
        ("]", False),
        ("([{}])", True),
    ]

    for s, expected in test_cases:
        result = solver.isValid(s)
        assert result == expected, f"failed for {s!r}: expected {expected}, got {result}"

    print("all tests passed")
