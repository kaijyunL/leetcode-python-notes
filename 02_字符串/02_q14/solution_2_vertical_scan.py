# 方法2：纵向扫描（面试主推）
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i, ch in enumerate(strs[0]):
            for word in strs[1:]:
                if i == len(word) or word[i] != ch:
                    return strs[0][:i]

        return strs[0]


def run_case(strs: List[str], expected: str) -> None:
    actual = Solution().longestCommonPrefix(strs[:])
    assert actual == expected


if __name__ == "__main__":
    run_case(["flower", "flow", "flight"], "fl")
    run_case(["dog", "racecar", "car"], "")
    run_case(["apple", "ape", "april"], "ap")
    run_case(["a"], "a")
    run_case([], "")

    print("all tests passed")
