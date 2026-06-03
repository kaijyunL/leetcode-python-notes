"""
LeetCode 24 - 两两交换链表中的节点 (Swap Nodes in Pairs)
https://leetcode.cn/problems/swap-nodes-in-pairs/

题目：给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
      必须在不修改节点内部的值的情况下完成本题（只能进行节点交换）。
"""

from typing import Optional


# ─────────────────────────────────────────────
# 链表节点定义
# ─────────────────────────────────────────────
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ─────────────────────────────────────────────
# 工具函数：列表 → 链表
# ─────────────────────────────────────────────
def build_linked_list(values: list) -> Optional[ListNode]:
    """将 Python 列表转换为链表，返回头节点"""
    if not values:
        return None
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


# ─────────────────────────────────────────────
# 工具函数：链表 → 列表
# ─────────────────────────────────────────────
def linked_list_to_list(head: Optional[ListNode]) -> list:
    """将链表转换为 Python 列表，便于打印"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ═════════════════════════════════════════════
# 方法一：值交换（伪暴力）
# 时间复杂度：O(n)  空间复杂度：O(1)
# ⚠️ 注意：此方法违反题目规定（不能修改节点值），仅供理解题意
# ═════════════════════════════════════════════
def swapPairs_v1(head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    while cur and cur.next:
        # 直接交换相邻两个节点的值（违反题意，仅作演示）
        cur.val, cur.next.val = cur.next.val, cur.val
        # 跳过当前已处理的这对节点，移向下一对
        cur = cur.next.next
    return head


# ═════════════════════════════════════════════
# 方法二：迭代（哑节点 + 指针重连）⭐ 最优解 - 推荐
# 时间复杂度：O(n)  空间复杂度：O(1)
# ═════════════════════════════════════════════
def swapPairs_v2(head: Optional[ListNode]) -> Optional[ListNode]:
    # 创建哑节点：统一对头节点和普通节点的处理，避免特殊讨论
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy  # prev 始终指向待交换对的前一个节点

    while prev.next and prev.next.next:
        # 定位待交换的两个节点
        first = prev.next        # 第一个节点（交换后排在后面）
        second = prev.next.next  # 第二个节点（交换后排在前面）

        # 三步完成指针重连（倒序连接，逻辑更清晰）
        first.next = second.next  # 步骤1: first 跳过 second，连到后续节点
        second.next = first       # 步骤2: second 反向连回 first，完成交换
        prev.next = second        # 步骤3: 前驱节点指向交换后的新首节点 second

        # 将 prev 移向下一对的前驱（交换后 first 排在后面，它就是下一对的前驱）
        prev = first

    # dummy.next 是新链表的头节点
    return dummy.next


# ═════════════════════════════════════════════
# 方法三：递归
# 时间复杂度：O(n)  空间复杂度：O(n)（递归栈）
# ═════════════════════════════════════════════
def swapPairs_v3(head: Optional[ListNode]) -> Optional[ListNode]:
    # 递归终止条件：链表为空，或只剩一个节点，不需要也无法交换
    if not head or not head.next:
        return head

    # second 是当前对的第二个节点，交换后它会成为新的头
    second = head.next

    # 🔑 关键步骤：
    # 1. 先递归处理 second 之后的链表（head.next.next 开始的部分）
    # 2. 递归结果挂到 head 的后面（head 交换后排第二，它的 next 是后续链表的新头）
    head.next = swapPairs_v3(second.next)

    # 让 second 指向 head，完成当前这对的交换
    second.next = head

    # 返回当前对的新头节点（原来的 second）
    return second


# ─────────────────────────────────────────────
# 测试与验证
# ─────────────────────────────────────────────
def run_tests():
    """运行所有测试用例，验证三种解法的正确性"""

    # 测试用例：[输入列表, 期望输出列表]
    test_cases = [
        ([1, 2, 3, 4],  [2, 1, 4, 3]),  # 标准偶数长度
        ([1, 2, 3],     [2, 1, 3]),      # 奇数长度（最后一个节点无需交换）
        ([1],           [1]),            # 单节点
        ([],            []),             # 空链表
        ([1, 2],        [2, 1]),         # 只有一对
        ([1, 2, 3, 4, 5, 6], [2, 1, 4, 3, 6, 5]),  # 较长的偶数链表
    ]

    methods = [
        ("方法一：值交换（伪暴力）⚠️", swapPairs_v1),
        ("方法二：迭代（哑节点）  ✅", swapPairs_v2),
        ("方法三：递归            ✅", swapPairs_v3),
    ]

    for method_name, method in methods:
        print(f"\n{'='*55}")
        print(f"  {method_name}")
        print(f"{'='*55}")
        all_pass = True
        for inputs, expected in test_cases:
            # 重新构建链表（避免上一个方法修改了同一链表）
            head = build_linked_list(inputs)
            result_head = method(head)
            result = linked_list_to_list(result_head)
            status = "✅ 通过" if result == expected else "❌ 失败"
            if result != expected:
                all_pass = False
            print(f"  输入: {str(inputs):<20} → 输出: {str(result):<20} 期望: {str(expected):<20} {status}")
        print(f"  {'全部通过 🎉' if all_pass else '存在失败用例 ⚠️'}")


if __name__ == "__main__":
    print("LeetCode 24 - 两两交换链表中的节点")
    print("=" * 55)
    run_tests()

    # ── 单独演示方法二（迭代）的步骤过程 ──────────────────
    print("\n\n【演示】方法二 迭代过程（输入: [1, 2, 3, 4]）")
    print("-" * 55)

    class DebugListNode:
        """带调试输出的链表节点"""
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def debug_swap(head):
        """带过程打印的迭代解法演示"""
        dummy = DebugListNode(0)
        dummy.next = head
        prev = dummy
        step = 1
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            print(f"  第 {step} 次交换: {first.val} ↔ {second.val}")
            
            # 使用更清晰的倒序连接逻辑
            first.next = second.next
            second.next = first
            prev.next = second
            
            prev = first
            step += 1
        return dummy.next

    demo_head = build_linked_list([1, 2, 3, 4])
    result = debug_swap(demo_head)
    print(f"  最终结果: {linked_list_to_list(result)}")
