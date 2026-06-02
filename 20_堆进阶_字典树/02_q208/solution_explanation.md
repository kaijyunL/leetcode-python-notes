# LeetCode 208. 实现 Trie（前缀树）（Implement Trie / Prefix Tree）解析

## 题目描述

实现一个 `Trie` 类，支持下面三个操作：

```python
insert(word)
search(word)
startsWith(prefix)
```

其中：

- `insert(word)`：插入一个单词
- `search(word)`：判断一个完整单词是否存在
- `startsWith(prefix)`：判断是否存在某个单词以这个前缀开头

经典例子：

```text
Trie trie = new Trie()
trie.insert("apple")
trie.search("apple")    -> True
trie.search("app")      -> False
trie.startsWith("app")  -> True
trie.insert("app")
trie.search("app")      -> True
```

---

## 先理解题意

这题的重点不是“把字符串存起来”这么简单。

它真正要支持的是两种不同的查询：

1. **完整单词是否存在**
2. **某个前缀是否存在**

最容易混淆的是这一组操作：

```text
先 insert("apple")

search("app") -> False
startsWith("app") -> True
```

为什么？

因为：

```text
a -> p -> p 这条路径确实存在
但 app 这个单词本身还没有结束
```

所以这题不只要记录“路径有没有”，还要记录：

```text
某个节点是不是一个单词的结尾
```

也就是后面 Trie 里常见的：

```text
is_end
```

另外，这题本身没有必要强行拆成很多方法。

因为它的核心价值就在于：

```text
从线性扫描，过渡到真正适合做前缀查询的 Trie
```

所以这里给两种方法就够了：

- 方法一：直接存所有单词
- 方法二：Trie / 前缀树

---

## 方法一：直接存所有单词

### 思路

最直接的做法，就是把插入过的单词全部存下来。

比如用一个列表：

```python
self.words = []
```

三个操作分别怎么做：

- `insert(word)`：直接追加到列表里
- `search(word)`：遍历列表，看看有没有完全相等的单词
- `startsWith(prefix)`：遍历列表，看看有没有单词以 `prefix` 开头

### 代码

```python
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
```

### 评价

这个方法的优点是：

```text
非常直观，几乎不用额外设计数据结构
```

但问题也很明显：

```text
每次 search / startsWith 都要把所有单词重新扫一遍
```

尤其是 `startsWith(prefix)`，明明我们只是想查一个前缀，结果却要拿这个前缀去和很多单词重复比较。

比如插入了：

```text
apple
application
apply
apt
```

查询 `startsWith("app")` 时，会反复去比较这些单词的前几个字符。

这就是重复劳动。

### 复杂度

设：

- `n` = 当前插入的单词个数
- `L` = 单词平均长度
- `P` = 前缀长度

复杂度：

- `insert`：`O(1)`
- `search`：`O(n * L)`
- `startsWith`：`O(n * P)`
- 空间复杂度：`O(n * L)`

所以这个方法能做，但不适合把它当成这题的标准答案。

---

## 方法二：Trie / 前缀树（面试主推）

### 核心思路

既然很多单词会共享前缀，那我们就不要把这些前缀重复存很多次。

而是把它们合并成一棵树。

比如插入这些单词：

```text
apple
app
apt
```

它们都以 `ap` 开头，所以前两层路径可以共用。

Trie 的每个节点主要保存两类信息：

1. `children`：从当前字符往下走，下一层有哪些字符
2. `is_end`：当前节点是不是某个单词的结尾

可以理解成：

```text
children 负责“路通不通”
is_end 负责“这个位置能不能算一个完整单词”
```

---

### 为什么一定要有 `is_end`

这是这题最关键的细节。

先只插入：

```text
apple
```

Trie 大概是这样：

```text
root
└── a
    └── p
        └── p
            └── l
                └── e* 
```

这里 `*` 表示这个节点是某个单词的结尾，也就是 `is_end = True`。

这时：

- `search("apple")` 应该返回 `True`
- `search("app")` 应该返回 `False`
- `startsWith("app")` 应该返回 `True`

注意：

```text
app 这条路径存在
但第三个 p 这个节点还不是单词结尾
```

如果后来再插入：

```text
app
```

那就变成：

```text
root
└── a
    └── p
        └── p*
            └── l
                └── e*
```

这时 `search("app")` 才会变成 `True`。

所以：

```text
search 看的是“路径存在 + 结尾标记为 True”
startsWith 只看“路径是否存在”
```

---

### `insert` 怎么做

插入一个单词时，从根节点开始，一个字符一个字符往下走。

如果当前字符对应的子节点不存在，就新建一个。

例如插入 `apple`：

```text
root -> a -> p -> p -> l -> e
```

最后走到 `e` 对应的节点时，把：

```text
is_end = True
```

表示有单词在这里结束。

代码过程就是：

```python
node = self.root
for ch in word:
    if ch not in node.children:
        node.children[ch] = TrieNode()
    node = node.children[ch]
node.is_end = True
```

这里的 `node` 可以理解成：

```text
当前走到哪一个节点
```

每处理完一个字符，就把 `node` 往下一层推进。

---

### `search` 怎么做

`search(word)` 要求这个单词完整存在。

做法也是从根节点开始，按字符往下走：

- 如果某个字符对应的子节点不存在，直接返回 `False`
- 如果整条路径都走完了，再看最后那个节点的 `is_end` 是不是 `True`

也就是说：

```text
路径存在，不代表单词存在
必须最后一个节点是结尾节点才行
```

代码逻辑：

```python
node = self.root
for ch in word:
    if ch not in node.children:
        return False
    node = node.children[ch]
return node.is_end
```

---

### `startsWith` 怎么做

`startsWith(prefix)` 比 `search(word)` 更简单。

因为它不要求前缀本身是一个完整单词。

它只要求：

```text
prefix 这条路径能不能顺着走下去
```

所以：

- 如果中途某个字符不存在，返回 `False`
- 如果整个前缀都能走完，直接返回 `True`

代码逻辑：

```python
node = self.root
for ch in prefix:
    if ch not in node.children:
        return False
    node = node.children[ch]
return True
```

---

### 面试代码

```python
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
```

---

### 复杂度

设单词长度为 `L`，前缀长度为 `P`。

则：

- `insert(word)`：`O(L)`
- `search(word)`：`O(L)`
- `startsWith(prefix)`：`O(P)`

空间复杂度：

- `O(总字符数)`

更准确地说，是所有插入单词形成的节点总数。

如果很多单词共享前缀，Trie 会把公共前缀共用掉。

这也是它比“直接存所有字符串”更适合做前缀查询的原因。

---

### 为什么它最适合面试

这题最适合面试的方法就是 Trie。

原因很直接：

1. **题目本身就在考前缀结构设计**
2. `insert / search / startsWith` 三个操作都能自然落到 Trie 的节点移动上
3. 代码量不大，但能清楚体现你是否真的理解“路径”和“单词结尾”是两回事

面试里可以这样解释：

```text
我用一棵前缀树来存所有单词。

每个节点有两个信息：
1. children：下一层字符到子节点的映射
2. is_end：是否有单词在这里结束

insert 就是沿着字符往下走，没有就新建；
search 要求整条路径存在，并且最后节点的 is_end 为 True；
startsWith 只要求前缀路径存在，不要求 is_end 为 True。

这样 insert 和 search 都是按单词长度走一遍，
startsWith 也是按前缀长度走一遍。
```

最容易出错的点就是：

```text
不要把“路径存在”和“单词存在”混为一谈
```

也就是：

```text
search 最后一定要检查 is_end
```

---

## 总结

| 方法 | `insert` | `search` | `startsWith` | 空间 | 评价 |
| --- | --- | --- | --- | --- | --- |
| 方法一：直接存所有单词 | `O(1)` | `O(n * L)` | `O(n * P)` | `O(n * L)` | 直观，但前缀查询慢 |
| 方法二：Trie / 前缀树 | `O(L)` | `O(L)` | `O(P)` | `O(总字符数)` | 面试主推 |

这题真正该掌握的是：

```text
search 和 startsWith 的区别，
本质上就是“是否要求当前节点是单词结尾”。
```

最适合面试的方法：**方法二：Trie / 前缀树**。
