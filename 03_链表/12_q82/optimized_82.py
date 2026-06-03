# 定义链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    """
    方法二：一次遍历（双指针/指针跳跃）- 最优解
    
    思路：
    1. 使用一个 dummy 哑节点指向 head，方便处理头节点被删除的情况。
    2. 使用 pre 指针指向当前确定不重复的最后一个节点。
    3. 使用 cur 指针探测前方的节点。
    4. 如果 cur 和 cur.next 值相同，说明遇到了重复，通过循环跳过所有相同的节点。
    5. 如果 cur 和 cur.next 不同，说明 cur 是唯一的，将 pre.next 指向 cur，并移动 pre。
    """
    if not head:
        return None
    
    dummy = ListNode(0, head)
    pre = dummy
    
    while pre.next:
        cur = pre.next
        
        # 检查是否有重复
        if cur.next and cur.val == cur.next.val:
            # 发现重复，寻找重复段的末尾
            val = cur.val
            while cur and cur.val == val:
                cur = cur.next
            # 跳过所有重复节点，pre 的 next 直接指向重复段后的第一个节点
            # 注意：此处 pre 并不移动，因为新接上的节点可能仍然是重复的（在下一轮循环检查）
            pre.next = cur
        else:
            # 没有重复，pre 移动到下一个节点
            pre = pre.next
            
    return dummy.next

# --- 测试代码 ---
def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res) if res else "Empty List")

def create_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

if __name__ == "__main__":
    # 测试用例 1: [1,2,3,3,4,4,5] -> [1,2,5]
    head1 = create_list([1, 2, 3, 3, 4, 4, 5])
    print("输入: 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5")
    result1 = deleteDuplicates(head1)
    print("输出: ", end="")
    print_list(result1)

    # 测试用例 2: [1,1,1,2,3] -> [2,3]
    head2 = create_list([1, 1, 1, 2, 3])
    print("\n输入: 1 -> 1 -> 1 -> 2 -> 3")
    result2 = deleteDuplicates(head2)
    print("输出: ", end="")
    print_list(result2)
