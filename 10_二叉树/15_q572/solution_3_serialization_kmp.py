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
    def isSubtree(
        self,
        root: Optional[TreeNode],
        subRoot: Optional[TreeNode],
    ) -> bool:
        """
        方法三：前序序列化 + KMP
        时间复杂度：O(m + n)
        空间复杂度：O(m + n)
        """

        root_tokens = self.serialize(root)
        sub_root_tokens = self.serialize(subRoot)
        return self.kmp_search(root_tokens, sub_root_tokens)

    def serialize(self, node: Optional[TreeNode]) -> list[str]:
        if node is None:
            return ["#"]
        return [str(node.val)] + self.serialize(node.left) + self.serialize(node.right)

    def kmp_search(self, text: list[str], pattern: list[str]) -> bool:
        if not pattern:
            return True

        prefix = self.build_prefix(pattern)
        pattern_index = 0

        for token in text:
            while pattern_index > 0 and token != pattern[pattern_index]:
                pattern_index = prefix[pattern_index - 1]

            if token == pattern[pattern_index]:
                pattern_index += 1

            if pattern_index == len(pattern):
                return True

        return False

    def build_prefix(self, pattern: list[str]) -> list[int]:
        prefix = [0] * len(pattern)
        matched = 0

        for index in range(1, len(pattern)):
            while matched > 0 and pattern[index] != pattern[matched]:
                matched = prefix[matched - 1]

            if pattern[index] == pattern[matched]:
                matched += 1
                prefix[index] = matched

        return prefix


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
        ([3, 4, 5, 1, 2], [4, 1, 2], True),
        ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False),
        ([1, 1], [1], True),
        ([], [], True),
        ([1], [2], False),
    ]

    solution = Solution()
    for root_values, sub_root_values, expected in test_cases:
        root = build_tree(root_values)
        sub_root = build_tree(sub_root_values)
        output = solution.isSubtree(root, sub_root)
        print(
            f"输入: root={root_values}, subRoot={sub_root_values}, "
            f"输出: {output}, 期望: {expected}"
        )
        assert output == expected
