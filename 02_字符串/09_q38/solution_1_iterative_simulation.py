# 方法1：迭代模拟（面试主推）
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"

        for _ in range(2, n + 1):
            ans = []
            i = 0

            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                    i += 1

                ans.append(str(count))
                ans.append(s[i])
                i += 1

            s = "".join(ans)

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
