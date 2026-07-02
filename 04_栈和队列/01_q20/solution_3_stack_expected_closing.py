class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        expected = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for ch in s:
            if ch in expected:
                stack.append(expected[ch])
            else:
                if not stack or stack.pop() != ch:
                    return False

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
