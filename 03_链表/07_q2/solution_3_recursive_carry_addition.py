# 方法3：递归逐位相加（补充理解）

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        def dfs(
            n1: Optional[ListNode],
            n2: Optional[ListNode],
            carry: int,
        ) -> Optional[ListNode]:
            if not n1 and not n2 and carry == 0:
                return None

            val1 = n1.val if n1 else 0
            val2 = n2.val if n2 else 0
            total = val1 + val2 + carry

            node = ListNode(total % 10)
            node.next = dfs(
                n1.next if n1 else None,
                n2.next if n2 else None,
                total // 10,
            )
            return node

        return dfs(l1, l2, 0)


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

    assert linked_list_to_list(solution.addTwoNumbers(build_linked_list([2, 4, 3]), build_linked_list([5, 6, 4]))) == [7, 0, 8]
    assert linked_list_to_list(solution.addTwoNumbers(build_linked_list([0]), build_linked_list([0]))) == [0]
    assert linked_list_to_list(solution.addTwoNumbers(build_linked_list([5]), build_linked_list([5]))) == [0, 1]
    assert linked_list_to_list(solution.addTwoNumbers(build_linked_list([9, 9, 9, 9, 9, 9, 9]), build_linked_list([9, 9, 9, 9]))) == [8, 9, 9, 9, 0, 0, 0, 1]
    assert linked_list_to_list(solution.addTwoNumbers(build_linked_list([1, 8]), build_linked_list([0]))) == [1, 8]

    print("all tests passed")
