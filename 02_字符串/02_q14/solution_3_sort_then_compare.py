# 方法3：排序后只比较首尾字符串
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        i = 0

        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1

        return first[:i]


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
