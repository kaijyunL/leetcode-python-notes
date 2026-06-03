from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList_array(self, head: Optional[ListNode]) -> None:
        """
        方法一：使用列表（数组）存储节点
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        # 1. 遍历链表，将所有节点按顺序存入列表
        vec = []
        node = head
        while node:
            vec.append(node)
            node = node.next
            
        # 2. 设置双指针，从一头一尾交替重建链表
        i, j = 0, len(vec) - 1
        while i < j:
            # 正常情况下：前面的元素连向后面的元素，例如第一个节点连向最后一个节点
            vec[i].next = vec[j]
            i += 1
            # 判断奇偶，一旦双指针相遇说明连完了，及时跳出循环，避免自己连自己或交叉覆盖
            if i == j:
                break
            # 后面的元素接着连向它前面的元素，例如最后一个节点连向第二节点
            vec[j].next = vec[i]
            j -= 1
            
        # 3. 非常重要：重排结束后，最后的那个节点（在原链表的相对靠中间的位置）的 next 必须置为空，否则会出现死循环环路
        vec[i].next = None

    def reorderList_optimal(self, head: Optional[ListNode]) -> None:
        """
        方法二：寻找中间节点 + 反转后半段 + 交替合并 (空间复杂度 O(1) 的最优解法)
        """
        if not head or not head.next:
            return
        
        # 1. 寻找中点 (利用经典快慢指针)
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # 从中点断开链表，分成前一段 head 和 后一段 mid
        mid = slow.next
        slow.next = None
        
        # 2. 反转后半段链表 (把 mid 开头的链表反转，变成倒序)
        prev = None
        curr = mid
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head2 = prev  # 反转后的后半段链表头节点
        
        # 3. 交替合并两段链表 (head1 代表前半部分，head2 代表后半部分反转后的部分)
        head1 = head
        while head1 and head2:
            # 提前保存接下来需要遍历的节点
            next1 = head1.next
            next2 = head2.next
            
            # head1 的节点连向 head2 的节点
            head1.next = head2
            head1 = next1 # head1 的指针前进
            
            # head2 的节点再连回调原来的 next1
            head2.next = head1
            head2 = next2 # head2 的指针前进


# ==============================
# 下面为测试和打印代码，供用户直接运行验证
# ==============================
def build_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res))

if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4],       # 预期输出: 1 -> 4 -> 2 -> 3
        [1, 2, 3, 4, 5]     # 预期输出: 1 -> 5 -> 2 -> 4 -> 3
    ]
    
    print("=== 方法一：数组（List）解法测试 ===")
    for arr in test_cases:
        head = build_list(arr)
        print(f"原链表: ", end="")
        print_list(build_list(arr))
        Solution().reorderList_array(head)
        print(f"重排后: ", end="")
        print_list(head)
        print("-" * 30)
        
    print("\n=== 方法二：最优解法测试 (找中点+反转+合并) ===")
    for arr in test_cases:
        head = build_list(arr)
        print(f"原链表: ", end="")
        print_list(build_list(arr))
        Solution().reorderList_optimal(head)
        print(f"重排后: ", end="")
        print_list(head)
        print("-" * 30)
