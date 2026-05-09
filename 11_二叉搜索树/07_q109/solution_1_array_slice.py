from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        解法一：链表转数组 + 递归切片
        时间复杂度：O(n log n)
        空间复杂度：O(n)
        """
        nums: list[int] = []

        while head:
            nums.append(head.val)
            head = head.next

        def build(values: list[int]) -> Optional[TreeNode]:
            if not values:
                return None

            mid = len(values) // 2
            root = TreeNode(values[mid])
            root.left = build(values[:mid])
            root.right = build(values[mid + 1 :])
            return root

        return build(nums)


def build_linked_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


def inorder_values(root: Optional[TreeNode]) -> list[int]:
    values: list[int] = []

    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return
        dfs(node.left)
        values.append(node.val)
        dfs(node.right)

    dfs(root)
    return values


def is_balanced(root: Optional[TreeNode]) -> bool:
    def height(node: Optional[TreeNode]) -> int:
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

    result: list[Optional[int]] = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
            continue

        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)

    while result and result[-1] is None:
        result.pop()

    return result


if __name__ == "__main__":
    test_cases = [
        [-10, -3, 0, 5, 9],
        [1],
        [],
        [1, 2],
        [1, 2, 3, 4, 5, 6],
    ]

    solution = Solution()
    for values in test_cases:
        head = build_linked_list(values)
        root = solution.sortedListToBST(head)
        level_order = serialize_level_order(root)
        print(f"输入链表: {values}, 输出层序: {level_order}")
        assert inorder_values(root) == values
        assert is_balanced(root)
