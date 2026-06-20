# 方法2：递归
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)
        parts = []
        i = 0

        while i < len(prev):
            count = 1
            while i + 1 < len(prev) and prev[i] == prev[i + 1]:
                count += 1
                i += 1

            parts.append(str(count))
            parts.append(prev[i])
            i += 1

        return "".join(parts)


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
