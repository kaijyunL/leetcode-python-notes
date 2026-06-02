# 方法3：Trie + DFS（面试主推）
# 普通字符沿唯一子节点向下；遇到 . 时递归尝试所有子节点
# addWord O(L)，普通 search O(L)，最坏会因通配符分叉变大


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.is_end

            ch = word[index]

            if ch == ".":
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False

            if ch not in node.children:
                return False
            return dfs(node.children[ch], index + 1)

        return dfs(self.root, 0)


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
