# LeetCode 692 — 前 K 个高频单词（Top K Frequent Words）

## 题目

给定一个单词列表 `words` 和一个整数 `k`，请返回出现频率前 `k` 高的单词。

返回结果按以下规则排序：
1. 频率高的排前面
2. 频率相同时，按**字典序升序**排序

### 示例

```
输入: words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解释: "i" 和 "love" 都出现 2 次，频率相同，按字典序 "i" < "love"
```

```
输入: words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解释: 频率分别为 4, 3, 2, 1
```

---

## 核心难点

这题和 Q347「前 K 个高频元素」很像，但多了一个排序要求：

```
频率高的更靠前
频率相同，字典序小的更靠前
```

所以一个单词的优先级可以理解成：

```
(-出现次数, 单词)
```

因为 Python 默认是升序排序：
- `-出现次数` 越小，说明原始出现次数越大
- `单词` 越小，说明字典序越靠前

另外，下面复杂度中：
- `n` 表示 `words` 的总长度
- `m` 表示不同单词的个数，`m <= n`

## 解法一览

| 解法 | 时间 | 空间 | 是否推荐面试 |
|---|---|---|---|
| 1. 哈希表 + 排序 | O(n + m log m) | O(m) | 简单推荐 |
| 2. 哈希表 + 堆 | O(n + m log k + k log k) | O(m + k) | **进阶推荐 ✅** |

---

## 解法 1：哈希表 + 排序

**思路：** 统计频率后，按"频率降序 + 字典序升序"排序，取前 k 个。

代码：

```python
freq = Counter(words)
return sorted(freq.keys(), key=lambda w: (-freq[w], w))[:k]
```

排序 key：

```python
(-freq[w], w)
```

含义：
- `-freq[w]`：出现次数越多，排序越靠前
- `w`：出现次数相同，字典序越小，排序越靠前

### 示例

```
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
```

统计频率：

```
i: 2
love: 2
leetcode: 1
coding: 1
```

按 `(-频率, 单词)` 排序：

```
i        -> (-2, "i")
love     -> (-2, "love")
coding   -> (-1, "coding")
leetcode -> (-1, "leetcode")
```

结果：

```
["i", "love"]
```

### 复杂度

统计频率需要 `O(n)`。

排序的是不同单词，共 `m` 个，所以排序需要 `O(m log m)`。

总时间复杂度：

```
O(n + m log m)
```

空间复杂度：

```
O(m)
```

---

## 解法 2：哈希表 + 堆 ⭐ 面试推荐

**思路：** 维护一个大小为 `k` 的最小堆。

题目要的是：

```
频率高的排前面
频率相同，字典序小的排前面
```

堆里只保留 `k` 个单词。每次加入新单词后，如果堆大小超过 `k`，就弹出堆顶。

因此堆顶应该放：

```
频率最低的单词
频率相同时，字典序最大的单词
```

这样弹出堆顶后，堆里留下的就是当前频率最高的 `k` 个单词；频率相同时，会留下字典序更小的单词。

所以堆的比较规则应该是：

```
(频率升序, 字典序降序)
```

也就是：
- 频率小的排在堆顶
- 频率相同时，字典序大的排在堆顶

### 为什么不能直接写 `(count, word)`？

这是这题最容易写错的地方。

如果堆里存：

```python
(count, word)
```

Python 最小堆会先比较 `count`，`count` 相同再比较 `word`。

对于：

```python
words = ["a", "b", "c"]
k = 2
```

三个单词频率都为 `1`。正确答案应该是：

```python
["a", "b"]
```

因为频率相同，字典序小的更靠前。

但 `(count, word)` 的堆顶会是：

```python
(1, "a")
```

当堆大小超过 `k` 时，会先弹出 `"a"`，这正好弹掉了应该保留的单词。

所以堆里不能直接用 `(count, word)`。

### Python 中如何实现“字典序降序”？

Python 的 `heapq` 不支持传入自定义 `key`，所以可以给单词包一层，让它在比较时反过来：

```python
class ReverseWord:
    def __init__(self, word: str):
        self.word = word

    def __lt__(self, other: "ReverseWord") -> bool:
        return self.word > other.word
```

这样：

```python
ReverseWord("c") < ReverseWord("b")
```

会被认为是 `True`，也就是字典序大的 `"c"` 会更靠近堆顶。

堆中保存：

```python
(count, ReverseWord(word), word)
```

含义是：

```
先按 count 升序
count 相同，再按 word 的反向字典序
最后保留原始 word 用于返回答案
```

### 代码框架

```python
freq = Counter(words)
heap = []

for word, count in freq.items():
    heapq.heappush(heap, (count, ReverseWord(word), word))
    if len(heap) > k:
        heapq.heappop(heap)

return [word for count, _, word in sorted(heap, key=lambda item: (-item[0], item[2]))]
```

最后为什么还要排序？

堆只能保证堆顶是当前最小元素，不能保证整个堆数组有序。题目要求最终结果按：

```
频率降序 + 字典序升序
```

返回，所以最后需要对堆中的 `k` 个元素再排一次。

### 复杂度

统计频率：

```
O(n)
```

遍历 `m` 个不同单词，每次堆操作是 `O(log k)`：

```
O(m log k)
```

最后排序堆中的 `k` 个元素：

```
O(k log k)
```

总时间复杂度：

```
O(n + m log k + k log k)
```

空间复杂度：

```
O(m + k)
```

其中 `Counter` 占 `O(m)`，堆占 `O(k)`。

---

## 面试建议

如果只是要快速写出正确答案，优先写解法 1：排序法。它最短、最稳定、也最不容易出错。

如果面试官追问 Top K 优化，再讲解法 2：堆法。

讲堆法时重点说清楚三句话：

1. 我维护一个大小为 `k` 的最小堆
2. 堆顶放频率最低的单词
3. 频率相同时，堆顶放字典序最大的单词

这题的坑也在这里：`(count, word)` 会在频率相同时弹出字典序小的单词，是错的。
