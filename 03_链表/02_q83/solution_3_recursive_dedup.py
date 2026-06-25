# 方法3：递归去重（补充理解）

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        head.next = self.deleteDuplicates(head.next)

        if head.val == head.next.val:
            return head.next
        return head


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

    assert linked_list_to_list(solution.deleteDuplicates(build_linked_list([]))) == []
    assert linked_list_to_list(solution.deleteDuplicates(build_linked_list([1]))) == [1]
    assert linked_list_to_list(solution.deleteDuplicates(build_linked_list([1, 1, 2]))) == [1, 2]
    assert linked_list_to_list(solution.deleteDuplicates(build_linked_list([1, 1, 2, 3, 3]))) == [1, 2, 3]
    assert linked_list_to_list(solution.deleteDuplicates(build_linked_list([1, 1, 1, 1]))) == [1]

    print("all tests passed")
