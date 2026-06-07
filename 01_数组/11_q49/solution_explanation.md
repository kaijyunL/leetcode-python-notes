# LeetCode 49. 字母异位词分组（Group Anagrams）解析

## 题目描述

给你一个字符串数组 `strs`，将 **字母异位词** 组合在一起返回。可以按任意顺序返回结果列表。

**字母异位词**：重新排列源单词的所有字母得到的新单词。

例如：

```text
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

结果是（顺序不限）：

```text
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

因为：

- `eat`、`tea`、`ate` 三个词字母完全相同，互为异位词
- `tan`、`nat` 互为异位词
- `bat` 自己一组

---

## 先理解这题最关键的一句话

判断两个词是不是字母异位词，最直观的办法是：

```text
把两个词的字母都排序，排完之后如果相等，它们就是异位词
```

比如：

```text
sorted("eat") = ['a', 'e', 't']
sorted("tea") = ['a', 'e', 't']
```

两个一模一样，所以是异位词。

但如果用两两比较，要 `O(n^2)` 次对比，太慢。

真正的核心是换一个角度想：

```text
给每个词算一个“代表键”，让所有异位词算出同一个键，再用哈希表按键分组
```

一旦这句话想明白，这题就顺了。剩下的区别只是：**用什么当这个键**。

---

## 方法一：暴力匹配

### 思路

维护一个结果列表，里面每个元素是一个已经分好的组。

每遇到一个新词，就遍历已有的组，跟组内第一个词比较：

```text
排序后相等 → 加入这个组
都不相等 → 自己新建一组
```

### 代码

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        def is_anagram(s1, s2):
            if len(s1) != len(s2):
                return False
            return sorted(s1) == sorted(s2)

        for s in strs:
            found = False
            for group in res:
                if is_anagram(s, group[0]):
                    group.append(s)
                    found = True
                    break
            if not found:
                res.append([s])

        return res
```

### 为什么可行

因为它完全按定义来：每个新词都和已有每个组逐一比对，匹配上才归类，所以结果一定正确。

### 为什么会慢

- 外层遍历每个词
- 内层又要遍历已有的组，每次比较还要排序

最坏情况下组数接近词数，总操作次数是：

```text
O(n^2 * k log k)
```

其中 `n` 是词数，`k` 是单词最大长度。数据一大就超时。

### 复杂度

- 时间复杂度：`O(n^2 * k log k)`
- 空间复杂度：`O(n * k)`（不算返回值）

---

## 方法二：哈希表 + 排序后的字符串作为 Key（面试主推）

### 核心思路

异位词排序后必然相等，那就直接拿排序后的字符串当哈希表的键。

用 `["eat", "tea", "tan", "ate"]` 走一遍，看哈希表怎么长出来的：

```text
来 "eat" → 排序后 "aet" → {"aet": ["eat"]}
来 "tea" → 排序后 "aet" → {"aet": ["eat", "tea"]}
来 "tan" → 排序后 "ant" → {"aet": ["eat", "tea"], "ant": ["tan"]}
来 "ate" → 排序后 "aet" → {"aet": ["eat", "tea", "ate"], "ant": ["tan"]}
```

遍历完，直接返回哈希表所有的 value 即可。

### 面试代码

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            anagram_map[key].append(s)

        return list(anagram_map.values())
```

### 这里为什么用 defaultdict(list)

`defaultdict(list)` 的意思是：访问一个不存在的键时，自动先放一个空列表 `[]` 进去。

所以 `anagram_map[key].append(s)` 这一行不用先判断键在不在，直接 append 就行，省掉了手动初始化的判断。

### 为什么这个方法最适合面试

1. **代码极简**：核心就 3 行，面试现场写完几乎不会出错
2. **思路自然**：直接从“排序后相等”这个直觉推出来，不需要额外铺垫
3. **复杂度够用**：`O(n * k log k)` 在 LeetCode 上稳过，单词长度一般不大，排序的常数很小
4. **不一定要上最优解**：方法三能把 `log k` 干掉，但代码更长，面试官不追问就用这个版本

### 复杂度

- 时间复杂度：`O(n * k log k)` —— 遍历 `n` 个词，每个词排序 `O(k log k)`
- 空间复杂度：`O(n * k)`

---

## 方法三：哈希表 + 字母计数作为 Key（最优解）

### 核心思路

方法二的瓶颈在排序的 `O(k log k)`。如果不排序，怎么给一个词算出统一的键？

```text
用一个长度为 26 的数组，记录每个字母出现的次数
```

异位词的字母构成完全相同，所以它们的计数数组也完全相同，天然就是统一的键。

比如：

```text
"abbc" → a 出现 1 次，b 出现 2 次，c 出现 1 次
       → [1, 2, 1, 0, 0, ..., 0]  （长度 26）
```

因为 Python 字典的键必须可哈希，而列表不可哈希，所以把计数数组转成 `tuple` 再当键。

### 面试代码

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            counts = [0] * 26
            for ch in s:
                counts[ord(ch) - ord('a')] += 1
            anagram_map[tuple(counts)].append(s)

        return list(anagram_map.values())
```

这里 `ord(ch) - ord('a')` 把字母映射成 `0~25` 的下标：`'a'` 算出 0，`'b'` 算出 1，以此类推。

### 和方法二的递进关系

两种方法的框架完全一样，区别只在“用什么当键”：

- 方法二：用排序提取特征，`O(k log k)`
- 方法三：用计数提取特征，`O(k)`

优化点就是把每个词的排序换成了一次 `O(k)` 的线性扫描。当单词很长时优势明显，但代码比方法二长，面试时如果不追问可以不写。

### 复杂度

- 时间复杂度：`O(n * k)` —— 遍历 `n` 个词，每个词统计字母 `O(k)`
- 空间复杂度：`O(n * k)`

---

## 面试里可以怎么讲

你可以这样说：

```text
异位词排序后一定相等，所以我可以把排序后的字符串当作哈希表的键，
一次遍历，把每个词丢进对应的桶里，最后返回所有桶就行。

如果还想去掉排序的 log k，可以改成用长度 26 的字母计数数组当键，
这样每个词只需要 O(k) 的扫描，整体降到 O(n * k)。
```

先讲方法二，再说能优化到方法三，层次最完整。

---

## 总结

| 方法 | 时间复杂度 | 空间复杂度 | 评价 |
| --- | --- | --- | --- |
| 方法一：暴力匹配 | `O(n^2 * k log k)` | `O(n * k)` | 直观，但太慢 |
| 方法二：哈希表 + 排序 Key | `O(n * k log k)` | `O(n * k)` | 面试主推，代码最简 |
| 方法三：哈希表 + 计数 Key | `O(n * k)` | `O(n * k)` | 最优解，面试官追问再写 |

这题最重要的一句话就是：

```text
给每个词算一个统一的“代表键”，异位词的键相同，用哈希表按键分组
```

只要这句话想清楚，键用排序还是用计数，都能自己推出来。
