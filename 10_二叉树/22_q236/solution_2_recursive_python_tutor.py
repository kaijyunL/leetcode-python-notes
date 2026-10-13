from typing import Optional


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
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


root = TreeNode(
    3,
    TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
    TreeNode(1, TreeNode(0), TreeNode(8)),
)
p = root.left.left
q = root.left.right.right

ans = Solution().lowestCommonAncestor(root, p, q)
print(ans.val)
