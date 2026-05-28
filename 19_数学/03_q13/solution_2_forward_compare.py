# 方法2：正序遍历，和右边一位比较


class Solution:
    def romanToInt(self, s: str) -> int:
        value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        ans = 0

        for i, ch in enumerate(s):
            if i < len(s) - 1 and value[ch] < value[s[i + 1]]:
                ans -= value[ch]
            else:
                ans += value[ch]

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
