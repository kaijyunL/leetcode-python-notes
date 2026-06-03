# 延续 83 题风格的 82 题解法
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    """
    延续 83 题的风格：一次遍历，if-else 逻辑。
    
    83 题逻辑：
    if curr.val == curr.next.val: curr.next = curr.next.next (删下一个)
    else: curr = curr.next (移动当前)
    
    82 题演变：
    if pre.next.val == pre.next.next.val: 把等值的全删了 (铲除后面)
    else: pre = pre.next (移动当前)
    """
    # 82 题必须用 dummy，因为 head 可能被删
    dummy = ListNode(0, head)
    pre = dummy
    
    # 延续 83 题的循环结构，但因为要判定下两个，条件变为如下：
    while pre.next and pre.next.next:
        # 判定逻辑：检查 pre 后面的两个节点是否重复
        if pre.next.val == pre.next.next.val:
            # 发现重复！延续 83 题的“删除”思路，但这里要全删
            val = pre.next.val
            while pre.next and pre.next.val == val:
                pre.next = pre.next.next
            # 删完后 pre 不动，继续在下一轮循环检查新的 pre.next
        else:
            # 没有重复，pre 移动到下一个节点（这个节点是安全的）
            pre = pre.next
            
    return dummy.next

# --- 测试代码 ---
def create_and_test(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    
    res_node = deleteDuplicates(dummy.next)
    
    res = []
    while res_node:
        res.append(str(res_node.val))
        res_node = res_node.next
    print(f"输入: {arr} -> 输出: {' -> '.join(res) if res else 'Empty'}")

if __name__ == "__main__":
    create_and_test([1, 2, 3, 3, 4, 4, 5])
    create_and_test([1, 1, 1, 2, 3])
