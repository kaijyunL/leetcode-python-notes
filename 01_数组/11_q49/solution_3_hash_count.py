# 方法3：哈希表 + 字母计数作为 Key（最优解）

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            counts = [0] * 26
            for ch in s:
                counts[ord(ch) - ord('a')] += 1
            groups[tuple(counts)].append(s)  # 列表不可哈希，转 tuple

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
