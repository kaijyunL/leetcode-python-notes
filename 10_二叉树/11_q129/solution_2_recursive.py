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
        解法2：DFS 递归累积数字（面试推荐）
        时间复杂度：O(n)
        空间复杂度：O(h)
        """

        def dfs(node: Optional[TreeNode], current: int) -> int:
            if node is None:
                return 0

            current = current * 10 + node.val

            if node.left is None and node.right is None:
                return current

            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)


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

