# 方法3：收集节点后按切分点重连

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head

        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        n = len(nodes)
        k %= n
        if k == 0:
            return head

        new_tail = nodes[n - k - 1]
        new_head = new_tail.next
        nodes[-1].next = head
        new_tail.next = None
        return new_head


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

    assert linked_list_to_list(solution.rotateRight(build_linked_list([]), 2)) == []
    assert linked_list_to_list(solution.rotateRight(build_linked_list([1]), 0)) == [1]
    assert linked_list_to_list(solution.rotateRight(build_linked_list([1]), 3)) == [1]
    assert linked_list_to_list(solution.rotateRight(build_linked_list([1, 2, 3, 4, 5]), 2)) == [4, 5, 1, 2, 3]
    assert linked_list_to_list(solution.rotateRight(build_linked_list([0, 1, 2]), 4)) == [2, 0, 1]
    assert linked_list_to_list(solution.rotateRight(build_linked_list([1, 2]), 1)) == [2, 1]
    assert linked_list_to_list(solution.rotateRight(build_linked_list([1, 2]), 2)) == [1, 2]

    print("all tests passed")
