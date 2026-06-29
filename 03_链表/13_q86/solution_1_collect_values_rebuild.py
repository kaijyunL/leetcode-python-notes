# 方法1：收集值后重建链表

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        values = []
        cur = head

        while cur:
            values.append(cur.val)
            cur = cur.next

        ordered = [value for value in values if value < x]
        ordered += [value for value in values if value >= x]

        dummy = ListNode(0)
        tail = dummy

        for value in ordered:
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
    cur = head

    while cur:
        result.append(cur.val)
        cur = cur.next

    return result


if __name__ == "__main__":
    solution = Solution()

    assert linked_list_to_list(solution.partition(build_linked_list([]), 3)) == []
    assert linked_list_to_list(solution.partition(build_linked_list([1]), 3)) == [1]
    assert linked_list_to_list(solution.partition(build_linked_list([4]), 3)) == [4]
    assert linked_list_to_list(solution.partition(build_linked_list([1, 4, 3, 2, 5, 2]), 3)) == [1, 2, 2, 4, 3, 5]
    assert linked_list_to_list(solution.partition(build_linked_list([1, 4, 3, 2]), 3)) == [1, 2, 4, 3]
    assert linked_list_to_list(solution.partition(build_linked_list([2, 1]), 2)) == [1, 2]
    assert linked_list_to_list(solution.partition(build_linked_list([1, 2, 2]), 3)) == [1, 2, 2]
    assert linked_list_to_list(solution.partition(build_linked_list([4, 5, 6]), 3)) == [4, 5, 6]

    print("all tests passed")
