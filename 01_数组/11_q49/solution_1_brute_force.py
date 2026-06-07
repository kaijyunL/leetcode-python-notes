# 方法1：暴力匹配

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        def is_anagram(s1, s2):
            if len(s1) != len(s2):
                return False
            return sorted(s1) == sorted(s2)

        for s in strs:
            found = False
            for group in res:
                # 只需和组内第一个词比（同组内所有词互为异位词）
                if is_anagram(s, group[0]):
                    group.append(s)
                    found = True
                    break
            if not found:
                res.append([s])

        return res


def normalize(groups):
    return sorted(sorted(g) for g in groups)


if __name__ == "__main__":
    solution = Solution()

    assert normalize(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == \
        normalize([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
    assert normalize(solution.groupAnagrams([""])) == [[""]]
    assert normalize(solution.groupAnagrams(["a"])) == [["a"]]

    print("all tests passed")
