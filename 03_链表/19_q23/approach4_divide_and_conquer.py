from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        分治法合并：
        1. 将 k 个链表平分成两份。
        2. 递归调用 self.mergeKLists 合并左侧部分。
        3. 递归调用 self.mergeKLists 合并右侧部分。
        4. 最后使用 self.mergeTwoLists 合并这两份链表。
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
            
        mid = len(lists) // 2
        # 注意：这里调用的是 self.mergeKLists
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        
        return self.mergeTwoLists(l, r)

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        合并两个升序链表 (LeetCode 21)
        """
        dummy = ListNode(0)
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        curr.next = l1 if l1 else l2
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
    # 创建示例: [[1,4,5],[1,3,4],[2,6]]
    sol = Solution()
    list1 = create_linked_list([1, 4, 5])
    list2 = create_linked_list([1, 3, 4])
    list3 = create_linked_list([2, 6])
    
    lists = [list1, list2, list3]
    # 调用类的实例方法
    result = sol.mergeKLists(lists)
    print("分治合并 (Solution类) 结果:")
    print_linked_list(result)
