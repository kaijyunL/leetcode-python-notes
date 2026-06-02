# 方法2：按长度分桶
# 先按长度过滤候选单词，再逐个比较；. 仍表示任意一个字符
# addWord O(1)，search O(kL)，空间 O(nL)


class WordDictionary:
    def __init__(self):
        self.groups = {}

    def addWord(self, word: str) -> None:
        length = len(word)
        if length not in self.groups:
            self.groups[length] = []
        self.groups[length].append(word)

    def search(self, pattern: str) -> bool:
        length = len(pattern)
        if length not in self.groups:
            return False

        for word in self.groups[length]:
            matched = True
            for i in range(length):
                if pattern[i] != "." and pattern[i] != word[i]:
                    matched = False
                    break

            if matched:
                return True

        return False


if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    assert wd.search("pad") is False
    assert wd.search("bad") is True
    assert wd.search(".ad") is True
    assert wd.search("b..") is True

    wd = WordDictionary()
    for word in ["at", "and", "an", "add"]:
        wd.addWord(word)
    assert wd.search("a") is False
    assert wd.search(".at") is False
    wd.addWord("bat")
    assert wd.search(".at") is True
    assert wd.search("an.") is True
    assert wd.search("a.d.") is False
    assert wd.search("b.") is False
    assert wd.search("a.d") is True

    print("all tests passed")
