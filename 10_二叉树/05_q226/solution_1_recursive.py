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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        解法1：递归 DFS（面试推荐）
        时间复杂度：O(n)
        空间复杂度：O(h)
        """
        if root is None:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


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


def tree_to_list(root: Optional[TreeNode]) -> list[Optional[int]]:
    if root is None:
        return []

    values = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
            continue

        values.append(node.val)
        queue.append(node.left)
        queue.append(node.right)

    while values and values[-1] is None:
        values.pop()

    return values


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),
    ]

    for values, expected in test_cases:
        root = build_tree(values)
        output = tree_to_list(solution.invertTree(root))
        print(f"输入: {values}, 输出: {output}, 期望: {expected}")
        assert output == expected
