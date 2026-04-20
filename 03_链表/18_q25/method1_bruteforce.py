# -*- coding: utf-8 -*-

"""
LeetCode 第 25 题: K 个一组翻转链表 (Method 1: Brute Force with List Buffer)
思路分析:
1. 将链表中的所有节点装进数组。
2. 将数组按照每 k 个一组进行分组。
3. 如果一组中有 k 个节点, 将这组节点反转。
4. 重新串联这些节点的 .next 指针。
5. 最后返回新的头节点。
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    if not head or k == 1:
        return head
    
    # 1. 遍历链表, 把所有节点存入一个列表
    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next
    
    # 2. 对列表节点按照 k 进行分组处理
    # 每隔 k 个拿一组, 长度为 n, 步长为 k
    n = len(nodes)
    for i in range(0, n - n % k, k):
        # 取出这一组的 k 个节点
        group = nodes[i : i + k]
        # 反转这一组在原列表中的顺序 (原地切片反转)
        nodes[i : i + k] = group[::-1]
    
    # 3. 重新串联所有节点的 next 指针
    for i in range(n - 1):
        nodes[i].next = nodes[i + 1]
    
    # 4. 最后一个节点的 next 要指向 None
    nodes[-1].next = None
    
    # 返回反转后的第一个节点
    return nodes[0]

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
    test_arr = [1, 2, 3, 4, 5]
    test_k = 2
    print(f"输入: {test_arr}, k = {test_k}")
    
    head = create_list(test_arr)
    new_head = reverseKGroup(head, test_k)
    
    print("输出: ", end="")
    print_list(new_head)
    
    # 预期: 2 -> 1 -> 4 -> 3 -> 5
