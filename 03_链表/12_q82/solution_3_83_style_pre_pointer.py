# 方法3：延续 83 题风格的前驱指针写法

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy

        while pre.next and pre.next.next:
            if pre.next.val == pre.next.next.val:
                value = pre.next.val
                while pre.next and pre.next.val == value:
                    pre.next = pre.next.next
            else:
                pre = pre.next

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

    assert linked_list_to_list(solution.deleteDuplicates(build_linked_list([]))) == []
    assert linked_list_to_list(solution.deleteDuplicates(build_linked_list([1]))) == [1]
    assert linked_list_to_list(solution.deleteDuplicates(build_linked_list([1, 1]))) == []
    assert linked_list_to_list(solution.deleteDuplicates(build_linked_list([1, 1, 2]))) == [2]
    assert linked_list_to_list(solution.deleteDuplicates(build_linked_list([1, 2, 2]))) == [1]
    assert linked_list_to_list(solution.deleteDuplicates(build_linked_list([1, 2, 3, 3, 4, 4, 5]))) == [1, 2, 5]
    assert linked_list_to_list(solution.deleteDuplicates(build_linked_list([1, 1, 1, 2, 3]))) == [2, 3]
    assert linked_list_to_list(solution.deleteDuplicates(build_linked_list([1, 1, 2, 2, 3, 3]))) == []

    print("all tests passed")
