# LeetCode 547. 省份数量 (Number of Provinces)

## 题目描述
有 `n` 个城市，其中一些彼此相连，另一些没有相连。如果城市 `a` 与城市 `b` 直接相连，且城市 `b` 与城市 `c` 直接相连，那么城市 `a` 与城市 `c` **间接相连**。

**省份** 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 `n × n` 的邻接矩阵 `isConnected`：
- `isConnected[i][j] = 1` 表示城市 `i` 和城市 `j` 直接相连
- `isConnected[i][j] = 0` 表示二者不直接相连

返回矩阵中**省份的数量**。

### 示例
```
输入: isConnected = [[1,1,0],
                     [1,1,0],
                     [0,0,1]]
输出: 2
解释: 城市 0 和 1 相连，是一个省份；城市 2 自成一个省份。

输入: isConnected = [[1,0,0],
                     [0,1,0],
                     [0,0,1]]
输出: 3
解释: 三个城市两两不相连，各自一个省份。
```

---

## 先建立题感

把题目剥皮，本质就一句话：

> **给你一张无向图（用邻接矩阵表示），求"连通分量"的个数。**

- "省份" = 连通分量
- "直接相连" = 一条边
- "间接相连" = 同一个连通分量
- "省份数量" = 连通分量的个数

只要看出这一层翻译，剩下的就是用什么方法数连通分量的事。

数连通分量的三大经典方法：

| 方法 | 思路 | 数据结构 |
|---|---|---|
| DFS | 从一个点出发遍历整个连通块 | 递归 + visited |
| BFS | 同上，换队列 | 队列 + visited |
| **并查集** | 把每条边的两个端点合并；数最终的根 | 并查集 |

---

## 解法循序渐进

### 方法一：DFS（最直观）

#### 思路
1. 维护一个 `visited` 数组
2. 对每个城市 `i`：
   - 如果还没访问过，省份数 +1，然后从 `i` 出发 DFS 把整片连通块全部标成已访问
3. 最后返回省份数

**核心直觉：每开启一次 DFS = 发现一个新省份。**

DFS 内部就是普通的"遍历邻接矩阵"：

```python
def dfs(i):
    for j in range(n):
        if isConnected[i][j] == 1 and not visited[j]:
            visited[j] = True
            dfs(j)
```

#### 复杂度
- 时间：`O(n²)`（要扫整张邻接矩阵）
- 空间：`O(n)`（visited + 递归栈）

#### 代码文件
- `solution_1_dfs.py`

---

### 方法二：BFS（迭代版）

#### 思路
和方法一思路完全一样，把递归换成队列：

1. 遍历每个城市 `i`
2. 没访问过 → 省份 +1 → 从 `i` 启动 BFS：把队列里相连且未访问的城市都丢进队列，逐个 popleft
3. 最后返回省份数

#### 为什么也算最优
- 时间空间复杂度和 DFS 一样
- 没有递归栈深度风险，工程上更稳

#### 复杂度
- 时间：`O(n²)`
- 空间：`O(n)`

#### 代码文件
- `solution_2_bfs.py`

---

### 方法三：并查集（Union-Find，**最适合面试**）

这是本题最推荐的标准面试解法，并查集本身就是高频考点，下面详细讲。

#### 核心思路
**把每对相连的城市"合并"到同一组，最后数有多少组就是答案。**

并查集（Disjoint Set Union, DSU）就是为这种"动态合并 + 查询是否同组"的场景而生的数据结构。它支持两个操作：

| 操作 | 含义 | 复杂度 |
|---|---|---|
| `find(x)` | 找 x 所在集合的代表（"根"） | 近似 O(1) |
| `union(x, y)` | 合并 x 和 y 所在的两个集合 | 近似 O(1) |

#### 算法步骤
1. 初始化：每个城市自己是一个集合（`parent[i] = i`）
2. 遍历邻接矩阵的**上三角**（无向图，避免重复处理）
3. 对每条边 `(i, j)`：`union(i, j)`
4. 最后数有多少个 `i` 满足 `parent[i] == i`（即根节点的个数），就是省份数

#### 并查集的两大优化

并查集裸写是 `O(n)` 一次操作，加上**两个优化**后能近似 `O(1)`：

**优化 1：路径压缩（Path Compression）**

`find(x)` 时把路径上所有节点直接挂到根上，让下次查询变成一步：

```python
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])   # ← 关键这一行：递归找到根并把当前节点直接挂上去
    return parent[x]
```

**优化 2：按秩合并（Union by Rank / Size）**

合并两个集合时，把"小的"挂到"大的"下面，避免树变高：

```python
def union(x, y):
    rx, ry = find(x), find(y)
    if rx == ry:
        return
    if rank[rx] < rank[ry]:
        parent[rx] = ry
    elif rank[rx] > rank[ry]:
        parent[ry] = rx
    else:
        parent[ry] = rx
        rank[rx] += 1
```

两个优化都加上，单次操作摊销复杂度是 **`O(α(n))`**（反阿克曼函数，实际上 ≈ O(1)，n 再大也几乎是常数）。

#### 为什么 547 是并查集入门最经典的题

1. **题目就是"问连通分量数"**——并查集的本职工作
2. **`n ≤ 200`**，复杂度不卡，DFS / BFS / 并查集都过得了，所以**这题适合用来练手**
3. **能直接迁移**到：
   - [200 岛屿数量](../01_q200/)
   - [684 冗余连接](https://leetcode.com/problems/redundant-connection/)
   - [721 账户合并](https://leetcode.com/problems/accounts-merge/)
   - [990 等式方程](https://leetcode.com/problems/satisfiability-of-equality-equations/)
   - [1319 网络变得连通](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)
4. **面试官经常追问**"会并查集吗"——这题就是最自然的入口

#### 为什么它最适合面试

1. **展示你会"工业级"数据结构**：DFS/BFS 任何人都能写，会并查集说明你的算法工具箱更全
2. **逻辑非常清晰**：建集合 → 合并相连点 → 数根
3. **能自然扩展到动态问题**：如果题目变成"实时添加边，每次查询连通分量数"，DFS/BFS 每次都要重算，并查集只要 `union` 一次 + 维护计数即可
4. **小细节多，能展示功底**：路径压缩、按秩合并、计数优化都是加分项
5. **代码模板化**：背一次，一辈子用

#### 容易写错的地方（面试自检清单）

**1. 只遍历上三角，不要重复处理**

```python
for i in range(n):
    for j in range(i + 1, n):    # ✅ j 从 i+1 开始
        if isConnected[i][j] == 1:
            union(i, j)
```

无向图的邻接矩阵是对称的，扫一半就够了；扫全图不会出错但浪费一半时间。

**2. 对角线不用 union**

`isConnected[i][i] = 1` 是规定的（自己和自己"相连"），union 自己没意义，所以从 `j = i+1` 开始就自然跳过了。

**3. 路径压缩的写法**

最常见的两种正确写法：

```python
# 递归版（最简洁，背这个就够了）
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 迭代版（避免深图爆栈）
def find(x):
    root = x
    while parent[root] != root:
        root = parent[root]
    while parent[x] != root:
        parent[x], x = root, parent[x]
    return root
```

**常见错误写法**：
```python
def find(x):
    while parent[x] != x:
        x = parent[x]    # ❌ 只找到根但没压缩路径
    return x
```
这样能跑通但失去了优化效果，最坏情况下退化成 O(n)。

**4. 计数的两种方式**

```python
# 方式 A：最后数有多少个自己是自己的根
return sum(1 for i in range(n) if find(i) == i)

# 方式 B：union 时维护一个 count 变量（更高效）
count = n
def union(x, y):
    nonlocal count
    rx, ry = find(x), find(y)
    if rx == ry:
        return
    # ... 合并 ...
    count -= 1   # ✅ 每成功合并一次，集合数减 1
```

方式 B 更优雅，面试时建议用，能多展示一个细节。

#### 一个小例子

`isConnected = [[1,1,0,0], [1,1,1,0], [0,1,1,0], [0,0,0,1]]`

初始：`parent = [0, 1, 2, 3]`，省份数 `count = 4`

| 边 | union 操作 | parent 变化 | count |
|---|---|---|---|
| (0, 1) | union(0, 1) | `[1, 1, 2, 3]` | 3 |
| (1, 2) | union(1, 2) | `[1, 2, 2, 3]` | 2 |
| (0, 2) | find(0)=2, find(2)=2，已同组 | 不变 | 2 |
| (其他) | 都不连通 | 不变 | 2 |

返回 `count = 2` ✅

#### 复杂度
- 时间：`O(n² · α(n))` ≈ `O(n²)`
  - 邻接矩阵扫一半：`O(n²)`
  - 每次 union 摊销 `O(α(n)) ≈ O(1)`
- 空间：`O(n)`
  - `parent` + `rank`

#### 代码文件
- `solution_3_union_find.py`

---

## 三种方法怎么选

### 如果你只想最快 AC
DFS（方法一）最短，5 分钟写完。

### 如果你在准备面试
**首选讲法：方法三（并查集）**

原因：
1. 这是连通性问题的"教科书答案"，能展示数据结构功底
2. 547 是并查集最经典的入门题，错过这个机会就浪费了
3. 后续能直接复用模板写 200、684、721、990……
4. 面试官很可能就在等你说出"并查集"这三个字

**但如果时间不够，方法一（DFS）也是标准解答**，写得快、不易错，面试官不会扣分——只是会失去一个展示并查集的机会。

### 如果面试官继续追问
- "如果是动态加边呢？" → 并查集天然支持，DFS 每次都要重算
- "复杂度能不能更低？" → 并查集近似 O(n²)（α 是反阿克曼，几乎常数）
- "怎么扩展到加权并查集？" → 维护到根的距离，可以解 399 除法求值

---

## 并查集模板（背下来一辈子受用）

```python
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.count -= 1
        return True
```

这套模板涵盖：路径压缩 + 按秩合并 + 计数维护 + union 返回是否实际合并。**几乎所有并查集题都能用这个模板套**。

---

## 面试回答模板
你可以直接这样说：

```text
这道题翻译过来就是"求无向图连通分量的个数"。
有三种方法：DFS、BFS、并查集。

我会用并查集，因为这题就是并查集的经典入门场景：
- 每个城市先各自一个集合
- 遍历邻接矩阵上三角，每遇到一条边就把两端 union
- 维护一个 count，初始为 n，每次成功合并就 -1
- 最后 count 就是省份数

并查集要做两个优化：
1. find 用路径压缩，每次查询顺手把路径上的点直接挂到根
2. union 按秩合并，小树挂到大树下，避免树退化成链

加上这两个优化后单次操作摊销复杂度 O(α(n))，几乎是常数。
整体时间复杂度 O(n²)（扫邻接矩阵），空间 O(n)。

并查集的好处是：如果题目改成"动态加边，实时查询连通分量数"，
DFS 每次都要重新跑一遍 O(n²)，而并查集只要 O(α(n)) 处理一条边，
非常适合在线场景。
```

---

## 总结
- **最直观的写法**：DFS（方法一）
- **同样最优的迭代写法**：BFS（方法二）
- **最适合面试的写法**：并查集 + 路径压缩 + 按秩合并（**首选**）

三种方法时间复杂度都是 `O(n²)`，区别在于"展现的算法功底"和"是否能扩展到动态问题"。面试时优先讲并查集，背熟模板能横扫一大批题。
