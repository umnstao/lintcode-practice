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
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        prev = dummy
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next
        return dummy.next