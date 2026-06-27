# 方法1：转成整数相加后再转回链表

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        def to_number(node: Optional[ListNode]) -> int:
            place = 1
            number = 0

            while node:
                number += node.val * place
                place *= 10
                node = node.next

            return number

        total = to_number(l1) + to_number(l2)

        if total == 0:
            return ListNode(0)

        dummy = ListNode(0)
        cur = dummy
        while total:
            cur.next = ListNode(total % 10)
            cur = cur.next
            total //= 10

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

    assert linked_list_to_list(solution.addTwoNumbers(build_linked_list([2, 4, 3]), build_linked_list([5, 6, 4]))) == [7, 0, 8]
    assert linked_list_to_list(solution.addTwoNumbers(build_linked_list([0]), build_linked_list([0]))) == [0]
    assert linked_list_to_list(solution.addTwoNumbers(build_linked_list([5]), build_linked_list([5]))) == [0, 1]
    assert linked_list_to_list(solution.addTwoNumbers(build_linked_list([9, 9, 9, 9, 9, 9, 9]), build_linked_list([9, 9, 9, 9]))) == [8, 9, 9, 9, 0, 0, 0, 1]
    assert linked_list_to_list(solution.addTwoNumbers(build_linked_list([1, 8]), build_linked_list([0]))) == [1, 8]

    print("all tests passed")
