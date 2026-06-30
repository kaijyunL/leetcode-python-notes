from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def merge(
        self,
        left: Optional[ListNode],
        right: Optional[ListNode],
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        tail.next = left if left else right
        return dummy.next


def build_linked_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    values = []
    cur = head
    while cur:
        values.append(cur.val)
        cur = cur.next
    return values


if __name__ == "__main__":
    test_cases = [
        ([], []),
        ([1], [1]),
        ([4, 2, 1, 3], [1, 2, 3, 4]),
        ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
        ([2, 1], [1, 2]),
        ([3, 3, 2, 2, 1], [1, 2, 2, 3, 3]),
        ([5, -2, 5, 7, 0], [-2, 0, 5, 5, 7]),
    ]

    solution = Solution()
    for values, expected in test_cases:
        head = build_linked_list(values)
        sorted_head = solution.sortList(head)
        assert linked_list_to_list(sorted_head) == expected

    assert solution.sortList(None) is None

    print("all tests passed")
