# 方法1：手动模拟（面试主推）


class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        sign = 1
        ans = 0
        int_max = 2**31 - 1
        int_min = -2**31

        while i < n and s[i] == " ":
            i += 1

        if i == n:
            return 0

        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1

        limit = int_max if sign == 1 else -int_min

        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord("0")

            if ans > (limit - digit) // 10:
                return int_max if sign == 1 else int_min

            ans = ans * 10 + digit
            i += 1

        return sign * ans


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
