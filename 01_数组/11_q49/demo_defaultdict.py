from collections import defaultdict

def demo_defaultdict():
    # 1. 列表默认值 (用于分组)
    groups = defaultdict(list)
    groups["fruit"].append("apple")
    print(f"分组示例: {dict(groups)}") # {'fruit': ['apple']}

    # 2. 整数默认值 (用于计数)
    counts = defaultdict(int)
    counts["score"] += 1
    print(f"计数示例: {dict(counts)}") # {'score': 1}

    # 3. 原理解析：为什么传 list?
    # 因为 list 是一个函数，调用它会产生空列表
    factory_output = list()
    print(f"调用 list() 的结果: {factory_output}")

if __name__ == "__main__":
    demo_defaultdict()
