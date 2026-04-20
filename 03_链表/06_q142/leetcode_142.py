class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 方法一：哈希表法
    def detectCycle_hash(self, head: ListNode) -> ListNode:
        """
        使用哈希集合记录访问过的节点。
        时间复杂度: O(N)
        空间复杂度: O(N)
        """
        visited = set()
        node = head
        while node is not None:
            # 如果节点已经在集合中，说明找到了环的入口
            if node in visited:
                return node
            # 把当前节点加入集合
            visited.add(node)
            node = node.next
        # 走到尽头无环
        return None

    # 方法二：快慢指针法（最优解法）
    def detectCycle_fast_slow(self, head: ListNode) -> ListNode:
        """
        使用快慢指针，先判断是否有环，再找到环的入口。
        时间复杂度: O(N)
        空间复杂度: O(1)
        """
        slow = head
        fast = head
        
        # 阶段一：判断是否有环
        has_cycle = False
        while fast is not None and fast.next is not None:
            slow = slow.next          # 慢指针走一步
            fast = fast.next.next     # 快指针走两步
            
            # 只要快慢指针相遇，说明有环
            if slow == fast:
                has_cycle = True
                break
        
        # 如果没有环，直接返回 None
        if not has_cycle:
            return None
        
        # 阶段二：寻找环的入口
        # 将 fast 指针重置到头节点
        fast = head
        # 只有在两个指针不相遇时才继续走，当它们相遇时就是循环的入口
        while slow != fast:
            slow = slow.next  # 现在慢指针继续每次走一步
            fast = fast.next  # 快指针也每次只走一步
            
        # 再次相遇点即为环的入口
        return slow


# ----------------- 测试代码 -----------------
def create_linked_list_with_cycle(values, pos):
    """
    辅助函数：创建一个带环的链表
    :param values: 链表节点的值列表
    :param pos: 环的入口索引（从 0 开始），如果是 -1 表示无环
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    nodes = [head]
    
    for val in values[1:]:
        new_node = ListNode(val)
        current.next = new_node
        current = new_node
        nodes.append(new_node)
        
    if pos != -1:
        current.next = nodes[pos]
        
    return head


def main():
    sol = Solution()
    
    # 测试用例 1：有环链表 [3, 2, 0, -4]，入口在索引 1 (值为 2)
    print("测试用例 1: 链表 = [3, 2, 0, -4], 环入口在 pos = 1 (节点值 2)")
    head1 = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    res_hash1 = sol.detectCycle_hash(head1)
    res_opt1 = sol.detectCycle_fast_slow(head1)
    print(f"-> 哈希表法结果: 环的入口值为 {res_hash1.val if res_hash1 else 'None'}")
    print(f"-> 快慢指针法结果: 环的入口值为 {res_opt1.val if res_opt1 else 'None'}")
    print("-" * 50)

    # 测试用例 2：有环链表 [1, 2]，入口在索引 0 (值为 1)
    print("测试用例 2: 链表 = [1, 2], 环入口在 pos = 0 (节点值 1)")
    head2 = create_linked_list_with_cycle([1, 2], 0)
    res_opt2 = sol.detectCycle_fast_slow(head2)
    print(f"-> 快慢指针法结果: 环的入口值为 {res_opt2.val if res_opt2 else 'None'}")
    print("-" * 50)

    # 测试用例 3：无环链表 [1]
    print("测试用例 3: 链表 = [1], 无环 (pos = -1)")
    head3 = create_linked_list_with_cycle([1], -1)
    res_opt3 = sol.detectCycle_fast_slow(head3)
    print(f"-> 快慢指针法结果: 环的入口值为 {res_opt3.val if res_opt3 else 'None'}")
    print("-" * 50)

if __name__ == "__main__":
    main()
