# 方法2：哈希表 + 排序字符串作为 Key（面试主推）

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)

        return list(groups.values())


def normalize(groups):
    return sorted(sorted(g) for g in groups)


if __name__ == "__main__":
    solution = Solution()

    assert normalize(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == \
        normalize([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
    assert normalize(solution.groupAnagrams([""])) == [[""]]
    assert normalize(solution.groupAnagrams(["a"])) == [["a"]]

    print("all tests passed")
