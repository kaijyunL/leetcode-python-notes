# solution_brute_force.py
# LeetCode 206. 反转链表 - 暴力方法 (辅助数组)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        # 1. 遍历链表，将所有结点的值存入数组
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        # 2. 从后向前遍历数组，修改结点的值（以此反转值，而非结点）
        # 或者创建一个新的链表（为了性能，这里选择重建值）
        curr = head
        for val in reversed(values):
            curr.val = val
            curr = curr.next
        
        return head

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
