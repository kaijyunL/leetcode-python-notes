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
        解法3：递归传上下界
        时间复杂度：O(n)
        空间复杂度：O(h)
        """

        def dfs(
            node: Optional[TreeNode],
            lower: Optional[int],
            upper: Optional[int],
        ) -> bool:
            if not node:
                return True

            if lower is not None and node.val <= lower:
                return False
            if upper is not None and node.val >= upper:
                return False

            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

        return dfs(root, None, None)


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
