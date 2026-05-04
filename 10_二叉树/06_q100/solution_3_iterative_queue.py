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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        解法3：迭代 BFS / 队列
        时间复杂度：O(n)
        空间复杂度：O(w)
        """
        queue = deque([(p, q)])

        while queue:
            node_p, node_q = queue.popleft()

            if node_p is None and node_q is None:
                continue

            if node_p is None or node_q is None:
                return False

            if node_p.val != node_q.val:
                return False

            queue.append((node_p.left, node_q.left))
            queue.append((node_p.right, node_q.right))

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
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
        ([], [], True),
        ([1], [], False),
    ]

    solution = Solution()
    for p_values, q_values, expected in test_cases:
        p = build_tree(p_values)
        q = build_tree(q_values)
        output = solution.isSameTree(p, q)
        print(f"输入: p={p_values}, q={q_values}, 输出: {output}, 期望: {expected}")
        assert output == expected

