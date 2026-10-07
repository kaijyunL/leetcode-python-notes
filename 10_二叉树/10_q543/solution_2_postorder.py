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
        解法2：后序 DFS + 全局最大值（面试推荐）
        时间复杂度：O(n)
        空间复杂度：O(h)
        """
        ans = 0

        def height(node):
            nonlocal ans

            if node is None:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            ans = max(ans, left_height + right_height)

            return 1 + max(left_height, right_height)

        height(root)
        return ans


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
