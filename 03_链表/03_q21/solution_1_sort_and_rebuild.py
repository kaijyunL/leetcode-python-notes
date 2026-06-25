# 方法1：收集后排序重建

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        values = []

        cur = list1
        while cur:
            values.append(cur.val)
            cur = cur.next

        cur = list2
        while cur:
            values.append(cur.val)
            cur = cur.next

        values.sort()

        dummy = ListNode(0)
        cur = dummy

        for value in values:
            cur.next = ListNode(value)
            cur = cur.next

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

    assert linked_list_to_list(solution.mergeTwoLists(build_linked_list([]), build_linked_list([]))) == []
    assert linked_list_to_list(solution.mergeTwoLists(build_linked_list([]), build_linked_list([0]))) == [0]
    assert linked_list_to_list(solution.mergeTwoLists(build_linked_list([1, 2, 4]), build_linked_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert linked_list_to_list(solution.mergeTwoLists(build_linked_list([1, 1, 2]), build_linked_list([1, 3]))) == [1, 1, 1, 2, 3]

    print("all tests passed")
