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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        解法1：中序遍历收集 + 排序后重写
        时间复杂度：O(n log n)
        空间复杂度：O(n)
        """
        values: list[int] = []

        def collect(node: Optional[TreeNode]) -> None:
            if not node:
                return
            collect(node.left)
            values.append(node.val)
            collect(node.right)

        def rewrite(node: Optional[TreeNode], index: list[int]) -> None:
            if not node:
                return
            rewrite(node.left, index)
            node.val = values[index[0]]
            index[0] += 1
            rewrite(node.right, index)

        collect(root)
        values.sort()
        rewrite(root, [0])


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


def inorder_values(root: Optional[TreeNode]) -> list[int]:
    values: list[int] = []

    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return
        dfs(node.left)
        values.append(node.val)
        dfs(node.right)

    dfs(root)
    return values


if __name__ == "__main__":
    test_cases = [
        ([1, 3, None, None, 2], [1, 2, 3]),
        ([3, 1, 4, None, None, 2], [1, 2, 3, 4]),
    ]

    solution = Solution()
    for values, expected_inorder in test_cases:
        root = build_tree(values)
        solution.recoverTree(root)
        actual = inorder_values(root)
        print(f"输入: {values}, 输出: {actual}, 期望: {expected_inorder}")
        assert actual == expected_inorder
