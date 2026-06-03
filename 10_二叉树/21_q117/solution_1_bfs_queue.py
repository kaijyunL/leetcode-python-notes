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
        解法1：BFS 队列
        时间复杂度：O(n)
        空间复杂度：O(w)
        """
        if root is None:
            return None

        queue = deque([root])

        while queue:
            prev = None
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()

                if prev:
                    prev.next = node
                prev = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

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
    level_start = root

    while level_start:
        node = level_start
        next_level_start = None

        while node:
            ans.append(node.val)
            if next_level_start is None:
                next_level_start = node.left or node.right
            node = node.next

        ans.append("#")
        level_start = next_level_start

    return ans


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5, None, 7], [1, "#", 2, 3, "#", 4, 5, 7, "#"]),
        ([1, None, 2, 3], [1, "#", 2, "#", 3, "#"]),
        ([1, 2, 3, 4, None, None, 5], [1, "#", 2, 3, "#", 4, 5, "#"]),
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
