# -*- coding: utf-8 -*-
# LeetCode 第 83 题：删除排序链表中的重复元素
# 解法 1：暴力法（使用哈希集合）

class ListNode:
    """定义单链表节点"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    """
    使用哈希集合追踪已遍历过的值
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    # 如果链表为空或只有一个节点，直接返回
    if not head:
        return head
    
    seen = {head.val} # 存储见过的元素
    curr = head
    
    # 遍历链表，从第二个节点开始检查
    while curr.next:
        if curr.next.val in seen:
            # 发现重复，跳过重复节点
            curr.next = curr.next.next
        else:
            # 不是重复，加入集合并继续向前
            seen.add(curr.next.val)
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
    
    print("--- 解法 1：暴力法 (Hash Set) 测试 ---")
    for tc in test_cases:
        head = create_list(tc)
        print(f"原链表: {tc}")
        result = deleteDuplicates(head)
        print("去重后: ", end="")
        print_list(result)
        print("-" * 30)
