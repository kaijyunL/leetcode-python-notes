# 解法一：两次遍历（基础计算长度法）

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 创建一个哑节点，并将其 next 指向头节点
        dummy = ListNode(0, head)
        
        # 第一次遍历：统计链表长度
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
            
        # 第二次遍历：找到要删除且节点的前驱节点
        # 它在正数第 length - n 个位置（由于有 dummy，所以刚好走 length - n 步）
        current = dummy
        for _ in range(length - n):
            current = current.next
            
        # 执行删除操作：跨过当前节点的 next 节点
        current.next = current.next.next
        
        # dummy.next 指向的始终是真正的（可能被更新了的）头节点
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
