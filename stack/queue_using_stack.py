# 用队列实现堆栈


class MyQueue:

    def __init__(self):
        self.first_stack = []
        self.second_stack = []


    def push(self, x: int) -> None:
        self.first_stack.append(x)


    def pop(self) -> int:
        if not self.second_stack:
            while self.first_stack:
                self.second_stack.append(self.first_stack.pop())
        return self.second_stack.pop()



    def peek(self) -> int:
        if not self.second_stack:
            while self.first_stack:
                self.second_stack.append(self.first_stack.pop())
        return self.second_stack[-1]


    def empty(self) -> bool:
        return not bool(self.first_stack + self.second_stack)


obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
print(param_2)
param_3 = obj.peek()
print(param_3)
param_4 = obj.empty()
print(param_4)
param_5 = obj.pop()
print(param_5)
param_6 = obj.empty()
print(param_6)