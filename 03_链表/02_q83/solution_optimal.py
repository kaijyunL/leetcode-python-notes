# -*- coding: utf-8 -*-
# LeetCode 第 83 题：删除排序链表中的重复元素
# 解法 2：最优解法（利用排序链表的相邻重复特性）

class ListNode:
    """定义单链表节点"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    """
    一次遍历比较当前节点与下一个节点的值。
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    # 定义遍历指针
    curr = head
    
    # 只要当前节点和下一个节点都存在，就继续遍历
    # 这里的条件已经涵盖了 head 为空或只有一个节点的情况，因此不需要额外的 if 判空
    while curr and curr.next:
        # 核心逻辑：既然是有序链表，重复元素必相邻
        if curr.val == curr.next.val:
            # 找到重复元素，删除下一个节点（跳过重复）
            curr.next = curr.next.next
        else:
            # 不是重复元素，指针向后移动一步
            curr = curr.next
            
    return head

def print_list(head: ListNode):
    """打印链表的实用工具函数"""
    vals = []
    curr = head
    while curr:
        vals.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(vals) if vals else "Empty List")

def create_list(arr):
    """从列表创建链表的实用工具函数"""
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

# 测试代码
if __name__ == "__main__":
    test_cases = [
        [1, 1, 2],
        [1, 1, 2, 3, 3],
        [1, 1, 1],
        []
    ]
    
    print("--- 解法 2：一次遍历 (O(1) Space) 测试 ---")
    for tc in test_cases:
        head = create_list(tc)
        print(f"原链表: {tc}")
        result = deleteDuplicates(head)
        print("去重后: ", end="")
        print_list(result)
        print("-" * 30)
