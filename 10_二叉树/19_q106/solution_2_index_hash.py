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
        inorder: list[int],
        postorder: list[int],
    ) -> Optional[TreeNode]:
        """
        解法2：递归 + 哈希表 + 下标边界（面试推荐）
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        inorder_map = {value: index for index, value in enumerate(inorder)}

        def build(in_left, in_right, post_left, post_right):
            if post_left > post_right:
                return None

            root_val = postorder[post_right]
            root = TreeNode(root_val)
            root_inorder_index = inorder_map[root_val]
            left_size = root_inorder_index - in_left

            root.left = build(
                in_left,
                root_inorder_index - 1,
                post_left,
                post_left + left_size - 1,
            )
            root.right = build(
                root_inorder_index + 1,
                in_right,
                post_left + left_size,
                post_right - 1,
            )

            return root

        return build(0, len(inorder) - 1, 0, len(postorder) - 1)


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
        ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1]),
        ([2, 1], [2, 1], [1, 2]),
        ([1, 2], [2, 1], [1, None, 2]),
        ([2, 3, 1], [3, 2, 1], [1, 2, None, None, 3]),
    ]

    solution = Solution()
    for inorder, postorder, expected in test_cases:
        root = solution.buildTree(inorder, postorder)
        output = serialize_level_order(root)
        print(
            f"输入: inorder={inorder}, postorder={postorder}, "
            f"输出: {output}, 期望: {expected}"
        )
        assert output == expected
