from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        dummy = ListNode(0, head)
        step = 1

        while step < length:
            prev = dummy
            cur = dummy.next

            while cur:
                left = cur
                right = self.split(left, step)
                cur = self.split(right, step)
                merged_head, merged_tail = self.merge(left, right)
                prev.next = merged_head
                prev = merged_tail

            step *= 2

        return dummy.next

    def split(self, head: Optional[ListNode], size: int) -> Optional[ListNode]:
        if head is None:
            return None

        for _ in range(size - 1):
            if head.next is None:
                break
            head = head.next

        second = head.next
        head.next = None
        return second

    def merge(
        self,
        left: Optional[ListNode],
        right: Optional[ListNode],
    ) -> tuple[Optional[ListNode], Optional[ListNode]]:
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
        while tail.next:
            tail = tail.next

        return dummy.next, tail


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
        ([1, 2, 3, 4], [1, 2, 3, 4]),
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
