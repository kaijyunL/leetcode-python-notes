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
        解法2：递归 + 哈希表 + 下标边界（面试推荐）
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        inorder_map = {value: index for index, value in enumerate(inorder)}

        def build(
            pre_left: int,
            pre_right: int,
            in_left: int,
            in_right: int,
        ) -> Optional[TreeNode]:
            if pre_left > pre_right:
                return None

            root_val = preorder[pre_left]
            root = TreeNode(root_val)
            root_index = inorder_map[root_val]
            left_size = root_index - in_left

            root.left = build(
                pre_left + 1,
                pre_left + left_size,
                in_left,
                root_index - 1,
            )
            root.right = build(
                pre_left + left_size + 1,
                pre_right,
                root_index + 1,
                in_right,
            )

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)


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
