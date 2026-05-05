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
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        """
        解法2：递归 + 下标边界（面试推荐）
        时间复杂度：O(n)
        空间复杂度：O(log n)
        """
        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums) - 1)


def inorder_values(root: Optional[TreeNode]) -> list[int]:
    ans = []

    def dfs(node):
        if not node:
            return

        dfs(node.left)
        ans.append(node.val)
        dfs(node.right)

    dfs(root)
    return ans


def is_balanced(root: Optional[TreeNode]) -> bool:
    def height(node):
        if not node:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)

        if left_height == -1 or right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    return height(root) != -1


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
        [-10, -3, 0, 5, 9],
        [1],
        [],
        [1, 2],
        [1, 2, 3, 4, 5, 6],
    ]

    solution = Solution()
    for nums in test_cases:
        root = solution.sortedArrayToBST(nums)
        output = serialize_level_order(root)
        print(f"输入: nums={nums}, 输出层序: {output}")
        assert inorder_values(root) == nums
        assert is_balanced(root)
