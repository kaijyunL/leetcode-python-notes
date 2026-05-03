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
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        """
        解法3：Morris 前序遍历
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        ans = []
        cur = root

        while cur is not None:
            if cur.left is None:
                ans.append(cur.val)
                cur = cur.right
                continue

            pred = cur.left
            while pred.right is not None and pred.right is not cur:
                pred = pred.right

            if pred.right is None:
                ans.append(cur.val)
                pred.right = cur
                cur = cur.left
            else:
                pred.right = None
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
        [1, None, 2, 3],
        [1, 2, 3, 4, 5, None, 6],
        [],
    ]

    solution = Solution()
    for values in test_cases:
        root = build_tree(values)
        print(f"输入: {values}, 输出: {solution.preorderTraversal(root)}")
