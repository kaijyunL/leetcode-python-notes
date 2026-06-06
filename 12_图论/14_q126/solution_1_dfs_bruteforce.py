# 方法1：构图后 DFS 枚举所有路径

from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        words = list(word_set)
        if beginWord not in word_set:
            words.append(beginWord)

        graph: DefaultDict[str, List[str]] = defaultdict(list)
        n = len(words)

        for i in range(n):
            for j in range(i + 1, n):
                if self._is_neighbor(words[i], words[j]):
                    graph[words[i]].append(words[j])
                    graph[words[j]].append(words[i])

        for word in graph:
            graph[word].sort()

        result: List[List[str]] = []
        path = [beginWord]
        used = {beginWord}
        shortest_length = float("inf")

        def dfs(word):
            nonlocal shortest_length

            if len(path) > shortest_length:
                return

            if word == endWord:
                if len(path) < shortest_length:
                    shortest_length = len(path)
                    result.clear()
                result.append(path.copy())
                return

            for next_word in graph[word]:
                if next_word in used:
                    continue
                used.add(next_word)
                path.append(next_word)
                dfs(next_word)
                path.pop()
                used.remove(next_word)

        dfs(beginWord)
        return result

    def _is_neighbor(self, word1: str, word2: str) -> bool:
        diff = 0

        for char1, char2 in zip(word1, word2):
            if char1 != char2:
                diff += 1
                if diff > 1:
                    return False

        return diff == 1


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
