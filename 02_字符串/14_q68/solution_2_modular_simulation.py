# 方法2：模块化模拟（面试主推）


class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        ans = []
        n = len(words)
        left = 0

        while left < n:
            right, letters = self._find_right(words, left, maxWidth)
            is_last_line = right == n - 1

            if left == right or is_last_line:
                ans.append(self._left_justify(words, left, right, maxWidth))
            else:
                ans.append(self._middle_justify(words, left, right, letters, maxWidth))

            left = right + 1

        return ans

    def _find_right(self, words: list[str], left: int, maxWidth: int) -> tuple[int, int]:
        right = left
        letters = len(words[left])
        n = len(words)

        while right + 1 < n and letters + len(words[right + 1]) + (right - left + 1) <= maxWidth:
            right += 1
            letters += len(words[right])

        return right, letters

    def _left_justify(self, words: list[str], left: int, right: int, maxWidth: int) -> str:
        line = " ".join(words[left : right + 1])
        return line + " " * (maxWidth - len(line))

    def _middle_justify(
        self,
        words: list[str],
        left: int,
        right: int,
        letters: int,
        maxWidth: int,
    ) -> str:
        gap_count = right - left
        total_spaces = maxWidth - letters
        avg_spaces, extra_spaces = divmod(total_spaces, gap_count)
        parts = []

        for i in range(left, right):
            parts.append(words[i])
            spaces = avg_spaces + (1 if i - left < extra_spaces else 0)
            parts.append(" " * spaces)

        parts.append(words[right])
        return "".join(parts)


def run_case(words: list[str], maxWidth: int, expected: list[str]) -> None:
    actual = Solution().fullJustify(words, maxWidth)
    assert actual == expected


if __name__ == "__main__":
    run_case(
        ["This", "is", "an", "example", "of", "text", "justification."],
        16,
        ["This    is    an", "example  of text", "justification.  "],
    )
    run_case(
        ["What", "must", "be", "acknowledgment", "shall", "be"],
        16,
        ["What   must   be", "acknowledgment  ", "shall be        "],
    )
    run_case(
        [
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        20,
        [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  ",
        ],
    )
    run_case(["Longword"], 10, ["Longword  "])

    print("all tests passed")
