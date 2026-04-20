from node import ListNode, create_list, print_list

def rotateRight_brute(head: ListNode, k: int) -> ListNode:
    """
    暴力解法：每次旋转 1 个位置，重复 k 次。
    时间复杂度: O(k * n)
    空间复杂度: O(1)
    """
    if not head or not head.next or k == 0:
        return head
    
    # 只需要移动 k % n 次，因为旋转 n 次等于原地踏步
    # 需要先求长度
    n = 0
    curr = head
    while curr:
        n += 1
        curr = curr.next
    
    k = k % n
    if k == 0:
        return head
    
    for _ in range(k):
        # 找到倒数第二个节点 prev 和倒数第一个节点 tail
        prev = None
        tail = head
        while tail.next:
            prev = tail
            tail = tail.next
        
        # 将 tail 提升为新的头节点，断开原来的尾部连接
        # 这里 tail.next 指向原 head
        # prev.next 指向 None
        tail.next = head
        head = tail
        if prev:
            prev.next = None
            
    return head

if __name__ == "__main__":
    print("-" * 10, "暴力旋转演示", "-" * 10)
    arr = [1, 2, 3, 4, 5]
    k = 2
    head = create_list(arr)
    print(f"原链表: ")
    print_list(head)
    print(f"旋转次数 k = {k}")
    
    new_head = rotateRight_brute(head, k)
    print(f"旋转后的链表: ")
    print_list(new_head)
