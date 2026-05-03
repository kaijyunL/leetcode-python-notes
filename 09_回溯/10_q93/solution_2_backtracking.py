class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        """
        解法2：基础回溯 + 总长度剪枝 — 面试推荐
        时间复杂度: O(1)
        空间复杂度: O(1)
        """
        if len(s) < 4 or len(s) > 12:
            return []

        ans = []
        path = []

        def is_valid(part: str) -> bool:
            if len(part) > 1 and part[0] == "0":
                return False
            return int(part) <= 255

        def backtrack(start: int) -> None:
            if len(path) == 4:
                if start == len(s):
                    ans.append(".".join(path))
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start + length]
                if not is_valid(part):
                    continue

                path.append(part)
                backtrack(start + length)
                path.pop()

        backtrack(0)
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
