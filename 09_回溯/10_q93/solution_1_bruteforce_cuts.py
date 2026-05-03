class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        """
        解法1：三重循环枚举切点
        时间复杂度: O(1)
        空间复杂度: O(1)
        """
        ans = []

        def is_valid(part: str) -> bool:
            if not part or len(part) > 3:
                return False
            if len(part) > 1 and part[0] == "0":
                return False
            return int(part) <= 255

        n = len(s)

        for len1 in range(1, 4):
            for len2 in range(1, 4):
                for len3 in range(1, 4):
                    len4 = n - len1 - len2 - len3
                    if len4 < 1 or len4 > 3:
                        continue

                    p1 = s[:len1]
                    p2 = s[len1:len1 + len2]
                    p3 = s[len1 + len2:len1 + len2 + len3]
                    p4 = s[len1 + len2 + len3:]

                    if all(is_valid(part) for part in [p1, p2, p3, p4]):
                        ans.append(".".join([p1, p2, p3, p4]))

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        "25525511135",
        "0000",
        "101023",
        "1111",
    ]

    for s in test_cases:
        print(f"输入: s={s!r}, 输出: {solution.restoreIpAddresses(s)}")
