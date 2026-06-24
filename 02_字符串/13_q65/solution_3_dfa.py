# 方法3：有限状态机（DFA）


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        states = [
            {"sign": 1, "digit": 2, "dot": 3},
            {"digit": 2, "dot": 3},
            {"digit": 2, "dot": 4, "exp": 6},
            {"digit": 5},
            {"digit": 5, "exp": 6},
            {"digit": 5, "exp": 6},
            {"sign": 7, "digit": 8},
            {"digit": 8},
            {"digit": 8},
        ]

        state = 0

        for ch in s:
            if ch in "+-":
                token = "sign"
            elif ch in "eE":
                token = "exp"
            elif ch == ".":
                token = "dot"
            elif ch.isdigit():
                token = "digit"
            else:
                return False

            if token not in states[state]:
                return False

            state = states[state][token]

        return state in {2, 4, 5, 8}


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
