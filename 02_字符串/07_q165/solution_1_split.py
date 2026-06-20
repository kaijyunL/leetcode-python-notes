# 方法1：split() 后逐段比较
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        parts1 = version1.split(".")
        parts2 = version2.split(".")

        for i in range(max(len(parts1), len(parts2))):
            num1 = int(parts1[i]) if i < len(parts1) else 0
            num2 = int(parts2[i]) if i < len(parts2) else 0

            if num1 > num2:
                return 1
            if num1 < num2:
                return -1

        return 0


def run_case(version1: str, version2: str, expected: int) -> None:
    actual = Solution().compareVersion(version1, version2)
    assert actual == expected


if __name__ == "__main__":
    run_case("1.01", "1.001", 0)
    run_case("1.0", "1.0.0", 0)
    run_case("0.1", "1.1", -1)
    run_case("1.0.1", "1", 1)
    run_case("7.5.2.4", "7.5.3", -1)

    print("all tests passed")
