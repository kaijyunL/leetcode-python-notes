# 方法2：哑节点 + 快慢指针固定间距（面试主推）

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
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
    assert linked_list_to_list(solution.removeNthFromEnd(build_linked_list([1, 2, 3, 4]), 4)) == [2, 3, 4]

    print("all tests passed")
