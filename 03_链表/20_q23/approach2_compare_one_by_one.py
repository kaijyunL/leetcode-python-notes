# approach2_compare_one_by_one.py
# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    """
    逐一比较解法：每次从 k 个链表的头节点中寻找最小的值。
    """
    dummy = ListNode(0)
    curr = dummy
    
    # 只要在列表中有一个节点不为空，则就必须继续循环
    while True:
        min_val = float('inf')
        min_idx = -1
        
        # 依次检查每个子链表的头节点
        for i in range(len(lists)):
            if lists[i] and lists[i].val < min_val:
                min_val = lists[i].val
                min_idx = i
        
        # 如果当前没有找到任何有效的头节点（即所有链表都为空），跳出循环
        if min_idx == -1:
            break
            
        # 把找到的最小节点加入到结果链表中
        curr.next = lists[min_idx]
        curr = curr.next
        
        # 将那条链表的指针向后移动一位
        lists[min_idx] = lists[min_idx].next
        
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
    print("逐一比较解法结果:")
    print_linked_list(result)
