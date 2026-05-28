# 方法3：倒序遍历


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
        prev = 0

        for ch in reversed(s):
            cur = value[ch]
            if cur < prev:
                ans -= cur
            else:
                ans += cur
                prev = cur

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
