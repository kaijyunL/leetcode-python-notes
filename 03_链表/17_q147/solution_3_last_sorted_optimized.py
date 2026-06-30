from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy = ListNode(0, head)
        last_sorted = head
        cur = head.next

        while cur:
            if last_sorted.val <= cur.val:
                last_sorted = cur
            else:
                prev = dummy
                while prev.next and prev.next.val <= cur.val:
                    prev = prev.next

                last_sorted.next = cur.next
                cur.next = prev.next
                prev.next = cur

            cur = last_sorted.next

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
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([3, 3, 2, 2, 1], [1, 2, 2, 3, 3]),
        ([2, 1, 2, 1], [1, 1, 2, 2]),
    ]

    solution = Solution()
    for values, expected in test_cases:
        head = build_linked_list(values)
        sorted_head = solution.insertionSortList(head)
        assert linked_list_to_list(sorted_head) == expected

    assert solution.insertionSortList(None) is None

    print("all tests passed")
