"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here

        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy.next
        prev = dummy
        while cur and cur.next:
            while cur and cur.next and cur.val == cur.next.val:
                cur = cur.next
            if prev.next == cur:
                prev = cur
                cur = cur.next
            else:
                cur = cur.next
                prev.next = cur
        return dummy.next
