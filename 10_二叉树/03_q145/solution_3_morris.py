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
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        """
        解法3：Morris 后序遍历
        时间复杂度：O(n)
        空间复杂度：O(1)，不计返回结果
        """
        ans = []
        dummy = TreeNode(0, left=root)
        cur = dummy

        def reverse_path(start: TreeNode, end: TreeNode) -> None:
            if start is end:
                return

            prev = None
            node = start
            stop = end.right

            while node is not stop:
                next_node = node.right
                node.right = prev
                prev = node
                node = next_node

        def collect_reverse(start: TreeNode, end: TreeNode) -> None:
            reverse_path(start, end)

            node = end
            while True:
                ans.append(node.val)
                if node is start:
                    break
                node = node.right

            reverse_path(end, start)

        while cur is not None:
            if cur.left is None:
                cur = cur.right
                continue

            pred = cur.left
            while pred.right is not None and pred.right is not cur:
                pred = pred.right

            if pred.right is None:
                pred.right = cur
                cur = cur.left
            else:
                pred.right = None
                collect_reverse(cur.left, pred)
                cur = cur.right

        return ans


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
        ([1, None, 2, 3], [3, 2, 1]),
        ([1, 2, 3, 4, 5, None, 6], [4, 5, 2, 6, 3, 1]),
        ([1], [1]),
        ([], []),
    ]

    solution = Solution()
    for values, expected in test_cases:
        root = build_tree(values)
        output = solution.postorderTraversal(root)
        print(f"输入: {values}, 输出: {output}, 期望: {expected}")
        assert output == expected

