# approach3_priority_queue.py
# -*- coding: utf-8 -*-

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    """
    优先队列解法 (最小堆)：
    1. 将所有非空链表的第一个节点放入最小堆中。
    2. 弹出堆顶（最小节点），并将其加入结果链表。
    3. 如果该节点所在的链表仍有后续节点，将其后续节点压入堆。
    4. 直到堆为空。
    """
    dummy = ListNode(0)
    curr = dummy
    
    # 堆中存储 (val, index, node)
    # 这里的 index 是为了在值相等时也能比较
    heap = []
    
    # 首先把每个链表的头节点放进堆
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(heap, (l.val, i, l))
    
    # 只要堆中还有节点
    while heap:
        val, i, node = heapq.heappop(heap)
        
        # 将弹出的节点连入结果列表
        curr.next = node
        curr = curr.next
        
        # 如果当前对应的链表还有下一个节点，把下一个节点放入堆中
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
            
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
    print("堆优化解法结果:")
    print_linked_list(result)
