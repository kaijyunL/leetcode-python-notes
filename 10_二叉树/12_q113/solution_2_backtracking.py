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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        """
        解法2：DFS 回溯（面试推荐）
        时间复杂度：O(n * h)
        空间复杂度：O(h)，不计返回结果
        """
        ans = []
        path = []

        def dfs(node: Optional[TreeNode], remain: int) -> None:
            if node is None:
                return

            path.append(node.val)

            if node.left is None and node.right is None:
                if node.val == remain:
                    ans.append(path[:])
            else:
                next_remain = remain - node.val
                dfs(node.left, next_remain)
                dfs(node.right, next_remain)

            path.pop()

        dfs(root, targetSum)
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
        (
            [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1],
            22,
            [[5, 4, 11, 2], [5, 8, 4, 5]],
        ),
        ([1, 2, 3], 5, []),
        ([1, 2], 3, [[1, 2]]),
        ([], 0, []),
    ]

    solution = Solution()
    for values, target_sum, expected in test_cases:
        root = build_tree(values)
        output = solution.pathSum(root, target_sum)
        print(
            f"输入: root={values}, targetSum={target_sum}, "
            f"输出: {output}, 期望: {expected}"
        )
        assert output == expected
