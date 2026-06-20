# 方法2：逐位模拟加法（面试主推）
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        ans = []

        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            total = digit_a + digit_b + carry

            ans.append(str(total % 2))
            carry = total // 2

            i -= 1
            j -= 1

        return "".join(reversed(ans))


def run_case(a: str, b: str, expected: str) -> None:
    actual = Solution().addBinary(a, b)
    assert actual == expected


if __name__ == "__main__":
    run_case("11", "1", "100")
    run_case("1010", "1011", "10101")
    run_case("0", "0", "0")
    run_case("1", "111", "1000")
    run_case("1111", "1", "10000")

    print("all tests passed")
