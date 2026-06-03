# 解法二：使用栈（空间换时间）

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        stack = []
        
        # 第一次遍历：将包括 dummy 在内的所有节点压入栈中
        current = dummy
        while current:
            stack.append(current)
            current = current.next
            
        # 弹出栈顶的 n 个元素，这些是倒数的那 n 个节点
        for _ in range(n):
            stack.pop()
            
        # 此时栈顶剩下的节点，就是要删除节点的前驱节点
        prev = stack[-1]
        
        # 执行删除
        prev.next = prev.next.next
        
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
