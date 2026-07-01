from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k <= 1:
            return head

        dummy = ListNode(0, head)
        pre = dummy

        while True:
            kth = self.get_kth(pre, k)
            if kth is None:
                break

            group_head = pre.next
            group_next = kth.next
            kth.next = None

            new_head = self.reverse_list(group_head)
            pre.next = new_head
            group_head.next = group_next

            pre = group_head

        return dummy.next

    def get_kth(self, start: ListNode, k: int) -> Optional[ListNode]:
        cur = start
        for _ in range(k):
            cur = cur.next
            if cur is None:
                return None
        return cur

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
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
