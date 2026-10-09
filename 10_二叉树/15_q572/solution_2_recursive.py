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
        方法二：递归 DFS（面试推荐）
        时间复杂度：O(mn)
        空间复杂度：O(h + k)
        """

        if subRoot is None:
            return True
        if root is None:
            return False

        if self.is_same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_same_tree(self, first, second):
        if first is None and second is None:
            return True
        if first is None or second is None:
            return False
        if first.val != second.val:
            return False

        return self.is_same_tree(first.left, second.left) and self.is_same_tree(first.right, second.right)


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
