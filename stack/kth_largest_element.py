class KthLargest:
    def __init__(self, k: int, nums: list):
        self.kth = k
        self.list = []
        while nums:
            self.insert(nums.pop())

    def add(self, val: int) -> int:
        # 有序插入
        self.insert(val)
        # 返回结果
        return self.list[self.kth - 1]

    def insert(self, num: int):
        i = 0
        for val in self.list:
            if val <= num:
                self.list.insert(i, num)
                break
            i += 1
        if i == len(self.list):
            self.list.append(num)


k = 3
arr = [4, 5, 8, 2]
kthLargest = KthLargest(3, arr)
print(kthLargest.list)
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))
