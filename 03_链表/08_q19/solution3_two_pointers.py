# 解法三：双指针 / 快慢指针（一趟遍历最优解）

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        
        # 初始化快慢指针
        fast = dummy
        slow = dummy
        
        # 1. 让快指针先走 n 步
        for _ in range(n):
            fast = fast.next
            
        # 2. 快慢指针一起走，直到快指针的下一个是没有节点（到达末尾）
        # 这样能保证 slow 刚好停在要删除的节点的前一个！
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        # 3. 此时 slow 停在了要删除节点的前驱，执行删除
        slow.next = slow.next.next
        
        return dummy.next

# 测试代码
if __name__ == "__main__":
    def print_list(head):
        res = []
        while head:
            res.append(str(head.val))
            head = head.next
        print("->".join(res) if res else "Empty")

    def build_list(arr):
        dummy = ListNode()
        curr = dummy
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    arr = [1, 2, 3, 4, 5]
    n = 2
    print(f"原链表: {arr}, 尝试删除倒数第 {n} 个节点")
    head = build_list(arr)
    sol = Solution()
    new_head = sol.removeNthFromEnd(head, n)
    print("删除后: ", end="")
    print_list(new_head)
