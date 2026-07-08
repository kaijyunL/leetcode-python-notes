class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []
        cur = ""
        repeat = 0

        for ch in s:
            if ch.isdigit():
                repeat = repeat * 10 + int(ch)
            elif ch == "[":
                count_stack.append(repeat)
                string_stack.append(cur)
                cur = ""
                repeat = 0
            elif ch == "]":
                times = count_stack.pop()
                previous = string_stack.pop()
                cur = previous + cur * times
            else:
                cur += ch

        return cur


def run_test() -> None:
    solver = Solution()
    test_cases = [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        ("10[a]", "aaaaaaaaaa"),
        ("abc3[cd]xyz", "abccdcdcdxyz"),
        ("2[ab3[c]]", "abcccabccc"),
    ]

    for s, expected in test_cases:
        result = solver.decodeString(s)
        assert result == expected, f"failed for {s!r}: expected {expected}, got {result}"


if __name__ == "__main__":
    run_test()
    print("all tests passed")
