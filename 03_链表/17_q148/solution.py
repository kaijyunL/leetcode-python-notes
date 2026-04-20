#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LeetCode 148: 排序链表 (Sort List)
包含了三种解法，并带有详细的中文注解。
代码附带简单的测试，你可以直接运行本文件进行验证。
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # -----------------------------------------------------------------
    # 方法一： 转换为数组排序 (时间 O(NlogN), 空间 O(N))
    # -----------------------------------------------------------------
    def sortList_Array(self, head: ListNode) -> ListNode:
        """
        简单直观，但是申请了 O(N) 的数组空间，不满足题目对空间复杂度的要求。
        """
        if not head or not head.next:
            return head
        
        # 1. 遍历链表提取值
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
            
        # 2. 数组排序
        vals.sort()
        
        # 3. 重新赋值给链表
        curr = head
        for val in vals:
            curr.val = val
            curr = curr.next
            
        return head


    # -----------------------------------------------------------------
    # 方法二： 自顶向下的归并排序 (时间 O(NlogN), 空间 O(logN) 因为有递归栈)
    # -----------------------------------------------------------------
    def sortList_TopDownMerge(self, head: ListNode) -> ListNode:
        """
        使用了递归，递归深度为 log(N)。这是最经典也是容易理解手写的 O(NlogN) 链表排序。
        """
        # 递归出口：空链表或只有一个节点，天然是有序的
        if not head or not head.next:
            return head
            
        # 1. 找到链表中点并断开 (快慢指针法)
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # mid 为右半部分的头节点
        mid = slow.next
        # 将左半部分的尾节点断开
        slow.next = None
        
        # 2. 递归地对左右两半进行子问题排序
        left = self.sortList_TopDownMerge(head)
        right = self.sortList_TopDownMerge(mid)
        
        # 3. 合并返回的两个已排序左、右链表
        return self._merge(left, right)
        
    def _merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        """
        合并两个有序链表（辅助函数，等同于 LeetCode 21）
        """
        dummy = ListNode(0)
        curr = dummy
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        # 把剩下不为空的部分直接接到末尾
        curr.next = list1 if list1 else list2
            
        return dummy.next


    # -----------------------------------------------------------------
    # 方法三： 自底向上的归并排序 (时间 O(NlogN), 空间 O(1)) -- 最优解
    # -----------------------------------------------------------------
    def sortList_BottomUpMerge(self, head: ListNode) -> ListNode:
        """
        不使用递归。从长度为 1 的子序列开始两两合并，然后是长度 2，长度 4...
        直到每次合并覆盖完等于（或大于）整条链表的长度。达到 O(1) 的额外空间。
        """
        if not head or not head.next:
            return head
            
        # 1. 获取链表总长度
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        dummy = ListNode(0)
        dummy.next = head
        
        # 2. step 为每次合并的子链表长度，从 1 开始，每次翻倍: 1, 2, 4, 8...
        step = 1
        while step < length:
            prev = dummy
            curr = dummy.next
            
            # 从头到尾按照 step 大小开始两两切割、合并
            while curr:
                # 寻找并截取第一段长度最长为 step 的子链表 head1
                head1 = curr
                for i in range(1, step):
                    if curr.next: 
                        curr = curr.next
                    else: 
                        break
                
                # 如果找不到第二段的开头，说明当前后面没有元素可以跟 head1 配对合并了，将 head1 接上并直接跳出
                if not curr.next: 
                    prev.next = head1
                    break
                    
                # 寻找并截取第二段总长最长为 step 的子链表 head2
                head2 = curr.next
                curr.next = None # 重要：将第一段子链表尾部与后面的节点断开
                
                curr = head2
                for i in range(1, step):
                    if curr.next: 
                        curr = curr.next
                    else: 
                        break
                
                # 保留下一个待处理的起始位置 nxt
                nxt = curr.next
                curr.next = None # 将第二段子链表尾部与后面的节点断开
                
                # 合并截取出来的 head1 和 head2 两个短链表
                merged_head, merged_tail = self._merge_and_get_tail(head1, head2)
                
                # 拼接到被处理完的链表序列后
                prev.next = merged_head
                # prev 前进到这部分合并后链表的末尾，准备去连接下一组结果
                prev = merged_tail
                # curr 挪到下次配对处理的起点
                curr = nxt
                
            # 本轮（当前步长）合并完成，步长翻倍
            step *= 2
            
        return dummy.next

    def _merge_and_get_tail(self, head1: ListNode, head2: ListNode) -> tuple:
        """
        合并两个有序链表，并返回 (合并后的头节点, 合并后的尾节点)
        """
        dummy = ListNode(0)
        curr = dummy
        while head1 and head2:
            if head1.val < head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
            
        curr.next = head1 if head1 else head2
            
        # prev 需要移动到合并后这段链表的真正的尾部位置
        while curr.next:
            curr = curr.next
            
        return dummy.next, curr


# =======================================================
# 下方为测试代码，可直接运行文件来直观验证各方法结果
# =======================================================
def print_list(head: ListNode):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals) if vals else "Empty")

def create_list(vals: list) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    for val in vals:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

if __name__ == "__main__":
    sol = Solution()

    # 测试用例
    nums = [4, 2, 1, 3]
    print("====== LeetCode 148 排序链表 测试 ======\n")
    print("原链表:")
    print_list(create_list(nums))
    
    print("\n[方法一：数组排序]")
    head1 = create_list(nums)
    print_list(sol.sortList_Array(head1))

    print("\n[方法二：自顶向下归并排序]")
    head2 = create_list(nums)
    print_list(sol.sortList_TopDownMerge(head2))
    
    print("\n[方法三：自底向上归并排序 - 应对更复杂的测试用例]")
    nums_complex = [-1, 5, 3, 4, 0]
    head3_orig = create_list(nums_complex)
    print(f"原链表: ")
    print_list(head3_orig)
    print("排序后: ")
    head3 = create_list(nums_complex)
    print_list(sol.sortList_BottomUpMerge(head3))
