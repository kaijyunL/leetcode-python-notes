# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_with_limit(head, limit=10):
    """打印链表，带限制以防死循环"""
    res = []
    curr = head
    count = 0
    while curr and count < limit:
        res.append(str(curr.val))
        curr = curr.next
        count += 1
    if count >= limit:
        res.append("... (检测到可能的死循环)")
    print(" -> ".join(res))

def partition_demo(head: ListNode, x: int, fix_bug: bool) -> ListNode:
    before_dummy = ListNode(0)
    after_dummy = ListNode(0)
    before = before_dummy
    after = after_dummy
    
    curr = head
    while curr:
        if curr.val < x:
            before.next = curr
            before = before.next
        else:
            after.next = curr
            after = after.next
        curr = curr.next
        
    if fix_bug:
        print(" [修复模式] 执行 after.next = None")
        after.next = None
    else:
        print(" [错误演示] 跳过 after.next = None")
        # 此时 after 指向的节点的 next 仍然保留着原链表中的指向

    before.next = after_dummy.next
    return before_dummy.next

if __name__ == "__main__":
    # 构造具体用例: 1 -> 4 -> 3 -> 2, x = 3
    # 关键点：末尾的 2 是 < 3 的，而它前面的节点 3 是 >= 3 的。
    # 在原链表中 3 -> 2。如果我们不切断 3.next，它会一直指着 2。
    
    x = 3
    
    print("--- 场景 A: 忘记切断后半部分末尾 (会导致死循环) ---")
    node3 = ListNode(3, ListNode(2)) # 3 -> 2
    head_a = ListNode(1, ListNode(4, node3)) # 1 -> 4 -> 3 -> 2
    res_a = partition_demo(head_a, x, fix_bug=False)
    print("结果链表：", end="")
    print_with_limit(res_a)

    print("\n--- 场景 B: 正确切断后半部分末尾 ---")
    node3_b = ListNode(3, ListNode(2))
    head_b = ListNode(1, ListNode(4, node3_b))
    res_b = partition_demo(head_b, x, fix_bug=True)
    print("结果链表：", end="")
    print_with_limit(res_b)
