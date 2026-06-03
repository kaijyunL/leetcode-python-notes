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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        解法2：递归原地展开
        时间复杂度：最坏 O(n^2)
        空间复杂度：O(h)
        """
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        if not root.left:
            return

        right = root.right
        root.right = root.left
        root.left = None

        tail = root.right
        while tail.right:
            tail = tail.right
        tail.right = right


def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    if not values:
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


def serialize_right_chain(root: Optional[TreeNode]) -> list[int]:
    ans = []
    cur = root

    while cur:
        ans.append(cur.val)
        cur = cur.right

    return ans


def all_left_none(root: Optional[TreeNode]) -> bool:
    cur = root

    while cur:
        if cur.left:
            return False
        cur = cur.right

    return True


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 5, 3, 4, None, 6], [1, 2, 3, 4, 5, 6]),
        ([], []),
        ([0], [0]),
        ([1, 2, None, 3], [1, 2, 3]),
        ([1, None, 2, None, 3], [1, 2, 3]),
    ]

    solution = Solution()
    for values, expected in test_cases:
        root = build_tree(values)
        solution.flatten(root)
        output = serialize_right_chain(root)
        print(f"输入: {values}, 输出右链: {output}, 期望: {expected}")
        assert output == expected
        assert all_left_none(root)
