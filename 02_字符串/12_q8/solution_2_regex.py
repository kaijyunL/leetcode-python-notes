# 方法2：正则表达式

import re


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        match = re.match(r"[+-]?\d+", s)
        if not match:
            return 0

        ans = int(match.group())
        int_max = 2**31 - 1
        int_min = -2**31
        return max(int_min, min(int_max, ans))


def run_case(s: str, expected: int) -> None:
    actual = Solution().myAtoi(s)
    assert actual == expected


if __name__ == "__main__":
    run_case("42", 42)
    run_case("   -42", -42)
    run_case("4193 with words", 4193)
    run_case("words and 987", 0)
    run_case("-91283472332", -2147483648)
    run_case("2147483648", 2147483647)
    run_case("+-12", 0)
    run_case("   +0 123", 0)

    print("all tests passed")
