class Solution:
    def partition(self, s: str) -> list[list[str]]:
        """
        解法1：暴力切割 + 最后校验
        时间复杂度: O(n * 2^n)
        空间复杂度: O(n * 2^n)
        """
        ans = []
        n = len(s)

        def is_palindrome(part: str) -> bool:
            return part == part[::-1]

        for mask in range(1 << (n - 1)):
            path = []
            start = 0

            for i in range(n - 1):
                if mask & (1 << i):
                    path.append(s[start:i + 1])
                    start = i + 1

            path.append(s[start:])

            if all(is_palindrome(part) for part in path):
                ans.append(path)

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        "aab",
        "a",
        "efe",
        "aaa",
    ]

    for s in test_cases:
        print(f"输入: s={s!r}, 输出: {solution.partition(s)}")
