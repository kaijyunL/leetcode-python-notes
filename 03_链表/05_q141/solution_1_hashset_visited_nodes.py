# 方法1：哈希集合记录访问过的节点

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        cur = head

        while cur:
            if cur in visited:
                return True
            visited.add(cur)
            cur = cur.next

        return False


def build_linked_list_with_cycle(values: list[int], pos: int) -> Optional[ListNode]:
    if not values:
        return None

    nodes = [ListNode(value) for value in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


if __name__ == "__main__":
    solution = Solution()

    assert solution.hasCycle(build_linked_list_with_cycle([3, 2, 0, -4], 1)) is True
    assert solution.hasCycle(build_linked_list_with_cycle([1, 2], 0)) is True
    assert solution.hasCycle(build_linked_list_with_cycle([1], -1)) is False
    assert solution.hasCycle(build_linked_list_with_cycle([1, 2, 3, 4], -1)) is False
    assert solution.hasCycle(build_linked_list_with_cycle([1], 0)) is True
    assert solution.hasCycle(None) is False

    print("all tests passed")
