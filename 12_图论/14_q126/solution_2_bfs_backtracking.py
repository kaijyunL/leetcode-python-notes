# 方法2：BFS 分层 + 记录前驱 + 回溯（面试主推）

from collections import defaultdict
from string import ascii_lowercase
from typing import DefaultDict, List, Set


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        current_level: Set[str] = {beginWord}
        parents: DefaultDict[str, Set[str]] = defaultdict(set)
        found_end = False

        while current_level and not found_end:
            word_set -= current_level
            next_level: Set[str] = set()

            for word in current_level:
                for i in range(len(word)):
                    original_char = word[i]

                    for char in ascii_lowercase:
                        if char == original_char:
                            continue

                        next_word = word[:i] + char + word[i + 1 :]
                        if next_word not in word_set:
                            continue

                        if next_word == endWord:
                            found_end = True

                        next_level.add(next_word)
                        parents[next_word].add(word)

            current_level = next_level

        if not found_end:
            return []

        result: List[List[str]] = []
        path = [endWord]

        def backtrack(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for prev_word in sorted(parents[word]):
                path.append(prev_word)
                backtrack(prev_word)
                path.pop()

        backtrack(endWord)
        return result


if __name__ == "__main__":
    solution = Solution()

    def normalize(paths):
        return sorted(tuple(path) for path in paths)

    expected = normalize([
        ["hit", "hot", "dot", "dog", "cog"],
        ["hit", "hot", "lot", "log", "cog"],
    ])

    assert normalize(solution.findLadders(
        "hit",
        "cog",
        ["hot", "dot", "dog", "lot", "log", "cog"],
    )) == expected

    assert solution.findLadders(
        "hit",
        "cog",
        ["hot", "dot", "dog", "lot", "log"],
    ) == []

    assert solution.findLadders(
        "a",
        "c",
        ["a", "b", "c"],
    ) == [["a", "c"]]

    print("all tests passed")
