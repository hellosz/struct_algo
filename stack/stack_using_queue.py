class MyStack:

    def __init__(self):
        self.list = []
        self.attach_list = []


    def push(self, x: int) -> None:
        if self.list:
            while self.list:
                self.attach_list.append(self.list.pop(0))
        self.list.append(x)
        self.list += self.attach_list
        self.attach_list = []


    def pop(self) -> int:
        return self.list.pop(0)


    def top(self) -> int:
        return self.list[0]


    def empty(self) -> bool:
        return not bool(self.list)



obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
print(param_2)
param_3 = obj.pop()
print(param_3)
param_4 = obj.pop()
print(param_4)
param_5 = obj.empty()
print(param_5)
