from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k <= 1:
            return head

        stop = head
        for _ in range(k):
            if stop is None:
                return head
            stop = stop.next

        new_head = self.reverse_range(head, stop)
        head.next = self.reverseKGroup(stop, k)
        return new_head

    def reverse_range(
        self,
        start: Optional[ListNode],
        stop: Optional[ListNode],
    ) -> Optional[ListNode]:
        prev = stop
        cur = start

        while cur is not stop:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        return prev


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
        ([], 2, []),
        ([1], 1, [1]),
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1, 2, 3, 4, 5], 5, [5, 4, 3, 2, 1]),
        ([1, 2, 3, 4, 5], 6, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4], 2, [2, 1, 4, 3]),
        ([1, 2, 3, 4, 5, 6], 4, [4, 3, 2, 1, 5, 6]),
    ]

    solution = Solution()
    for values, k, expected in test_cases:
        head = build_linked_list(values)
        reversed_head = solution.reverseKGroup(head, k)
        assert linked_list_to_list(reversed_head) == expected

    assert solution.reverseKGroup(None, 3) is None

    print("all tests passed")
