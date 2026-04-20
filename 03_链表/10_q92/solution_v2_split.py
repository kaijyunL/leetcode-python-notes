# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        解法二：切断与反转（三步走）
        时间复杂度：O(N) - 最多遍历两次
        空间复杂度：O(1) - 仅需常量级额外空间
        """
        def reverse_linked_list(head):
            pre = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

        # 使用虚拟头节点，简化 head 被反转的情况
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node

        # 第 1 步：从虚拟头节点走 left - 1 步，来到 left 节点的前驱节点
        for _ in range(left - 1):
            pre = pre.next

        # 第 2 步：从 pre 再走 right - left + 1 步，来到 right 节点
        right_node = pre
        for _ in range(right - left + 1):
            right_node = right_node.next

        # 第 3 步：切断出一个子链表（截取 [left, right] 部分）
        left_node = pre.next
        curr = right_node.next

        # 注意：切断连接
        pre.next = None
        right_node.next = None

        # 第 4 步：反转子链表
        reverse_linked_list(left_node)

        # 第 5 步：接回原链表
        # 反转后，right_node 变成了子链表的头，left_node 变成了尾
        pre.next = right_node
        left_node.next = curr
        
        return dummy_node.next

def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res))

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("原链表：", end="")
    print_list(head)
    
    sol = Solution()
    new_head = sol.reverseBetween(head, 2, 4)
    print("反转后 (2-4)：", end="")
    print_list(new_head)
