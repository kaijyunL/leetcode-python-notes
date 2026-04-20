# solution_recursive.py
# LeetCode 206. 反转链表 - 递归法 (理解难点，但优雅)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 1. 递归终止条件：当前结点为空或者为最后一个结点
        if not head or not head.next:
            return head
        
        # 2. 递归调用，返回反转后链表的新头结点（一直传递到最后那个节点）
        new_head = self.reverseList(head.next)
        
        # 3. 反转操作：让 head 的下一个结点的 next 反过来指向 head
        # 这样就完成了 head 和 head.next 两个结点之间的方向倒置
        head.next.next = head
        
        # 4. 断开 head 指向 head.next 的原始连接，防止形成环
        head.next = None
        
        # 返回每一份递归中最终的新头结点
        return new_head

# --- 测试代码 ---
def create_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res))

if __name__ == "__main__":
    test_arr = [1, 2, 3, 4, 5]
    head = create_list(test_arr)
    print("原始链表: ", end="")
    print_list(head)
    
    sol = Solution()
    rev_head = sol.reverseList(head)
    print("反转后链表: ", end="")
    print_list(rev_head)
