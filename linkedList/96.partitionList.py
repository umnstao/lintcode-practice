"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode
    """
    def partition(self, head, x):
        # write your code here
        cur = head

        dd = ListNode(-1)
        la = dd
        dummy = ListNode(-1)
        lb = dummy
        while cur:
            if cur.val < x:
                la.next = cur
                la = la.next
            else:
                lb.next = cur
                lb = lb.next
            cur = cur.next
        lb.next = None
        la.next = dummy.next
        return dd.next

