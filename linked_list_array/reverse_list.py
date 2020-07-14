# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head:
            # 初始值
            pre, cur, next = None, head, head.next

            # 遍历所有节点
            while cur:
                head, cur.next, pre, cur = cur, pre, cur, cur.next
            return head
        else:
            return None

# 数据初始化
node3, node2, node1 = ListNode(3), ListNode(2), ListNode(1)
node2.next = node3
node1.next = node2

so = Solution()
head = so.reverseList(node1)
while head:
    print("当前链表的值为%s" % head.val)
    head = head.next

