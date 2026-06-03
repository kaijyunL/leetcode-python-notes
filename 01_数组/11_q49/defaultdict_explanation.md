# 理解 Python defaultdict(list)

在 LeetCode 49 题的代码中，我们使用了 `collections.defaultdict(list)`。很多同学会好奇：**为什么要传 `list` 进去？**

## 1. 什么是 `default_factory`？
`defaultdict` 的第一个参数被称为 **`default_factory`（默认值工厂）**。
*   它必须是一个**可调用对象（Callable）**，比如函数或类名。
*   当你访问一个字典中**不存在**的键（Key）时，`defaultdict` 会自动调用这个函数，用它的返回值作为该键的初始值。

## 2. 为什么传 `list`？
在 Python 中，`list` 不仅仅是一个类型名称，它还是一个**构造函数**。
*   当你直接调用 `list()` 时，它会返回一个**空的列表 `[]`**。

所以，`defaultdict(list)` 的含义是：
> “如果我访问的 Key 不存在，请自动帮我生成一个**空列表 `[]`** 存进去。”

---

## 3. 对比：普通字典 vs defaultdict

### 场景：我们要把单词存入对应的组
假设我们要处理单词 `eat`，它的 key 是 `aet`。

#### 使用普通字典 `dict`：
你必须手动检查 Key 是否存在，否则会报 `KeyError`。
```python
d = {}
key = "aet"
if key not in d:
    d[key] = []  # 手动初始化
d[key].append("eat")
```

#### 使用 `defaultdict(list)`：
逻辑极其简洁，不需要判断。
```python
from collections import defaultdict
d = defaultdict(list)
key = "aet"
d[key].append("eat") # 如果 "aet" 不存在，它会自动执行 d["aet"] = list()，然后再 append
```

---

## 4. 常见的其它用法
除了 `list`，你还可以传入其它的工厂函数：
*   `defaultdict(int)`：找不到 Key 时返回 `0`（常用于计数）。
*   `defaultdict(set)`：找不到 Key 时返回空集合 `set()`（用于去重分组）。
*   `defaultdict(lambda: "None")`：自定义默认返回字符串 `"None"`。

## 总结
在 49 题中，我们要将属于同一组的多个单词收集起来。**`list` 作为入参，就是告诉字典：每个新组的初始状态都应该是一个可以装东西的“空篮子（列表）”。**
