from collections import defaultdict, deque
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        解法1：把树看成无向图，暴力枚举所有路径
        时间复杂度：O(n^2)
        空间复杂度：O(n)
        """
        graph = defaultdict(list)
        nodes = []

        def build_graph(node):
            if not node:
                return

            nodes.append(node)

            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                build_graph(node.left)

            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                build_graph(node.right)

        build_graph(root)

        ans = float("-inf")

        def dfs(node, parent, current_sum):
            nonlocal ans

            current_sum += node.val
            ans = max(ans, current_sum)

            for nxt in graph[node]:
                if nxt != parent:
                    dfs(nxt, node, current_sum)

        for start in nodes:
            dfs(start, None, 0)

        return ans


def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        node = queue.popleft()

        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1

        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1

    return root


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], 6),
        ([-10, 9, 20, None, None, 15, 7], 42),
        ([-3], -3),
        ([2, -1], 2),
        ([-2, -1], -1),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 48),
    ]

    solution = Solution()
    for values, expected in test_cases:
        root = build_tree(values)
        output = solution.maxPathSum(root)
        print(f"输入: {values}, 输出: {output}, 期望: {expected}")
        assert output == expected
