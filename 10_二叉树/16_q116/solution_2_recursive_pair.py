from collections import deque
from typing import Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
        next: Optional["Node"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        """
        解法2：递归连接相邻节点
        时间复杂度：O(n)
        空间复杂度：O(h)
        """
        if root is None:
            return None

        def connect_two(node1: Optional[Node], node2: Optional[Node]) -> None:
            if node1 is None or node2 is None:
                return

            node1.next = node2

            connect_two(node1.left, node1.right)
            connect_two(node2.left, node2.right)
            connect_two(node1.right, node2.left)

        connect_two(root.left, root.right)
        return root


def build_tree(values: list[Optional[int]]) -> Optional[Node]:
    if not values:
        return None

    iter_values = iter(values)
    root_val = next(iter_values)
    if root_val is None:
        return None

    root = Node(root_val)
    queue = deque([root])

    while queue:
        node = queue.popleft()

        try:
            left_val = next(iter_values)
            if left_val is not None:
                node.left = Node(left_val)
                queue.append(node.left)

            right_val = next(iter_values)
            if right_val is not None:
                node.right = Node(right_val)
                queue.append(node.right)
        except StopIteration:
            break

    return root


def serialize_by_next(root: Optional[Node]) -> list[int | str]:
    ans = []
    leftmost = root

    while leftmost:
        node = leftmost
        next_leftmost = None

        while node:
            ans.append(node.val)
            if next_leftmost is None:
                next_leftmost = node.left or node.right
            node = node.next

        ans.append("#")
        leftmost = next_leftmost

    return ans


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7], [1, "#", 2, 3, "#", 4, 5, 6, 7, "#"]),
        ([1], [1, "#"]),
        ([], []),
    ]

    solution = Solution()
    for values, expected in test_cases:
        root = build_tree(values)
        connected = solution.connect(root)
        output = serialize_by_next(connected)
        print(f"输入: {values}, 输出: {output}, 期望: {expected}")
        assert output == expected
