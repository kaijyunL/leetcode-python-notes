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
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        """
        解法2：显式栈 + 访问标记（面试推荐）
        时间复杂度：O(n)
        空间复杂度：O(h)，不计返回结果
        """
        if root is None:
            return []

        ans = []
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if visited:
                ans.append(node.val)
                continue

            stack.append((node, True))
            if node.right is not None:
                stack.append((node.right, False))
            if node.left is not None:
                stack.append((node.left, False))

        return ans


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
        ([1, None, 2, 3], [3, 2, 1]),
        ([1, 2, 3, 4, 5, None, 6], [4, 5, 2, 6, 3, 1]),
        ([1], [1]),
        ([], []),
    ]

    solution = Solution()
    for values, expected in test_cases:
        root = build_tree(values)
        output = solution.postorderTraversal(root)
        print(f"输入: {values}, 输出: {output}, 期望: {expected}")
        assert output == expected

