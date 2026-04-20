from node import ListNode, create_list, print_list

def rotateRight_optimal(head: ListNode, k: int) -> ListNode:
    """
    最优解法：找到长度 n，成环，找到 (n - k % n) 个节点作为新的末尾，并断开环。
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    if not head or not head.next or k == 0:
        return head
    
    # 步骤 1：找到长度，并找到原来的尾节点
    n = 1
    old_tail = head
    while old_tail.next:
        n += 1
        old_tail = old_tail.next
    
    # 步骤 2：实际旋转位移取模
    k = k % n
    if k == 0:
        return head
    
    # 步骤 3：老尾部连接老头部，形成一个环
    old_tail.next = head
    
    # 步骤 4：寻找新的尾部位置。
    # 新的尾部在从 head 开始的第 (n - k - 1) 个位置。
    # 或者从 old_tail 开始走 (n - k) 个位置。
    new_tail = old_tail
    for _ in range(n - k):
        new_tail = new_tail.next
        
    # 步骤 5：新尾部的下一个即为新头部
    new_head = new_tail.next
    
    # 步骤 6：断开环
    new_tail.next = None
    
    return new_head

if __name__ == "__main__":
    print("-" * 10, "最优旋转演示", "-" * 10)
    arr = [1, 2, 3, 4, 5]
    k = 2
    head = create_list(arr)
    print(f"原链表: ")
    print_list(head)
    print(f"旋转次数 k = {k}")
    
    new_head = rotateRight_optimal(head, k)
    print(f"旋转后的链表: ")
    print_list(new_head)
    
    # 示例 2: [0, 1, 2], k = 4
    print("\n示例 2:")
    arr2 = [0, 1, 2]
    k2 = 4
    head2 = create_list(arr2)
    print(f"原链表: ")
    print_list(head2)
    print(f"旋转次数 k = {k2} (相当于旋转 {k2 % 3} 次)")
    
    new_head2 = rotateRight_optimal(head2, k2)
    print(f"旋转后的链表: ")
    print_list(new_head2)
