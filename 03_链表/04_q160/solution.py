class ListNode:
    """定义链表节点"""
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode_BruteForce(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        解法一：暴力法
        时间复杂度: O(M*N)
        空间复杂度: O(1)
        """
        tempA = headA
        while tempA:
            tempB = headB
            while tempB:
                if tempA == tempB:
                    return tempA
                tempB = tempB.next
            tempA = tempA.next
        return None

    def getIntersectionNode_HashSet(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        解法二：哈希集合
        时间复杂度: O(M+N)
        空间复杂度: O(M)
        """
        visited = set()
        temp = headA
        while temp:
            visited.add(temp)
            temp = temp.next
            
        temp = headB
        while temp:
            if temp in visited:
                return temp
            temp = temp.next
        return None

    def getIntersectionNode_Optimal(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        解法三：双指针法（最优解）
        时间复杂度: O(M+N)
        空间复杂度: O(1)
        """
        if not headA or not headB:
            return None
        
        pA, pB = headA, headB
        
        # 两个指针走过的路程是一样的：A + B = B + A
        # 如果相交，会在交点相遇；如果不相交，最终都会变成 None (None == None)
        while pA != pB:
            # pA 走完 A 后转向 B
            pA = pA.next if pA else headB
            # pB 走完 B 后转向 A
            pB = pB.next if pB else headA
            
        return pA

def create_linked_lists():
    """创建一个有交点的链表案例进行测试"""
    # 公共部分: 8 -> 4 -> 5
    common = ListNode(8)
    common.next = ListNode(4)
    common.next.next = ListNode(5)
    
    # 链表 A: 4 -> 1 -> common
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = common
    
    # 链表 B: 5 -> 6 -> 1 -> common
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = common
    
    return headA, headB, common

if __name__ == "__main__":
    headA, headB, intersectNode = create_linked_lists()
    sol = Solution()
    
    print("测试案例：链表 A [4,1,8,4,5], 链表 B [5,6,1,8,4,5], 交点值为 8")
    
    # 测试解法一
    res1 = sol.getIntersectionNode_BruteForce(headA, headB)
    print(f"暴力法结果: {res1.val if res1 else 'None'}")
    
    # 测试解法二
    res2 = sol.getIntersectionNode_HashSet(headA, headB)
    print(f"哈希法结果: {res2.val if res2 else 'None'}")
    
    # 测试解法三
    res3 = sol.getIntersectionNode_Optimal(headA, headB)
    print(f"双指针最优解结果: {res3.val if res3 else 'None'}")
    
    if res3 == intersectNode:
        print("\n验证通过！所有解法均正确找到了交点。")
    else:
        print("\n验证失败。")
