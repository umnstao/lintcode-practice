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
    @return: The node where the cycle begins.
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        fast = head
        slow = head
        entry = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                while slow != entry:
                    slow = slow.next
                    entry = entry.next
                return entry
        return None
