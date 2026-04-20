class ListNode:
    """
    单链表节点定义
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_list(arr):
    """
    从列表创建单链表
    """
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

def print_list(head):
    """
    打印单链表
    """
    output = []
    current = head
    while current:
        output.append(str(current.val))
        current = current.next
    print(" -> ".join(output) if output else "Empty List")
