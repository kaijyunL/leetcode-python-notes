# 方法1：辅助数组重建答案

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        current = head

        while current:
            values.append(current.val)
            current = current.next

        dummy = ListNode(0)
        tail = dummy

        for value in reversed(values):
            tail.next = ListNode(value)
            tail = tail.next

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
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result


if __name__ == "__main__":
    solution = Solution()

    assert linked_list_to_list(solution.reverseList(build_linked_list([]))) == []
    assert linked_list_to_list(solution.reverseList(build_linked_list([1]))) == [1]
    assert linked_list_to_list(solution.reverseList(build_linked_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert linked_list_to_list(solution.reverseList(build_linked_list([1, 1, 2, 3]))) == [3, 2, 1, 1]

    print("all tests passed")
