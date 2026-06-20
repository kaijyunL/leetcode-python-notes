# 方法3：位运算
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)

        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry

        return bin(x)[2:]


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
