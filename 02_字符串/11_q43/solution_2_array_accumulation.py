# 方法2：数组累加（面试主推）


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)
        pos = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                total = mul + pos[p2]
                pos[p2] = total % 10
                pos[p1] += total // 10

        start = 0
        while start < len(pos) and pos[start] == 0:
            start += 1

        ans = [str(x) for x in pos[start:]]
        return "".join(ans)


def run_case(num1: str, num2: str, expected: str) -> None:
    actual = Solution().multiply(num1, num2)
    assert actual == expected


if __name__ == "__main__":
    run_case("2", "3", "6")
    run_case("123", "456", "56088")
    run_case("9133", "0", "0")
    run_case("99", "99", "9801")
    run_case("123456789", "987654321", "121932631112635269")

    print("all tests passed")
