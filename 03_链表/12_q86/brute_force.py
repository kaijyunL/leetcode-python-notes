# -*- coding: utf-8 -*-

class ListNode:
    """定义链表节点"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition_brute_force(head: ListNode, x: int) -> ListNode:
    """
    方法一：简单暴力法
    思路：
    1. 遍历原链表，取出所有节点值放到一个数组中。
    2. 创建两个新的辅助数组：一个存放所有小于 x 的值，另一个存放所有大于或等于 x 的值。
    3. 合并这两个数组。
    4. 遍历合并后的数组，重新构造出一个新链表。
    """
    if not head:
        return None
    
    # 步骤1：遍历原链表，取出所有节点值
    values = []
    curr = head
    while curr:
        values.append(curr.val)
        curr = curr.next
    
    # 步骤2：根据值和 x 的比较，将所有的值分流到两个列表中
    less = []
    greater_or_equal = []
    for val in values:
        if val < x:
            less.append(val)
        else:
            greater_or_equal.append(val)
    
    # 步骤3：合并两个列表
    combined = less + greater_or_equal
    
    # 步骤4：构造新链表
    dummy = ListNode(0)
    new_curr = dummy
    for val in combined:
        new_curr.next = ListNode(val)
        new_curr = new_curr.next
        
    return dummy.next

# --- 测试代码 ---
def print_list(node):
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    print(" -> ".join(res))

def create_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

if __name__ == "__main__":
    # 测试用例: [1,4,3,2,5,2], x = 3
    # 期望输出: [1,2,2,4,3,5]
    head = create_list([1, 4, 3, 2, 5, 2])
    print("原链表：", end="")
    print_list(head)
    
    x = 3
    result = partition_brute_force(head, x)
    print(f"分隔结果 (x={x})：", end="")
    print_list(result)
