# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        解法四：206式迭代法（逻辑延续性最好）
        为了区分变量：
        - before_start: 反转区间【前一个】节点（保持固定）
        - prev: 206 题中的翻转指针（不断移动）
        """
        # 1. 设置虚拟头节点
        dummy = ListNode(0, head)
        
        # 2. 定位到反转区域的前驱节点 before_start
        before_start = dummy
        for _ in range(left - 1):
            before_start = before_start.next
            
        # 3. 准备开始反转
        # start 指向区间第一个节点，反转后它将变成区间的最后一个节点
        start = before_start.next
        
        # ==========================================
        # 这一部分代码和 LeetCode 206 (反转链表) 完全一致
        # ==========================================
        prev = None  # 局部反转的新头部
        curr = start # 当前处理节点
        
        # 循环次数为区间长度：right - left + 1
        for _ in range(right - left + 1):
            # 1. 暂存
            next_temp = curr.next
            # 2. 反转
            curr.next = prev
            # 3. 前移
            prev = curr
            # 4. 前移
            curr = next_temp
        # ==========================================
            
        # 4. 最后的连接
        # 此时：
        # prev 指向了反转区间的最后一个节点（即新的一段的头）
        # curr 指向了反转区间后的第一个节点（即断点后的续接点）
        
        start.next = curr         # 让旧头（现尾）连上后面的剩余部分
        before_start.next = prev  # 让前面的部分连上新头
        
        return dummy.next

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
    # 反转位置 2 到 4 的节点
    new_head = sol.reverseBetween(head, 2, 4)
    print("206风格反转后 (2-4)：", end="")
    print_list(new_head)
