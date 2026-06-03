# 解法四：双指针（不使用 Dummy 节点）
# 核心思想：通过判断快指针是否移动到了末尾之外来识别是否需要删除头节点。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 1. 同样使用快慢指针，但初始化为 head
        fast = head
        slow = head
        
        # 2. 快指针先走 n 步
        for _ in range(n):
            fast = fast.next
            
        # 3. 特殊情况判断：
        # 如果快指针走完 n 步后已经是 None，说明链表长度恰好为 n，
        # 也就是说我们要删除的是倒数第 n 个节点，即“头节点”。
        if not fast:
            return head.next
            
        # 4. 快慢指针同步移动
        # 当 fast 到达最后一个节点时（fast.next 为 None），
        # slow 刚好在要删除节点的前一个位置。
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        # 5. 执行删除操作
        slow.next = slow.next.next
        
        return head

# 测试代码
if __name__ == "__main__":
    def print_list(head):
        res = []
        while head:
            res.append(str(head.val))
            head = head.next
        print("->".join(res) if res else "Empty")

    def build_list(arr):
        if not arr: return None
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    # 测试删除头节点
    arr1 = [1, 2, 3]
    n1 = 3
    print(f"测试1 - 原链表: {arr1}, 删除倒数第 {n1} 个节点 (头节点)")
    sol = Solution()
    res1 = sol.removeNthFromEnd(build_list(arr1), n1)
    print_list(res1)  # 预期输出: 2->3

    # 测试删除中间节点
    arr2 = [1, 2, 3, 4, 5]
    n2 = 2
    print(f"\n测试2 - 原链表: {arr2}, 删除倒数第 {n2} 个节点")
    res2 = sol.removeNthFromEnd(build_list(arr2), n2)
    print_list(res2)  # 预期输出: 1->2->3->5
