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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        解法1：自顶向下递归计算高度
        时间复杂度：最坏 O(n^2)
        空间复杂度：O(h)
        """
        if root is None:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        current_diameter = left_height + right_height
        subtree_diameter = max(
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right),
        )

        return max(current_diameter, subtree_diameter)

    def height(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        return 1 + max(self.height(node.left), self.height(node.right))


def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    iter_values = iter(values)
    root_value = next(iter_values)
    if root_value is None:
        return None

    root = TreeNode(root_value)
    queue = deque([root])

    while queue:
        node = queue.popleft()

        try:
            left_value = next(iter_values)
            if left_value is not None:
                node.left = TreeNode(left_value)
                queue.append(node.left)

            right_value = next(iter_values)
            if right_value is not None:
                node.right = TreeNode(right_value)
                queue.append(node.right)
        except StopIteration:
            break

    return root


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 1),
        ([1], 0),
        ([], 0),
    ]

    solution = Solution()
    for values, expected in test_cases:
        root = build_tree(values)
        output = solution.diameterOfBinaryTree(root)
        print(f"输入: {values}, 输出: {output}, 期望: {expected}")
        assert output == expected
