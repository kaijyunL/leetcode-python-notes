class MinStack:
    """
    暴力解法：获取最小值时遍历整个栈
    时间复杂度：getMin 为 O(N)，其余 O(1)
    """
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        if not self.stack:
            return None
        return min(self.stack)

if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(f"Minimum: {minStack.getMin()}")
    minStack.pop()
    print(f"Top: {minStack.top()}")
    print(f"Minimum: {minStack.getMin()}")
