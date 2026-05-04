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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        解法1：递归 DFS（面试推荐）
        时间复杂度：O(n)
        空间复杂度：O(h)
        """
        if root is None:
            return False

        if root.left is None and root.right is None:
            return root.val == targetSum

        remain = targetSum - root.val
        return self.hasPathSum(root.left, remain) or self.hasPathSum(root.right, remain)


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
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True),
        ([1, 2, 3], 5, False),
        ([1, 2], 1, False),
        ([1, 2], 3, True),
        ([], 0, False),
    ]

    solution = Solution()
    for values, target_sum, expected in test_cases:
        root = build_tree(values)
        output = solution.hasPathSum(root, target_sum)
        print(
            f"输入: root={values}, targetSum={target_sum}, "
            f"输出: {output}, 期望: {expected}"
        )
        assert output == expected

