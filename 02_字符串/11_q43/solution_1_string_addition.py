# 方法1：竖式乘法 + 字符串相加


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        def add_strings(s1: str, s2: str) -> str:
            i = len(s1) - 1
            j = len(s2) - 1
            carry = 0
            ans = []

            while i >= 0 or j >= 0 or carry:
                x = int(s1[i]) if i >= 0 else 0
                y = int(s2[j]) if j >= 0 else 0
                total = x + y + carry
                ans.append(str(total % 10))
                carry = total // 10
                i -= 1
                j -= 1

            return "".join(reversed(ans))

        ans = "0"
        zeros = 0

        for j in range(len(num2) - 1, -1, -1):
            y = int(num2[j])
            carry = 0
            parts = ["0"] * zeros

            for i in range(len(num1) - 1, -1, -1):
                x = int(num1[i])
                total = x * y + carry
                parts.append(str(total % 10))
                carry = total // 10

            if carry:
                parts.append(str(carry))

            current = "".join(reversed(parts))
            ans = add_strings(ans, current)
            zeros += 1

        return ans


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
