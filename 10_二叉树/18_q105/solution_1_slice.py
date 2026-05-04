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
    def buildTree(
        self,
        preorder: list[int],
        inorder: list[int],
    ) -> Optional[TreeNode]:
        """
        解法1：递归 + 数组切片
        时间复杂度：最坏 O(n^2)
        空间复杂度：最坏 O(n^2)
        """
        if not preorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)

        left_size = root_index

        root.left = self.buildTree(
            preorder[1 : 1 + left_size],
            inorder[:root_index],
        )
        root.right = self.buildTree(
            preorder[1 + left_size :],
            inorder[root_index + 1 :],
        )

        return root


def serialize_level_order(root: Optional[TreeNode]) -> list[Optional[int]]:
    if not root:
        return []

    ans = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            ans.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            ans.append(None)

    while ans and ans[-1] is None:
        ans.pop()

    return ans


if __name__ == "__main__":
    test_cases = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1]),
        ([1, 2], [2, 1], [1, 2]),
        ([1, 2, 3], [2, 3, 1], [1, 2, None, None, 3]),
    ]

    solution = Solution()
    for preorder, inorder, expected in test_cases:
        root = solution.buildTree(preorder, inorder)
        output = serialize_level_order(root)
        print(
            f"输入: preorder={preorder}, inorder={inorder}, "
            f"输出: {output}, 期望: {expected}"
        )
        assert output == expected
