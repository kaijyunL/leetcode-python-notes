# 方法2：哑节点 + 局部套用 206 反转模板（面试主推）

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

        dummy = ListNode(0, head)
        before_start = dummy
        for _ in range(left - 1):
            before_start = before_start.next

        start = before_start.next
        prev = None
        cur = start

        for _ in range(right - left + 1):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        start.next = cur
        before_start.next = prev
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

    assert linked_list_to_list(solution.reverseBetween(build_linked_list([1, 2, 3, 4, 5]), 2, 4)) == [1, 4, 3, 2, 5]
    assert linked_list_to_list(solution.reverseBetween(build_linked_list([5]), 1, 1)) == [5]
    assert linked_list_to_list(solution.reverseBetween(build_linked_list([3, 5]), 1, 2)) == [5, 3]
    assert linked_list_to_list(solution.reverseBetween(build_linked_list([1, 2, 3, 4, 5]), 1, 5)) == [5, 4, 3, 2, 1]
    assert linked_list_to_list(solution.reverseBetween(build_linked_list([1, 2, 3, 4, 5]), 3, 3)) == [1, 2, 3, 4, 5]
    assert linked_list_to_list(solution.reverseBetween(build_linked_list([1, 2, 3, 4]), 1, 3)) == [3, 2, 1, 4]

    print("all tests passed")
