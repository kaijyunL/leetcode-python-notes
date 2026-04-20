class MinStack:
    """
    最优解法：辅助栈（双栈法）
    时间复杂度：所有操作均为 O(1)
    空间复杂度：O(N)
    这是面试中最推荐的写法，逻辑清晰且易于维护。
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 注意：这里必须是 <=，因为如果有多个相同的最小值，pop时需要对应
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None

if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(f"Minimum: {minStack.getMin()}")
    minStack.pop()
    print(f"Top: {minStack.top()}")
    print(f"Minimum: {minStack.getMin()}")
