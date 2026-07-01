from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        values = []

        for head in lists:
            cur = head
            while cur:
                values.append(cur.val)
                cur = cur.next

        values.sort()

        dummy = ListNode(0)
        tail = dummy
        for value in values:
            tail.next = ListNode(value)
            tail = tail.next

        return dummy.next


def build_linked_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def build_linked_lists(groups: list[list[int]]) -> list[Optional[ListNode]]:
    return [build_linked_list(group) for group in groups]


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
        ([[]], []),
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([[1], [0]], [0, 1]),
        ([[], [2], [], [1, 3]], [1, 2, 3]),
        ([[-2, -1, -1], [-3, 4], [0]], [-3, -2, -1, -1, 0, 4]),
    ]

    solution = Solution()
    for groups, expected in test_cases:
        lists = build_linked_lists(groups)
        merged = solution.mergeKLists(lists)
        assert linked_list_to_list(merged) == expected

    assert solution.mergeKLists([]) is None

    print("all tests passed")
