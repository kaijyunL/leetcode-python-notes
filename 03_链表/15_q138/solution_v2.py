"""
LeetCode 第 138 题：复制带随机指针的链表 (Copy List with Random Pointer)
解法二：节点交替连接法 (Space O(1))
"""

class Node:
    """定义链表节点结构"""
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        利用原节点的 next 指针建立新旧节点的临时映射
        时间复杂度: O(N)
        空间复杂度: O(1) (排除返回结果本身)
        """
        if not head:
            return None
            
        # 1. 复制节点：A -> A' -> B -> B' -> C -> C'
        # 在每个节点后面插入其副本
        cur = head
        while cur:
            old_next = cur.next
            # 创建新节点并链接到当前节点后
            cur.next = Node(cur.val)
            cur.next.next = old_next
            # 移动到原来的下一个节点继续处理
            cur = old_next
            
        # 2. 设置副本节点的 random 指针
        # 新节点 A' 的 random 就是 A 的 random 的 next (即 A' 的副本)
        cur = head
        while cur:
            if cur.random:
                # cur.next 是新节点，cur.random.next 是原 random 节点对应的副本
                cur.next.random = cur.random.next
            cur = cur.next.next # 移动到下一个原节点
            
        # 3. 拆分链表
        # 将交替连接的链表分离成原链表和新链表
        cur = head
        new_head = head.next
        new_cur = new_head
        
        while cur:
            # 恢复原链表的 next 指针
            cur.next = cur.next.next
            # 移动原链表指针
            cur = cur.next
            # 链接新链表的 next 指针
            if cur:
                new_cur.next = cur.next
                # 移动新链表指针
                new_cur = new_cur.next
            else:
                new_cur.next = None
        
        return new_head

# --- 测试代码 ---
def print_list(head):
    """打印链表以验证结果 (值, 随机指针指向的值)"""
    res = []
    temp = head
    while temp:
        rand_val = temp.random.val if temp.random else "None"
        res.append(f"[{temp.val}, {rand_val}]")
        temp = temp.next
    print(" -> ".join(res))

if __name__ == "__main__":
    # 构建测试链表: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    # 格式为 [val, index_of_random_node]
    n1 = Node(7)
    n2 = Node(13)
    n3 = Node(11)
    n4 = Node(10)
    n5 = Node(1)
    
    n1.next, n1.random = n2, None
    n2.next, n2.random = n3, n1
    n3.next, n3.random = n4, n5
    n4.next, n4.random = n5, n3
    n5.next, n5.random = None, n1
    
    print("原链表状态：")
    print_list(n1)
    
    sol = Solution()
    copied_head = sol.copyRandomList(n1)
    
    print("复制链表状态：")
    print_list(copied_head)
    
    # 验证是否为全新节点
    print(f"\n验证原节点 n1 地址: {id(n1)}")
    print(f"验证新节点 n1' 地址: {id(copied_head)}")
    if id(n1) != id(copied_head):
        print("深拷贝验证完成。")
