# 方法2：求长度 + 成环 + 找新尾断开（面试主推）

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head

        length = 1
        old_tail = head
        while old_tail.next:
            length += 1
            old_tail = old_tail.next

        k %= length
        if k == 0:
            return head

        old_tail.next = head

        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head


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

    assert linked_list_to_list(solution.rotateRight(build_linked_list([]), 2)) == []
    assert linked_list_to_list(solution.rotateRight(build_linked_list([1]), 0)) == [1]
    assert linked_list_to_list(solution.rotateRight(build_linked_list([1]), 3)) == [1]
    assert linked_list_to_list(solution.rotateRight(build_linked_list([1, 2, 3, 4, 5]), 2)) == [4, 5, 1, 2, 3]
    assert linked_list_to_list(solution.rotateRight(build_linked_list([0, 1, 2]), 4)) == [2, 0, 1]
    assert linked_list_to_list(solution.rotateRight(build_linked_list([1, 2]), 1)) == [2, 1]
    assert linked_list_to_list(solution.rotateRight(build_linked_list([1, 2]), 2)) == [1, 2]

    print("all tests passed")
