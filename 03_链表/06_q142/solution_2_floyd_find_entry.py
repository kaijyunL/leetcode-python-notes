# 方法2：Floyd 相遇后找入口（面试主推）

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                entry = head
                while entry is not slow:
                    entry = entry.next
                    slow = slow.next
                return entry

        return None


def build_linked_list_with_cycle(
    values: list[int],
    pos: int,
) -> tuple[Optional[ListNode], Optional[ListNode]]:
    if not values:
        return None, None

    nodes = [ListNode(value) for value in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    entry = None
    if pos != -1:
        entry = nodes[pos]
        nodes[-1].next = entry

    return nodes[0], entry


if __name__ == "__main__":
    solution = Solution()

    head, entry = build_linked_list_with_cycle([3, 2, 0, -4], 1)
    assert solution.detectCycle(head) is entry

    head, entry = build_linked_list_with_cycle([1, 2], 0)
    assert solution.detectCycle(head) is entry

    head, entry = build_linked_list_with_cycle([1], -1)
    assert solution.detectCycle(head) is entry

    head, entry = build_linked_list_with_cycle([1], 0)
    assert solution.detectCycle(head) is entry

    head, entry = build_linked_list_with_cycle([1, 2, 3, 4, 5], 2)
    assert solution.detectCycle(head) is entry

    assert solution.detectCycle(None) is None

    print("all tests passed")
