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
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here

        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        prev = dummy
        fast = head
        for _ in range(n):
            fast = fast.next
        while fast:
            cur = cur.next
            prev = prev.next
            fast = fast.next
        prev.next = cur.next
        return dummy.next