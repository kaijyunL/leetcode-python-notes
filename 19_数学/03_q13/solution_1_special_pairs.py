# 方法1：显式处理特殊组合


class Solution:
    def romanToInt(self, s: str) -> int:
        single = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        pair = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        ans = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and s[i:i + 2] in pair:
                ans += pair[s[i:i + 2]]
                i += 2
            else:
                ans += single[s[i]]
                i += 1

        return ans


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    ]

    for s, expected in test_cases:
        assert solver.romanToInt(s) == expected

    print("all tests passed")
