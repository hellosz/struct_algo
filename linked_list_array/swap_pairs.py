# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 初始化 将self设置成头指针
        cur, cur.next = self, head
        # 遍历
        while cur.next and cur.next.next:
            cur.next.next.next, cur.next.next, cur.next = cur.next, cur.next.next.next, cur.next.next
            cur = cur.next.next
        return self.next


node5, node4, node3, node2, node1 = ListNode(5), ListNode(4), ListNode(3), ListNode(2), ListNode(1)
node4.next = node5
node3.next = node4
node2.next = node3
node1.next = node2

solution = Solution()
head = solution.swapPairs(node1)
while head:
    print("当前的链表值为%s" % head.val)
    head = head.next
