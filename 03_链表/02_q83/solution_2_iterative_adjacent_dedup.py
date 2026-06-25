# 方法2：一次遍历跳过相邻重复（面试主推）

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

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
    assert linked_list_to_list(solution.deleteDuplicates(build_linked_list([1, 2, 3, 4]))) == [1, 2, 3, 4]

    print("all tests passed")
