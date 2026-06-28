# 方法1：收集节点到数组后两两重连

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        for i in range(0, len(nodes) - 1, 2):
            nodes[i], nodes[i + 1] = nodes[i + 1], nodes[i]

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None

        return nodes[0]


def build_linked_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    result = []
    cur = head

    while cur:
        result.append(cur.val)
        cur = cur.next

    return result


if __name__ == "__main__":
    solution = Solution()

    assert linked_list_to_list(solution.swapPairs(build_linked_list([1, 2, 3, 4]))) == [2, 1, 4, 3]
    assert linked_list_to_list(solution.swapPairs(build_linked_list([1, 2, 3]))) == [2, 1, 3]
    assert linked_list_to_list(solution.swapPairs(build_linked_list([1]))) == [1]
    assert linked_list_to_list(solution.swapPairs(build_linked_list([]))) == []
    assert linked_list_to_list(solution.swapPairs(build_linked_list([1, 2]))) == [2, 1]

    print("all tests passed")
