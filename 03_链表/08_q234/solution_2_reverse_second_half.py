# 方法2：快慢指针 + 反转后半段 + 逐个比较（C++风格紧凑写法，面试主推）

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        cur = slow.next
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        p1 = head
        p2 = prev
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True


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
    assert solution.isPalindrome(None) is True
    assert solution.isPalindrome(build_linked_list([1, 2, 3, 4])) is False

    print("all tests passed")
