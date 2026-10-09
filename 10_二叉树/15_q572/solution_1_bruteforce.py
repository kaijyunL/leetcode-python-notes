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
    def isSubtree(
        self,
        root: Optional[TreeNode],
        subRoot: Optional[TreeNode],
    ) -> bool:
        """
        方法一：遍历候选节点 + 暴力比较
        时间复杂度：O(mn)
        空间复杂度：O(h)
        """

        def is_same_tree(
            first: Optional[TreeNode],
            second: Optional[TreeNode],
        ) -> bool:
            if first is None and second is None:
                return True
            if first is None or second is None:
                return False
            return (
                first.val == second.val
                and is_same_tree(first.left, second.left)
                and is_same_tree(first.right, second.right)
            )

        def visit(node: Optional[TreeNode]) -> bool:
            if node is None:
                return False
            if is_same_tree(node, subRoot):
                return True
            return visit(node.left) or visit(node.right)

        if subRoot is None:
            return True
        if root is None:
            return False
        return visit(root)


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
        ([3, 4, 5, 1, 2], [4, 1, 2], True),
        ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False),
        ([1, 1], [1], True),
        ([], [], True),
        ([1], [2], False),
    ]

    solution = Solution()
    for root_values, sub_root_values, expected in test_cases:
        root = build_tree(root_values)
        sub_root = build_tree(sub_root_values)
        output = solution.isSubtree(root, sub_root)
        print(
            f"输入: root={root_values}, subRoot={sub_root_values}, "
            f"输出: {output}, 期望: {expected}"
        )
        assert output == expected
