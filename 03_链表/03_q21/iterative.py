# LeetCode 21: 合并两个有序链表 - 2. 迭代法 (Iterative Pointer Replacement)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    """
    核心思路：
    1. 使用 dummy 虚拟头节点，避免判空逻辑复杂。
    2. 设置指针 curr 指向新链表的末梢。
    3. 同时扫描 list1 和 list2：
       - 谁小就把 curr.next 指向谁。
       - 对应链表向后移，curr 也向后移。
    4. 将未耗尽的链表直接拼接到末尾。
    """
    dummy = ListNode(0)
    curr = dummy
    
    # 只要 list1 和 list2 都还有节点，就比较它们
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
        
    # 如果其中一方空了，直接把另一方剩下的全部拼上去 (这是 O(1) 的操作)
    curr.next = list1 if list1 else list2
    
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
