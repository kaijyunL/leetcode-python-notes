# 方法1：贪心模拟


class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        ans = []
        n = len(words)
        i = 0

        while i < n:
            j = i
            letters = 0

            while j < n and letters + len(words[j]) + (j - i) <= maxWidth:
                letters += len(words[j])
                j += 1

            gap_count = j - i - 1
            is_last_line = j == n

            if gap_count == 0 or is_last_line:
                line = " ".join(words[i:j])
                ans.append(line + " " * (maxWidth - len(line)))
            else:
                total_spaces = maxWidth - letters
                avg_spaces, extra_spaces = divmod(total_spaces, gap_count)
                parts = []

                for k in range(i, j - 1):
                    parts.append(words[k])
                    spaces = avg_spaces + (1 if k - i < extra_spaces else 0)
                    parts.append(" " * spaces)

                parts.append(words[j - 1])
                ans.append("".join(parts))

            i = j

        return ans


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
