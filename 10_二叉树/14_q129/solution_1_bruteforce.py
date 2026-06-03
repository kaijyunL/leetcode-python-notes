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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        解法1：朴素暴力，先收集所有根到叶路径
        时间复杂度：O(n * h)
        空间复杂度：O(n * h)
        """
        all_paths = []

        def dfs(node: Optional[TreeNode], path: list[int]) -> None:
            if node is None:
                return

            new_path = path + [node.val]
            if node.left is None and node.right is None:
                all_paths.append(new_path)
                return

            dfs(node.left, new_path)
            dfs(node.right, new_path)

        dfs(root, [])

        total = 0
        for path in all_paths:
            number = 0
            for digit in path:
                number = number * 10 + digit
            total += number

        return total


def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    iter_values = iter(values)
    root_val = next(iter_values)
    if root_val is None:
        return None

    root = TreeNode(root_val)
    queue = deque([root])

    while queue:
        node = queue.popleft()

        try:
            left_val = next(iter_values)
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)

            right_val = next(iter_values)
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
        except StopIteration:
            break

    return root


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], 25),
        ([4, 9, 0, 5, 1], 1026),
        ([0, 1], 1),
        ([1], 1),
        ([], 0),
    ]

    solution = Solution()
    for values, expected in test_cases:
        root = build_tree(values)
        output = solution.sumNumbers(root)
        print(f"输入: {values}, 输出: {output}, 期望: {expected}")
        assert output == expected

