class Solution:
    def decodeString(self, s: str) -> str:
        decoded, _ = self._parse(s, 0)
        return decoded

    def _parse(self, s: str, index: int) -> tuple[str, int]:
        cur = []
        repeat = 0

        while index < len(s):
            ch = s[index]

            if ch.isdigit():
                repeat = repeat * 10 + int(ch)
            elif ch == "[":
                decoded, index = self._parse(s, index + 1)
                cur.append(decoded * repeat)
                repeat = 0
            elif ch == "]":
                return "".join(cur), index
            else:
                cur.append(ch)

            index += 1

        return "".join(cur), index


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
