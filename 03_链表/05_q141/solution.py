class ListNode:
    """定义单链表节点"""
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle_hashSet(self, head: ListNode) -> bool:
        """
        方法一：使用哈希表 (HashSet)
        思路：遍历链表，将访问过的节点存入集合，如果再次遇到已存在的节点则说明有环。
        """
        visited = set()
        curr = head
        while curr:
            # 如果当前节点已经在集合中，说明之前来过这里 -> 有环
            if curr in visited:
                return True
            # 否则记下当前节点，继续走下一步
            visited.add(curr)
            curr = curr.next
        # 如果走到了 None，说明没环
        return False

    def hasCycle_fastSlow(self, head: ListNode) -> bool:
        """
        方法二：快慢指针 (Floyd's Cycle-Finding Algorithm) - 最优解
        思路：慢指针走一步，快指针走两步。如果相遇则有环；如果快指针能走到头，则无环。
        """
        if not head or not head.next:
            return False
            
        slow = head      # 慢指针，每次走 1 步
        fast = head.next # 快指针，每次走 2 步 (也可以都从 head 开始)
        
        while slow != fast:
            # 如果 fast 走到了尽头说明无环
            if not fast or not fast.next:
                return False
            slow = slow.next      # slow 走 1 步
            fast = fast.next.next # fast 走 2 步
            
        # 跳出循环表示 slow == fast，即两指针相遇。
        return True

    def hasCycle_standard(self, head: ListNode) -> bool:
        """
        方法三：标准快慢指针 (推荐写法)
        思路：slow 和 fast 都从 head 出发。这种写法的泛用性最强（如：LeetCode 142 找入口）。
        注意：必须先移动再判断，否则初始时 slow == fast 会直接退出。
        """
        slow = fast = head
        
        # 只要 fast 还能往前走两步，就继续
        while fast and fast.next:
            slow = slow.next          # 走 1 步
            fast = fast.next.next     # 走 2 步
            
            # 移动之后进行判断
            if slow == fast:
                return True
                
        return False

# --- 测试代码 ---
def create_linked_list_with_cycle(arr, pos):
    """辅助函数：根据数组和环的位置创建链表"""
    if not arr: return None
    
    nodes = [ListNode(x) for x in arr]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
    
    if pos != -1:
        nodes[-1].next = nodes[pos] # 将尾部连接到指定的 pos 索引处形成环
        
    return nodes[0]

if __name__ == "__main__":
    sol = Solution()
    
    # 案例 1: 有环, 环在索引 1 处
    head1 = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    print(f"Case 1 (Standard): {sol.hasCycle_standard(head1)}")
    
    # 案例 2: 有环, 环在索引 0 处
    head2 = create_linked_list_with_cycle([1, 2], 0)
    print(f"Case 2 (Standard): {sol.hasCycle_standard(head2)}")
    
    # 案例 3: 无环
    head3 = create_linked_list_with_cycle([1], -1)
    print(f"Case 3 (Standard): {sol.hasCycle_standard(head3)}")
