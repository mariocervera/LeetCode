
class MinStack:

    def __init__(self):
        self.values = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.values.append(val)
        if not self.minimums or val <= self.minimums[-1]:
            self.minimums.append(val)

    def pop(self) -> None:
        val = self.values.pop()
        if self.minimums and self.minimums[-1] == val:
            self.minimums.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.minimums[-1]


# Tests

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # -3
minStack.pop()
print(minStack.top())  # 0
print(minStack.getMin())  # -2
