# 方法3：递归做对称比较

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front = head

        def dfs(node: Optional[ListNode]) -> bool:
            if node is None:
                return True

            if not dfs(node.next):
                return False

            if self.front.val != node.val:
                return False

            self.front = self.front.next
            return True

        return dfs(head)


def build_linked_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


if __name__ == "__main__":
    solution = Solution()

    assert solution.isPalindrome(build_linked_list([1, 2, 2, 1])) is True
    assert solution.isPalindrome(build_linked_list([1, 2, 3, 2, 1])) is True
    assert solution.isPalindrome(build_linked_list([1, 2])) is False
    assert solution.isPalindrome(build_linked_list([1])) is True
    assert solution.isPalindrome(build_linked_list([])) is True
    assert solution.isPalindrome(build_linked_list([1, 2, 3, 4])) is False

    print("all tests passed")
