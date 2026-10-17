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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        方法2：前缀和 + 哈希表（面试推荐）
        时间复杂度：O(n)
        空间复杂度：O(h)
        """
        prefix_count = {0: 1}

        def dfs(node: Optional[TreeNode], current_sum: int) -> int:
            if node is None:
                return 0

            current_sum += node.val
            count = prefix_count.get(current_sum - targetSum, 0)
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)

            # 回退当前节点，避免前缀和串到另一分支
            prefix_count[current_sum] -= 1
            if prefix_count[current_sum] == 0:
                del prefix_count[current_sum]
            return count

        return dfs(root, 0)


def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
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


if __name__ == "__main__":
    test_cases = [
        ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3),
        ([1, -1], 0, 1),
        ([1, 1, 1], 2, 2),
        ([0, 0], 0, 3),
        ([], 0, 0),
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
