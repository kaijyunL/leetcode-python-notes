# 方法四：状态压缩
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp_i_2 = 1
        dp_i_1 = 0 if s[0] == '0' else 1

        for i in range(2, n + 1):
            curr = 0

            if s[i - 1] != '0':
                curr += dp_i_1

            two_digits = int(s[i - 2:i])
            if 10 <= two_digits <= 26:
                curr += dp_i_2

            dp_i_2 = dp_i_1
            dp_i_1 = curr

        return dp_i_1


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        "12",
        "226",
        "06",
        "10",
    ]

    for s in test_cases:
        print(f"s={s}, ways={solver.numDecodings(s)}")
