# 方法2：双指针原地解析（面试主推）
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n1 = len(version1)
        n2 = len(version2)
        i = 0
        j = 0

        while i < n1 or j < n2:
            num1 = 0
            num2 = 0

            while i < n1 and version1[i] != ".":
                num1 = num1 * 10 + int(version1[i])
                i += 1

            while j < n2 and version2[j] != ".":
                num2 = num2 * 10 + int(version2[j])
                j += 1

            if num1 > num2:
                return 1
            if num1 < num2:
                return -1

            i += 1
            j += 1

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
