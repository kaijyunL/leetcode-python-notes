# solution_iterative.py
# LeetCode 206. 反转链表 - 双指针迭代法 (最优 O(1) 空间复杂度)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # prev 指向当前结点的前一个结点（初始为 None）
        prev = None
        # curr 指向当前正在处理的结点
        curr = head
        
        while curr:
            # 1. 暂存下一个结点的指针，防止断链
            next_temp = curr.next
            
            # 2. 将当前结点的 next 指向前一个结点（核心反转）
            curr.next = prev
            
            # 3. prev 指针前移到当前结点
            prev = curr
            
            # 4. curr 指针前移到之前暂存的下一个结点
            curr = next_temp
        
        # 当 curr 为空时，prev 就是反转后的新头结点
        return prev

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
