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
        解法3：迭代队列
        时间复杂度：O(n)
        空间复杂度：O(w)
        """
        if root is None:
            return True

        queue = deque([(root.left, root.right)])

        while queue:
            left, right = queue.popleft()

            if left is None and right is None:
                continue

            if left is None or right is None:
                return False

            if left.val != right.val:
                return False

            queue.append((left.left, right.right))
            queue.append((left.right, right.left))

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

