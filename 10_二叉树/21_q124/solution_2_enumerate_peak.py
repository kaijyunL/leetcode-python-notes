from collections import deque
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
        解法2：枚举每个节点作为路径最高点
        时间复杂度：最坏 O(n^2)
        空间复杂度：O(h)
        """
        nodes = []

        def collect(node):
            if not node:
                return

            nodes.append(node)
            collect(node.left)
            collect(node.right)

        def max_down(node):
            if not node:
                return 0

            left_gain = max(max_down(node.left), 0)
            right_gain = max(max_down(node.right), 0)
            return node.val + max(left_gain, right_gain)

        collect(root)

        ans = float("-inf")
        for node in nodes:
            left_gain = max(max_down(node.left), 0)
            right_gain = max(max_down(node.right), 0)
            ans = max(ans, node.val + left_gain + right_gain)

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
