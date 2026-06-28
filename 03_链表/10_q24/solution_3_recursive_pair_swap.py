# 方法3：递归两两交换

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head
        return second


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
