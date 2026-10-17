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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        方法1：从每个节点向下统计
        时间复杂度：O(nh)，最坏 O(n^2)
        空间复杂度：O(h)
        """
        def count_from(node: Optional[TreeNode], remain: int) -> int:
            if node is None:
                return 0

            count = int(node.val == remain)
            remain -= node.val
            count += count_from(node.left, remain)
            count += count_from(node.right, remain)
            return count

        def visit_starts(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            count = count_from(node, targetSum)
            count += visit_starts(node.left)
            count += visit_starts(node.right)
            return count

        return visit_starts(root)


def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        node = queue.popleft()

        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1

        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1

    return root


if __name__ == "__main__":
    test_cases = [
        ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3),
        ([1, -1], 0, 1),
        ([1, 1, 1], 2, 2),
        ([0, 0], 0, 3),
        ([], 0, 0),
    ]

    solution = Solution()
    for values, target_sum, expected in test_cases:
        root = build_tree(values)
        output = solution.pathSum(root, target_sum)
        print(
            f"输入: root={values}, targetSum={target_sum}, "
            f"输出: {output}, 期望: {expected}"
        )
        assert output == expected
