# 方法1：两次遍历统计长度

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        prev = dummy
        for _ in range(length - n):
            prev = prev.next

        prev.next = prev.next.next
        return dummy.next


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

    assert linked_list_to_list(solution.removeNthFromEnd(build_linked_list([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert linked_list_to_list(solution.removeNthFromEnd(build_linked_list([1]), 1)) == []
    assert linked_list_to_list(solution.removeNthFromEnd(build_linked_list([1, 2]), 1)) == [1]
    assert linked_list_to_list(solution.removeNthFromEnd(build_linked_list([1, 2]), 2)) == [2]
    assert linked_list_to_list(solution.removeNthFromEnd(build_linked_list([1, 2, 3]), 3)) == [2, 3]

    print("all tests passed")
