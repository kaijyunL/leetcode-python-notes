# 方法2：哑节点 + 迭代合并（面试主推）

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
        dummy = ListNode(0)
        cur = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 if list1 else list2
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
    assert linked_list_to_list(solution.mergeTwoLists(build_linked_list([5]), build_linked_list([1, 2, 6]))) == [1, 2, 5, 6]

    print("all tests passed")
