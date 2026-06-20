# 方法1：横向扫描
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


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
