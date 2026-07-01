from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k <= 1:
            return head

        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        for i in range(0, len(nodes), k):
            if i + k <= len(nodes):
                nodes[i : i + k] = reversed(nodes[i : i + k])

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        if nodes:
            nodes[-1].next = None
            return nodes[0]
        return None


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
    ]

    solution = Solution()
    for values, k, expected in test_cases:
        head = build_linked_list(values)
        reversed_head = solution.reverseKGroup(head, k)
        assert linked_list_to_list(reversed_head) == expected

    assert solution.reverseKGroup(None, 3) is None

    print("all tests passed")
