from typing import Optional


class Node:
    def __init__(
        self,
        x: int,
        next: Optional["Node"] = None,
        random: Optional["Node"] = None,
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None

        mapping: dict[Node, Node] = {}
        cur = head
        while cur:
            mapping[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            copy = mapping[cur]
            copy.next = mapping.get(cur.next)
            copy.random = mapping.get(cur.random)
            cur = cur.next

        return mapping[head]


def build_random_list(
    values_and_random: list[tuple[int, Optional[int]]],
) -> Optional[Node]:
    if not values_and_random:
        return None

    nodes = [Node(value) for value, _ in values_and_random]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    for i, (_, random_index) in enumerate(values_and_random):
        if random_index is not None:
            nodes[i].random = nodes[random_index]

    return nodes[0]


def serialize_random_list(head: Optional[Node]) -> list[tuple[int, Optional[int]]]:
    nodes = []
    node_to_index: dict[Node, int] = {}
    cur = head

    while cur:
        node_to_index[cur] = len(nodes)
        nodes.append(cur)
        cur = cur.next

    result = []
    for node in nodes:
        random_index = node_to_index[node.random] if node.random else None
        result.append((node.val, random_index))

    return result


def collect_nodes(head: Optional[Node]) -> list[Node]:
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    return nodes


def assert_deep_copy(original: Optional[Node], copied: Optional[Node]) -> None:
    assert serialize_random_list(original) == serialize_random_list(copied)

    original_nodes = collect_nodes(original)
    copied_nodes = collect_nodes(copied)
    assert len(original_nodes) == len(copied_nodes)

    copied_set = set(copied_nodes)
    for original_node, copied_node in zip(original_nodes, copied_nodes):
        assert original_node is not copied_node
        if copied_node.random is not None:
            assert copied_node.random in copied_set


if __name__ == "__main__":
    test_cases = [
        [],
        [(7, None)],
        [(1, 0)],
        [(1, 1), (2, 1)],
        [(3, None), (3, 0), (3, None)],
        [(7, None), (13, 0), (11, 4), (10, 2), (1, 0)],
    ]

    solution = Solution()
    for case in test_cases:
        head = build_random_list(case)
        original_snapshot = serialize_random_list(head)
        copied = solution.copyRandomList(head)

        assert serialize_random_list(head) == original_snapshot
        assert serialize_random_list(copied) == original_snapshot
        assert_deep_copy(head, copied)

    assert solution.copyRandomList(None) is None

    print("all tests passed")
