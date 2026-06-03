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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        解法1：层序遍历，逐层判断是否回文
        时间复杂度：O(n)
        空间复杂度：O(w)
        """
        if root is None:
            return True

        queue = deque([root])

        while queue:
            level = []
            has_next_level = False

            for _ in range(len(queue)):
                node = queue.popleft()

                if node is None:
                    level.append(None)
                    continue

                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

                if node.left or node.right:
                    has_next_level = True

            if level != level[::-1]:
                return False

            if not has_next_level:
                break

        return True


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
        ([1, 2, 2, 3, 4, 4, 3], True),
        ([1, 2, 2, None, 3, None, 3], False),
        ([1, 2, 2, 2, None, 2], False),
        ([1], True),
        ([], True),
    ]

    solution = Solution()
    for values, expected in test_cases:
        root = build_tree(values)
        output = solution.isSymmetric(root)
        print(f"输入: {values}, 输出: {output}, 期望: {expected}")
        assert output == expected

