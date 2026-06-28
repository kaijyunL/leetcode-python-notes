# 方法1：收集节点到数组后区间重连

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int,
    ) -> Optional[ListNode]:
        if head is None or left == right:
            return head

        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        nodes[left - 1:right] = reversed(nodes[left - 1:right])

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

    assert linked_list_to_list(solution.reverseBetween(build_linked_list([1, 2, 3, 4, 5]), 2, 4)) == [1, 4, 3, 2, 5]
    assert linked_list_to_list(solution.reverseBetween(build_linked_list([5]), 1, 1)) == [5]
    assert linked_list_to_list(solution.reverseBetween(build_linked_list([3, 5]), 1, 2)) == [5, 3]
    assert linked_list_to_list(solution.reverseBetween(build_linked_list([1, 2, 3, 4, 5]), 1, 5)) == [5, 4, 3, 2, 1]
    assert linked_list_to_list(solution.reverseBetween(build_linked_list([1, 2, 3, 4, 5]), 3, 3)) == [1, 2, 3, 4, 5]
    assert linked_list_to_list(solution.reverseBetween(build_linked_list([]), 1, 1)) == []

    print("all tests passed")
