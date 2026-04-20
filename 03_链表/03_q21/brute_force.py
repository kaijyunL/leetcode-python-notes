# LeetCode 21: 合并两个有序链表 - 1. 简单暴力法 (Brute Force)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    """
    核心思路：
    1. 遍历两个链表，将所有节点的值存入一个列表。
    2. 对该列表进行升序排序。
    3. 遍历排序后的列表，创建一个新的链表并返回。
    """
    nodes_val = []
    
    # 1. 提取 list1 的所有值
    curr = list1
    while curr:
        nodes_val.append(curr.val)
        curr = curr.next
        
    # 2. 提取 list2 的所有值
    curr = list2
    while curr:
        nodes_val.append(curr.val)
        curr = curr.next
        
    # 3. 对值进行升序排序 (时间复杂度 O(N log N))
    nodes_val.sort()
    
    # 4. 根据排序后的值创建新链表 (空间复杂度 O(N))
    dummy = ListNode(0)
    curr = dummy
    for val in nodes_val:
        curr.next = ListNode(val)
        curr = curr.next
        
    return dummy.next

# --- 测试代码 ---
def create_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_list(node):
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    print(" -> ".join(res) if res else "Empty")

if __name__ == "__main__":
    l1 = create_list([1, 2, 4])
    l2 = create_list([1, 3, 4])
    print("链表 1:", end=" ")
    print_list(l1)
    print("链表 2:", end=" ")
    print_list(l2)
    
    merged = mergeTwoLists(l1, l2)
    print("合并后:", end=" ")
    print_list(merged)
