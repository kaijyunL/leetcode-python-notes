# -*- coding: utf-8 -*-

class ListNode:
    """定义链表节点"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition_optimized(head: ListNode, x: int) -> ListNode:
    """
    方法二：最优双指针法
    核心思想：
    1. 创建两个新的虚拟头节点 dummy1 和 dummy2。
    2. dummy1 用来记录所有小于 x 的节点形成的链表。
    3. dummy2 用来记录所有大于或等于 x 的节点形成的链表。
    4. 遍历原链表，根据节点值将当前节点接到 dummy1 或 dummy2 的末尾。
    5. 最后将 dummy1 的尾部连接到 dummy2 的头部。
    """
    if not head:
        return None
    
    # 步骤1：初始化两个哑节点以及指向它们末尾的指针
    before_dummy = ListNode(0)  # 存放所有 < x 的节点
    after_dummy = ListNode(0)   # 存放所有 >= x 的节点
    
    before = before_dummy
    after = after_dummy
    
    # 步骤2：遍历链表并根据值分流
    curr = head
    while curr:
        if curr.val < x:
            before.next = curr
            before = before.next
        else:
            after.next = curr
            after = after.next
        curr = curr.next
        
    # 步骤3：重要！防止产生无限环。必须切断 after 的 next。
    after.next = None
    
    # 步骤4：合并两条新链表
    before.next = after_dummy.next
    
    # 最终返回 before 链表的头部
    return before_dummy.next

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
    result = partition_optimized(head, x)
    print(f"分隔结果 (x={x})：", end="")
    print_list(result)
