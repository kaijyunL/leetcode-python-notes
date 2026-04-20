# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        解法一：暴力法（辅助数组）
        时间复杂度：O(N) - 遍历两次链表，一次数组反转
        空间复杂度：O(N) - 需要额外数组存储节点值
        """
        if not head or left == right:
            return head
        
        # 1. 将链表值提取到列表中
        nodes = []
        curr = head
        while curr:
            nodes.append(curr.val)
            curr = curr.next
            
        # 2. 在列表中反转 [left-1, right-1] 区间
        # 注意：题目索引从 1 开始，列表索引从 0 开始
        l, r = left - 1, right - 1
        while l < r:
            nodes[l], nodes[r] = nodes[r], nodes[l]
            l += 1
            r -= 1
            
        # 3. 将反转后的值写回链表
        curr = head
        for val in nodes:
            curr.val = val
            curr = curr.next
            
        return head

def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res))

if __name__ == "__main__":
    # 测试案例：1 -> 2 -> 3 -> 4 -> 5, left=2, right=4
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("原链表：", end="")
    print_list(head)
    
    sol = Solution()
    new_head = sol.reverseBetween(head, 2, 4)
    print("反转后 (2-4)：", end="")
    print_list(new_head)
