#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LeetCode 147: 对链表进行插入排序 (Insertion Sort List)
包含：
 1. 将链表转数组的极简单暴力法
 2. 基础的插入排序法
 3. 优化尾节点判断的最优插入排序法
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # ---------------------------------------------------------
    # 方法一：转化为数组操作（简单暴力法）
    # ---------------------------------------------------------
    def insertionSortList_v1(self, head: ListNode) -> ListNode:
        """
        思路：把链表的值全部提取成为数组，让内置排序排好，再依序赋值给原链表。
        """
        if not head or not head.next:
            return head
        
        # 提取值
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
            
        # 让语言底层使用 O(N log N) 的排序法对数组排序
        values.sort()
        
        # 将排好序的值复原到链表节点上
        curr = head
        for val in values:
            curr.val = val
            curr = curr.next
            
        return head

    # ---------------------------------------------------------
    # 方法二：基础版链表插入排序
    # ---------------------------------------------------------
    def insertionSortList_v2(self, head: ListNode) -> ListNode:
        """
        思路：标准的原地插入逻辑，每次拿到待插入节点，都老老实实从dummy哑节点向后寻找插入位置。
        """
        if not head or not head.next:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        
        # curr 记录未排序队列的起始节点我们先把待排序的拿出来
        curr = head.next
        # 断开已排序队列与未排序队列，此时已排序只有原链表的第一个头节点
        head.next = None  
        
        while curr:
            next_node = curr.next  # 暂存未排序集合中的下一个节点
            
            # 每轮都从头开始寻找能够插入的前一个节点 prev
            prev = dummy
            while prev.next and prev.next.val <= curr.val:
                prev = prev.next
                
            # 执行: 把 curr 插入到 prev 后面的基本动作
            curr.next = prev.next
            prev.next = curr
            
            # 进入下一轮循环处理
            curr = next_node
            
        return dummy.next

    # ---------------------------------------------------------
    # 方法三：优化版链表插入排序（最优解）
    # ---------------------------------------------------------
    def insertionSortList_v3(self, head: ListNode) -> ListNode:
        """
        思路：加入 last_sorted 指针优化效率。
        如果待排序节点本来就比已有序队列最后一个节点还要大，直接跳过扫描。
        最优情况下可以达到 O(N) 的时间复杂度。
        """
        if not head or not head.next:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        
        last_sorted = head       # 初始化已排序部分的末尾节点
        curr = head.next         # 当前需要寻找安插位置的节点
        
        while curr:
            # 优化核心：若天然满足排序（大于当前已维护队列里最大的元素）
            if last_sorted.val <= curr.val:
                last_sorted = last_sorted.next
            else:
                # 只有发现顺序错构了，才退回去，从 dummy 原点开始寻找插入点
                prev = dummy
                while prev.next.val <= curr.val:
                    prev = prev.next
                    
                # 从原链表中剥离当前的 curr
                last_sorted.next = curr.next
                # 把 curr 插入到寻找好的 prev 后面
                curr.next = prev.next
                prev.next = curr
                
            # 更新进入未排序队列中的下一个节点
            curr = last_sorted.next
            
        return dummy.next


# ==================== 测试执行区 ==================== #
def create_linked_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(head):
    res = []
    curr = head
    while curr:
        res.append(str(curr.val))
        curr = curr.next
    return " -> ".join(res)

if __name__ == "__main__":
    solution = Solution()
    
    # 题目示例：输入为 -1 -> 5 -> 3 -> 4 -> 0
    arr = [-1, 5, 3, 4, 0]
    
    print("====== LeetCode 147 测试结果 ======")
    print(f"原始输入链表: {print_linked_list(create_linked_list(arr))}")
    
    head1 = create_linked_list(arr)
    print(f"[方法一] 将原链表转化为数组排序: {print_linked_list(solution.insertionSortList_v1(head1))}")

    head2 = create_linked_list(arr)
    print(f"[方法二] 基础版的链表插入排序: {print_linked_list(solution.insertionSortList_v2(head2))}")

    head3 = create_linked_list(arr)
    print(f"[方法三] 优化过尾节点的插入排序: {print_linked_list(solution.insertionSortList_v3(head3))}")
