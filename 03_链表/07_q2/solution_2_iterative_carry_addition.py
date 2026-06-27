# 方法2：哑节点 + 逐位模拟竖式加法（面试主推）

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
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            carry = total // 10
            cur.next = ListNode(total % 10)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

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
