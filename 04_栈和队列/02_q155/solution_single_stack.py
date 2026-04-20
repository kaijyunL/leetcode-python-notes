class MinStack:
    """
    进阶解法：栈中存储 (当前值, 当前最小值) 这种对子
    时间复杂度：所有操作均为 O(1)
    """
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None

if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(f"Minimum: {minStack.getMin()}")
    minStack.pop()
    print(f"Top: {minStack.top()}")
    print(f"Minimum: {minStack.getMin()}")
