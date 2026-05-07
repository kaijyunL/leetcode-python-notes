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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        解法3：递归中序 + 计数提前返回
        时间复杂度：最坏 O(n)
        空间复杂度：O(h)
        """
        count = 0
        answer: Optional[int] = None

        def inorder(node: Optional[TreeNode]) -> None:
            nonlocal count, answer

            if not node or answer is not None:
                return

            inorder(node.left)

            if answer is not None:
                return

            count += 1
            if count == k:
                answer = node.val
                return

            inorder(node.right)

        inorder(root)

        if answer is None:
            raise ValueError("k 超出节点数量")

        return answer


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
        ([3, 1, 4, None, 2], 1, 1),
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
        ([2, 1, 3], 2, 2),
        ([6, 3, 8, 2, 4, 7, 9, 1], 5, 6),
    ]

    solution = Solution()
    for values, k, expected in test_cases:
        root = build_tree(values)
        actual = solution.kthSmallest(root, k)
        print(f"输入: values={values}, k={k}, 输出: {actual}, 期望: {expected}")
        assert actual == expected
