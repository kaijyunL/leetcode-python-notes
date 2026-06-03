# 方法二：DFS + 哈希表（最适合面试）
from typing import Optional, List


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if node is None:
            return None

        visited = {}

        def dfs(old):
            if old in visited:
                return visited[old]

            # 先登记，再递归，避免环导致死循环
            new = Node(old.val)
            visited[old] = new
            for nei in old.neighbors:
                new.neighbors.append(dfs(nei))
            return new

        return dfs(node)


def build_graph(adj_list: List[List[int]]) -> Optional[Node]:
    if not adj_list:
        return None
    nodes = [Node(i + 1) for i in range(len(adj_list))]
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]
    return nodes[0]


def to_adj_list(node: Optional[Node]) -> List[List[int]]:
    if node is None:
        return []
    seen = {}
    order = []
    stack = [node]
    while stack:
        cur = stack.pop()
        if cur.val in seen:
            continue
        seen[cur.val] = cur
        order.append(cur)
        for nei in cur.neighbors:
            if nei.val not in seen:
                stack.append(nei)
    order.sort(key=lambda n: n.val)
    return [[nei.val for nei in n.neighbors] for n in order]


def run_demo() -> None:
    adj = [[2, 4], [1, 3], [2, 4], [1, 3]]
    original = build_graph(adj)
    cloned = Solution().cloneGraph(original)
    print("原图邻接表:", to_adj_list(original))
    print("克隆图邻接表:", to_adj_list(cloned))
    print("根节点是否为同一对象:", cloned is original)


if __name__ == "__main__":
    run_demo()
