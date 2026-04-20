# -*- coding: utf-8 -*-
# LeetCode 第 83 题：删除排序链表中的重复元素
# 解法 3：递归思想（追求简洁性）

class ListNode:
    """定义单链表节点"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    """
    通过递归处理子链表，然后处理当前节点与子链表的连接。
    时间复杂度: O(n)
    空间复杂度: O(n) (递归栈深度)
    """
    # 基本条件：如果链表为空，或者只有一个节点，直接回复
    if not head or not head.next:
        return head
    
    # 递归调用核心：让后续链表去重
    head.next = deleteDuplicates(head.next)
    
    # 比较逻辑：如果 head.val 与 head.next.val 相同，说明 head 重复了，返回 head.next（舍去 head）
    # 否则 head 不重复，直接返回本身。
    return head.next if head.val == head.next.val else head

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
    
    print("--- 解法 3：递归 (Elegant Recursion) 测试 ---")
    for tc in test_cases:
        head = create_list(tc)
        print(f"原链表: {tc}")
        result = deleteDuplicates(head)
        print("去重后: ", end="")
        print_list(result)
        print("-" * 30)
