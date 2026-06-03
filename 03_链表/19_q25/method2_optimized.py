# -*- coding: utf-8 -*-

"""
LeetCode 第 25 题: K 个一组翻转链表 (Method 2: Optimized In-place Iterative)
思路分析 (Optimal):
1. 首先实现一个辅助函数, 用于反转某个部分的链表。
2. 使用一个哨兵节点 (dummy node) 指向链表的 head, 方便后续返回新的头。
3. 维护 pre、end、start、next 指针。
   - pre: 每组翻转前的一个节点。
   - end: 当前这一组的最后一个节点。
   - start: 当前这一组的第一个节点。
   - next: 下一组的第一个节点。
4. 每次判断 end 是否存在 (后面是否还有 k 个节点), 如果没有则结束。
5. 每次翻转 [start, end] 这个区间的节点, 然后把 pre.next 指向翻转后的新头部, 
   新尾部指向 next, 并重置 pre 为新的尾部。
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================================
# 写法一 (原版): 用 while prev != tail 控制循环
# 优点: 不需要缓存 tail.next, 因为判断的是 prev 而非 curr
# ============================================================
def reverseKGroup_v1(head: ListNode, k: int) -> ListNode:
    def reverse_one_group(head: ListNode, tail: ListNode):
        prev = tail.next  # prev 指向下一组的头部
        curr = head
        while prev != tail:  # prev 追上 tail 时, 说明所有节点已翻转
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return tail, head  # 返回新的头(tail) 和 新的尾(head)

    dummy = ListNode(0)
    dummy.next = head
    pre = dummy

    while head:
        tail = pre
        for i in range(k):
            tail = tail.next
            if not tail:
                return dummy.next

        next_node = tail.next
        head, tail = reverse_one_group(head, tail)
        pre.next = head
        tail.next = next_node
        pre = tail
        head = next_node

    return dummy.next


# ============================================================
# 写法二 (纯 206 风格): 先切断、再翻转、再接回
# reverse_one_group 和 206 题的 reverseList 完全一样
# ============================================================
def reverseKGroup_v2(head: ListNode, k: int) -> ListNode:
    # 和 206 题一模一样的翻转函数, 零特殊处理
    def reverse_one_group(head: ListNode):
        prev = None
        curr = head
        while curr:               # 和 206 题完全一样!
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev               # 返回新的头节点

    dummy = ListNode(0)
    dummy.next = head
    pre = dummy

    while head:
        tail = pre
        for i in range(k):
            tail = tail.next
            if not tail:
                return dummy.next

        next_node = tail.next
        tail.next = None          # 先切断: 把这一组变成独立的小链表
        new_head = reverse_one_group(head)  # 纯 206 翻转
        pre.next = new_head       # 接回: 前面接上新头
        head.next = next_node     # 接回: 新尾(原 head)接上下一组
        pre = head                # 原 head 现在是新尾
        head = next_node

    return dummy.next

# --- 测试代码 ---
def print_list(head: ListNode):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res))

def create_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 2),  # 预期: 2 -> 1 -> 4 -> 3 -> 5
        ([1, 2, 3, 4, 5], 3),  # 预期: 3 -> 2 -> 1 -> 4 -> 5
        ([1, 2, 3, 4, 5], 1),  # 预期: 1 -> 2 -> 3 -> 4 -> 5
        ([1, 2, 3, 4, 5], 5),  # 预期: 5 -> 4 -> 3 -> 2 -> 1
    ]

    for arr, k in test_cases:
        print(f"输入: {arr}, k = {k}")

        head1 = create_list(arr)
        result1 = reverseKGroup_v1(head1, k)
        print("  写法一 (while prev != tail): ", end="")
        print_list(result1)

        head2 = create_list(arr)
        result2 = reverseKGroup_v2(head2, k)
        print("  写法二 (while curr != stop): ", end="")
        print_list(result2)

        print()
