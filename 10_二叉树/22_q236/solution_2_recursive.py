from collections import deque
from typing import Dict, List, Optional


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
        self, root: Optional[TreeNode], p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:
        """
        解法2：后序递归找分叉点（面试推荐）
        时间复杂度：O(n)
        空间复杂度：O(h)
        """
        if root is None:
            return None
        if root is p or root is q:
            return root

        left_result = self.lowestCommonAncestor(root.left, p, q)
        right_result = self.lowestCommonAncestor(root.right, p, q)

        if left_result is not None and right_result is not None:
            return root
        if left_result is not None:
            return left_result
        return right_result


def build_tree(values: List[Optional[int]]):
    if not values or values[0] is None:
        return None, {}

    root = TreeNode(values[0])
    nodes: Dict[int, TreeNode] = {root.val: root}
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        node = queue.popleft()

        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            nodes[node.left.val] = node.left
            queue.append(node.left)
        index += 1

        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            nodes[node.right.val] = node.right
            queue.append(node.right)
        index += 1

    return root, nodes


if __name__ == "__main__":
    test_cases = [
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 6, 4, 5),
        ([1, 2, 3], 2, 3, 1),
    ]

    solution = Solution()
    for values, p_val, q_val, expected in test_cases:
        root, nodes = build_tree(values)
        ans = solution.lowestCommonAncestor(root, nodes[p_val], nodes[q_val])
        print(f"输入: p={p_val}, q={q_val}, 输出: {ans.val}, 期望: {expected}")
        assert ans.val == expected
