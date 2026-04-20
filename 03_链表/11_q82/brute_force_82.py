import collections

# 定义链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    """
    方法一：暴力解法（哈希表计数）
    
    思路：
    1. 遍历一次链表，记录每个值出现的次数。
    2. 再次遍历链表（或根据记录的结果），只保留出现次数为 1 的节点。
    3. 这种方法直观，但需要额外的空间。
    """
    if not head:
        return None
    
    # 1. 计数
    counts = collections.Counter()
    curr = head
    while curr:
        counts[curr.val] += 1
        curr = curr.next
    
    # 2. 构建新链表
    dummy = ListNode(0)
    new_curr = dummy
    
    curr = head
    while curr:
        if counts[curr.val] == 1:
            new_curr.next = ListNode(curr.val)
            new_curr = new_curr.next
        curr = curr.next
        
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
