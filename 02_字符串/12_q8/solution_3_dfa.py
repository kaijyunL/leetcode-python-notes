# 方法3：有限状态机（DFA）


class Automaton:
    def __init__(self) -> None:
        self.state = "start"
        self.sign = 1
        self.ans = 0
        self.int_max = 2**31 - 1
        self.table = {
            "start": ["start", "signed", "in_number", "end"],
            "signed": ["end", "end", "in_number", "end"],
            "in_number": ["end", "end", "in_number", "end"],
            "end": ["end", "end", "end", "end"],
        }

    def get_col(self, ch: str) -> int:
        if ch == " ":
            return 0
        if ch in "+-":
            return 1
        if ch.isdigit():
            return 2
        return 3

    def feed(self, ch: str) -> None:
        self.state = self.table[self.state][self.get_col(ch)]

        if self.state == "signed":
            self.sign = 1 if ch == "+" else -1
        elif self.state == "in_number":
            self.ans = self.ans * 10 + int(ch)
            limit = self.int_max if self.sign == 1 else self.int_max + 1
            self.ans = min(self.ans, limit)


class Solution:
    def myAtoi(self, s: str) -> int:
        automaton = Automaton()

        for ch in s:
            automaton.feed(ch)
            if automaton.state == "end":
                break

        return automaton.sign * automaton.ans


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
