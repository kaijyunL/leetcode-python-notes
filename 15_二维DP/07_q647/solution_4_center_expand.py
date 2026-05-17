# 方法四：中心扩展
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand(left, right):
            total = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                total += 1
                left -= 1
                right += 1
            return total

        for i in range(len(s)):
            count += expand(i, i)
            count += expand(i, i + 1)

        return count


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        "abc",
        "aaa",
        "abba",
        "abac",
    ]

    for s in test_cases:
        print(f"s={s}, count={solver.countSubstrings(s)}")
