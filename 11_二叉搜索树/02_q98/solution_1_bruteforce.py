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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        解法1：暴力递归检查子树最值
        时间复杂度：最坏 O(n^2)
        空间复杂度：O(h)
        """

        def get_min(node: Optional[TreeNode]) -> float:
            if not node:
                return float("inf")
            return min(node.val, get_min(node.left), get_min(node.right))

        def get_max(node: Optional[TreeNode]) -> float:
            if not node:
                return float("-inf")
            return max(node.val, get_max(node.left), get_max(node.right))

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return True

            if get_max(node.left) >= node.val:
                return False
            if get_min(node.right) <= node.val:
                return False

            return dfs(node.left) and dfs(node.right)

        return dfs(root)


def build_tree(level_order: list[Optional[int]]) -> Optional[TreeNode]:
    if not level_order:
        return None

    values = iter(level_order)
    root_val = next(values)
    if root_val is None:
        return None

    root = TreeNode(root_val)
    queue = deque([root])

    while queue:
        node = queue.popleft()

        try:
            left_val = next(values)
        except StopIteration:
            break

        if left_val is not None:
            node.left = TreeNode(left_val)
            queue.append(node.left)

        try:
            right_val = next(values)
        except StopIteration:
            break

        if right_val is not None:
            node.right = TreeNode(right_val)
            queue.append(node.right)

    return root


if __name__ == "__main__":
    test_cases = [
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([2, 2, 2], False),
        ([10, 5, 15, None, None, 6, 20], False),
        ([8, 4, 10, 2, 6, 9, 12], True),
    ]

    solution = Solution()
    for values, expected in test_cases:
        root = build_tree(values)
        actual = solution.isValidBST(root)
        print(f"输入: {values}, 输出: {actual}, 期望: {expected}")
        assert actual == expected
