# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        解法三：头插法（一步到位，一次遍历）
        时间复杂度：O(N) - 只需要遍历一次
        空间复杂度：O(1) - 仅需常量级额外空间
        """
        # 设置 dummyNode 是这一类问题的一般做法
        dummy_node = ListNode(-1)
        dummy_node.next = head
        
        # 1. 找到 pre 节点（left 前面的那个节点）
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next
        
        # 2. 初始化 curr（指向 left 节点）
        curr = pre.next
        
        # 3. 开始头插法进行反转
        # 每次循环都将 curr.next 节点剔除，并插到 pre 之后
        # 循环次数：right - left
        for _ in range(right - left):
            nxt = curr.next           # 记录当前要搬运的节点 nxt
            curr.next = nxt.next      # curr 跳过 nxt，连接 nxt 的下一个节点
            nxt.next = pre.next       # nxt 的下一个指向 pre 当前的下一个（即已反转部分的头部）
            pre.next = nxt            # pre 指向 nxt，完成搬运
            
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
