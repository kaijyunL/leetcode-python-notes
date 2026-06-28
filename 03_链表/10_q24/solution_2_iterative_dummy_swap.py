# 方法2：哑节点 + 迭代指针重连（面试主推）

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first

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

    assert linked_list_to_list(solution.swapPairs(build_linked_list([1, 2, 3, 4]))) == [2, 1, 4, 3]
    assert linked_list_to_list(solution.swapPairs(build_linked_list([1, 2, 3]))) == [2, 1, 3]
    assert linked_list_to_list(solution.swapPairs(build_linked_list([1]))) == [1]
    assert linked_list_to_list(solution.swapPairs(build_linked_list([]))) == []
    assert linked_list_to_list(solution.swapPairs(build_linked_list([1, 2]))) == [2, 1]
    assert linked_list_to_list(solution.swapPairs(build_linked_list([1, 2, 3, 4, 5, 6]))) == [2, 1, 4, 3, 6, 5]

    print("all tests passed")
