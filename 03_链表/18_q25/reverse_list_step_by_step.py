# -*- coding: utf-8 -*-

"""
演示单链表反转的过程 (Iterative Reversal with Step-by-Step Visualization)
思路分析:
1. 维护三个指针: prev (前一个节点), curr (当前节点), next_temp (临时保存下一个节点)。
2. 每次循环, 让 curr.next 指向 prev, 实现反转。
3. 动态更新 prev 和 curr 的位置, 让它们向后移动。
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_str(head: ListNode, current_node: ListNode = None, prev_node: ListNode = None):
    """
    辅助函数: 把链表打印成字符串, 并标记当前指针的位置。
    """
    res = []
    curr = head
    while curr:
        val_str = str(curr.val)
        if curr == current_node:
            val_str = f"[{val_str} (curr)]"
        elif curr == prev_node:
            val_str = f"[{val_str} (prev)]"
        else:
            val_str = f"{val_str}"
        res.append(val_str)
        curr = curr.next
    
    if not res: return "None"
    return " -> ".join(res)

def reverse_list_with_steps(head: ListNode) -> ListNode:
    print("\n--- 开始反转单链表 ---")
    print(f"初始状态: {list_to_str(head)}")
    
    prev = None
    curr = head
    step = 1
    
    while curr:
        print(f"\nStep {step}:")
        # 1. 保存下一个节点 (防止断链)
        next_temp = curr.next
        print(f"  (1) 保存当前节点 {curr.val} 的下一个节点: {next_temp.val if next_temp else 'None'}")
        
        # 2. 修改当前节点的指针 (反向连接)
        curr.next = prev
        print(f"  (2) 令 {curr.val}.next 指向 {'None' if not prev else prev.val} (即之前处理过的部分)")
        
        # 此时整个链表在视觉上已经裂开了, 我们可以打印当前的反转结果
        # 注意: 这里只能从 curr 开始往回打印, 这部分已经是反转后的
        print(f"  此时已反转的部分: {list_to_str(curr)}")
        
        # 3. 指针整体后移 (核心步骤)
        prev = curr
        curr = next_temp
        print(f"  (3) 指针向后移: 现在 prev 在 {prev.val if prev else 'None'}, curr 在 {curr.val if curr else 'None'}")
        
        step += 1

    print("\n--- 反转完成 ---")
    print(f"最终结果 (从新的头节点开始): {list_to_str(prev)}")
    return prev

def create_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

if __name__ == "__main__":
    # 使用一个小例子来测试
    test_arr = [1, 2, 3, 4]
    head = create_list(test_arr)
    new_head = reverse_list_with_steps(head)
