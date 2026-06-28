# 方法3：哑节点 + 头插法区间反转

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
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next

        curr = pre.next
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt

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

    print("all tests passed")
