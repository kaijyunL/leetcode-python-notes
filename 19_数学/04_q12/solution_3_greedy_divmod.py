# 方法3：贪心加 divmod


class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        ans = []

        for value, symbol in values:
            count, num = divmod(num, value)
            ans.append(symbol * count)

        return "".join(ans)


if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        (3, "III"),
        (4, "IV"),
        (9, "IX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        (3999, "MMMCMXCIX"),
    ]

    for num, expected in test_cases:
        assert solver.intToRoman(num) == expected

    print("all tests passed")
