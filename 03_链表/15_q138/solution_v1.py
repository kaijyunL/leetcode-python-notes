"""
LeetCode 第 138 题：复制带随机指针的链表 (Copy List with Random Pointer)
解法一：哈希表法 (Hash Map)
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
        使用哈希表来记录原节点和副本节点的对应关系
        时间复杂度: O(N)
        空间复杂度: O(N)
        """
        if not head:
            return None
        
        # 1. 第一次遍历：创建副本节点并存入哈希表
        # key 存放原节点，value 存放对应的新节点
        mapping = {}
        cur = head
        while cur:
            # 只复制值 (val)，暂时不连接 next 和 random
            mapping[cur] = Node(cur.val)
            cur = cur.next
            
        # 2. 第二次遍历：根据映射关系，连接新节点的 next 和 random
        cur = head
        while cur:
            # 连接新节点的 next
            if cur.next:
                mapping[cur].next = mapping[cur.next]
            # 连接新节点的 random
            if cur.random:
                mapping[cur].random = mapping[cur.random]
            cur = cur.next
            
        # 返回新链表的头节点
        return mapping[head]

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
