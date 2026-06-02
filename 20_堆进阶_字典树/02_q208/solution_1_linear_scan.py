# 方法1：直接存所有单词
# insert 直接追加；search 和 startsWith 都线性扫描
# insert O(1)，search O(nL)，startsWith O(nP)，空间 O(nL)


class Trie:
    def __init__(self):
        self.words = []

    def insert(self, word: str) -> None:
        self.words.append(word)

    def search(self, word: str) -> bool:
        for saved in self.words:
            if saved == word:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for saved in self.words:
            if saved.startswith(prefix):
                return True
        return False


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True

    trie = Trie()
    for word in ["cat", "car", "dog"]:
        trie.insert(word)
    assert trie.search("car") is True
    assert trie.search("cap") is False
    assert trie.startsWith("ca") is True
    assert trie.startsWith("do") is True
    assert trie.startsWith("cow") is False

    print("all tests passed")
