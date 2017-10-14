"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        prev = None
        cur = head
        while cur:
            myNext = cur.next
            cur.next = prev
            prev = cur
            cur = myNext
        return prev