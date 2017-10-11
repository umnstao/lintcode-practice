"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        if head is None or head.next is None:
            return None
        mid = self.findMid(head)
        tail = self.reverse(mid.next)
        mid.next = None
        self.merge(head,tail)

    def merge(self,head,tail):
        sign = 1
        dummy = ListNode(-1)
        cur = dummy
        while head and tail:
            if sign == 1:
                cur.next = head
                head = head.next
                sign = 2
            else:
                cur.next = tail
                tail = tail.next
                sign = 1
            cur = cur.next
        if head:
            cur.next = head
        else:
            cur.next = tail


    def findMid(self, cur):
        # 1->2->3->4->None
        # return 3
        # 1->2->3->4->5->None
        # return 3
        fast = cur
        slow = cur
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    def reverse(self, cur):
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
