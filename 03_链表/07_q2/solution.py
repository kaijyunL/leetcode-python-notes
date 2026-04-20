# solution.py

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建一个虚拟头节点，方便最后返回结果链表的头
        # 这是链表题中非常常用的技巧，不用特殊判断头节点是否为 None
        dummy = ListNode(0)
        # curr 指针用来在结果链表上不断向后移动，构建整个链表
        curr = dummy
        # carry 用来记录进位，初始值为 0
        carry = 0
        
        # 当 l1 不为空，或 l2 不为空，或者还有进位没处理完时，继续循环
        # 即使两个链表都空了，如果最后还有进位（例如 5+5=10），也要再循环一次生成最高位的 "1"
        while l1 or l2 or carry:
            # 如果 l1 还有节点，取其值，否则取 0 来补齐
            val1 = l1.val if l1 else 0
            # 如果 l2 还有节点，取其值，否则取 0 来补齐
            val2 = l2.val if l2 else 0
            
            # 计算这一位的总和：l1的值 + l2的值 + 上一位传过来的进位
            total_sum = val1 + val2 + carry
            
            # 更新进位：总和除以 10 的整数商 (如 total_sum 是 18，进位就是 1)
            carry = total_sum // 10
            
            # 留在当前位的值：总和除以 10 的余数 (如 total_sum 是 18，当前位就是 8)
            # 并且把这个新节点直接挂在 curr 的后面
            curr.next = ListNode(total_sum % 10)
            
            # 将 curr 指针向后移动一位，准备处理下一次的节点
            curr = curr.next
            
            # 如果 l1 没走完，则向后移动 l1 的指针
            if l1:
                l1 = l1.next
            # 如果 l2 没走完，则向后移动 l2 的指针
            if l2:
                l2 = l2.next
                
        # 循环结束，dummy 后面挂的就是我们完整算出来的结果链表
        # 返回 dummy.next 即可（因为 dummy 本身是我们自己塞进去的占位符）
        return dummy.next

# ================= 辅助测试代码 =================
def printList(node: ListNode):
    """辅助函数：打印链表，返回字符串查看"""
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    print(" -> ".join(res))

def createList(arr):
    """辅助函数：根据 Python 数组创建链表"""
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

if __name__ == "__main__":
    # 测试用例 1: 342 + 465 = 807
    # 链表表示是反过来的：2 -> 4 -> 3 加上 5 -> 6 -> 4
    # 期望结果链表是：7 -> 0 -> 8
    
    print("----- 测试用例开始 -----")
    l1 = createList([2, 4, 3])
    l2 = createList([5, 6, 4])
    
    print("输入链表 1:")
    printList(l1)
    print("输入链表 2:")
    printList(l2)
    
    sol = Solution()
    res = sol.addTwoNumbers(l1, l2)
    
    print("\n输出结果链表:")
    printList(res)
    print("------------------------")
