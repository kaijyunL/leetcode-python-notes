class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        解法1：迭代扩展
        时间复杂度: O(n * 4^n)
        空间复杂度: O(n * 4^n)
        """
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        ans = [""]

        for digit in digits:
            next_ans = []
            for prefix in ans:
                for ch in phone[digit]:
                    next_ans.append(prefix + ch)
            ans = next_ans

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        "23",
        "2",
        "",
        "79",
    ]

    for digits in test_cases:
        print(f"输入: digits={digits!r}, 输出: {solution.letterCombinations(digits)}")
