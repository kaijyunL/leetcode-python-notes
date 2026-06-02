# LeetCode 211. 添加与搜索单词 - 数据结构设计（Design Add and Search Words Data Structure）解析

## 题目描述

设计一个数据结构 `WordDictionary`，支持下面两个操作：

```python
addWord(word)
search(word)
```

其中 `search(word)` 里的 `word` 不一定是普通字符串，它还可能包含字符 `.`。

规则是：

```text
. 可以匹配任意一个字母
```

例如：

```text
addWord("bad")
addWord("dad")
addWord("mad")

search("pad") -> False
search("bad") -> True
search(".ad") -> True
search("b..") -> True
```

---

## 先理解题意

这题本质上是 208 Trie 的升级版。

208 只有：

- 插入单词
- 查完整单词
- 查前缀

而 211 新增的难点是：

```text
search 里允许出现通配符 .
```

`search("bad")` 很简单，就是普通精确匹配。

真正的难点是：

```text
search("b..")
```

这里的意思不是找字符串字面量 `b..`。

而是：

```text
第 1 个字符必须是 b
第 2 个字符随便
第 3 个字符随便
```

所以它能匹配：

```text
bad
bed
big
```

只要长度一致、位置上能匹配就行。

这时就会出现一个关键变化：

```text
当遇到 . 时，不再只有一条路可以走，而是要尝试所有子节点
```

这也是为什么这题最后的标准解法会是：

```text
Trie + DFS
```

---

## 方法一：直接存所有单词，再逐个匹配

### 思路

最直接的做法，就是把所有单词都存下来。

`addWord(word)`：直接保存。

`search(pattern)`：把所有存过的单词拿出来，一个个和模式串比较。

比较时分两种情况：

- 如果 `pattern[i]` 是普通字符，那它必须和单词对应位置完全相等
- 如果 `pattern[i] == '.'`，那这个位置直接视为匹配成功

### 代码

```python
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
```

### 评价

这个方法的优点是：

```text
非常直观，通配符 . 也容易处理
```

但问题也很明显：

```text
每次 search 都要把所有单词重新扫一遍
```

如果已经加入了很多单词，查询会越来越慢。

### 复杂度

设：

- `n` = 当前单词数量
- `L` = 模式串平均长度

则：

- `addWord`：`O(1)`
- `search`：`O(n * L)`
- 空间复杂度：`O(n * L)`

---

## 方法二：按长度分桶，再逐个匹配

### 思路

观察一下：

```text
. 只能匹配“一个字符”
```

这意味着：

```text
search(pattern) 只能匹配和 pattern 长度相同的单词
```

比如：

- `search("b..")` 只可能匹配长度为 3 的单词
- 长度为 2 或 4 的单词，连比较都不用比较

所以我们可以做一个小优化：

```python
self.groups[length] = [所有这个长度的单词]
```

查询时只扫描同长度的那一桶。

### 代码

```python
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
```

### 评价

这个方法比方法一好一点，因为它先做了一层过滤：

```text
不同长度的单词直接排除
```

所以当单词长度分布比较散时，它会更快。

但本质问题没变：

```text
search 时还是要把一批候选单词挨个比
```

也就是说，它只是减少了候选范围，还没有利用“前缀共享”这件事。

### 复杂度

设某个长度桶里有 `k` 个单词，模式串长度是 `L`。

则：

- `addWord`：`O(1)`
- `search`：`O(k * L)`
- 空间复杂度：`O(n * L)`

当很多单词长度一样时，这个方法还是会慢。

---

## 方法三：Trie + DFS（面试主推）

### 核心思路

208 里我们已经知道：

```text
Trie 很适合处理“按字符一层层往下走”的问题
```

211 依然是按字符逐位匹配，只是多了一个特殊字符 `.`。

所以整体思路还是 Trie。

区别在于：

- 普通字符：只能沿着对应那一条边继续走
- `.`：可以匹配任意一个字符，所以要尝试当前节点的所有子节点

这就是 DFS 的来源。

可以把它理解成：

```text
普通字符 = 单路往下走
. = 分叉，所有路都要试
```

---

### Trie 节点里存什么

和 208 一样，每个节点需要两部分信息：

1. `children`：当前节点往下有哪些字符
2. `is_end`：是否有单词在这里结束

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
```

---

### `addWord` 怎么做

这个部分和 208 基本一样。

从根节点开始，按字符一层层往下走：

- 没有这个子节点就创建
- 有就直接往下走
- 最后把结尾节点标记为 `is_end = True`

例如加入：

```text
bad
```

路径就是：

```text
root -> b -> a -> d
```

最后 `d` 这个节点标记为单词结尾。

---

### `search` 为什么不能再像 208 那样直接写循环

208 的 `search(word)` 没有 `.`，所以每一层都只有一个确定字符。

比如搜：

```text
bad
```

那路径就是唯一的：

```text
b -> a -> d
```

直接循环就行。

但是 211 如果搜：

```text
b..
```

第一层 `b` 确定，没问题。

但到了第二层是 `.`，这时你不知道该往哪个子节点走。

假设当前节点下面有：

```text
a
r
e
```

那这三条路都得尝试。

所以：

```text
search 不再是单一路径问题，而是“可能分叉的搜索问题”
```

这正是 DFS 最自然的场景。

---

### DFS 到底在搜什么

定义一个递归函数：

```python
dfs(node, index)
```

它表示：

```text
当前站在 node 这个 Trie 节点上，
接下来要匹配 pattern[index:] 这一段后缀，
是否能匹配成功？
```

这个定义非常重要。

因为一旦你把递归函数的含义想清楚，后面的转移就会很自然。

---

### 递归终止条件

当：

```text
index == len(pattern)
```

说明模式串已经全部匹配完了。

这时不能直接返回 `True`，还要看：

```text
当前节点是不是某个完整单词的结尾
```

也就是：

```python
return node.is_end
```

为什么？

因为：

```text
模式串走完，只代表路径存在
不代表这里正好有单词结束
```

这个点和 208 的 `search` 本质完全一致。

---

### 当前字符是普通字母时怎么转移

如果：

```python
ch = pattern[index]
ch != '.'
```

那就只有一种走法：

- 如果 `ch` 不在 `node.children` 里，返回 `False`
- 如果在，就递归检查下一个位置

即：

```python
if ch not in node.children:
    return False
return dfs(node.children[ch], index + 1)
```

这一步很好理解，因为普通字符没有分叉。

---

### 当前字符是 `.` 时怎么转移

这是整题最关键的地方。

如果当前字符是：

```python
pattern[index] == '.'
```

它可以匹配任意一个字符。

也就是说，当前节点下面的每个子节点，都可能是下一步。

所以要做的是：

```text
遍历当前节点的所有子节点，只要有一条路能匹配成功，就返回 True
如果所有路都失败，才返回 False
```

代码就是：

```python
for child in node.children.values():
    if dfs(child, index + 1):
        return True
return False
```

注意这里为什么是 `index + 1`。

因为：

```text
. 虽然能匹配任意字符，但它也只匹配“一个字符”
```

所以模式串位置还是要往后走一格。

这是面试里非常容易说漏的细节。

---

### 用例子走一遍：`search(".ad")`

假设 Trie 里有：

```text
bad
dad
mad
```

从根节点开始搜索 `.ad`。

#### 第 1 位：`.`

因为是通配符，所以根节点下面所有子节点都要试：

- 试 `b`
- 试 `d`
- 试 `m`

#### 假设先试 `b`

剩下要匹配的是：

```text
ad
```

继续往下：

- `a` 必须存在
- `d` 必须存在
- 最后节点还必须是 `is_end = True`

这条路成功，所以整个搜索就返回 `True`。

这里不需要把所有路都搜完：

```text
只要有一条路成功，就可以立刻返回 True
```

---

### 再走一遍：`search("b..")`

假设 Trie 里有：

```text
bad
bed
boy
```

搜索 `b..`：

1. 第 1 位 `b`：只能走 `b`
2. 第 2 位 `.`：要尝试 `a / e / o`
3. 第 3 位 `.`：在各自分支下继续尝试下一层
4. 只要存在某条长度刚好匹配且落在 `is_end=True` 的路径，就返回 `True`

你会发现：

```text
. 的本质就是“把原来唯一的一条路径，扩展成多条候选路径”
```

所以用 DFS 最自然。

---

### 面试代码

```python
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
```

---

### 复杂度

#### `addWord`

如果单词长度是 `L`：

- 时间复杂度：`O(L)`
- 空间复杂度：最坏新增 `O(L)` 个节点

#### `search`

如果没有 `.`，那就是普通 Trie 查询：

- 时间复杂度：`O(L)`

如果有很多 `.``，就会分叉。

最坏情况下，模式串每一位都是 `.`，而且 Trie 很满，那么会尝试很多路径。

所以最坏时间复杂度可以写成：

- 最坏：`O(26^L)`

当然这是非常极端的上界。

实际面试里更重要的是说清楚：

```text
普通字符只走一条路，.
会导致分叉，所以 search 的复杂度取决于通配符的位置和 Trie 的分支情况。
```

---

### 为什么它最适合面试

这题最适合面试的方法就是：**Trie + DFS**。

原因是：

1. 插入操作天然适合 Trie
2. `.` 会造成多路分叉，DFS 正好处理“从当前节点继续尝试所有可能”
3. 代码量适中，能很好体现你对 Trie 和递归搜索的理解

面试里可以这样讲：

```text
我还是用 Trie 存单词。

addWord 和 208 一样，按字符插入。

search 的关键区别在于：
如果当前字符是普通字母，就沿着唯一对应的子节点继续搜索；
如果当前字符是 .，它可以匹配任意一个字母，
所以我要从当前节点的所有子节点继续递归，只要有一条路成功就返回 True。

递归函数 dfs(node, index) 表示：
从当前节点出发，能不能匹配 word[index:]。

当 index 到头时，只有当前节点是单词结尾，才算匹配成功。
```

最容易错的地方有三个：

1. `search` 结束时要检查 `is_end`
2. `.` 匹配的是任意一个字符，不是任意长度
3. `.` 分支要“有一个成功就返回 True”，不是必须全部成功

---

## 总结

| 方法 | `addWord` | `search` | 空间 | 评价 |
| --- | --- | --- | --- | --- |
| 方法一：直接存单词 | `O(1)` | `O(n * L)` | `O(n * L)` | 最直观，但每次都全扫 |
| 方法二：按长度分桶 | `O(1)` | `O(k * L)` | `O(n * L)` | 比全扫好一点，但本质还是枚举 |
| 方法三：Trie + DFS | `O(L)` | 普通情况 `O(L)`，最坏分叉很多 | `O(总字符数)` | 面试主推 |

这题真正要掌握的是：

```text
208 的 Trie 查询只有一条确定路径，
211 因为有 .，查询会从“单路”变成“多路分叉搜索”。
```

最适合面试的方法：**方法三：Trie + DFS**。
