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


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.values: list[int] = []
        self.index = 0

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inorder(node.left)
            self.values.append(node.val)
            inorder(node.right)

        inorder(root)

    def next(self) -> int:
        val = self.values[self.index]
        self.index += 1
        return val

    def hasNext(self) -> bool:
        return self.index < len(self.values)


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
        ([7, 3, 15, None, None, 9, 20], [3, 7, 9, 15, 20]),
        ([2, 1, 3], [1, 2, 3]),
    ]

    for values, expected in test_cases:
        root = build_tree(values)
        iterator = BSTIterator(root)
        actual = []
        while iterator.hasNext():
            actual.append(iterator.next())
        print(f"输入: {values}, 输出: {actual}, 期望: {expected}")
        assert actual == expected
