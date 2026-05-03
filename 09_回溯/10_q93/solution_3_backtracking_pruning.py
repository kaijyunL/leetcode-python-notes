class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        """
        解法3：回溯 + 递归内剪枝 — 进阶写法
        时间复杂度: O(1)
        空间复杂度: O(1)
        """
        ans = []
        path = []

        def is_valid(part: str) -> bool:
            if len(part) > 1 and part[0] == "0":
                return False
            return int(part) <= 255

        def backtrack(start: int) -> None:
            remaining_parts = 4 - len(path)
            remaining_chars = len(s) - start

            if remaining_chars < remaining_parts or remaining_chars > remaining_parts * 3:
                return

            if len(path) == 4:
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
