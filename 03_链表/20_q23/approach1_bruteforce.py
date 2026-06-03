# approach1_bruteforce.py
# -*- coding: utf-8 -*-

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    """
    暴力解法：
    1. 提取所有节点的值。
    2. 对这些值进行排序。
    3. 根据排序后的数组创建一个新的链表。
    """
    nodes = []
    # 1. 遍历所有的链表并将节点值存入数组中
    for l in lists:
        while l:
            nodes.append(l.val)
            l = l.next
    
    # 2. 对数组进行排序
    nodes.sort()
    
    # 3. 根据排序后的结果创建新链表
    dummy = ListNode(0)
    curr = dummy
    for val in nodes:
        curr.next = ListNode(val)
        curr = curr.next
        
    return dummy.next

# --- 测试代码 ---
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

if __name__ == "__main__":
    # 示例: [[1,4,5],[1,3,4],[2,6]]
    list1 = create_linked_list([1, 4, 5])
    list2 = create_linked_list([1, 3, 4])
    list3 = create_linked_list([2, 6])
    
    lists = [list1, list2, list3]
    result = mergeKLists(lists)
    print("暴力解法结果:")
    print_linked_list(result)
