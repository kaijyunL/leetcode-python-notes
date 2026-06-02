# 方法1：直接存所有单词
# search 时逐个单词比较；. 可以匹配任意一个字符
# addWord O(1)，search O(nL)，空间 O(nL)


class WordDictionary:
    def __init__(self):
        self.words = []

    def addWord(self, word: str) -> None:
        self.words.append(word)

    def search(self, pattern: str) -> bool:
        for word in self.words:
            if len(word) != len(pattern):
                continue

            matched = True
            for i in range(len(pattern)):
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
