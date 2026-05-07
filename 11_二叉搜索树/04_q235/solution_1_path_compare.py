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
    def lowestCommonAncestor(
        self,
        root: Optional[TreeNode],
        p: TreeNode,
        q: TreeNode,
    ) -> TreeNode:
        """
        解法1：记录两条路径后比较
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        path_p: list[TreeNode] = []
        path_q: list[TreeNode] = []

        def find_path(
            node: Optional[TreeNode],
            target: TreeNode,
            path: list[TreeNode],
        ) -> bool:
            if not node:
                return False

            path.append(node)

            if node == target:
                return True

            if find_path(node.left, target, path) or find_path(node.right, target, path):
                return True

            path.pop()
            return False

        find_path(root, p, path_p)
        find_path(root, q, path_q)

        ancestor = root
        for node_p, node_q in zip(path_p, path_q):
            if node_p != node_q:
                break
            ancestor = node_p

        return ancestor


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


def find_node(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    if not root:
        return None

    if root.val == target:
        return root

    left = find_node(root.left, target)
    if left:
        return left

    return find_node(root.right, target)


if __name__ == "__main__":
    test_cases = [
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
        ([2, 1], 2, 1, 2),
        ([5, 3, 6, 2, 4, None, None, 1], 1, 4, 3),
    ]

    solution = Solution()
    for values, p_val, q_val, expected in test_cases:
        root = build_tree(values)
        p = find_node(root, p_val)
        q = find_node(root, q_val)
        actual = solution.lowestCommonAncestor(root, p, q)
        print(
            f"输入: values={values}, p={p_val}, q={q_val}, "
            f"输出: {actual.val}, 期望: {expected}"
        )
        assert actual.val == expected
