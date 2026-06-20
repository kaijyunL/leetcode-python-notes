# 方法1：内置转换后相加
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


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
