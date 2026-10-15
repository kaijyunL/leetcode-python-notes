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


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        方法1：BFS 层序遍历 + 空节点标记（面试推荐）
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        tokens = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node is None:
                tokens.append("#")
                continue

            tokens.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        return ",".join(tokens)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        tokens = deque(data.split(","))
        root_value = tokens.popleft()
        if root_value == "#":
            return None

        root = TreeNode(int(root_value))
        queue = deque([root])

        while queue:
            node = queue.popleft()
            left_value = tokens.popleft()
            right_value = tokens.popleft()

            if left_value != "#":
                node.left = TreeNode(int(left_value))
                queue.append(node.left)

            if right_value != "#":
                node.right = TreeNode(int(right_value))
                queue.append(node.right)

        return root


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
        ([1, 2, 3, None, None, 4, 5], "1,2,3,#,#,4,5,#,#,#,#"),
        ([1, 2], "1,2,#,#,#"),
        ([1], "1,#,#"),
        ([], "#"),
    ]

    codec = Codec()
    for values, expected in test_cases:
        root = build_tree(values)
        data = codec.serialize(root)
        restored = codec.deserialize(data)
        round_trip_data = codec.serialize(restored)

        print(f"输入: {values}, 编码: {data}, 期望: {expected}")
        assert data == expected
        assert round_trip_data == data
