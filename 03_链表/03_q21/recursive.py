# LeetCode 21: 合并两个有序链表 - 3. 递归法 (Recursion)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    """
    核心思路：
    1. 比较 list1 和 list2 的头节点。
    2. 如果 list1 更小，则合并后的头节点是 list1。
       - list1 的 next 应该是 (list1.next 与 list2 合并后的链表)。
    3. 否则，合并后的头节点是 list2。
       - list2 的 next 应该是 (list1 与 list2.next 合并后的链表)。
    4. 递归的终止条件：如果任意链表为空，直接返回另一个链表。
    """
    # 终止条件
    if not list1: return list2
    if not list2: return list1
    
    # 递归步骤
    if list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2

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
