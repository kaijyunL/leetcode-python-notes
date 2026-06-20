# 方法3：groupby
from itertools import groupby


class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"

        for _ in range(2, n + 1):
            parts = []
            for digit, group in groupby(s):
                count = sum(1 for _ in group)
                parts.append(str(count))
                parts.append(digit)

            s = "".join(parts)

        return s


def run_case(n: int, expected: str) -> None:
    actual = Solution().countAndSay(n)
    assert actual == expected


if __name__ == "__main__":
    run_case(1, "1")
    run_case(2, "11")
    run_case(4, "1211")
    run_case(5, "111221")
    run_case(6, "312211")

    print("all tests passed")
