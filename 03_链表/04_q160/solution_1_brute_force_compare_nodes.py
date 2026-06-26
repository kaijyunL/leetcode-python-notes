# 方法1：暴力枚举比较节点引用

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(
        self,
        headA: Optional[ListNode],
        headB: Optional[ListNode],
    ) -> Optional[ListNode]:
        a = headA

        while a:
            b = headB
            while b:
                if a is b:
                    return a
                b = b.next
            a = a.next

        return None


def build_linked_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


def attach_tail(head: Optional[ListNode], tail: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return tail

    cur = head
    while cur.next:
        cur = cur.next
    cur.next = tail
    return head


def build_intersection_case(
    prefix_a: list[int],
    prefix_b: list[int],
    common: list[int],
) -> tuple[Optional[ListNode], Optional[ListNode], Optional[ListNode]]:
    common_head = build_linked_list(common)
    headA = attach_tail(build_linked_list(prefix_a), common_head)
    headB = attach_tail(build_linked_list(prefix_b), common_head)
    return headA, headB, common_head


if __name__ == "__main__":
    solution = Solution()

    headA, headB, common = build_intersection_case([4, 1], [5, 6, 1], [8, 4, 5])
    assert solution.getIntersectionNode(headA, headB) is common

    headA, headB, common = build_intersection_case([], [3], [7, 8])
    assert solution.getIntersectionNode(headA, headB) is common

    headA, headB, common = build_intersection_case([1, 9, 1], [], [2, 4])
    assert solution.getIntersectionNode(headA, headB) is common

    assert solution.getIntersectionNode(build_linked_list([2, 6, 4]), build_linked_list([1, 5])) is None
    assert solution.getIntersectionNode(None, build_linked_list([1])) is None
    assert solution.getIntersectionNode(None, None) is None

    print("all tests passed")
