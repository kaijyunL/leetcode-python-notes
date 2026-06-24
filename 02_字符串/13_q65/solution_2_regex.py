# 方法2：正则表达式

import re


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        pattern = r"[+-]?(\d+\.\d*|\.\d+|\d+)([eE][+-]?\d+)?"
        return bool(re.fullmatch(pattern, s))


def run_case(s: str, expected: bool) -> None:
    actual = Solution().isNumber(s)
    assert actual == expected, f"failed on {s!r}: expected {expected}, got {actual}"


if __name__ == "__main__":
    run_case("2", True)
    run_case("0089", True)
    run_case("-0.1", True)
    run_case("+3.14", True)
    run_case("4.", True)
    run_case("-.9", True)
    run_case("2e10", True)
    run_case("-90E3", True)
    run_case("3e+7", True)
    run_case("+6e-1", True)
    run_case("53.5e93", True)
    run_case(" 0.1 ", True)

    run_case("abc", False)
    run_case("1a", False)
    run_case("1e", False)
    run_case("e3", False)
    run_case("99e2.5", False)
    run_case("--6", False)
    run_case("-+3", False)
    run_case("95a54e53", False)
    run_case(".", False)
    run_case(" ", False)

    print("all tests passed")
