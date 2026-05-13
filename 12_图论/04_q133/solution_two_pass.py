from typing import Optional, List


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if node is None:
            return None

        old_to_new = {}

        # 第一遍：BFS 把所有老节点对应的新节点都建出来
        queue = [node]
        old_to_new[node] = Node(node.val)
        visited = {node}
        while queue:
            cur = queue.pop(0)
            for nei in cur.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    old_to_new[nei] = Node(nei.val)
                    queue.append(nei)

        # 第二遍：再走一次，把新节点之间连起来
        for old, new in old_to_new.items():
            for nei in old.neighbors:
                new.neighbors.append(old_to_new[nei])

        return old_to_new[node]


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
