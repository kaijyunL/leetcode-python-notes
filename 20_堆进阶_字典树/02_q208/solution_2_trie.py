# 方法2：Trie / 前缀树（面试主推）
# children 负责往下走，is_end 标记当前节点是否是单词结尾
# insert/search/startsWith 都只沿着字符串长度向下移动


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


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
