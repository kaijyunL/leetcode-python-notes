class Solution:
    def partition(self, s: str) -> list[list[str]]:
        """
        解法2：回溯 + 实时判断回文
        时间复杂度: O(n * 2^n)
        空间复杂度: O(n * 2^n)
        """
        ans = []
        path = []

        def is_palindrome(part: str) -> bool:
            return part == part[::-1]

        def backtrack(start: int) -> None:
            if start == len(s):
                ans.append(path[:])
                return

            for end in range(start, len(s)):
                part = s[start:end + 1]
                if not is_palindrome(part):
                    continue

                path.append(part)
                backtrack(end + 1)
                path.pop()

        backtrack(0)
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
