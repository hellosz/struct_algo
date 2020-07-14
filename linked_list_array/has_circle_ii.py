# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 遍历，前一个节点被后一个节点指向(无解，因为内循环陷入死循环)
class Solution:
    def hasCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if id(fast) == id(slow):
                cross = fast
                break
        if not cross:
            return None
        else:
            start = head
            while id(start) != id(cross):
                head, cross = head.next, cross.next
            return head




node4, node3, node2, node1 = ListNode(-4), ListNode(0), ListNode(2), ListNode(3)
node4.next = node2
node3.next = node4
node2.next = node3
node1.next = node2

solution = Solution()
result = solution.hasCycle(node1)
print(result.val)